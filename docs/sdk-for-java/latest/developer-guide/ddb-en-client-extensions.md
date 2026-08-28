---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-extensions.html
---

# Use extensions to customize DynamoDB Enhanced Client operations
<a name="ddb-en-client-extensions"></a>

The DynamoDB Enhanced Client API supports plugin extensions that provide functionality beyond mapping operations. Extensions use two hook methods to modify data during read and write operations:
+ `beforeWrite()` - Modifies a write operation before it happens
+ `afterRead()` - Modifies the results of a read operation after it happens

Some operations (such as item updates) perform both a write and then a read, so both hook methods are called.

## How extensions are loaded
<a name="ddb-en-client-extensions-loading"></a>

Extensions are loaded in the order that you specify in the enhanced client builder. The load order can be important because one extension can act on values that have been transformed by a previous extension.

By default, the enhanced client loads two extensions:
+ `[VersionedRecordExtension](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/extensions/VersionedRecordExtension.html)` - Provides optimistic locking
+ `[AtomicCounterExtension](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/extensions/AtomicCounterExtension.html)` - Automatically increments counter attributes

You can override the default behavior with the enhanced client builder and load any extension. You can also specify none if you don't want the default extensions.

**Important**
If you load your own extensions, the enhanced client doesn't load any default extensions. If you want the behavior provided by either default extension, you need to explicitly add it to the list of extensions.

The following example shows how to load a custom extension named `verifyChecksumExtension` after the `VersionedRecordExtension`. The `AtomicCounterExtension` is not loaded in this example.

```
DynamoDbEnhancedClientExtension versionedRecordExtension = VersionedRecordExtension.builder().build();

DynamoDbEnhancedClient enhancedClient =
    DynamoDbEnhancedClient.builder()
                          .dynamoDbClient(dynamoDbClient)
                          .extensions(versionedRecordExtension, verifyChecksumExtension)
                          .build();
```

## Available extension details and configuration
<a name="ddb-en-client-extensions-details"></a>

The following sections provide detailed information about each available extension in the SDK.

### Implement optimistic locking with the `VersionedRecordExtension`
<a name="ddb-en-client-extensions-VRE"></a>

The `VersionedRecordExtension` extension provides optimistic locking by incrementing and tracking an item version number as items are written to the database. A condition is added to every write that causes the write to fail if the version number of the actual persisted item doesn't match the value that the application last read.

#### Configuration
<a name="ddb-en-client-extensions-VRE-conf"></a>

To specify which attribute to use to track the item version number, tag a numeric attribute in the table schema.

The following snippet specifies that the `version` attribute should hold the item version number.

```
    @DynamoDbVersionAttribute
    public Integer getVersion() {...};
    public void setVersion(Integer version) {...};
```

The equivalent static table schema approach is shown in the following snippet.

```
    .addAttribute(Integer.class, a -> a.name("version")
                                       .getter(Customer::getVersion)
                                       .setter(Customer::setVersion)
                                        // Apply the 'version' tag to the attribute.
                                       .tags(VersionedRecordExtension.AttributeTags.versionAttribute())
```

#### How it works
<a name="ddb-en-client-extensions-VRE-how-it-works"></a>

Optimistic locking with the `VersionedRecordExtension` has the following impact on these `DynamoDbEnhancedClient` and `DynamoDbTable` methods:

**`putItem`**
New items are assigned a initial version value of 0. This can be configured with `@DynamoDbVersionAttribute(startAt = {{X}})`.

**`updateItem`**
If you retrieve an item, update one or more of its properties, and attempt to save the changes, the operation succeeds only if the version number on the client side and the server side match.
If successful, the version number is automatically incremented by 1. This can be configured with `@DynamoDbVersionAttribute(incrementBy = {{X}})`.

**`deleteItem`**
The `DynamoDbVersionAttribute` annotation has no effect. You must add a condition expressions manually when deleting an item.
The following example adds a conditional expression to ensure that the item deleted is the item that was read. In the following example `recordVersion` is the bean's attribute annotated with `@DynamoDbVersionAttribute`.

```
// 1. Read the item and get its current version.
Customer item = customerTable.getItem(Key.builder().partitionValue("someId").build());
// `recordVersion` is the bean's attribute that is annotated with `@DynamoDbVersionAttribute`.
AttributeValue currentVersion = item.getRecordVersion();

// 2. Create conditional delete with the `currentVersion` value.
DeleteItemEnhancedRequest deleteItemRequest =
    DeleteItemEnhancedRequest.builder()
       .key(KEY)
       .conditionExpression(Expression.builder()
           .expression("recordVersion = :current_version_value")
           .putExpressionValue(":current_version_value", currentVersion)
           .build()).build();

customerTable.deleteItem(deleteItemRequest);
```

**`transactWriteItems`**
+ `addPutItem`: This method has the same behavior as `putItem`.
+ `addUpdateItem`: This method has the same behavior as `updateItem`.
+ `addDeleteItem`: This method has the same behavior as `deleteItem`.

**`batchWriteItem`**
+ `addPutItem`: This method has the same behavior as `putItem`.
+ `addDeleteItem`: This method has the same behavior as `deleteItem`.

