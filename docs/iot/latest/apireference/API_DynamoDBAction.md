---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DynamoDBAction.html
---

# DynamoDBAction
<a name="API_DynamoDBAction"></a>

Describes an action to write to a DynamoDB table.

The `tableName`, `hashKeyField`, and `rangeKeyField` values must match the values used when you created the table.

The `hashKeyValue` and `rangeKeyvalue` fields use a substitution template syntax. These templates provide data at runtime. The syntax is as follows: ${*sql-expression*}.

You can specify any valid expression in a WHERE or SELECT clause, including JSON properties, comparisons, calculations, and functions. For example, the following field uses the third level of the topic:

 `"hashKeyValue": "${topic(3)}"`

The following field uses the timestamp:

 `"rangeKeyValue": "${timestamp()}"`

## Contents
<a name="API_DynamoDBAction_Contents"></a>

 ** hashKeyField **   <a name="iot-Type-DynamoDBAction-hashKeyField"></a>
The hash key name.
Type: String
Required: Yes

 ** hashKeyValue **   <a name="iot-Type-DynamoDBAction-hashKeyValue"></a>
The hash key value.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-DynamoDBAction-roleArn"></a>
The ARN of the IAM role that grants access to the DynamoDB table.
Type: String
Required: Yes

 ** tableName **   <a name="iot-Type-DynamoDBAction-tableName"></a>
The name of the DynamoDB table.
Type: String
Required: Yes

 ** hashKeyType **   <a name="iot-Type-DynamoDBAction-hashKeyType"></a>
The hash key type. Valid values are "STRING" or "NUMBER"
Type: String
Valid Values: `STRING | NUMBER`
Required: No

 ** operation **   <a name="iot-Type-DynamoDBAction-operation"></a>
The type of operation to be performed. This follows the substitution template, so it can be `${operation}`, but the substitution must result in one of the following: `INSERT`, `UPDATE`, or `DELETE`.
Type: String
Required: No

 ** payloadField **   <a name="iot-Type-DynamoDBAction-payloadField"></a>
The action payload. This name can be customized.
Type: String
Required: No

 ** rangeKeyField **   <a name="iot-Type-DynamoDBAction-rangeKeyField"></a>
The range key name.
Type: String
Required: No

 ** rangeKeyType **   <a name="iot-Type-DynamoDBAction-rangeKeyType"></a>
The range key type. Valid values are "STRING" or "NUMBER"
Type: String
Valid Values: `STRING | NUMBER`
Required: No

 ** rangeKeyValue **   <a name="iot-Type-DynamoDBAction-rangeKeyValue"></a>
The range key value.
Type: String
Required: No

## See Also
<a name="API_DynamoDBAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DynamoDBAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DynamoDBAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DynamoDBAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
