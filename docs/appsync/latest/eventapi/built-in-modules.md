---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/built-in-modules.html
---

# Built-in modules
<a name="built-in-modules"></a>

Modules are a part of the `APPSYNC_JS` runtime and provide utilities to help write functions and Event API handlers. This section describes the DynamoDB and Amazon RDS module functions that you can use to interact with these data sources.

## Amazon DynamoDB built-in module
<a name="DDB-built-in-module"></a>

The DynamoDB module functions provide an enhanced experience when interacting with DynamoDB data sources. You can make requests toward your DynamoDB data sources using the functions and without adding type mapping.

Modules are imported using `@aws-appsync/utils/dynamodb`:

```
import * as ddb from '@aws-appsync/utils/dynamodb';
```

### DynamoDB `get()` function
<a name="ddb-get-function"></a>

The DynamoDB `get()` function generates a `DynamoDBGetItemRequest` object to make a `GetItem` request to DynamoDB.

**Definition**

```
get<T>(payload: GetInput): DynamoDBGetItemRequest
```

**Example**

The following example fetches an item from DynamoDB in a `subscribe` handler.

```
import { get } from '@aws-appsync/utils/dynamodb';

export const onSubscribe = {
  request(ctx) {
    return ddb.get({key: {
      path: ctx.info.channel.path,
      sub: ctx.identity.sub
    }})
  },
  response(ctx) {
    console.log('Got the item:', ctx.result)
    if (!ctx.result){
      console.error("No info about this user for this channel path.")
      until.unauthorized()
    }
  }
}
```

### DynamoDB `query()` function
<a name="ddb-query-function"></a>

The DynamoDB `query()` function generates a `DynamoDBQueryRequest` object to make a `Query` request to DynamoDB.

**Definition**

```
query<T>(payload: QueryInput): DynamoDBQueryRequest
```

**Example**

The following example performs a query against a DynamoDB table.

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export const onPublish = {
  request(ctx) {
    // Find all items from this channel that exist on this path
    return ddb.query<{ channel: string; path: string }>({
      query: {
        channel: { eq: ctx.info.channelNamespace.name },
        path: { beginsWith: ctx.info.channe.path },
      },
      projection: ['channel', 'path', 'msgId'],
    })
  },
  response(ctx) {
    // Broadcast items that have not been saved to the table
    const ids = ctx.result.items.map(({ msgId }) =>  msgId )
    return ctx.events.filter(({ payload: { msgId } }) => !ids.includes(msgId))
  },
}
```

### DynamoDB `scan()` function
<a name="ddb-scan-function"></a>

The DynamoDB `scan()` function generates a `DynamoDBScanRequest` object to make a `Scan` request to DynamoDB.

**Definition**

```
scan<T>(payload: ScanInput): DynamoDBScanRequest
```

**Example**

The following example scans all items in a DynamoDB table.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx){
    return ddb.scan({
      limit: 20,
      projection: ['channel', 'path', 'msgId'],
      filter: { status: { eq: 'ACTIVE' } }
    })
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB `put()` function
<a name="ddb-put-function"></a>

The DynamoDB `put()` function generates a `DynamoDBPutItemRequest` object to make a `PutItem` request to DynamoDB.

**Definition**

```
put<T>(payload: PutInput): DynamoDBPutItemRequest
```

**Example**

The following example saves an event to a DynamoDB table in an `OnPublish` handler.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const {id, payload: item} = ctx.events[0]
    return ddb.put({ key: {id}, item })
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB `remove()` function
<a name="ddb-remove-function"></a>

The DynamoDB `remove()` function generates a `DynamoDBDeleteItemRequest` object to make a `DeleteItem` request to DynamoDB.

**Definition**

```
remove<T>(payload: RemoveInput): DynamoDBDeleteItemRequest
```

**Example**

This `OnPublish` handler deletes an item in a DynamoDB table and forwards an empty list. No event is broadcast.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const { id } = ctx.events[0]
    return ddb.remove({key: id});
  },
  response: (ctx) => ([])
}
```

### DynamoDB `update()` function
<a name="ddb-update-function"></a>

The DynamoDB `update()` function generates a `DynamoDBUpdateItemRequest` object to make an `UpdateItem` request to DynamoDB.

**Definition**

```
update<T>(payload: UpdateInput): DynamoDBUpdateItemRequest
```

**Example**

