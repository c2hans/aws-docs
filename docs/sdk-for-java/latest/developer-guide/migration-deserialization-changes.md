---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-deserialization-changes.html
---

# Deserialization differences between 1.x and 2.x of the AWS SDK for Java
<a name="migration-deserialization-changes"></a>

## Empty collections in V2 compared to `nulls` in V1
<a name="deserialization-diffs-list-obj-to-req-param"></a>

The SDK for Java v1.x and v2.x differ in how they deserialize JSON responses with lists and maps that are empty.

When the SDK receives a response with a missing property that is modeled as a list or map, V1 deserializes the missing property to `null`, whereas V2 deserializes the property to an immutable empty collection object.

For example, consider the response returned for the `describeTable` method from a DynamoDB client. The following example method contains a V2 DynamoDB client and a V1 DynamoDB client that both execute the `describeTable` method on a table that has no global secondary indexes

**Example of the deserialization of a property modeled as a list that is missing in the response**

```
public void deserializationDiffs(){

    DescribeTableResponse v2Response = dynamoDbClientV2.describeTable(builder -> builder.tableName(TABLE_NAME));
    // V2 provides has* methods on model objects for list/map members. No null check needed.
    LOGGER.info( String.valueOf(v2Response.table().hasGlobalSecondaryIndexes()) );
    LOGGER.info( String.valueOf(v2Response.table().globalSecondaryIndexes().isEmpty()) );
    // V2 deserialize to an empty collection.
    LOGGER.info(v2Response.table().globalSecondaryIndexes().toString());

    // V1 deserialize to null.
    DescribeTableResult v1Result = dynamoDbClientV1.describeTable(new DescribeTableRequest(TABLE_NAME));
    if (v1Result.getTable().getGlobalSecondaryIndexes() != null){
        LOGGER.info(v1Result.getTable().getGlobalSecondaryIndexes().toString());
    } else {
        LOGGER.info("The list of global secondary indexes returned by the V1 call is <null>");
    }
}
```
The following shows the logged output:

```
INFO  org.example.DeserializationDifferences:45 - false
INFO  org.example.DeserializationDifferences:46 - true
INFO  org.example.DeserializationDifferences:48 - []
INFO  org.example.DeserializationDifferences:55 - The list of global secondary indexes returned by the V1 call is <null>
```

The Java SDK 2.x takes an idiomatic approach by deserializing empty lists and maps to immutable empty collections instead of returning `null`, promoting safer and more concise code. With V2, you can check if a service returned an attribute modeled as a list or map with the `has*` method, such as the `hasGlobalSecondaryIndexes` shown in the previous example.

This approach avoids the need for explicit `null` checks and aligns with modern Java best practices for handling absent or empty data structures.

### Complete example
<a name="full-example-deserialization"></a>

```
package org.example;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.model.DescribeTableRequest;
import com.amazonaws.services.dynamodbv2.model.DescribeTableResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.BillingMode;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableResponse;
import software.amazon.awssdk.services.dynamodb.model.KeyType;
import software.amazon.awssdk.services.dynamodb.model.ScalarAttributeType;

import java.util.UUID;

public class DeserializationDifferences {
    private static final Logger LOGGER = LoggerFactory.getLogger(DeserializationDifferences.class);
    private static final String TABLE_NAME = "DeserializationTable-" + UUID.randomUUID();
    DynamoDbClient dynamoDbClientV2 = DynamoDbClient.create();
    AmazonDynamoDB dynamoDbClientV1 = AmazonDynamoDBClientBuilder.standard().withRegion(Regions.US_EAST_1).build();

    public static void main(String[] args) {

        DeserializationDifferences difference = new DeserializationDifferences();
        difference.createTable();
        difference.deserializationDiffs();
        difference.deleteTable();
    }

    public void createTable(){
        dynamoDbClientV2.createTable(b -> b
                .billingMode(BillingMode.PAY_PER_REQUEST)
                .tableName(TABLE_NAME)
                .keySchema(b1 -> b1.attributeName("Id").keyType(KeyType.HASH))
                .attributeDefinitions(b2 -> b2.attributeName("Id").attributeType(ScalarAttributeType.S)));
        dynamoDbClientV2.waiter().waitUntilTableExists(b -> b.tableName(TABLE_NAME));
    }

    public void deserializationDiffs(){

        DescribeTableResponse v2Response = dynamoDbClientV2.describeTable(builder -> builder.tableName(TABLE_NAME));
        // V2 provides has* methods on model objects for list/map members. No null check needed.
        LOGGER.info( String.valueOf(v2Response.table().hasGlobalSecondaryIndexes()) );
        LOGGER.info( String.valueOf(v2Response.table().globalSecondaryIndexes().isEmpty()) );
        // V2 deserialize to an empty collection.
        LOGGER.info(v2Response.table().globalSecondaryIndexes().toString());

        // V1 deserialize to null.
        DescribeTableResult v1Result = dynamoDbClientV1.describeTable(new DescribeTableRequest(TABLE_NAME));
        if (v1Result.getTable().getGlobalSecondaryIndexes() != null){
            LOGGER.info(v1Result.getTable().getGlobalSecondaryIndexes().toString());
        } else {
            LOGGER.info("The list of global secondary indexes returned by the V1 call is <null>");
        }
    }

    public void deleteTable(){
        dynamoDbClientV2.deleteTable(b -> b.tableName(TABLE_NAME));
        dynamoDbClientV2.waiter().waitUntilTableNotExists(b -> b.tableName(TABLE_NAME));
    }
}
```

The JSON response for the `describeTable` method from the V1 and V2 client contains no `GlobalSecondaryIndexes` attribute:

```
{
  "Table": {
    "AttributeDefinitions": [
      {
        "AttributeName": "Id",
        "AttributeType": "S"
      }
    ],
    "BillingModeSummary": {
      "BillingMode": "PAY_PER_REQUEST",
      "LastUpdateToPayPerRequestDateTime": ...
    },
    "CreationDateTime": ...,
    "DeletionProtectionEnabled": false,
    "ItemCount": 0,
    "KeySchema": [
      {
        "AttributeName": "Id",
        "KeyType": "HASH"
      }
    ],
    "ProvisionedThroughput": {
      "NumberOfDecreasesToday": 0,
      "ReadCapacityUnits": 0,
      "WriteCapacityUnits": 0
    },
    "TableArn": "arn:aws:dynamodb:us-east-1:11111111111:table/DeserializationTable-...",
    "TableId": "...",
    "TableName": "DeserializationTable-...",
    "TableSizeBytes": 0,
    "TableStatus": "ACTIVE",
    "TableThroughputModeSummary": {
      "LastUpdateToPayPerRequestDateTime": ...,
      "TableThroughputMode": "PAY_PER_REQUEST"
    },
    "WarmThroughput": {
      "ReadUnitsPerSecond": 12000,
      "Status": "ACTIVE",
      "WriteUnitsPerSecond": 4000
    }
  }
}
```
