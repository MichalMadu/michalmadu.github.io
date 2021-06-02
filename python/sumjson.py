import json
data = '''{
    "note": "This file contains the sample data for testing",
    "comments": [
        {
            "name": "Romina",
            "count": 97
        },
        {
            "name": "Laurie",
            "count": 97
        },
        {
            "name": "Bayli",
            "count": 90
        }
    ]
}'''

count = sum(map(lambda x: int(x['count']), json.loads(data)['comments']))

print(count)