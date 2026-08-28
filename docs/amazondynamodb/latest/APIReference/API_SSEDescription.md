---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SSEDescription.html
---

# SSEDescription
<a name="API_SSEDescription"></a>

The description of the server-side encryption status on the specified table.

## Contents
<a name="API_SSEDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InaccessibleEncryptionDateTime **   <a name="DDB-Type-SSEDescription-InaccessibleEncryptionDateTime"></a>
Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table's AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table's AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table's AWS KMS key remains inaccessible for more than seven days from this date.
Type: Timestamp
Required: No

 ** KMSMasterKeyArn **   <a name="DDB-Type-SSEDescription-KMSMasterKeyArn"></a>
The AWS KMS key ARN used for the AWS KMS encryption.
Type: String
Required: No

 ** SSEType **   <a name="DDB-Type-SSEDescription-SSEType"></a>
Server-side encryption type. The only supported value is:
+  `KMS` - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).
Type: String
Valid Values: `AES256 | KMS`
Required: No

 ** Status **   <a name="DDB-Type-SSEDescription-Status"></a>
Represents the current state of server-side encryption. The only supported values are:
+  `ENABLED` - Server-side encryption is enabled.
+  `UPDATING` - Server-side encryption is being updated.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | UPDATING`
Required: No

## See Also
<a name="API_SSEDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SSEDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SSEDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SSEDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
