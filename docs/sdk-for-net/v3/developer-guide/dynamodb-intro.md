---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/dynamodb-intro.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Using Amazon DynamoDB NoSQL databases
<a name="dynamodb-intro"></a>

**Note**
The programming models in these topics are present in both .NET Framework and .NET (Core), but the calling conventions differ, whether synchronous or asynchronous.

The AWS SDK for .NET supports Amazon DynamoDB, which is a fast NoSQL database service offered by AWS. The SDK provides three programming models for communicating with DynamoDB: the *low-level* model, the *document* model, and the *object persistence* model.

The following information introduces these models and their APIs, provides examples for how and when to use them, and gives you links to additional DynamoDB programming resources in the AWS SDK for .NET.

## Low-Level Model
<a name="dynamodb-intro-apis-low-level"></a>

The low-level programming model wraps direct calls to the DynamoDB service. You access this model through the [Amazon.DynamoDBv2](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/NDynamoDBv2.html) namespace.

Of the three models, the low-level model requires you to write the most code. For example, you must convert .NET data types to their equivalents in DynamoDB. However, this model gives you access to the most features.

The following examples show you how to use the low-level model to create a table, modify a table, and insert items into a table in DynamoDB.

### Creating a Table
<a name="dynamodb-intro-apis-low-level-create-table"></a>

In the following example, you create a table by using the `CreateTable` method of the `AmazonDynamoDBClient` class. The `CreateTable` method uses an instance of the `CreateTableRequest` class that contains characteristics such as required item attribute names, primary key definition, and throughput capacity. The `CreateTable` method returns an instance of the `CreateTableResponse` class.

```
// using Amazon.DynamoDBv2;
// using Amazon.DynamoDBv2.Model;

var client = new AmazonDynamoDBClient();

Console.WriteLine("Getting list of tables");
List<string> currentTables = client.ListTables().TableNames;
Console.WriteLine("Number of tables: " + currentTables.Count);
if (!currentTables.Contains("AnimalsInventory"))
{
    var request = new CreateTableRequest
    {
        TableName = "AnimalsInventory",
        AttributeDefinitions = new List<AttributeDefinition>
      {
        new AttributeDefinition
        {
          AttributeName = "Id",
          // "S" = string, "N" = number, and so on.
          AttributeType = "N"
        },
        new AttributeDefinition
        {
          AttributeName = "Type",
          AttributeType = "S"
        }
      },
        KeySchema = new List<KeySchemaElement>
      {
        new KeySchemaElement
        {
          AttributeName = "Id",
          // "HASH" = hash key, "RANGE" = range key.
          KeyType = "HASH"
        },
        new KeySchemaElement
        {
          AttributeName = "Type",
          KeyType = "RANGE"
        },
      },
        ProvisionedThroughput = new ProvisionedThroughput
        {
            ReadCapacityUnits = 10,
            WriteCapacityUnits = 5
        },
    };

    var response = client.CreateTable(request);

    Console.WriteLine("Table created with request ID: " +
      response.ResponseMetadata.RequestId);
}
```

### Verifying That a Table is Ready to Modify
<a name="dynamodb-intro-apis-low-level-verify-table"></a>

Before you can change or modify a table, the table has to be ready for modification. The following example shows how to use the low-level model to verify that a table in DynamoDB is ready. In this example, the target table to check is referenced through the `DescribeTable` method of the `AmazonDynamoDBClient` class. Every five seconds, the code checks the value of the table’s `TableStatus` property. When the status is set to `ACTIVE`, the table is ready to be modified.

```
// using Amazon.DynamoDBv2;
// using Amazon.DynamoDBv2.Model;

var client = new AmazonDynamoDBClient();
var status = "";

do
{
  // Wait 5 seconds before checking (again).
  System.Threading.Thread.Sleep(TimeSpan.FromSeconds(5));

  try
  {
    var response = client.DescribeTable(new DescribeTableRequest
    {
      TableName = "AnimalsInventory"
    });

    Console.WriteLine("Table = {0}, Status = {1}",
      response.Table.TableName,
      response.Table.TableStatus);

    status = response.Table.TableStatus;
  }
  catch (ResourceNotFoundException)
  {
    // DescribeTable is eventually consistent. So you might
    //   get resource not found.
  }

} while (status != TableStatus.ACTIVE);
```

