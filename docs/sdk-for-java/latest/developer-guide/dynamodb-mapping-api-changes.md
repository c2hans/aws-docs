---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html
---

# Changes in the DynamoDB mapping APIs between version 1 and version 2 of the SDK for Java
<a name="dynamodb-mapping-api-changes"></a>

## Create a client
<a name="dynamodb-mapping-api-changes-client"></a>

****

| Use case | V1 | V2 |
| --- | --- | --- |
|  Normal instantiation |  <pre>AmazonDynamoDB standardClient = AmazonDynamoDBClientBuilder.standard()<br />    .withCredentials(credentialsProvider)<br />    .withRegion(Regions.US_EAST_1)<br />    .build();<br />DynamoDBMapper mapper = new DynamoDBMapper(standardClient);</pre>  |  <pre>DynamoDbClient standardClient = DynamoDbClient.builder()<br />    .credentialsProvider(ProfileCredentialsProvider.create())<br />    .region(Region.US_EAST_1)<br />    .build();<br />DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()<br />    .dynamoDbClient(standardClient)<br />    .build();</pre>  |
|  Minimal instantiation |  <pre>AmazonDynamoDB standardClient = AmazonDynamoDBClientBuilder.standard();<br />DynamoDBMapper mapper = new DynamoDBMapper(standardClient);</pre>  |  <pre>DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.create();</pre>  |
|  With attribute transformer\* |  <pre>DynamoDBMapper mapper = new DynamoDBMapper(standardClient, <br />                        attributeTransformerInstance);</pre>  |  <pre>DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()<br />    .dynamoDbClient(standardClient)<br />    .extensions(extensionAInstance, extensionBInstance)<br />    .build();</pre>  |

\*Extensions in V2 correspond roughly to attribute transformers in V1. The [Use extensions to customize DynamoDB Enhanced Client operations](ddb-en-client-extensions.md) section contains more information on extensions in V2.

## Establish mapping to DynamoDB table/index
<a name="dynamodb-mapping-api-changes-mapping"></a>

In V1, you specify a DynamoDB table name through a bean annotation. In V2, a factory method, `table()`, produces an instance of `DynamoDbTable` that represents the remote DynamoDB table. The first parameter of the `table()` method is the DynamoDB table name.

****

