```python
from pymongo import MongoClient
import pandas as pd
import time,datetime

client = MongoClient('localhost',27017)['fund']
db = client.example # client['example']
collection = db.test_collection
data = dict()

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb","python","pymongo"],
        "date": datetime.datetime.utcnow()
}
```

```
posts = db.posts
post_id = posts.insert_one(post).inserted_id
```
## Reference_info
http://www.cnblogs.com/billyzh/p/5918598.html