### Inserting an Item into a Table
<a name="dynamodb-intro-apis-low-level-insert-item"></a>

In the following example, you use the low-level model to insert two items into a table in DynamoDB. Each item is inserted through the `PutItem` method of the `AmazonDynamoDBClient` class, using an instance of the `PutItemRequest` class. Each of the two instances of the `PutItemRequest` class takes the name of the table that the items will be inserted in, with a series of item attribute values.

```
// using Amazon.DynamoDBv2;
// using Amazon.DynamoDBv2.Model;

var client = new AmazonDynamoDBClient();

var request1 = new PutItemRequest
{
  TableName = "AnimalsInventory",
  Item = new Dictionary<string, AttributeValue>
  {
    { "Id", new AttributeValue { N = "1" }},
    { "Type", new AttributeValue { S = "Dog" }},
    { "Name", new AttributeValue { S = "Fido" }}
  }
};

var request2 = new PutItemRequest
{
  TableName = "AnimalsInventory",
  Item = new Dictionary<string, AttributeValue>
  {
    { "Id", new AttributeValue { N = "2" }},
    { "Type", new AttributeValue { S = "Cat" }},
    { "Name", new AttributeValue { S = "Patches" }}
  }
};

client.PutItem(request1);
client.PutItem(request2);
```

## Document Model
<a name="dynamodb-intro-apis-document"></a>

The document programming model provides an easier way to work with data in DynamoDB. This model is specifically intended for accessing tables and items in tables. You access this model through the [Amazon.DynamoDBv2.DocumentModel](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/NDynamoDBv2DocumentModel.html) namespace.

Compared to the low-level programming model, the document model is easier to code against DynamoDB data. For example, you don’t have to convert as many .NET data types to their equivalents in DynamoDB. However, this model doesn’t provide access to as many features as the low-level programming model. For example, you can use this model to create, retrieve, update, and delete items in tables. However, to create the tables, you must use the low-level model. Compared to the object persistence model, this model requires you to write more code to store, load, and query .NET objects.