| Use case | V1 | V2 |
| --- | --- | --- |
|  Map the Java POJO class to the DynamoDB table |  <pre>@DynamoDBTable(tableName ="Customer")<br />public class Customer {<br />  ...<br />}</pre>  |  <pre>DynamoDbTable<Customer> customerTable = enhancedClient.table("Customer",<br />    TableSchema.fromBean(Customer.class));</pre>  |
|  Map to a DynamoDB secondary index | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html)The section in the DynamoDB Developer Guide that discusses[ the V1 `query` method](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Methods.html#DynamoDBMapper.Methods.query) shows a complete example. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html)The [Use secondary indices](ddb-en-client-use-secindex.md) section in this guide provides more information. |

## Table operations
<a name="dynamodb-mapping-api-changes-tobleops"></a>

This section describes operation APIs that differ between V1 and V2 for most standard use cases.

In V2, all operations that involve a single table are called on the `DynamoDbTable` instance, not on the enhanced client. The enhanced client contains methods that can target multiple tables.

In the table named *Table operations* below, a POJO instance is referred to as `item` or as a specific type such as `customer1`. For the V2 examples the instances named, `table` is the result of previously calling `enhancedClient.table()` that returns a reference to the `DynamoDbTable` instance.

Note that most V2 operations can be called with a fluent consumer pattern even when not shown. For example,

```
Customer customer = table.getItem(r → r.key(key));
  or
Customer customer = table.getItem(r → r.key(k -> k.partitionValue("id").sortValue("email")))
```

For V1 operations, *Table operations* (below) contains some of the commonly used forms and not all overloaded forms. For example, the `load()` method has the following overloads:

```
mapper.load(Customer.class, hashKey)
mapper.load(Customer.class, hashKey, rangeKey)
mapper.load(Customer.class, hashKey, config)
mapper.load(Customer.class, hashKey, rangeKey, config)
mapper.load(item)
mapper.load(item, config)
```

*Table operations* (below) shows the commonly used forms:

```
mapper.load(item)
mapper.load(item, config)
```

**Table operations**

| Use case | V1 | V2 |
| --- | --- | --- |
| Write a Java POJO to a DynamoDB table<br />**DynamoDB operation:** `PutItem`, `UpdateItem` | <pre>mapper.save(item)<br />mapper.save(item, config)<br />mapper.save(item, saveExpression, config)</pre>In V1, `DynamoDBMapperConfig.SaveBehavior` and annotations determines which low-level DynamoDB method will be called. In general, `UpdateItem` is called except when using `SaveBehavior.CLOBBER` and `SaveBehavior.PUT`. Auto-generated keys are a special use case, and occasionally both `PutItem` and `UpdateItem` are used. |  <pre>table.putItem(putItemRequest)<br />table.putItem(item)<br />table.putItemWithResponse(item) //Returns metadata.<br /><br />updateItem(updateItemRequest)<br />table.updateItem(item)<br />table.updateItemWithResponse(item) //Returns metadata.</pre>  |
| Read an item from a DynamoDB table to a Java POJO<br />**DynamoDB operation:** `GetItem` |  <pre>mapper.load(item)<br />mapper.load(item, config)</pre>  |  <pre>table.getItem(getItemRequest)<br />table.getItem(item)<br />table.getItem(key)<br />table.getItemWithResponse(key) //Returns POJO with metadata.</pre>  |
| Delete an item from a DynamoDB table<br />**DynamoDB operation:** `DeleteItem` |  <pre>mapper.delete(item, deleteExpression, config)</pre>  |  <pre>table.deleteItem(deleteItemRequest)<br />table.deleteItem(item)<br />table.deleteItem(key)</pre>  |
| Query a DynamoDB table or secondary index and return a paginated list<br />**DynamoDB operation:** `Query` |  <pre>mapper.query(Customer.class, queryExpression)<br />mapper.query(Customer.class, queryExpression, <br />                             mapperConfig)</pre>  | <pre>table.query(queryRequest)<br />table.query(queryConditional)</pre>Use the returned `PageIterable.stream()` (lazy loading) for sync responses and `PagePublisher.subscribe()` for async responses |
| Query a DynamoDB table or secondary index and return a list<br />**DynamoDB operation:** `Query` |  <pre>mapper.queryPage(Customer.class, queryExpression)<br />mapper.queryPage(Customer.class, queryExpression, <br />                                 mapperConfig)</pre>  | <pre>table.query(queryRequest)<br />table.query(queryConditional)</pre>Use the returned `PageIterable.items()` (lazy loading) for sync responses and `PagePublisher.items.subscribe()` for async responses |
| Scan a DynamoDB table or secondary index and return a paginated list<br />**DynamoDB operation:** `Scan` |  <pre>mapper.scan(Customer.class, scanExpression)<br />mapper.scan(Customer.class, scanExpression, <br />                            mapperConfig)</pre>  | <pre>table.scan()<br />table.scan(scanRequest)</pre>Use the returned `PageIterable.stream()` (lazy loading) for sync responses and `PagePublisher.subscribe()` for async responses |
| Scan a DynamoDB table or secondary index and return a list<br />**DynamoDB operation:** `Scan` |  <pre>mapper.scanPage(Customer.class, scanExpression)<br />mapper.scanPage(Customer.class, scanExpression, <br />                                mapperConfig)</pre>  | <pre>table.scan()<br />table.scan(scanRequest)</pre>Use the returned `PageIterable.items()` (lazy loading) for sync responses and `PagePublisher.items.subscribe()` for async responses |
| Read multiple items from multiple tables in a batch<br />**DynamoDB operation:** `BatchGetItem` |  <pre>mapper.batchLoad(Arrays.asList(customer1, <br />                               customer2, <br />                               book1))<br />mapper.batchLoad(itemsToGet) <br />           // itemsToGet: Map<Class<?>, List<KeyPair>></pre>  |  <pre>enhancedClient.batchGetItem(batchGetItemRequest)<br /><br />enhancedClient.batchGetItem(r -> r.readBatches(<br />    ReadBatch.builder(Record1.class)<br />             .mappedTableResource(mappedTable1)<br />             .addGetItem(i -> i.key(k -> k.partitionValue(0)))<br />             .build(),<br />    ReadBatch.builder(Record2.class)<br />             .mappedTableResource(mappedTable2)<br />             .addGetItem(i -> i.key(k -> k.partitionValue(0)))<br />             .build()))<br /><br />// Iterate over pages with lazy loading or over all items <br />   from the same table.</pre>  |
| Write multiple items to multiple tables in a batch<br />**DynamoDB operation:** `BatchWriteItem` |  <pre>mapper.batchSave(Arrays.asList(customer1, <br />                               customer2, <br />                               book1)) </pre>  |  <pre>enhancedClient.batchWriteItem(batchWriteItemRequest)<br /><br />enhancedClient.batchWriteItem(r -> r.writeBatches(<br />    WriteBatch.builder(Record1.class)<br />             .mappedTableResource(mappedTable1)<br />             .addPutItem(item1)<br />             .build(),<br />    WriteBatch.builder(Record2.class)<br />             .mappedTableResource(mappedTable2)<br />             .addPutItem(item2)<br />             .build()))</pre>  |
| Delete multiple items from multiple tables in a batch<br />**DynamoDB operation:** `BatchWriteItem` |  <pre>mapper.batchDelete(Arrays.asList(customer1, <br />                                 customer2, <br />                                 book1)) </pre>  |  <pre>enhancedClient.batchWriteItem(r -> r.writeBatches(<br />    WriteBatch.builder(Record1.class)<br />             .mappedTableResource(mappedTable1)<br />             .addDeleteItem(item1key)<br />             .build(),<br />    WriteBatch.builder(Record2.class)<br />             .mappedTableResource(mappedTable2)<br />             .addDeleteItem(item2key)<br />             .build()))</pre>  |
| Write/delete multiple items in a batch<br />**DynamoDB operation:** `BatchWriteItem` |  <pre>mapper.batchWrite(Arrays.asList(customer1, book1), <br />                  Arrays.asList(customer2)) </pre>  |  <pre>enhancedClient.batchWriteItem(r -> r.writeBatches(<br />    WriteBatch.builder(Record1.class)<br />             .mappedTableResource(mappedTable1)<br />             .addPutItem(item1)<br />             .build(),<br />    WriteBatch.builder(Record2.class)<br />             .mappedTableResource(mappedTable2)<br />             .addDeleteItem(item2key)<br />             .build()))</pre>  |
| Carry out a transactional write<br />**DynamoDB operation:** `TransactWriteItems` |  <pre>mapper.transactionWrite(transactionWriteRequest)</pre>  |  <pre>enhancedClient.transactWriteItems(transasctWriteItemsRequest)</pre>  |
| Carry out a transactional read<br />**DynamoDB operation:** `TransactGetItems` |  <pre>mapper.transactionLoad(transactionLoadRequest)</pre>  |  <pre>enhancedClient.transactGetItems(transactGetItemsRequest) </pre>  |
| Get a count of matching items of a query<br />**DynamoDB operation:** `Query` with `Select.COUNT` |  <pre>mapper.count(Customer.class, queryExpression)</pre>  |  <pre>// Get the count from query results.<br />PageIterable<Customer> pageIterable =<br />    customerTable.query(QueryEnhancedRequest.builder()<br />        .queryConditional(queryConditional)<br />        .select(Select.COUNT)<br />        .build());<br />Iterator<Page<Customer>> iterator = pageIterable.iterator();<br />Page<Customer> page = iterator.next();<br />int count = page.count();<br /><br />// For a more concise approach, you can chain the method calls:<br />int count = customerTable.query(QueryEnhancedRequest.builder()<br />                .queryConditional(queryConditional)<br />                .select(Select.COUNT)<br />                .build())<br />            .iterator().next().count();</pre>  |
| Get a count of matching items of a scan<br />**DynamoDB operation:**`Scan` with `Select.COUNT` |  <pre>mapper.count(Customer.class, scanExpression)</pre>  |  <pre>// Get the count from scan results.<br />PageIterable<Customer> pageIterable =<br />    customerTable.scan(ScanEnhancedRequest.builder()<br />        .filterExpression(filterExpression)<br />        .select(Select.COUNT)<br />        .build());<br />Iterator<Page<Customer>> iterator = pageIterable.iterator();<br />Page<Customer> page = iterator.next();<br />int count = page.count();<br /><br />// For a more concise approach, you can chain the method calls:<br />int count = customerTable.scan(ScanEnhancedRequest.builder()<br />                .filterExpression(filterExpression)<br />                .select(Select.COUNT)<br />                .build())<br />            .iterator().next().count();</pre>  |
| Create a table in DynamoDB corresponding to the POJO class<br />**DynamoDB operation:** `CreateTable` | <pre>mapper.generateCreateTableRequest(Customer.class)</pre>The previous statement generates a low-level create table request; users must call `createTable` on the DynamoDB client. |  <pre>table.createTable(createTableRequest)<br /><br />table.createTable(r -> r.provisionedThroughput(defaultThroughput())<br />    .globalSecondaryIndices(<br />        EnhancedGlobalSecondaryIndex.builder()<br />            .indexName("gsi_1")<br />            .projection(p -> p.projectionType(ProjectionType.ALL))<br />            .provisionedThroughput(defaultThroughput())<br />            .build()));</pre>  |
| Perform a parallel scan in DynamoDB<br />**DynamoDB operation:** `Scan` with `Segment` and `TotalSegments` parameters |  <pre>mapper.parallelScan(Customer.class, <br />                    scanExpression, <br />                    numTotalSegments)</pre>  | Users are required to handle the worker threads and call `scan` for each segment:<pre>table.scan(r -> r.segment(0).totalSegments(5))</pre> |
| Integrate Amazon S3 with DynamoDB to store intelligent S3 links |  <pre>mapper.createS3Link(bucket, key)<br />mapper.getS3ClientCache()</pre>  | Not supported because it couples Amazon S3 and DynamoDB. |

## Map classes and properties
<a name="dynamodb-mapping-schemas"></a>

In both V1 and V2, you map classes to tables using bean-style annotations. V2 also offers [other ways to define schemas](ddb-en-client-adv-features.md#ddb-en-client-adv-features-schm-overview) for specific use cases, such as working with immutable classes.

### Bean annotations
<a name="dynamodb-mapping-schemas-annos"></a>

The following table shows the equivalent bean annotations for a specific use case that are used in V1 and V2. A `Customer` class scenario is used to illustrate parameters.

Annotations—as well as classes and enumerations—in V2 follow camel case convention and use 'DynamoDb', not 'DynamoDB'.

| Use case | V1 | V2 |
| --- | --- | --- |
| Map class to table |  <pre>@DynamoDBTable (tableName ="CustomerTable")</pre>  | <pre>@DynamoDbBean<br />@DynamoDbBean(converterProviders = {...})</pre>The table name is defined when calling the DynamoDbEnhancedClient\#table() method. |
| Designate a class member as a table attribute  |  <pre>@DynamoDBAttribute(attributeName = "customerName")</pre>  |  <pre>@DynamoDbAttribute("customerName") </pre>  |
| Designate a class member is a hash/partition key |  <pre>@DynamoDBHashKey </pre>  |  <pre>@DynamoDbPartitionKey</pre>  |
| Designate a class member is a range/sort key |  <pre>@DynamoDBRangeKey </pre>  |  <pre>@DynamoDbSortKey </pre>  |
| Designate a class member is a secondary index hash/partition key |  <pre>@DynamoDBIndexHashKey </pre>  |  <pre>@DynamoDbSecondaryPartitionKey </pre>  |
| Designate a class member is a secondary index range/sort key |  <pre>@DynamoDBIndexRangeKey </pre>  |  <pre>@DynamoDbSecondarySortKey </pre>  |
| Ignore this class member when mapping to a table |  <pre>@DynamoDBIgnore </pre>  |  <pre>@DynamoDbIgnore</pre>  |
| Designate a class member as an auto-generated UUID key attribute |  <pre>@DynamoDBAutoGeneratedKey</pre>  | <pre>@DynamoDbAutoGeneratedUuid </pre>The extension that provides this is not loaded by default; you must add the extension to client builder. |
| Designate a class member as an auto-generated timestamp attribute |  <pre>@DynamoDBAutoGeneratedTimestamp</pre>  | <pre>@DynamoDbAutoGeneratedTimestampAttribute</pre>The extension that provides this is not loaded by default; you must add the extension to client builder. |
| Designate a class member as an auto-incremented version attribute |  <pre>@DynamoDBVersionAttribute</pre>  | <pre>@DynamoDbVersionAttribute</pre>The extension that provides this is auto-loaded. |
| Designate a class member as requiring a custom conversion |  <pre>@DynamoDBTypeConverted</pre>  |  <pre>@DynamoDbConvertedBy</pre>  |
| Designate a class member to be stored as a different attribute type |  <pre>@DynamoDBTyped(<DynamoDBAttributeType>)</pre>  | Use an `AttributeConverter` implementation. V2 provides many built-in converters for common Java types. You can also implement your own custom `AttributeConverter` or `AttributeConverterProvider`. See [Control attribute conversion](ddb-en-client-adv-features-conversion.md) in this guide. |
| Designate a class that can be serialized to a DynamoDB document (JSON-style document) or sub-document  |  <pre>@DynamoDBDocument</pre>  | Use the Enhanced Document API. See the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html) |

### V2 additional annotations
<a name="dynamodb-mapping-schemas-annos-v2-addnl"></a>

| Use case | V1 | V2 |
| --- | --- | --- |
| Designate a class member not to be stored as a NULL attribute if the Java value is null | N/A |  <pre>@DynamoDbIgnoreNulls</pre>  |
| Designate a class member to be an empty object if all attributes are null | N/A |  <pre>@DynamoDbPreserveEmptyObject</pre>  |
| Designate special update action for a class member | N/A |  <pre>@DynamoDbUpdateBehavior</pre>  |
| Designate an immutable class | N/A |  <pre>@DynamoDbImmutable</pre>  |
| Designate a class member as an auto-incremented counter attribute | N/A | <pre>@DynamoDbAtomicCounter</pre>The extension that provides this functionality is auto-loaded. |

## Configuration
<a name="dynamodb-mapping-configuration"></a>

In V1, you generally control specific behaviors by using an instance of `DynamoDBMapperConfig`. You can supply the configuration object either when you create the mapper or when you make a request. In V2, configuration is specific to the request object for the operation.

| Use case | V1 | Default in V1 | V2 |
| --- | --- | --- | --- |
|  |  <pre>DynamoDBMapperConfig.builder()</pre>  |  |  |
| Batch load/write retry strategy |  <pre>  .withBatchLoadRetryStrategy(loadRetryStrategy)</pre> <pre>  .withBatchWriteRetryStrategy(writeRetryStrategy)</pre>  | retry failed items | Configure the retry strategy on the underlying DynamoDBClient. See [Configure retry behavior in the AWS SDK for Java 2.x](retry-strategy.md) in this guide. |
| Consistent reads |  <pre>  .withConsistentReads(CONSISTENT)</pre>  | EVENTUAL | By default, consistent reads is false for read operations. Override with .consistentRead(true) on the request object. |
| Conversion schema with sets of marshallers/unmarshallers | <pre>  .withConversionSchema(conversionSchema)</pre>Static implementations provide backwards compatibility with older versions. | V2\_COMPATIBLE | Not applicable. This is a legacy feature that refers to how the earliest versions of DynamoDB (V1) stored data types, and this behavior will not be preserved in the enhanced client. An example of behavior in DynamoDB V1 is storing booleans as Number instead of as Boolean. |
| Table names | <pre>  .withObjectTableNameResolver()<br />  .withTableNameOverride() <br />  .withTableNameResolver()</pre>Static implementations provide backwards compatibility with older versions | use annotation or guess from class | The table name is defined when calling the `DynamoDbEnhancedClient#table()` method. |
| Pagination load strategy | <pre>  .withPaginationLoadingStrategy(strategy)</pre> Options are: LAZY\_`LOADING`, `EAGER_LOADING`, or `ITERATION_ONLY` | LAZY\_LOADING |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html)  |
| Request metric collection |  <pre>  .withRequestMetricCollector(collector)</pre>  | null | Use metricPublisher() in ClientOverrideConfiguration when building the standard DynamoDB client.  |
| Save behavior | <pre>  .withSaveBehavior(SaveBehavior.CLOBBER) </pre>Options are `UPDATE`, `CLOBBER`, `PUT`, `APPEND_SET`, or `UPDATE_SKIP_NULL_ATTRIBUTES`. | UPDATE | In V2, you call `putItem()` or `updateItem()` explicitly.<br />`CLOBBER or PUT`: Corresponding action in v 2 is calling `putItem()`. There is no specific `CLOBBER` configuration.<br />`UPDATE`: Corresponds to `updateItem()`<br />`UPDATE_SKIP_NULL_ATTRIBUTES`: Corresponds to `updateItem()`. Control update behavior with the request setting `ignoreNulls` and the annotation/tag `DynamoDbUpdateBehavior`.<br />`APPEND_SET`: Not supported |
| Type converter factory |  <pre>  .withTypeConverterFactory(typeConverterFactory) </pre>  | standard type converters | Set on the bean by using<pre>@DynamoDbBean(converterProviders = {ConverterProvider.class, <br />        DefaultAttributeConverterProvider.class})</pre> |