This `OnPublish` handler increases the account received item before it is broadcast.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const { id, payload } = ctx.events[0]
    return ddb.update({
      key: { id },
      condition: { version: { eq: payload.version } },
      update: { ...payload, version: ddb.operations.increment(1) },
    });
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB `batchGet()` function
<a name="ddb-batchget-function"></a>

The DynamoDB `batchGet()` function generates a `DynamoDBBatchGetItemRequest` object to make an `BatchGetItem` request to retrieve multiple items from one or more DynamoDB tables.

**Definition**

```
batchGet<T>(payload: BatchGetInput): DynamoDBBatchGetItemRequest
```

**Example**

The following example retrieves multiple items from a DynamoDB table in a single request/

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    return ddb.batchGet({
      tables: {
        users: {
          keys: ctx.events.map(e => ({id: e.payload.id})),
          projection: ['id', 'name', 'email']
        }
      }
    })
  },
  response(ctx) {
    const users = ctx.result.data.users.reduce((acc, cur) => {
      acc[cur.id] = cur
    }, {})
    return ctx.events.map(event => {
      return {
        id: event.id,
        payload: {...event.payload, ...users[event.payload.id]}
      }
    })
  }
}
```

### DynamoDB `batchPut()` function
<a name="ddb-batchput-function"></a>

The DynamoDB `batchput()` function generates a `DynamoDBBatchPutItemRequest` object to make an `BatchWriteItem` request to put multiple items into one or more DynamoDB tables.

**Definition**

```
batchPut<T>(payload: BatchPutInput): DynamoDBBatchPutItemRequest
```

**Example**

The following example writes multiple items to a DynamoDB table in a single request.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    return ddb.batchPut({
      tables: {
        messages: ctx.events.map(({ id, payload }) => ({
          channel: ctx.info.channelNamespace.name,
          id,
          ...payload
        })),
      }
    });
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB `batchDelete()` function
<a name="ddb-batchdelete-function"></a>

The DynamoDB `batchDelete()` function generates a `DynamoDBBatchDeleteItemRequest` object to make an `BatchWriteItem` request to delete multiple items from one or more DynamoDB tables.

**Definition**

```
batchDelete(payload: BatchDeleteInput): DynamoDBBatchDeleteItemRequest
```

**Example**

The following example deletes multiple items from a DynamoDB table in a single request.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const name = ctx.info.channelNamespace.name
    return ddb.batchDelete({
      tables: {
        [name]: ctx.events.map(({ payload }) => ({ id: payload.id })),
      }
    });
  },
  response: (ctx) => ([])
}
```

### DynamoDB `transactGet()` function
<a name="ddb-transactget-function"></a>

The DynamoDB `transactGet()` function generates a `DynamoDBTransactGetItemsRequest` object to make an `TransactGetItems` request to retrieve multiple items with strong consistency in a single atomic transaction.

**Definition**

```
transactGet(payload: TransactGetInput): DynamoDBTransactGetItemsRequest
```

**Example**

The following example retrieves multiple items in a single atomic transaction.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    return ddb.transactGet({
      items: ctx.events.map(event => ({
        table: event.payload.table,
        key: { id: event.payload.id },
        projection: [...event.payload.fields]
      }))
    })
  },
  response(ctx) {
    items = ctx.result.items
    return ctx.events.map((event, i) => ({
      id: event.id,
      payload: { ...event.payload, ...items[i] }
    }))
  }
}
```

### DynamoDB `transactWrite()` function
<a name="ddb-transactwrite-function"></a>

The DynamoDB `transactWrite()` function generates a `DynamoDBTransactWriteItemsRequest` object to make an `TransactWriteItems` request to perform multiple write operations in a single atomic transaction.

**Definition**

```
transactWrite(payload: TransactWriteInput): DynamoDBTransactWriteItemsRequest
```

**Example**

The following example performs multiple write operations in a single atomic transaction.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const order = ctx.events[0]
    return ddb.transactWrite({
      items: [
        {
          putItem: {
            table: 'Orders',
            key: { id: order.payload.id },
            item: {
              status: 'PENDING',
              createdAt: util.time.toISOString(),
              items: order.items.map(({ id }) => id)
            }
          }
        },
        ...(order.items.map(({ id, item }) => ({
          putItem: {
            table: 'Items',
            key: { orderId: order.payload.id, id },
            item
          }
        })))
      ]
    });
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB set utilities
<a name="built-in-ddb-modules-set-utilities"></a>

The `@aws-appsync/utils/dynamodb` provides the following `set` utility functions that you can use to work with string sets, number sets, and binary sets.

 **`toStringSet`**
Converts a list of strings to the DynamoDB string set format.

 **`toNumberSet`**
Converts a list of numbers to the DynamoDB string set format.

 **`toBinarySet`**
Converts a list of binary to the DynamoDB string set format.

**Example**

The following example converts a list of strings to DynamoDB string set format.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    const { id, payload } = ctx.events[0]
    return ddb.update({
      key: { id },
      update: {segments: ddb.toStringSet(ctx.info.channel.segments)},
    });
  },
  response: (ctx) => ctx.events
}
```