For more information about the DynamoDB document programming model, see [.NET: Document model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKMidLevel.html) in the [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

The following sections provide information about how to create a representation of the desired DynamoDB table, and examples about how to use the document model to insert items into tables and get items from tables.

### Create a representation of the table
<a name="dynamodb-intro-apis-document-table"></a>

To perform data operations using the document model, you must first create an instance of the `Table` class that represents a specific table. There are two primary ways to do this.

**LoadTable method**

The first mechanism is to use one of the static `LoadTable` methods of the [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTable.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTable.html) class, similar to the following example:

```
var client = new AmazonDynamoDBClient();
Table table = Table.LoadTable(client, "Reply");
```

**Note**
While this mechanism works, under certain conditions, it can sometimes lead to additional latency or deadlocks due to cold-start and thread-pool behaviors. For more information about these behaviors, see the blog post [Improved DynamoDB Initialization Patterns for the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/improved-dynamodb-initialization-patterns-for-the-aws-sdk-for-net/).

**TableBuilder**

An alternative mechanism, the [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTableBuilder.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTableBuilder.html) class, was introduced in [version 3.7.203 of the AWSSDK.DynamoDBv2 NuGet package](https://www.nuget.org/packages/AWSSDK.DynamoDBv2/3.7.203). This mechanism can address the behaviors mentioned above by removing certain implicit method calls; specifically, the `DescribeTable` method. This mechanism is used in a manner similar to the following example:

```
var client = new AmazonDynamoDBClient();
var table = new TableBuilder(client, "Reply")
    .AddHashKey("Id", DynamoDBEntryType.String)
    .AddRangeKey("ReplyDateTime", DynamoDBEntryType.String)
    .AddGlobalSecondaryIndex("PostedBy-Message-index", "Author", DynamoDBEntryType.String, "Message", DynamoDBEntryType.String)
    .Build();
```

For more information about this alternative mechanism, see again the blog post [Improved DynamoDB Initialization Patterns for the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/improved-dynamodb-initialization-patterns-for-the-aws-sdk-for-net/).

### Inserting an item into a table
<a name="dynamodb-intro-apis-document-insert-item"></a>

In the following example, a reply is inserted into the Reply table through the `PutItemAsync` method of the `Table` class. The `PutItemAsync` method takes an instance of the `Document` class; the `Document` class is simply a collection of initialized attributes.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DocumentModel;

// Create a representation of the "Reply" table
//  by using one of the mechanisms described previously.

// Then, add a reply to the table.
var newReply = new Document();
newReply["Id"] = Guid.NewGuid().ToString();
newReply["ReplyDateTime"] = DateTime.UtcNow;
newReply["PostedBy"] = "Author1";
newReply["Message"] = "Thank you!";

await table.PutItemAsync(newReply);
```

### Getting an item from a table
<a name="dynamodb-intro-apis-document-get-item"></a>

In the following example, a reply is retrieved through the `GetItemAsync` method of the `Table` class. To determine the reply to get, the `GetItemAsync` method uses the hash-and-range primary key of the target reply.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DocumentModel;

// Create a representation of the "Reply" table
//  by using one of the mechanisms described previously.

// Then, get a reply from the table
//  where "guid" is the hash key and "datetime" is the range key.
var reply = await table.GetItemAsync(guid, datetime);
Console.WriteLine("Id = " + reply["Id"]);
Console.WriteLine("ReplyDateTime = " + reply["ReplyDateTime"]);
Console.WriteLine("PostedBy = " + reply["PostedBy"]);
Console.WriteLine("Message = " + reply["Message"]);
```

The preceding example implicitly converts the table values to strings for the `WriteLine` method. You can do explicit conversions by using the various "As[type]" methods of the `DynamoDBEntry` class. For example, you can explicitly convert the value for `Id` from a `Primitive` data type to a GUID through the `AsGuid()` method:

```
var guid = reply["Id"].AsGuid();
```

## Object Persistence Model
<a name="dynamodb-intro-apis-object-persistence"></a>

The object persistence programming model is specifically designed for storing, loading, and querying .NET objects in DynamoDB. You access this model through the [Amazon.DynamoDBv2.DataModel](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/NDynamoDBv2DataModel.html) namespace.

Of the three models, the object persistence model is the easiest to code against whenever you are storing, loading, or querying DynamoDB data. For example, you work with DynamoDB data types directly. However, this model provides access only to operations that store, load, and query .NET objects in DynamoDB. For example, you can use this model to create, retrieve, update, and delete items in tables. However, you must first create your tables using the low-level model, and then use this model to map your .NET classes to the tables.

For more information about the DynamoDB object persistence programming model, see [.NET: Object persistence model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html) in the [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

The following examples show you how to define a .NET class that represents a DynamoDB item, use an instance of the .NET class to insert an item into a DynamoDB table, and use an instance of the .NET class to get an item from the table.

### Defining a .NET class that represents an item in a table
<a name="dynamodb-intro-apis-object-persistence-net-class-item"></a>

In the following example of a class definition, the `DynamoDBTable` attribute specifies the table name, while the `DynamoDBHashKey` and `DynamoDBRangeKey` attributes model the table's hash-and-range primary key. The `DynamoDBGlobalSecondaryIndexHashKey` attribute is defined so that a query for replies by a specific author can be constructed.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

[DynamoDBTable("Reply")]
public class Reply
{
    [DynamoDBHashKey]
    public string Id { get; set; }

    [DynamoDBRangeKey(StoreAsEpoch = false)]
    public DateTime ReplyDateTime { get; set; }

    [DynamoDBGlobalSecondaryIndexHashKey("PostedBy-Message-Index",
        AttributeName ="PostedBy")]
    public string Author { get; set; }

    [DynamoDBGlobalSecondaryIndexRangeKey("PostedBy-Message-Index")]
    public string Message { get; set; }
}
```

### Creating a context for the object persistence model
<a name="dynamodb-intro-apis-object-persistence-context"></a>

To use the object persistence programming model for DynamoDB, you must create a context, which provides a connection to DynamoDB and enables you to access tables, perform various operations, and run queries.

**Basic context**

The following example shows how to create the most basic context.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

var client = new AmazonDynamoDBClient();
var context = new DynamoDBContext(client);
```

**Context with DisableFetchingTableMetadata property**

The following example shows how you might additionally set the `DisableFetchingTableMetadata` property of the `DynamoDBContextConfig` class to prevent implicit calls to the `DescribeTable` method.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

var client = new AmazonDynamoDBClient();
var context = new DynamoDBContext(client, new DynamoDBContextConfig
{
    DisableFetchingTableMetadata = true
});
```

If the `DisableFetchingTableMetadata` property is set to `false` (the default), as shown in the first example, you can omit attributes that describe the key and index structure of table items from the `Reply` class. These attributes will instead be inferred through an implicit call to the `DescribeTable` method. If `DisableFetchingTableMetadata` is set to `true`, as shown in the second example, methods of the object persistence model such as `SaveAsync` and `QueryAsync` rely entirely on the attributes defined in the `Reply` class. In this case, a call to the `DescribeTable` method doesn't occur.

**Note**
Under certain conditions, calls to the `DescribeTable` method can sometimes lead to additional latency or deadlocks due to cold-start and thread-pool behaviors. For this reason, it is sometimes advantageous to avoid calls to that method.
For more information about these behaviors, see the blog post [Improved DynamoDB Initialization Patterns for the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/improved-dynamodb-initialization-patterns-for-the-aws-sdk-for-net/).

### Using an instance of the .NET class to insert an item into a table
<a name="dynamodb-intro-apis-object-persistence-net-insert-item"></a>

In this example, an item is inserted through the `SaveAsync` method of the `DynamoDBContext` class, which takes an initialized instance of the .NET class that represents the item.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

// Create an appropriate context for the object persistence programming model,
//  examples of which have been described earlier.

// Create an object that represents the new item.
var reply = new Reply()
{
    Id = Guid.NewGuid().ToString(),
    ReplyDateTime = DateTime.UtcNow,
    Author = "Author1",
    Message = "Thank you!"
};

// Insert the item into the table.
await context.SaveAsync<Reply>(reply, new DynamoDBOperationConfig
{
    IndexName = "PostedBy-Message-index"
});
```

### Using an instance of a .NET class to get items from a table
<a name="dynamodb-intro-apis-object-persistence-net-get-item"></a>

In this example, a query is created to find all the records of "Author1" by using the `QueryAsync` method of the `DynamoDBContext` class. Then, items are retrieved through the query's `GetNextSetAsync` method.

```
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

// Create an appropriate context for the object persistence programming model,
//  examples of which have been described earlier.

// Construct a query that finds all replies by a specific author.
var query = context.QueryAsync<Reply>("Author1", new DynamoDBOperationConfig
{
    IndexName = "PostedBy-Message-index"
});

// Display the result.
var set = await query.GetNextSetAsync();
foreach (var item in set)
{
    Console.WriteLine("Id = " + item.Id);
    Console.WriteLine("ReplyDateTime = " + item.ReplyDateTime);
    Console.WriteLine("PostedBy = " + item.Author);
    Console.WriteLine("Message = " + item.Message);
}
```

### Additional information about the object persistence model
<a name="dynamodb-intro-apis-object-persistence-more-into"></a>

The examples and explanations shown above sometimes include a property of the `DynamoDBContext` class called `DisableFetchingTableMetadata`. This property, which was introduced in [version 3.7.203 of the AWSSDK.DynamoDBv2 NuGet package](https://www.nuget.org/packages/AWSSDK.DynamoDBv2/3.7.203), allows you to avoid certain conditions that might cause additional latency or deadlocks due to cold-start and thread-pool behaviors. For more information, see the blog post [Improved DynamoDB Initialization Patterns for the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/improved-dynamodb-initialization-patterns-for-the-aws-sdk-for-net/).

The following is some additional information about this property.
+ This property can be set globally in your `app.config` or `web.config` file if you're using .NET Framework.
+ This property can be set globally by using the [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Amazon/TAWSConfigsDynamoDB.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Amazon/TAWSConfigsDynamoDB.html) class, as shown in the following example.

  ```
  // Set the DisableFetchingTableMetadata property globally
  // before constructing any context objects.
  AWSConfigsDynamoDB.Context.DisableFetchingTableMetadata = true;

  var client = new AmazonDynamoDBClient();
  var context = new DynamoDBContext(client);
  ```
+ In some cases, you can't add DynamoDB attributes to a .NET class; for example, if the class is defined in a dependency. In such cases, it's possible to still take advantage of the `DisableFetchingTableMetadata` property. To do so, use the [https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTableBuilder.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/DynamoDBv2/TTableBuilder.html) class in addition to the `DisableFetchingTableMetadata` property. The `TableBuilder` class was also introduced in [version 3.7.203 of the AWSSDK.DynamoDBv2 NuGet package](https://www.nuget.org/packages/AWSSDK.DynamoDBv2/3.7.203).

  ```
  // Set the DisableFetchingTableMetadata property globally
  // before constructing any context objects.
  AWSConfigsDynamoDB.Context.DisableFetchingTableMetadata = true;

  var client = new AmazonDynamoDBClient();
  var context = new DynamoDBContext(client);

  var table = new TableBuilder(client, "Reply")
      .AddHashKey("Id", DynamoDBEntryType.String)
      .AddRangeKey("ReplyDateTime", DynamoDBEntryType.String)
      .AddGlobalSecondaryIndex("PostedBy-Message-index", "Author", DynamoDBEntryType.String,
          "Message", DynamoDBEntryType.String)
      .Build();

  // This registers the "Reply" table we constructed via the builder.
  context.RegisterTableDefinition(table);

  // Now operations like this will work,
  // even if the Reply class was not annotated with this index.
  var query = context.QueryAsync<Reply>("Author1", new DynamoDBOperationConfig()
  {
      IndexName = "PostedBy-Message-index"
  });
  ```

## More information
<a name="dynamodb-intro-more-info"></a>

 **Using the AWS SDK for .NET to program DynamoDB, information and examples**
+  [DynamoDB APIs](http://blogs.aws.amazon.com/net/post/Tx17SQHVEMW8MXC/DynamoDB-APIs)
+  [DynamoDB Series Kickoff](http://blogs.aws.amazon.com/net/post/Tx2XQOCY08QMTKO/DynamoDB-Series-Kickoff)
+  [DynamoDB Series - Document Model](http://blogs.aws.amazon.com/net/post/Tx2R0WG46GQI1JI/DynamoDB-Series-Document-Model)
+  [DynamoDB Series - Conversion Schemas](http://blogs.aws.amazon.com/net/post/Tx2TCOGWG7ARUH5/DynamoDB-Series-Conversion-Schemas)
+  [DynamoDB Series - Object Persistence Model](http://blogs.aws.amazon.com/net/post/Tx20L86FLMBW51P/DynamoDB-Series-Object-Persistence-Model)
+  [DynamoDB Series - Expressions](http://blogs.aws.amazon.com/net/post/TxZQM7VA9AUZ9L/DynamoDB-Series-Expressions)
+  [Using Expressions with Amazon DynamoDB and the AWS SDK for .NET](dynamodb-expressions.md)
+  [JSON support in Amazon DynamoDB](dynamodb-json.md)

 **Low-Level model, information and examples**
+  [Working with Tables Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetWorkingWithTables.html)
+  [Working with Items Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetItemCRUD.html)
+  [Querying Tables Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetQuerying.html)
+  [Scanning Tables Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetScanning.html)
+  [Working with Local Secondary Indexes Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSILowLevelDotNet.html)
+  [Working with Global Secondary Indexes Using the AWS SDK for .NET Low-Level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSILowLevelDotNet.html)

 **Document model, information and examples**
+  [DynamoDB Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModel.DataTypes)
+  [DynamoDBEntry](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TDynamoDBv2DocumentModelDynamoDBEntry.html)
+  [.NET: Document Model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKMidLevel.html)

 **Object persistence model, information and examples**
+  [.NET: Object Persistence Model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html)

 **Other useful information**
+ See [Integrating AWS with .NET Aspire](aspire-integrations.md) for information about developing with Amazon DynamoDB local through .NET Aspire.

**Topics**
+ [Low-Level Model](#dynamodb-intro-apis-low-level)
+ [Document Model](#dynamodb-intro-apis-document)
+ [Object Persistence Model](#dynamodb-intro-apis-object-persistence)
+ [More information](#dynamodb-intro-more-info)
+ [Using expressions](dynamodb-expressions.md)
+ [JSON support](dynamodb-json.md)