### Per-operation configuration
<a name="dynamodb-mapping-configuration-per-op"></a>

In V1, some operations, such as `query()`, are highly configurable through an “expression” object submitted to the operation. For example:

```
DynamoDBQueryExpression<Customer> emailBwQueryExpr = new DynamoDBQueryExpression<Customer>()
    .withRangeKeyCondition("Email",
        new Condition()
            .withComparisonOperator(ComparisonOperator.BEGINS_WITH)
            .withAttributeValueList(
                new AttributeValue().withS("my")));

mapper.query(Customer.class, emailBwQueryExpr);
```

In V2, instead of using a configuration object, you set parameters on the request object by using a builder. For example:

```
QueryEnhancedRequest emailBw = QueryEnhancedRequest.builder()
    .queryConditional(QueryConditional
        .sortBeginsWith(kb -> kb
            .sortValue("my"))).build();

customerTable.query(emailBw);
```

## Conditionals
<a name="dynamodb-mapping-conditionals"></a>

In V2, conditional and filtering expressions are expressed using an `Expression` object, which encapsulates the condition and the mapping of names and filters.

| Use case | Operations | V1 | V2 |
| --- | --- | --- | --- |
| Expected attribute conditions | save(), delete(), query(), scan() |  <pre>new DynamoDBSaveExpression()<br />  .withExpected(Collections.singletonMap(<br />      "otherAttribute", new ExpectedAttributeValue(false)))<br />  .withConditionalOperator(ConditionalOperator.AND);</pre>  | Deprecated; use ConditionExpression instead. |
| Condition expression | delete() |  <pre>deleteExpression.setConditionExpression("zipcode = :zipcode")<br />deleteExpression.setExpressionAttributeValues(...)<br /></pre>  |  <pre>Expression conditionExpression =<br />    Expression.builder()<br />        .expression("#key = :value OR #key1 = :value1")<br />        .putExpressionName("#key", "attribute")<br />        .putExpressionName("#key1", "attribute3")<br />        .putExpressionValue(":value", AttributeValues.stringValue("wrong"))<br />        .putExpressionValue(":value1", AttributeValues.stringValue("three"))<br />        .build();<br /><br />DeleteItemEnhancedRequest request = DeleteItemEnhancedRequest.builder()<br />         .conditionExpression(conditionExpression).build();</pre>  |
| Filter expression | query(), scan() |  <pre>scanExpression<br />  .withFilterExpression("#statename = :state")<br />  .withExpressionAttributeValues(attributeValueMapBuilder.build())<br />  .withExpressionAttributeNames(attributeNameMapBuilder.build())<br /></pre>  |  <pre>Map<String, AttributeValue> values = singletonMap(":key", stringValue("value"));<br />Expression filterExpression =<br />    Expression.builder()<br />        .expression("name = :key")<br />        .expressionValues(values)<br />        .build();<br />QueryEnhancedRequest request = QueryEnhancedRequest.builder()<br />    .filterExpression(filterExpression).build();<br /></pre>  |
| Condition expression for query | query() |  <pre>queryExpression.withKeyConditionExpression()</pre>  |  <pre>QueryConditional keyEqual = QueryConditional.keyEqualTo(b -> b<br />                .partitionValue("movie01"));<br /><br />QueryEnhancedRequest tableQuery = QueryEnhancedRequest.builder()<br />                .queryConditional(keyEqual)<br />                .build();</pre>  |

