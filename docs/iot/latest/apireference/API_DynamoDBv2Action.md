---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DynamoDBv2Action.html
---

# DynamoDBv2Action
<a name="API_DynamoDBv2Action"></a>

Describes an action to write to a DynamoDB table.

This DynamoDB action writes each attribute in the message payload into it's own column in the DynamoDB table.

## Contents
<a name="API_DynamoDBv2Action_Contents"></a>

 ** putItem **   <a name="iot-Type-DynamoDBv2Action-putItem"></a>
Specifies the DynamoDB table to which the message data will be written. For example:
 `{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }`
Each attribute in the message payload will be written to a separate column in the DynamoDB database.
Type: [PutItemInput](API_PutItemInput.md) object
Required: Yes

 ** roleArn **   <a name="iot-Type-DynamoDBv2Action-roleArn"></a>
The ARN of the IAM role that grants access to the DynamoDB table.
Type: String
Required: Yes

## See Also
<a name="API_DynamoDBv2Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DynamoDBv2Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DynamoDBv2Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DynamoDBv2Action)