### DynamoDB conditions and filters
<a name="built-in-ddb-modules-conditions-filters"></a>

You can use the following operators to create filters and conditions.

|
|
| Operator | Description | Possible value types |
| --- |--- |--- |
| eq | Equal | number, string, boolean |
| ne | Not equal | number, string, boolean |
| le | Less than or equal | number, string |
| lt | Less than | number, string |
| ge | Greater than or equal | number, string |
| gt | Greater than | number, string |
| contains | Like | string |
| notContains | Not like | string |
| beginsWith | Starts with prefix | string |
| between | Between two values | number, string |
| attributeExists | The attribute is not null | number, string, boolean |
| size | checks the length of the element | string |

You can combine these operators with `and`, `or`, and `not`.

```
const condition = {
  and: [
    { name: { eq: 'John Doe' }},
    { age: { between: [10, 30] }},
    {or: [
      {id :{ attributeExists: true}}
    ]}
  ]
}
```

### DynamoDB operations
<a name="built-in-ddb-modules-operations"></a>

The DynamoDB operations object provides utility functions for common DynamoDB operations. These utilities are particularly useful in update() function calls.

The following operations are available:

 **`add(value)`**
A helper function that adds a a value to the item when updating DynamoDB.

 **`remove()`**
A helper function that removes an attribute from an item when updating DynamoDB.

**`replace(value)`**
A helper function that replaces an existing attribute when updating an item in DynamoDB. This is useful for when you want to update the entire object or sub-object in the attribute.

**`increment(amount)`**
A helper function that increments a numeric attribute by the specified amount when updating DynamoDB.

**`decrement(amount)`**
A helper function that decrements a numeric attribute by the specified amount when updating DynamoDB.

**`append(value)`**
A helper function that appends a value to a list attribute in DynamoDB.

**`prepend(value)`**
A helper function that prepends a value to a list attribute in DynamoDB.

**`updateListItem(value, index)`**
A helper function that updates an item in a list.

**Example**

The following example demonstrates how to use various operations in an update request.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
request(ctx) {
  return ddb.update({
    key: { id },
    update: {
      counter: ddb.operations.increment(1),
      tags: ddb.operations.append(['things']),
      items: ddb.operations.add({key: 'value'}),
      oldField: ddb.operations.remove(),
    },
  });
}

