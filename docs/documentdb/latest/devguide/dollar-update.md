---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/dollar-update.html
---

# $
<a name="dollar-update"></a>

The `$` positional operator updates the first array element that matches the query condition. It acts as a placeholder for the matched array element's position.

**Parameters**
+ `field.$`: The array field with the positional operator to update the first matching element.

## Example (MongoDB Shell)
<a name="dollar-update-examples"></a>

The following example demonstrates using the `$` positional operator to update a specific array element.

**Create sample documents**

```
db.inventory.insertMany([
  { _id: 1, item: "Widget", quantities: [10, 20, 30] },
  { _id: 2, item: "Gadget", quantities: [5, 15, 25] }
]);
```

**Query example**

```
db.inventory.updateOne(
  { _id: 1, quantities: 20 },
  { $set: { "quantities.$": 22 } }
);
```

**Output**

```
{
  "_id" : 1,
  "item" : "Widget",
  "quantities" : [ 10, 22, 30 ]
}
```

## Code examples
<a name="dollar-update-code"></a>

To view a code example for using the `$` positional operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function updateDocument() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('inventory');

  await collection.updateOne(
    { _id: 1, quantities: 20 },
    { $set: { "quantities.$": 22 } }
  );

  const updatedDocument = await collection.findOne({ _id: 1 });
  console.log(updatedDocument);

  await client.close();
}

updateDocument();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def update_document():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.inventory

    collection.update_one(
        {'_id': 1, 'quantities': 20},
        {'$set': {'quantities.$': 22}}
    )

    updated_document = collection.find_one({'_id': 1})
    print(updated_document)

    client.close()

update_document()
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