## Type conversion
<a name="dynamodb-mapping-type-conv"></a>

### Default converters
<a name="dynamodb-mapping-type-conv-defaults"></a>

In V2, the SDK provides a set of default converters for all common types. You can change type converters both at the overall provider level as well as for a single attribute. You can find a list of the available converters in the [AttributeConverter](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/AttributeConverter.html) API reference.

### Set a custom converter for an attribute
<a name="dynamodb-mapping-type-conv-anno"></a>

In V1, you can annotate a getter method with `@DynamoDBTypeConverted` to specify the class that converts between the Java attribute type and a DynamoDB attribute type. For instance, a `CurrencyFormatConverter` that converts between a Java `Currency` type and DynamoDB String can be applied as shown in the following snippet.

```
@DynamoDBTypeConverted(converter = CurrencyFormatConverter.class)
public Currency getCurrency() { return currency; }
```

The V2 equivalent of the previous snippet is shown below.

```
@DynamoDbConvertedBy(CurrencyFormatConverter.class)
public Currency getCurrency() { return currency; }
```

**Note**
In V1, you can apply the annotation to the attribute itself , a type or a user-defined annotation, V2 supports applying the annotation it only to the getter.

### Add a type converter factory or provider
<a name="dynamodb-mapping-type-conv-factory"></a>