export function response(ctx) {
  return ctx.result;
}
```

### Inputs
<a name="built-in-ddb-modules-inputs"></a>

 **`Type GetInput<T>`**

```
GetInput<T>: {
    consistentRead?: boolean;
    key: DynamoDBKey<T>;
}
```
**Type Declaration**
+ `consistentRead?: boolean` (optional)

  An optional boolean to specify whether you want to perform a strongly consistent read with DynamoDB.
+ `key: DynamoDBKey<T>` (required)

  A required parameter that specifies the key of the item in DynamoDB. DynamoDB items may have a single hash key or hash and sort keys.

**`Type PutInput<T>`**

```
PutInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T> | null;
    customPartitionKey?: string;
    item: Partial<T>;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
}
```
**Type Declaration**
+ `_version?: number` (optional)
+ `condition?: DynamoDBFilterObject<T> | null` (optional)

  When you put an object in a DynamoDB table, you can optionally specify a conditional expression that controls whether the request should succeed or not based on the state of the object already in DynamoDB before the operation is performed.
+ `customPartitionKey?: string` (optional)

  When enabled, this string value modifies the format of the `ds_sk` and `ds_pk` records used by the delta sync table when versioning has been enabled. When enabled, the processing of the `populateIndexFields` entry is also enabled.
+ `item: Partial<T>` (required)

  The rest of the attributes of the item to be placed into DynamoDB.
+ `key: DynamoDBKey<T>` (required)

  A required parameter that specifies the key of the item in DynamoDB on which the put will be performed. DynamoDB items may have a single hash key or hash and sort keys.
+ `populateIndexFields?: boolean` (optional)

  A boolean value that, when enabled along with the `customPartitionKey`, creates new entries for each record in the delta sync table, specifically in the `gsi_ds_pk` and `gsi_ds_sk` columns. For more information, see [Conflict detection and sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) in the *AWS AppSync GraphQL Developer Guide*.

**`Type QueryInput<T>`**

```
QueryInput<T>: ScanInput<T> & {
    query: DynamoDBKeyCondition<Required<T>>;
}
```
**Type Declaration**
+ `query: DynamoDBKeyCondition<Required<T>>` (required)

  Specifies a key condition that describes items to query. For a given index, the condition for a partition key should be an equality and the sort key a comparison or a `beginsWith` (when it's a string). Only number and string types are supported for partition and sort keys.

  **Example**

  Take the `User` type below:

  ```
  type User = {
    id: string;
    name: string;
    age: number;
    isVerified: boolean;
    friendsIds: string[]
  }
  ```

  The query can only include the following fields: `id`, `name`, and `age`:

  ```
  const query: QueryInput<User> = {
      name: { eq: 'John' },
      age: { gt: 20 },
  }
  ```

**`Type RemoveInput<T>`**

```
RemoveInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T>;
    customPartitionKey?: string;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
}
```
**Type Declaration**
+ `_version?: number` (optional)
+ `condition?: DynamoDBFilterObject<T>` (optional)

  When you remove an object in DynamoDB, you can optionally specify a conditional expression that controls whether the request should succeed or not based on the state of the object already in DynamoDB before the operation is performed.

  **Example**

  The following example is a `DeleteItem` expression containing a condition that allows the operation succeed only if the owner of the document matches the user making the request.

  ```
  type Task = {
    id: string;
    title: string;
    description: string;
    owner: string;
    isComplete: boolean;
  }
  const condition: DynamoDBFilterObject<Task> = {
    owner: { eq: 'XXXXXXXXXXXXXXXX' },
  }

  remove<Task>({
     key: {
       id: 'XXXXXXXXXXXXXXXX',
    },
    condition,
  });
  ```
+ `customPartitionKey?: string` (optional)

  When enabled, the `customPartitionKey` value modifies the format of the `ds_sk` and `ds_pk` records used by the delta sync table when versioning has been enabled. When enabled, the processing of the `populateIndexFields` entry is also enabled.
+ `key: DynamoDBKey<T>` (required)

  A required parameter that specifies the key of the item in DynamoDB that is being removed. DynamoDB items may have a single hash key or hash and sort keys.

  **Example**

  If a `User` only has the hash key with a user `id`, then the key would look like this:

  ```
  type User = {
  	id: number
  	name: string
  	age: number
  	isVerified: boolean
  }
  const key: DynamoDBKey<User> = {
  	id: 1,
  }
  ```

  If the table user has a hash key (`id`) and sort key (`name`), then the key would look like this:

  ```
  type User = {
  	id: number
  	name: string
  	age: number
  	isVerified: boolean
  	friendsIds: string[]
  }

  const key: DynamoDBKey<User> = {
  	id: 1,
  	name: 'XXXXXXXXXX',
  }
  ```
+ `populateIndexFields?: boolean` (optional)

  A boolean value that, when enabled along with the `customPartitionKey`, creates new entries for each record in the delta sync table, specifically in the `gsi_ds_pk` and `gsi_ds_sk` columns.

**`Type ScanInput<T>`**

```
ScanInput<T>: {
    consistentRead?: boolean | null;
    filter?: DynamoDBFilterObject<T> | null;
    index?: string | null;
    limit?: number | null;
    nextToken?: string | null;
    scanIndexForward?: boolean | null;
    segment?: number;
    select?: DynamoDBSelectAttributes;
    totalSegments?: number;
}
```
**Type Declaration**
+ `consistentRead?: boolean | null` (optional)

  An optional boolean to indicate consistent reads when querying DynamoDB. The default value is `false`.
+ `filter?: DynamoDBFilterObject<T> | null` (optional)

  An optional filter to apply to the results after retrieving it from the table.
+ `index?: string | null` (optional)

  An optional name of the index to scan.
+ `limit?: number | null` (optional)

  An optional max number of results to return.
+ `nextToken?: string | null` (optional)

  An optional pagination token to continue a previous query. This would have been obtained from a previous query.
+ `scanIndexForward?: boolean | null` (optional)

  An optional boolean to indicate whether the query is performed in ascending or descending order. By default, this value is set to `true`.
+ `segment?: number` (optional)
+ `select?: DynamoDBSelectAttributes` (optional)

  Attributes to return from DynamoDB. By default, the AWS AppSync DynamoDB resolver only returns attributes that are projected into the index. The supported values are:
  + `ALL_ATTRIBUTES`

    Returns all the item attributes from the specified table or index. If you query a local secondary index, DynamoDB fetches the entire item from the parent table for each matching item in the index. If the index is configured to project all item attributes, all of the data can be obtained from the local secondary index and no fetching is required.
  + `ALL_PROJECTED_ATTRIBUTES`

    Returns all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES`.
  + `SPECIFIC_ATTRIBUTES`

    Returns only the attributes listed in `ProjectionExpression`. This return value is equivalent to specifying `ProjectionExpression` without specifying any value for `AttributesToGet`.
