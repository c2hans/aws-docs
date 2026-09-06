---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use.html
---

# Learn the basics of the DynamoDB Enhanced Client API
<a name="ddb-en-client-use"></a>

This topic discusses the basic features of the DynamoDB Enhanced Client API and compares it to the [standard DynamoDB client API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/package-summary.html).

If you are new to the DynamoDB Enhanced Client API, we recommend that you go through the [introductory tutorial](ddb-en-client-getting-started.md) to familiarize yourself with fundamental classes.

## DynamoDB items in Java
<a name="ddb-en-client-use-usecase"></a>

DynamoDB tables store items. Depending on your use case, items on the Java side can take the form of statically structured data or structures created dynamically.

If your use case calls for items with a consistent set of attributes, use [annotated classes](ddb-en-client-gs-tableschema.md#ddb-en-client-gs-tableschema-anno-bean) or use a [builder](ddb-en-client-gs-tableschema.md#ddb-en-client-gs-tableschema-builder) to generate the appropriate statically-typed `TableSchema`.

Alternatively, if you need to store items that consist of varying structures, create a `DocumentTableSchema`. `DocumentTableSchema` is part of the [Enhanced Document API](ddb-en-client-doc-api.md) and requires only a statically-typed primary key and works with `EnhancedDocument` instances to hold the data elements. The Enhanced Document API is covered in another [topic.](ddb-en-client-doc-api.md)

## Attribute types for data model classes
<a name="ddb-en-client-use-types"></a>

Although DynamoDB supports [a small number of attribute types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) compared to the rich type system of Java, the DynamoDB Enhanced Client API provides mechanisms to convert members of a Java class to and from DynamoDB attribute types.

The attribute types (properties) of your Java data classes should be objects types, not primitives. For example, always use `Long` and `Integer` object data types, not `long` and `int` primitives.

By default, the DynamoDB Enhanced Client API supports attribute converters for a large number of types, such as [Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html), [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html), [BigDecimal](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/internal/converter/attribute/BigDecimalAttributeConverter.html), and [Instant](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/internal/converter/attribute/InstantAsStringAttributeConverter.html). The list appears in the [known implementing classes of the AttributeConverter interface](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/AttributeConverter.html). The list includes many types and collections such as maps, lists, and sets.

To store the data for an attribute type that isn't supported by default or doesn't conform to the JavaBean convention, you can write a custom `AttributeConverter` implementation to do the conversion. See the attribute conversion section for an [example](ddb-en-client-adv-features-conversion.md#ddb-en-client-adv-features-conversion-example).

To store the data for an attribute type whose class conforms to the Java beans specification (or an [immutable data class](ddb-en-client-use-immut.md)), you can take two approaches.
+ If you have access to the source file, you can annotate the class with `@DynamoDbBean` (or `@DynamoDbImmutable`). The section that discusses nested attributes shows [examples](ddb-en-client-adv-features-nested.md#ddb-en-client-adv-features-nested-map-anno) of using annotated classes.
+ If do not have access to the source file of the JavaBean data class for the attribute (or you don't want to annotate the source file of a class that you do have access to), then you can use the builder approach. This creates a table schema without defining the keys. Then, you can nest this table schema inside another table schema to perform the mapping. The nested attribute section has an [example](ddb-en-client-adv-features-nested.md#ddb-en-client-adv-features-nested-map-builder) showing use of nested schemas.

### Null values
<a name="ddb-en-client-use-types-nulls"></a>

When you use the `putItem` method, the enhanced client does not include null-valued attributes of a mapped data object in the request to DynamoDB.

The SDK's default behavior for `updateItem` requests removes attributes from the item in DynamoDB that are set to null in the object that you submit in the `updateItem` method. If you intend to update some attribute values and keep the others unchanged, you have two options.
+ Retrieve the item (by using `getItem`) before you make changes to values. By using this approach, the SDK submits all updated and old values to DynamoDB.
+ Use either the `[IgnoreNullsMode](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/IgnoreNullsMode.html).SCALAR_ONLY` or `IgnoreNullsMode.MAPS_ONLY` when you build the request to update the item. Both modes ignore null-valued properties in the object that represent scalar attributes in DynamoDB. The [Update items that contain complex types](ddb-en-client-adv-features-nested.md#ddb-en-client-adv-features-nested-updates) topic in this guide contains more information about the `IgnoreNullsMode` values and how to work with complex types.

The following example demonstrates `ignoreNullsMode()` for the `updateItem()` method.

```
    public static void updateItemNullsExample() {
        Customer customer = new Customer();
        customer.setCustName("CustomerName");
        customer.setEmail("email");
        customer.setId("1");
        customer.setRegistrationDate(Instant.now());

        logger.info("Original customer: {}", customer);

        // Put item with values for all attributes.
        try {
            customerAsyncDynamoDbTable.putItem(customer).join();
        } catch (RuntimeException rte) {
            logger.error("A exception occurred during putItem: {}", rte.getCause().getMessage(), rte);
            return;
        }

        // Create a Customer instance with the same 'id' and 'email' values, but a different 'name' value.
        // Do not set the 'registrationDate' attribute.
        Customer customerForUpdate = new Customer();
        customerForUpdate.setCustName("NewName");
        customerForUpdate.setEmail("email");
        customerForUpdate.setId("1");

        // Update item without setting the 'registrationDate' property and set IgnoreNullsMode to SCALAR_ONLY.
        try {
            Customer updatedWithNullsIgnored = customerAsyncDynamoDbTable.updateItem(b -> b
                            .item(customerForUpdate)
                            .ignoreNullsMode(IgnoreNullsMode.SCALAR_ONLY))
                    .join();
            logger.info("Customer updated with nulls ignored: {}", updatedWithNullsIgnored.toString());
        } catch (RuntimeException rte) {
            logger.error("An exception occurred during updateItem: {}", rte.getCause().getMessage(), rte);
            return;
        }

        // Update item without setting the registrationDate attribute and not setting ignoreNulls to true.
        try {
            Customer updatedWithNullsUsed = customerAsyncDynamoDbTable.updateItem(customerForUpdate)
                    .join();
            logger.info("Customer updated with nulls used: {}", updatedWithNullsUsed.toString());
        } catch (RuntimeException rte) {
            logger.error("An exception occurred during updateItem: {}", rte.getCause().getMessage(), rte);
        }
    }

// Logged lines.
Original customer: Customer [id=1, name=CustomerName, email=email, regDate=2024-10-11T14:12:30.222858Z]
Customer updated with nulls ignored: Customer [id=1, name=NewName, email=email, regDate=2024-10-11T14:12:30.222858Z]
Customer updated with nulls used: Customer [id=1, name=NewName, email=email, regDate=null]
```

## DynamoDB Enhanced Client basic methods
<a name="ddb-en-client-use-basic-ops"></a>

Basic methods of the enhanced client map to the DynamoDB service operations that they're named after. The following examples show the simplest variation of each method. You can customize each method by passing in an enhanced request object. Enhanced request objects offer most of the features available in the standard DynamoDB client. They are fully documented in the AWS SDK for Java 2.x API Reference.

The example uses the [`Customer` class](ddb-en-client-gs-tableschema.md#ddb-en-client-gs-tableschema-anno-bean-cust) shown previously.

```
// CreateTable
customerTable.createTable();

// GetItem
Customer customer = customerTable.getItem(Key.builder().partitionValue("a123").build());

// UpdateItem
Customer updatedCustomer = customerTable.updateItem(customer);

// PutItem
customerTable.putItem(customer);

// DeleteItem
Customer deletedCustomer = customerTable.deleteItem(Key.builder().partitionValue("a123").sortValue(456).build());

// Query
PageIterable<Customer> customers = customerTable.query(keyEqualTo(k -> k.partitionValue("a123")));

// Scan
PageIterable<Customer> customers = customerTable.scan();

// BatchGetItem
BatchGetResultPageIterable batchResults =
    enhancedClient.batchGetItem(r -> r.addReadBatch(ReadBatch.builder(Customer.class)
                                      .mappedTableResource(customerTable)
                                      .addGetItem(key1)
                                      .addGetItem(key2)
                                      .addGetItem(key3)
                                      .build()));

// BatchWriteItem
batchResults = enhancedClient.batchWriteItem(r -> r.addWriteBatch(WriteBatch.builder(Customer.class)
                                                   .mappedTableResource(customerTable)
                                                   .addPutItem(customer)
                                                   .addDeleteItem(key1)
                                                   .addDeleteItem(key1)
                                                   .build()));

// TransactGetItems
transactResults = enhancedClient.transactGetItems(r -> r.addGetItem(customerTable, key1)
                                                        .addGetItem(customerTable, key2));

// TransactWriteItems
enhancedClient.transactWriteItems(r -> r.addConditionCheck(customerTable,
                                                           i -> i.key(orderKey)
                                                                 .conditionExpression(conditionExpression))
                                        .addUpdateItem(customerTable, customer)
                                        .addDeleteItem(customerTable, key));
```

## Compare DynamoDB Enhanced Client to standard DynamoDB client
<a name="ddb-en-client-use-compare"></a>

Both DynamoDB client APIs—[standard](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/package-summary.html) and [enhanced](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/package-summary.html)—let you work with DynamoDB tables to perform CRUD (create, read, update and delete) data-level operations. The difference between the client APIs is how that is accomplished. Using the standard client, you work directly with low-level data attributes. The enhanced client API uses familiar Java classes and maps to the low-level API behind the scenes.

While both client APIs support data-level operations, the standard DynamoDB client also supports resource-level operations. Resource-level operations manage the database, such as creating backups, listing tables, and updating tables. The enhanced client API supports a select number of resource-level operations such as creating, describing, and deleting tables.

To illustrate the different approaches used by the two client APIs, the following code examples show the creation of the same `ProductCatalog` table using the standard client and the enhanced client.

### Compare: Create a table using the standard DynamoDB client
<a name="ddb-en-client-use-compare-cs1"></a>

```
DependencyFactory.dynamoDbClient().createTable(builder -> builder
        .tableName(TABLE_NAME)
        .attributeDefinitions(
                b -> b.attributeName("id").attributeType(ScalarAttributeType.N),
                b -> b.attributeName("title").attributeType(ScalarAttributeType.S),
                b -> b.attributeName("isbn").attributeType(ScalarAttributeType.S)
        )
        .keySchema(
                builder1 -> builder1.attributeName("id").keyType(KeyType.HASH),
                builder2 -> builder2.attributeName("title").keyType(KeyType.RANGE)
        )
        .globalSecondaryIndexes(builder3 -> builder3
                        .indexName("products_by_isbn")
                        .keySchema(builder2 -> builder2
                                .attributeName("isbn").keyType(KeyType.HASH))
                        .projection(builder2 -> builder2
                                .projectionType(ProjectionType.INCLUDE)
                                .nonKeyAttributes("price", "authors"))
                        .provisionedThroughput(builder4 -> builder4
                                .writeCapacityUnits(5L).readCapacityUnits(5L))
        )
        .provisionedThroughput(builder1 -> builder1
                .readCapacityUnits(5L).writeCapacityUnits(5L))
);
```

### Compare: Create a table using the DynamoDB Enhanced Client
<a name="ddb-en-client-use-compare-cs2"></a>

```
DynamoDbEnhancedClient enhancedClient = DependencyFactory.enhancedClient();
productCatalog = enhancedClient.table(TABLE_NAME, TableSchema.fromImmutableClass(ProductCatalog.class));
productCatalog.createTable(b -> b
        .provisionedThroughput(b1 -> b1.readCapacityUnits(5L).writeCapacityUnits(5L))
        .globalSecondaryIndices(b2 -> b2.indexName("products_by_isbn")
                .projection(b4 -> b4
                        .projectionType(ProjectionType.INCLUDE)
                        .nonKeyAttributes("price", "authors"))
                .provisionedThroughput(b3 -> b3.writeCapacityUnits(5L).readCapacityUnits(5L))
        )
);
```

The enhanced client uses the following annotated data class. The DynamoDB Enhanced Client maps Java data types to DynamoDB data types for less verbose code that is easier to follow. `ProductCatalog` is an example of using an immutable class with the DynamoDB Enhanced Client. The use of Immutable classes for mapped data classes is [discussed later](ddb-en-client-use-immut.md) in this topic.

### `ProductCatalog` class
<a name="ddb-en-client-use-compare-cs3"></a>

```
package org.example.tests.model;

import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbIgnore;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbImmutable;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSecondaryPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSortKey;

import java.math.BigDecimal;
import java.util.Objects;
import java.util.Set;

@DynamoDbImmutable(builder = ProductCatalog.Builder.class)
public class ProductCatalog implements Comparable<ProductCatalog> {
    private Integer id;
    private String title;
    private String isbn;
    private Set<String> authors;
    private BigDecimal price;

    private ProductCatalog(Builder builder){
        this.authors = builder.authors;
        this.id = builder.id;
        this.isbn = builder.isbn;
        this.price = builder.price;
        this.title = builder.title;
    }

    public static Builder builder(){ return new Builder(); }

    @DynamoDbPartitionKey
    public Integer id() { return id; }

    @DynamoDbSortKey
    public String title() { return title; }

    @DynamoDbSecondaryPartitionKey(indexNames = "products_by_isbn")
    public String isbn() { return isbn; }
    public Set<String> authors() { return authors; }
    public BigDecimal price() { return price; }

    public static final class Builder {
      private Integer id;
      private String title;
      private String isbn;
      private Set<String> authors;
      private BigDecimal price;
      private Builder(){}

      public Builder id(Integer id) { this.id = id; return this; }
      public Builder title(String title) { this.title = title; return this; }
      public Builder isbn(String ISBN) { this.isbn = ISBN; return this; }
      public Builder authors(Set<String> authors) { this.authors = authors; return this; }
      public Builder price(BigDecimal price) { this.price = price; return this; }
      public ProductCatalog build() { return new ProductCatalog(this); }
  }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("ProductCatalog{");
        sb.append("id=").append(id);
        sb.append(", title='").append(title).append('\'');
        sb.append(", isbn='").append(isbn).append('\'');
        sb.append(", authors=").append(authors);
        sb.append(", price=").append(price);
        sb.append('}');
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ProductCatalog that = (ProductCatalog) o;
        return id.equals(that.id) && title.equals(that.title) && Objects.equals(isbn, that.isbn) && Objects.equals(authors, that.authors) && Objects.equals(price, that.price);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, title, isbn, authors, price);
    }

    @Override
    @DynamoDbIgnore
    public int compareTo(ProductCatalog other) {
        if (this.id.compareTo(other.id) != 0){
            return this.id.compareTo(other.id);
        } else {
            return this.title.compareTo(other.title);
        }
    }
}
```

The following two code examples of a batch write illustrate the verboseness and lack of type safety when using the standard client as opposed to the enhanced client.

### Compare: Batch write using the standard DynamoDB client
<a name="ddb-en-client-use-compare-cs4"></a>

```
    public static void batchWriteStandard(DynamoDbClient dynamoDbClient, String tableName) {

        Map<String, AttributeValue> catalogItem = Map.of(
                "authors", AttributeValue.builder().ss("a", "b").build(),
                "id", AttributeValue.builder().n("1").build(),
                "isbn", AttributeValue.builder().s("1-565-85698").build(),
                "title", AttributeValue.builder().s("Title 1").build(),
                "price", AttributeValue.builder().n("52.13").build());

        Map<String, AttributeValue> catalogItem2 = Map.of(
                "authors", AttributeValue.builder().ss("a", "b", "c").build(),
                "id", AttributeValue.builder().n("2").build(),
                "isbn", AttributeValue.builder().s("1-208-98073").build(),
                "title", AttributeValue.builder().s("Title 2").build(),
                "price", AttributeValue.builder().n("21.99").build());

        Map<String, AttributeValue> catalogItem3 = Map.of(
                "authors", AttributeValue.builder().ss("g", "k", "c").build(),
                "id", AttributeValue.builder().n("3").build(),
                "isbn", AttributeValue.builder().s("7-236-98618").build(),
                "title", AttributeValue.builder().s("Title 3").build(),
                "price", AttributeValue.builder().n("42.00").build());

        Set<WriteRequest> writeRequests = Set.of(
                WriteRequest.builder().putRequest(b -> b.item(catalogItem)).build(),
                WriteRequest.builder().putRequest(b -> b.item(catalogItem2)).build(),
                WriteRequest.builder().putRequest(b -> b.item(catalogItem3)).build());

        Map<String, Set<WriteRequest>> productCatalogItems = Map.of(
                "ProductCatalog", writeRequests);

        BatchWriteItemResponse response = dynamoDbClient.batchWriteItem(b -> b.requestItems(productCatalogItems));

        logger.info("Unprocessed items: " + response.unprocessedItems().size());
    }
```

### Compare: Batch write using the DynamoDB Enhanced Client
<a name="ddb-en-client-use-compare-cs5"></a>

```
    public static void batchWriteEnhanced(DynamoDbTable<ProductCatalog> productCatalog) {
        ProductCatalog prod = ProductCatalog.builder()
                .id(1)
                .isbn("1-565-85698")
                .authors(new HashSet<>(Arrays.asList("a", "b")))
                .price(BigDecimal.valueOf(52.13))
                .title("Title 1")
                .build();
        ProductCatalog prod2 = ProductCatalog.builder()
                .id(2)
                .isbn("1-208-98073")
                .authors(new HashSet<>(Arrays.asList("a", "b", "c")))
                .price(BigDecimal.valueOf(21.99))
                .title("Title 2")
                .build();
        ProductCatalog prod3 = ProductCatalog.builder()
                .id(3)
                .isbn("7-236-98618")
                .authors(new HashSet<>(Arrays.asList("g", "k", "c")))
                .price(BigDecimal.valueOf(42.00))
                .title("Title 3")
                .build();

        BatchWriteResult batchWriteResult = DependencyFactory.enhancedClient()
                .batchWriteItem(b -> b.writeBatches(
                        WriteBatch.builder(ProductCatalog.class)
                                .mappedTableResource(productCatalog)
                                .addPutItem(prod).addPutItem(prod2).addPutItem(prod3)
                                .build()
                ));
        logger.info("Unprocessed items: " + batchWriteResult.unprocessedPutItemsForTable(productCatalog).size());
    }
```
