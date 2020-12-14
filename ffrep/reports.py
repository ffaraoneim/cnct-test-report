class MyCoolReport:

    def get_columns(self):
        return [
            'ID',
            'Name',
            'Family ID',
            'Family Name',
        ]

    def execute(self, client, params=None):
        results = []
        for cat in client.categories.all():
            results.append(
                (
                    cat['id'],
                    cat['name'],
                    cat.get('family', {}).get('id'),
                    cat.get('family', {}).get('name'),
                )
            )
        return results