+ `totalSegments?: number` (optional)

**`Type DynamoDBSyncInput<T>`**

```
DynamoDBSyncInput<T>: {
    basePartitionKey?: string;
    deltaIndexName?: string;
    filter?: DynamoDBFilterObject<T> | null;
    lastSync?: number;
    limit?: number | null;
    nextToken?: string | null;
}
```
**Type Declaration**
+ `basePartitionKey?: string` (optional)

  The partition key of the base table to be used when performing a Sync operation. This field allows a Sync operation to be performed when the table utilizes a custom partition key.
+ `deltaIndexName?: string` (optional)

  The index used for the Sync operation. This index is required to enable a Sync operation on the whole delta store table when the table uses a custom partition key. The Sync operation will be performed on the GSI (created on `gsi_ds_pk` and `gsi_ds_sk`).
+ `filter?: DynamoDBFilterObject<T> | null` (optional)

  An optional filter to apply to the results after retrieving it from the table.
+ `lastSync?: number` (optional)

  The moment, in epoch milliseconds, at which the last successful Sync operation started. If specified, only items that have changed after `lastSync` are returned. This field should only be populated after retrieving all pages from an initial Sync operation. If omitted, results from the base table will be returned. Otherwise, results from the delta table will be returned.
+ `limit?: number | null` (optional)

  An optional maximum number of items to evaluate at a single time. If omitted, the default limit will be set to `100` items. The maximum value for this field is `1000` items.
+ `nextToken?: string | null` (optional)

**`Type DynamoDBUpdateInput<T>`**

```
DynamoDBUpdateInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T>;
    customPartitionKey?: string;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
    update: DynamoDBUpdateObject<T>;
}
```
**Type Declaration**
+ `_version?: number` (optional)
+ `condition?: DynamoDBFilterObject<T>` (optional)

  When you update an object in DynamoDB, you can optionally specify a conditional expression that controls whether the request should succeed or not based on the state of the object already in DynamoDB before the operation is performed.
+ `customPartitionKey?: string` (optional)

  When enabled, the `customPartitionKey` value modifies the format of the `ds_sk` and `ds_pk` records used by the delta sync table when versioning has been enabled. When enabled, the processing of the `populateIndexFields` entry is also enabled.
+ `key: DynamoDBKey<T>` (required)

  A required parameter that specifies the key of the item in DynamoDB that is being updated. DynamoDB items may have a single hash key or hash and sort keys.
+ `populateIndexFields?: boolean` (optional)

  A boolean value that, when enabled along with the `customPartitionKey`, creates new entries for each record in the delta sync table, specifically in the `gsi_ds_pk` and `gsi_ds_sk` columns.
+ `update: DynamoDBUpdateObject<T>`

  An object that specifies the attributes to be updated along with the new values for them. The update object can be used with `add`, `remove`, `replace`, `increment`, `decrement`, `append`, `prepend`, `updateListItem`.

## Amazon RDS module functions
<a name="built-in-rds-modules"></a>

Amazon RDS module functions provide an enhanced experience when interacting with databases configured with the Amazon RDS Data API. The module is imported using `@aws-appsync/utils/rds`:

```
import * as rds from '@aws-appsync/utils/rds';
```

Functions can also be imported individually. For instance, the import below uses `sql`:

```
import { sql } from '@aws-appsync/utils/rds';
```

### Select
<a name="built-in-rds-modules-functions-select"></a>

The `select` utility creates a `SELECT` statement to query your relational database.

**Basic use**

In its basic form, you can specify the table you want to query.

```
import { select, createPgStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    // Generates statement:
    // "SELECT * FROM "persons"
    return createPgStatement(select({table: 'persons'}));
  }
}
```

You can also specify the schema in your table identifier:.

```
import { select, createPgStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT * FROM "private"."persons"
    return createPgStatement(select({table: 'private.persons'}));
  }
}
```

**Specifying columns**

You can specify columns with the `columns` property. If this isn't set to a value, it defaults to `*`.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name']
    }));
  }
}
```

You can also specify a column's table.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "persons"."name"
    // FROM "persons"
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'persons.name']
    }));
  }
}
```

**Limits and offsets**

You can apply `limit` and `offset` to the query.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // LIMIT :limit
    // OFFSET :offset
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        limit: 10,
        offset: 40
    }));
  }
}
```

**Order By**

You can sort your results with the `orderBy` property. Provide an array of objects specifying the column and an optional `dir` property.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name" FROM "persons"
    // ORDER BY "name", "id" DESC
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        orderBy: [{column: 'name'}, {column: 'id', dir: 'DESC'}]
    }));
  }
}
```

**Filters**

You can build filters by using the special condition object.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: {name: {eq: 'Stephane'}}
    }));
  }
}
```

You can also combine filters.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME and "id" > :ID
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: {name: {eq: 'Stephane'}, id: {gt: 10}}
    }));
  }
}
```

