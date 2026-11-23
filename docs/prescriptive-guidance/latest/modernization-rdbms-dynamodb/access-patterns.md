---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/access-patterns.html
---

# Access patterns

As mentioned earlier in this guide, you can choose from three access patterns to perform create, read, update, and delete (CRUD) operations on DynamoDB tables: object persistence interface, document interfaces, and low-level API interface. The following sections describe each interface. For our SQL Server to DynamoDB use case, we chose the object persistence interface for simplicity, readability, and ease of maintenance.

## Object persistence interface
<a name="object-persistence-interface"></a>

The object persistence interface provides a high-level, abstracted access mechanism for performing CRUD operations on DynamoDB items by using .NET models, similar to Entity Framework entities. The interface properties map to DynamoDB item attributes. The AWS SDK for .NET supports custom property attributes in this model to customize the serialization and deserialization of individual properties, to handle null values, and for type conversions.

Sample model used in the application:

```
[DynamoDBTable("AppLibrary")]
public class ProdApp
{
      [DynamoDBHashKey]
      public string PK { get; set; }     //Partition key

      [DynamoDBRangeKey]
      public string SK { get; set; }     //Sort key

      [DynamoDBGlobalSecondaryIndexRangeKey("Version-index")]
      [DynamoDBProperty]
      public int Version { get; set; }
       . . .
      [DynamoDBProperty]
      public Int64 TTL { get; set; }
}
```

Item access:

```
var _dynamoDbClient = new AmazonDynamoDBClient(AWSCredentials);
var _context = new DynamoDBContext(_dynamoDbClient);

public ProdApp GetProdAppById (Guid id, int version)
{
     var pk = $"{id}-{version}";
     return _context.Load(pk, ItemType.ProductionApplication);
}
```

For more information, see [Object persistence interface](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKs.Interfaces.Mapper.html) in the DynamoDB documentation.

## Document interfaces
<a name="document-interface"></a>

The document interfaces model provides document-based access (similar to XMLDocument in .NET) to a DynamoDB item. This model provides a higher-level programming interface, but  translates its calls to low-level APIs to perform the operation.

```
var _dynamoDbClient = new AmazonDynamoDBClient(AWSCredentials);
var _table = Table.LoadTable(_dynamoDbClient, "AppLibrary");

public ProdApp GetProdAppById (Guid id, int version)
{
      var pk = $"{id}-{version}";
     var doc = _table.GetItem(pk, ItemType.ProductionApplication);
      var app = new ProdApp {
          PK = doc["PK"],
          SK = doc["SK"],
          Version = doc["Version"],
          . . .
      };
      return app;
 }
```

For more information, see [Document interfaces](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKs.Interfaces.Document.html) in the DynamoDB documentation.

## Low-level API
<a name="low-level-api"></a>

The AWS SDK for DynamoDB also provides low-level API access to perform CRUD operations by using the **PutItem**,  **GetItem**,  **UpdateItem**,  and **DeleteItem** methods. This model provides complete control over attribute mapping and type conversions. The response for these calls is a dictionary of key-value pairs.

```
[DynamoDBTable("AppLibrary")]
public class ProdApp
{
        [DynamoDBHashKey]
        public string PK { get; set; }     //Partition key

        [DynamoDBRangeKey]
         public string SK { get; set; }     //Sort key

        [DynamoDBGlobalSecondaryIndexRangeKey("Version-index")]
        [DynamoDBProperty]
        public int Version { get; set; }
              . . .
        [DynamoDBProperty]
        public ProdConfig Config  { get; set; }
}

var _dynamoDbClient = new AmazonDynamoDBClient(AWSCredentials);

public ProdApp GetProdAppById (Guid id, int version)
{
    var pk = $"{id}-{version}";
    var resp = _dynamoDbClient.Query(queryRequest);
    var item = resp.Items[0];
    var app = new ProdApp {
         PK = item["PK"].S,
         SK = item["SK"].S,
         Version = Convert.ToInt32(item["Version"].S),
         . . .
         Config = new ProdConfig {
               Name = item["Config"].M["Name"].S,
               Id = Conver.ToInt32(item["Config"].M["Id"].S)
         }
    };
    return app;
 }
```

For more information, see [Low-level interfaces](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKs.Interfaces.LowLevel.html) in the DynamoDB documentation.
