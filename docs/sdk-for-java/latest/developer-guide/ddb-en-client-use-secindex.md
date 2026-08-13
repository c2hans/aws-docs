---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-secindex.html
---

# Use secondary indices
<a name="ddb-en-client-use-secindex"></a>

The [primary key](ddb-en-client-gs-tableschema.md#ddb-en-client-gs-tableschema-anno-bean) of a table defines the primary index, which determines how DynamoDB stores and retrieves items by default.

Secondary indexes provide alternative keys that you use in query and scan operations. Global secondary indexes (GSI) have a partition key and an optional sort key that can differ from those on the base table. In contrast, local secondary indexes (LSI) share the partition key of the primary index but define a different sort key.

## Define keys for global and local secondary indexes
<a name="ddb-en-client-use-secindex-annomodel"></a>

Attributes that participate in secondary indices require either the `@DynamoDbSecondaryPartitionKey` or `@DynamoDbSecondarySortKey` annotation.

The following class shows annotations for two indices. The GSI named *SubjectLastPostedDateIndex* uses the `Subject` attribute for the partition key and the `LastPostedDateTime` for the sort key. The LSI named *ForumLastPostedDateIndex* uses the `ForumName` as its partition key and `LastPostedDateTime` as its sort key.

Note that the `Subject` attribute serves a dual role. It is the primary key's sort key and the partition key of the GSI named *SubjectLastPostedDateIndex*.

### `MessageThread` class
<a name="ddb-en-client-use-secindex-class"></a>

The `MessageThread` class is suitable to use as a data class for the [example Thread table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleTables.html) in the *Amazon DynamoDB Developer Guide*.

#### Imports
<a name="ddb-en-client-use-secindex-classimports"></a>

```
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSecondaryPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSecondarySortKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSortKey;

import java.util.List;
```

```
@DynamoDbBean
public class MessageThread {
    private String ForumName;
    private String Subject;
    private String Message;
    private String LastPostedBy;
    private String LastPostedDateTime;
    private Integer Views;
    private Integer Replies;
    private Integer Answered;
    private List<String> Tags;

    @DynamoDbPartitionKey
    public String getForumName() {
        return ForumName;
    }

    public void setForumName(String forumName) {
        ForumName = forumName;
    }

    // Sort key for primary index and partition key for GSI "SubjectLastPostedDateIndex".
    @DynamoDbSortKey
    @DynamoDbSecondaryPartitionKey(indexNames = "SubjectLastPostedDateIndex")
    public String getSubject() {
        return Subject;
    }

    public void setSubject(String subject) {
        Subject = subject;
    }

    // Sort key for GSI "SubjectLastPostedDateIndex" and sort key for LSI "ForumLastPostedDateIndex".
    @DynamoDbSecondarySortKey(indexNames = {"SubjectLastPostedDateIndex", "ForumLastPostedDateIndex"})
    public String getLastPostedDateTime() {
        return LastPostedDateTime;
    }

    public void setLastPostedDateTime(String lastPostedDateTime) {
        LastPostedDateTime = lastPostedDateTime;
    }
    public String getMessage() {
        return Message;
    }

    public void setMessage(String message) {
        Message = message;
    }

    public String getLastPostedBy() {
        return LastPostedBy;
    }

    public void setLastPostedBy(String lastPostedBy) {
        LastPostedBy = lastPostedBy;
    }

    public Integer getViews() {
        return Views;
    }

    public void setViews(Integer views) {
        Views = views;
    }

    @DynamoDbSecondaryPartitionKey(indexNames = "ForumRepliesIndex")
    public Integer getReplies() {
        return Replies;
    }

    public void setReplies(Integer replies) {
        Replies = replies;
    }

    public Integer getAnswered() {
        return Answered;
    }

    public void setAnswered(Integer answered) {
        Answered = answered;
    }

    public List<String> getTags() {
        return Tags;
    }

    public void setTags(List<String> tags) {
        Tags = tags;
    }

    public MessageThread() {
        this.Answered = 0;
        this.LastPostedBy = "";
        this.ForumName = "";
        this.Message = "";
        this.LastPostedDateTime = "";
        this.Replies = 0;
        this.Views = 0;
        this.Subject = "";
    }

    @Override
    public String toString() {
        return "MessageThread{" +
                "ForumName='" + ForumName + '\'' +
                ", Subject='" + Subject + '\'' +
                ", Message='" + Message + '\'' +
                ", LastPostedBy='" + LastPostedBy + '\'' +
                ", LastPostedDateTime='" + LastPostedDateTime + '\'' +
                ", Views=" + Views +
                ", Replies=" + Replies +
                ", Answered=" + Answered +
                ", Tags=" + Tags +
                '}';
    }
}
```

## Create the index
<a name="ddb-en-client-use-secindex-confindex"></a>

Beginning with version 2.20.86 of the SDK for Java, the `createTable()` method automatically generates secondary indexes from data class annotations. By default, all attributes from the base table are copied to an index and the provisioned throughput values are 20 read capacity units and 20 write capacity units.

However, if you use an SDK version prior to 2.20.86, you need to build the index along with the table as shown in the following example. This example builds the two indexes for the `Thread` table. The [builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/CreateTableEnhancedRequest.Builder.html) parameter has methods to configure both types of indexes as shown after comment lines 1 and 2. You use the index builder's `indexName()` method to associate the index names specified in the data class annotations with the intended type of index.

This code configures all of the table attributes to end up in both indexes after comment lines 3 and 4. More information about [attribute projections](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html#LSI.Projections) is available in the *Amazon DynamoDB Developer Guide*.

```
    public static void createMessageThreadTable(DynamoDbTable<MessageThread> messageThreadDynamoDbTable, DynamoDbClient dynamoDbClient) {
        messageThreadDynamoDbTable.createTable(b -> b
                // 1. Generate the GSI.
                .globalSecondaryIndices(gsi -> gsi.indexName("SubjectLastPostedDateIndex")
                        // 3. Populate the GSI with all attributes.
                        .projection(p -> p
                                .projectionType(ProjectionType.ALL))
                )
                // 2. Generate the LSI.
                .localSecondaryIndices(lsi -> lsi.indexName("ForumLastPostedDateIndex")
                        // 4. Populate the LSI with all attributes.
                        .projection(p -> p
                                .projectionType(ProjectionType.ALL))
                )
        );
```

## Query by using an index
<a name="ddb-en-client-use-secindex-query"></a>

The following example queries the local secondary index *ForumLastPostedDateIndex*.

Following comment line 2, you create a [QueryConditional](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/QueryConditional.html) object that is required when calling the [DynamoDbIndex.query()](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/DynamoDbIndex.html#query(java.util.function.Consumer)) method.

You get a reference to the index you want to query after comment line 3 by passing in the name of the index. Following comment line 4, you call the `query()` method on the index passing in the `QueryConditional` object.

You also configure the query to return three attribute values as shown after comment line 5. If `attributesToProject()` is not called, the query returns all attribute values. Notice that the specified attribute names begin with lowercase letters. These attribute names match those used in the table, not necessarily the attribute names of the data class.

Following comment line 6, iterate through the results and log each item returned by the query and also store it in the list to return to the caller.

```
public class IndexScanExamples {
    private static Logger logger = LoggerFactory.getLogger(IndexScanExamples.class);

    public static List<MessageThread> queryUsingSecondaryIndices(String lastPostedDate,
                                                                 DynamoDbTable<MessageThread> threadTable) {
        // 1. Log the parameter value.
        logger.info("lastPostedDate value: {}", lastPostedDate);

        // 2. Create a QueryConditional whose sort key value must be greater than or equal to the parameter value.
        QueryConditional queryConditional = QueryConditional.sortGreaterThanOrEqualTo(qc ->
                qc.partitionValue("Forum02").sortValue(lastPostedDate));

        // 3. Specify the index name to query.
        final DynamoDbIndex<MessageThread> forumLastPostedDateIndex = threadTable.index("ForumLastPostedDateIndex");

        // 4. Perform the query using the QueryConditional object.
        final SdkIterable<Page<MessageThread>> pagedResult = forumLastPostedDateIndex.query(q -> q
                .queryConditional(queryConditional)
                // 5. Request three attribute in the results.
                .attributesToProject("forumName", "subject", "lastPostedDateTime"));

        List<MessageThread> collectedItems = new ArrayList<>();
        // 6. Iterate through pages response and sort the items.
        pagedResult.stream().forEach(page -> page.items().stream()
                .sorted(Comparator.comparing(MessageThread::getLastPostedDateTime))
                .forEach(mt -> {
                    // 7. Log the returned items and add the collection to return to the caller.
                    logger.info(mt.toString());
                    collectedItems.add(mt);
                }));
        return collectedItems;
    }
```

The following items exist in the database before the query is run.

```
MessageThread{ForumName='Forum01', Subject='Subject01', Message='Message01', LastPostedBy='', LastPostedDateTime='2023.03.28', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject02', Message='Message02', LastPostedBy='', LastPostedDateTime='2023.03.29', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject04', Message='Message04', LastPostedBy='', LastPostedDateTime='2023.03.31', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject08', Message='Message08', LastPostedBy='', LastPostedDateTime='2023.04.04', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject10', Message='Message10', LastPostedBy='', LastPostedDateTime='2023.04.06', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum03', Subject='Subject03', Message='Message03', LastPostedBy='', LastPostedDateTime='2023.03.30', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum03', Subject='Subject06', Message='Message06', LastPostedBy='', LastPostedDateTime='2023.04.02', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum03', Subject='Subject09', Message='Message09', LastPostedBy='', LastPostedDateTime='2023.04.05', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum05', Subject='Subject05', Message='Message05', LastPostedBy='', LastPostedDateTime='2023.04.01', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum07', Subject='Subject07', Message='Message07', LastPostedBy='', LastPostedDateTime='2023.04.03', Views=0, Replies=0, Answered=0, Tags=null}
```

The logging statements at lines 1 and 6 result in the following console output.

```
lastPostedDate value: 2023.03.31
MessageThread{ForumName='Forum02', Subject='Subject04', Message='', LastPostedBy='', LastPostedDateTime='2023.03.31', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject08', Message='', LastPostedBy='', LastPostedDateTime='2023.04.04', Views=0, Replies=0, Answered=0, Tags=null}
MessageThread{ForumName='Forum02', Subject='Subject10', Message='', LastPostedBy='', LastPostedDateTime='2023.04.06', Views=0, Replies=0, Answered=0, Tags=null}
```

The query returned items with a `forumName` value of *Forum02* and a `lastPostedDateTime` value greater than or equal to *2023.03.31*. The results show `message` values with an empty string although the `message` attributes have values in the index. This is because the message attribute was not projected by the code after comment line 5.

## Use composite keys for global secondary indexes (GSI)
<a name="ddb-en-client-use-secindex-composite"></a>

The SDK for Java 2.x DynamoDB Enhanced Client supports composite keys for global secondary indexes. You can define up to four partition key attributes and four sort key attributes for a single GSI. This removes the need to concatenate multiple attributes into a single string key on the client side.

Use the `order` parameter on the `@DynamoDbSecondaryPartitionKey` and `@DynamoDbSecondarySortKey` annotations to specify the position of each attribute in the composite key. The `order` parameter accepts values from the [`Order`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/mapper/Order.html) enum (part of the Enhanced DynamoDB Client): `FIRST`, `SECOND`, `THIRD`, and `FOURTH`.

### Annotate data class with composite key annotations
<a name="ddb-en-client-use-secindex-composite-anno"></a>

The following example models an order table. The base table uses `orderId` as the partition key. A GSI named *OrdersByStatusDateAmount* uses a composite partition key of `customerId` and `status`, and a composite sort key of `orderDate` and `amount`. This design lets you query a customer's orders filtered by status, date, and amount threshold.

#### Imports
<a name="ddb-en-client-use-secindex-composite-annoimports"></a>

```
import software.amazon.awssdk.enhanced.dynamodb.mapper.Order;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSecondaryPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSecondarySortKey;
```

```
@DynamoDbBean
public class OrderItem {
    private String orderId;
    private String customerId;
    private String status;
    private String orderDate;
    private Integer amount;

    @DynamoDbPartitionKey
    public String getOrderId() {
        return orderId;
    }
    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    // First partition key attribute for the GSI.
    @DynamoDbSecondaryPartitionKey(indexNames = "OrdersByStatusDateAmount", order = Order.FIRST)
    public String getCustomerId() {
        return customerId;
    }
    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    // Second partition key attribute for the GSI.
    @DynamoDbSecondaryPartitionKey(indexNames = "OrdersByStatusDateAmount", order = Order.SECOND)
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    // First sort key attribute for the GSI.
    @DynamoDbSecondarySortKey(indexNames = "OrdersByStatusDateAmount", order = Order.FIRST)
    public String getOrderDate() {
        return orderDate;
    }
    public void setOrderDate(String orderDate) {
        this.orderDate = orderDate;
    }

    // Second sort key attribute for the GSI.
    @DynamoDbSecondarySortKey(indexNames = "OrdersByStatusDateAmount", order = Order.SECOND)
    public Integer getAmount() {
        return amount;
    }
    public void setAmount(Integer amount) {
        this.amount = amount;
    }
}
```

### Query by using a composite key index
<a name="ddb-en-client-use-secindex-composite-query"></a>

When you query a composite key index, use the `addPartitionValue()` and `addSortValue()` methods on the [Key](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/Key.html) builder. Add values in the same order as the `Order` values defined in the annotations. All partition keys are required. Sort keys are optional and can be provided from left to right.

You create a [QueryConditional](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/QueryConditional.html) object to specify the condition for the query. Use `keyEqualTo` for exact matches, or a sort key condition such as `sortGreaterThan`, `sortLessThan`, `sortBetween`, or `sortBeginsWith`. The condition applies to the last sort key you provide.

The following examples query the *OrdersByStatusDateAmount* GSI, progressively adding sort keys to narrow the results.

```
DynamoDbIndex<OrderItem> index = orderTable.index("OrdersByStatusDateAmount");

// All PENDING orders for customer-123.
SdkIterable<Page<OrderItem>> allPending = index.query(q -> q
        .queryConditional(QueryConditional.keyEqualTo(k -> k
                .addPartitionValue("customer-123")
                .addPartitionValue("PENDING"))));

// PENDING orders on a specific date.
SdkIterable<Page<OrderItem>> pendingOnDate = index.query(q -> q
        .queryConditional(QueryConditional.keyEqualTo(k -> k
                .addPartitionValue("customer-123")
                .addPartitionValue("PENDING")
                .addSortValue("2025-11-04"))));

// PENDING orders on a specific date with amount greater than 100.
SdkIterable<Page<OrderItem>> filtered = index.query(q -> q
        .queryConditional(QueryConditional.sortGreaterThan(k -> k
                .addPartitionValue("customer-123")
                .addPartitionValue("PENDING")
                .addSortValue("2025-11-04")
                .addSortValue(100))));
```

For more information, see [Multi-key support for Global Secondary Index in DynamoDB](https://aws.amazon.com/blogs/database/multi-key-support-for-global-secondary-index-in-amazon-dynamodb/).