You can create `OR` statements.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME OR "id" > :ID
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: { or: [
            { name: { eq: 'Stephane' } },
            { id: { gt: 10 } }
        ]}
    }));
  }
}
```

You can negate a condition with `not`.

```
export const onPublish = {
  request(ctx) {
    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE NOT ("name" = :NAME AND "id" > :ID)
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: { not: [
            { name: { eq: 'Stephane' } },
            { id: { gt: 10 } }
        ]}
    }));
  }
}
```

You can also use the following operators to compare values:

|
|
| Operator | Description | Possible value types |
| --- |--- |--- |
| eq | Equal | number, string, boolean |
| ne | Not equal | number, string, boolean |
| le | Less than or equal | number, string |
| lt | Less than | number, string |
| ge | Greater than or equal | number, string |
| gt | Greater than | number, string |
| contains | Like | string |
| notContains | Not like | string |
| beginsWith | Starts with prefix | string |
| between | Between two values | number, string |
| attributeExists | The attribute is not null | number, string, boolean |
| size | checks the length of the element | string |

### Insert
<a name="built-in-rds-modules-functions-insert"></a>

The `insert` utility provides a straightforward way of inserting single row items in your database with the `INSERT` operation.

**Single item insertions**

To insert an item, specify the table and then pass in your object of values. The object keys are mapped to your table columns. Columns names are automatically escaped, and values are sent to the database using the variable map.

```
import { insert, createMySQLStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({ table: 'persons', values });

    // Generates statement:
    // INSERT INTO `persons`(`name`)
    // VALUES(:NAME)
    return createMySQLStatement(insertStatement);
  }
}
```

**MySQL use case**

You can combine an `insert` followed by a `select` to retrieve your inserted row.

```
import { insert, select, createMySQLStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({ table: 'persons', values });
    const selectStatement = select({
        table: 'persons',
        columns: '*',
        where: { id: { eq: values.id } },
        limit: 1,
    });

    // Generates statement:
    // INSERT INTO `persons`(`name`)
    // VALUES(:NAME)
    // and
    // SELECT *
    // FROM `persons`
    // WHERE `id` = :ID
    return createMySQLStatement(insertStatement, selectStatement);
  }
}
```

**Postgres use case**

With Postgres, you can use [`returning`](https://www.postgresql.org/docs/current/dml-returning.html) to obtain data from the row that you inserted. It accepts `*` or an array of column names:

```
import { insert, createPgStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({
        table: 'persons',
        values,
        returning: '*'
    });

    // Generates statement:
    // INSERT INTO "persons"("name")
    // VALUES(:NAME)
    // RETURNING *
    return createPgStatement(insertStatement);
  }
}
```

### Update
<a name="built-in-rds-modules-functions-update"></a>

The `update` utility allows you to update existing rows. You can use the condition object to apply changes to the specified columns in all the rows that satisfy the condition. For example, let's presume that we have a schema that allows us to make this mutation. The following example updates the `name` of `Person` with the `id` value of `3` but only if we've known them (`known_since`) since the year `2000`.

```
mutation Update {
    updatePerson(
        input: {id: 3, name: "Jon"},
        condition: {known_since: {ge: "2000"}}
    ) {
    id
    name
  }
}
```

Our update handler looks like the following:

```
import { update, createPgStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const { input: { id, ...values }, condition } = ctx.args;
    const where = {
        ...condition,
        id: { eq: id },
    };
    const updateStatement = update({
        table: 'persons',
        values,
        where,
        returning: ['id', 'name'],
    });

    // Generates statement:
    // UPDATE "persons"
    // SET "name" = :NAME, "birthday" = :BDAY, "country" = :COUNTRY
    // WHERE "id" = :ID
    // RETURNING "id", "name"
    return createPgStatement(updateStatement);
  }
}
```

We can add a check to our condition to make sure that only the row that has the primary key `id` equal to `3` is updated. Similarly, for Postgres `inserts`, you can use `returning` to return the modified data.

### Remove
<a name="built-in-rds-modules-functions-remove"></a>

The `remove` utility allows you to delete existing rows. You can use the condition object on all rows that satisfy the condition. Note that `delete` is a reserved keyword in JavaScript. Use `remove` instead.

```
import { remove, createPgStatement } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const { input: { id }, condition } = ctx.args;
    const where = { ...condition, id: { eq: id } };
    const deleteStatement = remove({
        table: 'persons',
        where,
        returning: ['id', 'name'],
    });

    // Generates statement:
    // DELETE "persons"
    // WHERE "id" = :ID
    // RETURNING "id", "name"
    return createPgStatement(deleteStatement);
  }
}
```

### Casting
<a name="built-in-rds-modules-casting"></a>

In some cases, you might require more specificity about the correct object type to use in your statement. You can use the provided type hints to specify the type of your parameters. AWS AppSync supports the [same type hints](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_SqlParameter.html#rdsdtataservice-Type-SqlParameter-typeHint) as the Data API. You can cast your parameters by using the `typeHint` functions from the AWS AppSync `rds` module.

The following example allows you to send an array as a value that is casted as a JSON object. We use the `->` operator to retrieve the element at the `index` `2` in the JSON array.

```
import { sql, createPgStatement, toJsonObject, typeHint } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const arr = ctx.args.list_of_ids
    const statement = sql`select ${typeHint.JSON(arr)}->2 as value`
    return createPgStatement(statement)
  }
}
```

Casting is also useful when handling and comparing `DATE`, `TIME`, and `TIMESTAMP`:

```
import { select, createPgStatement, typeHint } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const when = ctx.args.when
    const statement = select({
        table: 'persons',
        where: { createdAt : { gt: typeHint.DATETIME(when) } }
    })
    return createPgStatement(statement)
  }
}
```

The following example demonstrates how to send the current date and time.

```
import { sql, createPgStatement, typeHint } from '@aws-appsync/utils/rds';

export const onPublish = {
  request(ctx) {
    const now = util.time.nowFormatted('YYYY-MM-dd HH:mm:ss')
    return createPgStatement(sql`select ${typeHint.TIMESTAMP(now)}`)
  }
}
```

**Available type hints**
+ `typeHint.DATE` — The corresponding parameter is sent as an object of the `DATE` type to the database. The accepted format is `YYYY-MM-DD`.
+ `typeHint.DECIMAL` — The corresponding parameter is sent as an object of the `DECIMAL` type to the database.
+ `typeHint.JSON` — The corresponding parameter is sent as an object of the `JSON` type to the database.
+ `typeHint.TIME` — The corresponding string parameter value is sent as an object of the `TIME` type to the database. The accepted format is `HH:MM:SS[.FFF]`.
+ `typeHint.TIMESTAMP` — The corresponding string parameter value is sent as an object of the `TIMESTAMP` type to the database. The accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]`.
+ `typeHint.UUID` — The corresponding string parameter value is sent as an object of the `UUID` type to the database.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