**Note**
DynamoDB global tables use a ['last writer wins' reconciliation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) between concurrent updates, where DynamoDB makes a best effort to determine the last writer. If you use global tables, this 'last writer wins' policy means that locking strategies may not work as expected, because all replicas will eventually converge based on the last write determined by DynamoDB.

#### How to disable
<a name="ddb-en-client-extensions-VRE-how-to-disable"></a>

To disable optimistic locking, do not use the `@DynamoDbVersionAttribute` annotation.

### Implement counters with the `AtomicCounterExtension`
<a name="ddb-en-client-extensions-ACE"></a>

The `AtomicCounterExtension` extension increments a tagged numerical attribute each time a record is written to the database. You can specify start and increment values. If no values are specified, the start value is set to 0 and the attribute's value increments by 1.

#### Configuration
<a name="ddb-en-client-extensions-ACE-conf"></a>

To specify which attribute is a counter, tag an attribute of type `Long` in the table schema.

The following snippet shows the use of the default start and increment values for the `counter` attribute.

```
    @DynamoDbAtomicCounter
    public Long getCounter() {...};
    public void setCounter(Long counter) {...};
```

The static table schema approach is shown in the following snippet. The atomic counter extension uses a start value of 10 and increments the value by 5 each time the record is written.

```
    .addAttribute(Integer.class, a -> a.name("counter")
                                       .getter(Customer::getCounter)
                                       .setter(Customer::setCounter)
                                        // Apply the 'atomicCounter' tag to the attribute with start and increment values.
                                       .tags(StaticAttributeTags.atomicCounter(10L, 5L))
```

### Add timestamps with the `AutoGeneratedTimestampRecordExtension`
<a name="ddb-en-client-extensions-AGTE"></a>

The `AutoGeneratedTimestampRecordExtension` extension automatically updates tagged attributes of type `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` with a current timestamp every time the item is successfully written to the database. This extension is not loaded by default.

#### Configuration
<a name="ddb-en-client-extensions-AGTE-conf"></a>

To specify which attribute to update with the current timestamp, tag the `Instant` attribute in the table schema.

The `lastUpdate` attribute is the target of the extension's behavior in the following snippet. Note the requirement that the attribute must be an `Instant` type.

```
    @DynamoDbAutoGeneratedTimestampAttribute
    public Instant getLastUpdate() {...}
    public void setLastUpdate(Instant lastUpdate) {...}
```

The equivalent static table schema approach is shown in the following snippet.

```
     .addAttribute(Instant.class, a -> a.name("lastUpdate")
                                        .getter(Customer::getLastUpdate)
                                        .setter(Customer::setLastUpdate)
                                        // Applying the 'autoGeneratedTimestamp' tag to the attribute.
                                        .tags(AutoGeneratedTimestampRecordExtension.AttributeTags.autoGeneratedTimestampAttribute())
```

### Generate a UUID with the AutoGeneratedUuidExtension
<a name="ddb-en-client-extensions-AGUE"></a>

The `AutoGeneratedUuidExtension` extension generates a unique UUID (Universally Unique Identifier) for an attribute when a new record is written to the database. Uses the Java JDK [UUID.randomUUID()](https://docs.oracle.com/javase/8/docs/api/java/util/UUID.html#randomUUID--) method and applies to attributes of type `java.lang.String`. This extension is not loaded by default.

#### Configuration
<a name="ddb-en-client-extensions-AGUE-conf"></a>

The `uniqueId` attribute is the target of the extension's behavior in the following snippet.

```
    @AutoGeneratedUuidExtension
    public String getUniqueId() {...}
    public void setUniqueId(String uniqueId) {...}
```

The equivalent static table schema approach is shown in the following snippet.

```
     .addAttribute(String.class, a -> a.name("uniqueId")
                                        .getter(Customer::getUniqueId)
                                        .setter(Customer::setUniqueId)
                                        // Applying the 'autoGeneratedUuid' tag to the attribute.
                                        .tags(AutoGeneratedUuidExtension.AttributeTags.autoGeneratedUuidAttribute())
```

If you want the extension to populate the UUID only for `putItem` methods and not for `updateItem` methods, add the [update behavior](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/mapper/UpdateBehavior.html) annotation as shown in the following snippet.

```
    @AutoGeneratedUuidExtension
    @DynamoDbUpdateBehavior(UpdateBehavior.WRITE_IF_NOT_EXISTS)
    public String getUniqueId() {...}
    public void setUniqueId(String uniqueId) {...}
```

If you use the static table schema approach, use the following equivalent code.

```
     .addAttribute(String.class, a -> a.name("uniqueId")
                                        .getter(Customer::getUniqueId)
                                        .setter(Customer::setUniqueId)
                                        // Applying the 'autoGeneratedUuid' tag to the attribute.
                                        .tags(AutoGeneratedUuidExtension.AttributeTags.autoGeneratedUuidAttribute(),
                                              StaticAttributeTags.updateBehavior(UpdateBehavior.WRITE_IF_NOT_EXISTS))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