In V1, you can provide your own set of type converters, or override the types you care about by adding a type converter factory to the configuration. The type converter factory extends `DynamoDBTypeConverterFactory`, and overrides are done by getting a reference to the default set and extending it. The following snippet demonstrates how to do this.

```
DynamoDBTypeConverterFactory typeConverterFactory =
    DynamoDBTypeConverterFactory.standard().override()
        .with(String.class, CustomBoolean.class, new DynamoDBTypeConverter<String, CustomBoolean>() {
            @Override
            public String convert(CustomBoolean bool) {
                return String.valueOf(bool.getValue());
            }
            @Override
            public CustomBoolean unconvert(String string) {
                return new CustomBoolean(Boolean.valueOf(string));
            }}).build();
DynamoDBMapperConfig config =
    DynamoDBMapperConfig.builder()
        .withTypeConverterFactory(typeConverterFactory)
        .build();
DynamoDBMapper mapperWithTypeConverterFactory = new DynamoDBMapper(dynamo, config);
```

V2 provides similar functionality through the `@DynamoDbBean` annotation. You can provide a single `AttributeConverterProvider` or a chain of ordered `AttributeConverterProvider`s. Note that if you supply your own chain of attribute converter providers, you will override the default converter provider and must include it in the chain to use its attribute converters.

```
@DynamoDbBean(converterProviders = {
   ConverterProvider1.class,
   ConverterProvider2.class,
   DefaultAttributeConverterProvider.class})
public class Customer {
  ...
}
```

The section on [attribute conversion](ddb-en-client-adv-features-conversion.md#ddb-en-client-adv-features-conversion-example) in this guide contains a complete example for V2.
