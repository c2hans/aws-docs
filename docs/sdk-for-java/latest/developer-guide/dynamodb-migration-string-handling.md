---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migration-string-handling.html
---

# String handling differences between version 1 and version 2 of the SDK for Java
<a name="dynamodb-migration-string-handling"></a>

V1 and V2 handle empty strings differently when sending data to DynamoDB:
+ **V1**: Converts empty strings to null values before sending to DynamoDB (resulting in no attribute)
+ **V2**: Sends empty strings as actual empty string values to DynamoDB

**Important**
After migrating to V2, if you don't want empty strings stored in DynamoDB, you must implement custom converters. Without custom converters, V2 stores empty strings as actual empty string attributes in your DynamoDB items, which differs from V1's behavior of omitting these attributes entirely.

**Example custom converter for V2 that converts an empty string attribute to null**

```
/**
 * Custom converter that maintains V1 behavior by converting empty strings to null values
 * when writing to DynamoDB, ensuring compatibility with existing data. No attribute will be saved to DynamoDB.
 */
public class NullifyEmptyStringConverter implements AttributeConverter<String> {
    @Override
    public AttributeValue transformFrom(String value) {
        if (value == null || value.isEmpty()) {
            return AttributeValue.builder().nul(true).build();
        }
        return AttributeValue.builder().s(value).build();
    }

    @Override
    public String transformTo(AttributeValue attributeValue) {
        if (attributeValue.nul()) {
            return null;
        }
        return attributeValue.s();
    }

    @Override
    public EnhancedType<String> type() {
        return EnhancedType.of(String.class);
    }

    @Override
    public AttributeValueType attributeValueType() {
        return AttributeValueType.S;
    }
}

// V2 usage:
@DynamoDbBean
public class Customer {
    private String name;

    @DynamoDbConvertedBy(NullifyEmptyStringConverter.class)
    public String getName() {
        return name;
    }
}
```
