---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-searchable-encryption.html
---

# Searchable encryption in DynamoDB
<a name="ddb-searchable-encryption"></a>

To configure your Amazon DynamoDB tables for searchable encryption, you must use the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) to generate, encrypt, and decrypt the data keys used to protect your items. You must also include the [`SearchConfig`](ddb-net-using.md#ddb-net-search-config) in your table encryption configuration.

**Note**
If you're using the Java client-side encryption library for DynamoDB, you must use the low-level AWS Database Encryption SDK for DynamoDB API to encrypt, sign, verify, and decrypt your table items. The DynamoDB Enhanced Client and lower-level `DynamoDBItemEncryptor` do not support searchable encryption.

**Topics**
+ [Configuring secondary indexes with beacons](#ddb-beacon-indexes)
+ [Testing beacon outputs](#ddb-beacon-testing)

## Configuring secondary indexes with beacons
<a name="ddb-beacon-indexes"></a>

After you [configure your beacons](configure-beacons.md), you must configure a secondary index that reflects each beacon before you can search on the encrypted attributes.

When you configure a standard or compound beacon, the AWS Database Encryption SDK adds the `aws_dbe_b_` prefix to the beacon name so that the server can easily identify beacons. For example, if you name a compound beacon, `compoundBeacon`, the full beacon name is actually `aws_dbe_b_compoundBeacon`. If you want to configure [secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) that include a standard or compound beacon, you must include the `aws_dbe_b_` prefix when you identify the beacon name.

**Partition and sort keys**
You cannot encrypt primary key values. Your partition and sort keys must be signed. Your primary key values cannot be a standard or compound beacon.
Your primary key values must be `SIGN_ONLY`, unless you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.
Your primary key values can be signed beacons. If you configured distinct signed beacons for each of your primary key values, you must specify the attribute name that identifies the primary key value as the signed beacon name. However, the AWS Database Encryption SDK does not add the `aws_dbe_b_` prefix to signed beacons. Even if you configured distinct signed beacons for your primary key values, you only need to specify the attribute names for the primary key values when you configure a secondary index.

**Local secondary indexes**
The sort key for a [local secondary index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html) can be a beacon.
If you specify a beacon for the sort key, the type must be String. If you specify a standard or compound beacon for the sort key, you must include the `aws_dbe_b_` prefix when you specify the beacon name. If you specify a signed beacon, specify the beacon name without any prefix.

**Global secondary indexes**
The partition and sort keys for a [global secondary index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html) can both be beacons.
If you specify a beacon for the partition or sort key, the type must be String. If you specify a standard or compound beacon for the sort key, you must include the `aws_dbe_b_` prefix when you specify the beacon name. If you specify a signed beacon, specify the beacon name without any prefix.

**Attribute projections**
A [projection](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.Projections) is the set of attributes that is copied from a table into a secondary index. The partition key and sort key of the table are always projected into the index; you can project other attributes to support your application's query requirements. DynamoDB provides three different options for attribute projections: `KEYS_ONLY`, `INCLUDE`, and `ALL`.
If you use the INCLUDE attribute projection to search on a beacon, you must specify the names for all of the attributes that the beacon is constructed from and the beacon name with the `aws_dbe_b_` prefix. For example, if you configured a compound beacon, `compoundBeacon`, from `field1`, `field2`, and `field3`, you must specify `aws_dbe_b_compoundBeacon`, `field1`, `field2`, and `field3` in the projection.
A global secondary index can only use the attributes explicitly specified in the projection, but a local secondary index can use any attribute.

## Testing beacon outputs
<a name="ddb-beacon-testing"></a>

If you [configured compound beacons](configure-beacons.md#config-compound-beacons) or constructed your beacons using [virtual fields](configure-beacons.md#create-virtual-field), we recommend verifying that these beacons produce the expected output before populating your DynamoDB table.

The AWS Database Encryption SDK provides the `DynamoDbEncryptionTransforms` service to help you troubleshoot virtual field and compound beacon outputs.

### Testing virtual fields
<a name="ddb-beacon-testing-virtual-field"></a>

The following snippet creates test items, defines the `DynamoDbEncryptionTransforms` service with the [DynamoDB table encryption configuration](ddb-java-using.md#ddb-config-encrypt), and demonstrates how to use `ResolveAttributes` to verify that the virtual field produces the expected output.

------
#### [ Java ]

**See the complete code sample**: [VirtualBeaconSearchableEncryptionExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/searchableencryption/VirtualBeaconSearchableEncryptionExample.java)

```
// Create test items
final PutItemRequest itemWithHasTestResultPutRequest = PutItemRequest.builder()
    .tableName(ddbTableName)
    .item(itemWithHasTestResult)
    .build();

final PutItemResponse itemWithHasTestResultPutResponse = ddb.putItem(itemWithHasTestResultPutRequest);

final PutItemRequest itemWithNoHasTestResultPutRequest = PutItemRequest.builder()
    .tableName(ddbTableName)
    .item(itemWithNoHasTestResult)
    .build();

final PutItemResponse itemWithNoHasTestResultPutResponse = ddb.putItem(itemWithNoHasTestResultPutRequest);

// Define the DynamoDbEncryptionTransforms service
final DynamoDbEncryptionTransforms trans = DynamoDbEncryptionTransforms.builder()
    .DynamoDbTablesEncryptionConfig(encryptionConfig).build();

// Verify configuration
final ResolveAttributesInput resolveInput = ResolveAttributesInput.builder()
    .TableName(ddbTableName)
    .Item(itemWithHasTestResult)
    .Version(1)
    .build();
final ResolveAttributesOutput resolveOutput = trans.ResolveAttributes(resolveInput);

// Verify that VirtualFields has the expected value
Map<String, String> vf = new HashMap<>();
vf.put("stateAndHasTestResult", "CAt");
assert resolveOutput.VirtualFields().equals(vf);
```

------
#### [ C\# / .NET ]

**See the complete code sample**: [VirtualBeaconSearchableEncryptionExample.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/searchableencryption/VirtualBeaconSearchableEncryptionExample.cs).

```
 // Create item with hasTestResult=true
var itemWithHasTestResult = new Dictionary<String, AttributeValue>
{
    ["customer_id"] = new AttributeValue("ABC-123"),
    ["create_time"] = new AttributeValue { N = "1681495205" },
    ["state"] = new AttributeValue("CA"),
    ["hasTestResult"] = new AttributeValue { BOOL = true }
};

// Create item with hasTestResult=false
var itemWithNoHasTestResult = new Dictionary<String, AttributeValue>
{
    ["customer_id"] = new AttributeValue("DEF-456"),
    ["create_time"] = new AttributeValue { N = "1681495205" },
    ["state"] = new AttributeValue("CA"),
    ["hasTestResult"] = new AttributeValue { BOOL = false }
};

// Define the DynamoDbEncryptionTransforms service
var trans = new DynamoDbEncryptionTransforms(encryptionConfig);

// Verify configuration
var resolveInput = new ResolveAttributesInput
{
    TableName = ddbTableName,
    Item = itemWithHasTestResult,
    Version = 1
};
var resolveOutput = trans.ResolveAttributes(resolveInput);

// Verify that VirtualFields has the expected value
Debug.Assert(resolveOutput.VirtualFields.Count == 1);
Debug.Assert(resolveOutput.VirtualFields["stateAndHasTestResult"] == "CAt");
```

------
#### [ Rust ]

**See the complete code sample**: [virtual\_beacon\_searchable\_encryption.rs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/searchableencryption/virtual_beacon_searchable_encryption.rs).

```
// Create item with hasTestResult=true
let item_with_has_test_result = HashMap::from([
    (
        "customer_id".to_string(),
        AttributeValue::S("ABC-123".to_string()),
    ),
    (
        "create_time".to_string(),
        AttributeValue::N("1681495205".to_string()),
    ),
    ("state".to_string(), AttributeValue::S("CA".to_string())),
    ("hasTestResult".to_string(), AttributeValue::Bool(true)),
]);

// Create item with hasTestResult=false
let item_with_no_has_test_result = HashMap::from([
    (
        "customer_id".to_string(),
        AttributeValue::S("DEF-456".to_string()),
    ),
    (
        "create_time".to_string(),
        AttributeValue::N("1681495205".to_string()),
    ),
    ("state".to_string(), AttributeValue::S("CA".to_string())),
    ("hasTestResult".to_string(), AttributeValue::Bool(false)),
]);

// Define the transform service
let trans = transform_client::Client::from_conf(encryption_config.clone())?;

// Verify the configuration
let resolve_output = trans
    .resolve_attributes()
    .table_name(ddb_table_name)
    .item(item_with_has_test_result.clone())
    .version(1)
    .send()
    .await?;

// Verify that VirtualFields has the expected value
let virtual_fields = resolve_output.virtual_fields.unwrap();
assert_eq!(virtual_fields.len(), 1);
assert_eq!(virtual_fields["stateAndHasTestResult"], "CAt");
```

------

### Testing compound beacons
<a name="ddb-beacon-testing-compound-beacon"></a>

The following snippet creates a test item, defines the `DynamoDbEncryptionTransforms` service with the [DynamoDB table encryption configuration](ddb-java-using.md#ddb-config-encrypt), and demonstrates how to use `ResolveAttributes` to verify that the compound beacon produces the expected output.

------
#### [ Java ]

**See the complete code sample**: [CompoundBeaconSearchableEncryptionExample.java](https://github.com/aws/aws-database-encryption-sdk-dynamodb//blob/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples/searchableencryption/CompoundBeaconSearchableEncryptionExample.java)

```
// Create an item with both attributes used in the compound beacon.
final HashMap<String, AttributeValue> item = new HashMap<>();
item.put("work_id", AttributeValue.builder().s("9ce39272-8068-4efd-a211-cd162ad65d4c").build());
item.put("inspection_date", AttributeValue.builder().s("2023-06-13").build());
item.put("inspector_id_last4", AttributeValue.builder().s("5678").build());
item.put("unit", AttributeValue.builder().s("011899988199").build());

// Define the DynamoDbEncryptionTransforms service
final DynamoDbEncryptionTransforms trans = DynamoDbEncryptionTransforms.builder()
    .DynamoDbTablesEncryptionConfig(encryptionConfig).build();

// Verify configuration
final ResolveAttributesInput resolveInput = ResolveAttributesInput.builder()
    .TableName(ddbTableName)
    .Item(item)
    .Version(1)
    .build();

final ResolveAttributesOutput resolveOutput = trans.ResolveAttributes(resolveInput);

// Verify that CompoundBeacons has the expected value
Map<String, String> cbs = new HashMap<>();
cbs.put("last4UnitCompound", "L-5678.U-011899988199");
assert resolveOutput.CompoundBeacons().equals(cbs);
// Note : the compound beacon actually stored in the table is not "L-5678.U-011899988199"
// but rather something like "L-abc.U-123", as both parts are EncryptedParts
// and therefore the text is replaced by the associated beacon
```

------
#### [ C\# / .NET ]

**See the complete code sample**: [CompoundBeaconSearchableEncryptionExample.cs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/searchableencryption/CompoundBeaconSearchableEncryptionExample.cs)

```
// Create an item with both attributes used in the compound beacon
var item = new Dictionary<String, AttributeValue>
{
    ["work_id"] = new AttributeValue("9ce39272-8068-4efd-a211-cd162ad65d4c"),
    ["inspection_date"] = new AttributeValue("2023-06-13"),
    ["inspector_id_last4"] = new AttributeValue("5678"),
    ["unit"] = new AttributeValue("011899988199")
};

// Define the DynamoDbEncryptionTransforms service
var trans = new DynamoDbEncryptionTransforms(encryptionConfig);

// Verify configuration
var resolveInput = new ResolveAttributesInput
{
    TableName = ddbTableName,
    Item = item,
    Version = 1
};
var resolveOutput = trans.ResolveAttributes(resolveInput);

// Verify that CompoundBeacons has the expected value
Debug.Assert(resolveOutput.CompoundBeacons.Count == 1);
Debug.Assert(resolveOutput.CompoundBeacons["last4UnitCompound"] == "L-5678.U-011899988199");
// Note : the compound beacon actually stored in the table is not "L-5678.U-011899988199"
// but rather something like "L-abc.U-123", as both parts are EncryptedParts
// and therefore the text is replaced by the associated beacon
```

------
#### [ Rust ]

**See the complete code sample**: [compound\_beacon\_searchable\_encryption.rs](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/searchableencryption/compound_beacon_searchable_encryption.rs)

```
// Create an item with both attributes used in the compound beacon
let item = HashMap::from([
    (
        "work_id".to_string(),
        AttributeValue::S("9ce39272-8068-4efd-a211-cd162ad65d4c".to_string()),
    ),
    (
        "inspection_date".to_string(),
        AttributeValue::S("2023-06-13".to_string()),
    ),
    (
        "inspector_id_last4".to_string(),
        AttributeValue::S("5678".to_string()),
    ),
    (
        "unit".to_string(),
        AttributeValue::S("011899988199".to_string()),
    ),
]);

// Define the transforms service
let trans = transform_client::Client::from_conf(encryption_config.clone())?;

// Verify configuration
let resolve_output = trans
    .resolve_attributes()
    .table_name(ddb_table_name)
    .item(item.clone())
    .version(1)
    .send()
    .await?;

// Verify that CompoundBeacons has the expected value
let compound_beacons = resolve_output.compound_beacons.unwrap();
assert_eq!(compound_beacons.len(), 1);
assert_eq!(
    compound_beacons["last4UnitCompound"],
    "L-5678.U-011899988199"
);
// but rather something like "L-abc.U-123", as both parts are EncryptedParts
// and therefore the text is replaced by the associated beacon
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
