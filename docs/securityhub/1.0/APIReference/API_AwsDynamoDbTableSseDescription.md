---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableSseDescription.html
---

# AwsDynamoDbTableSseDescription
<a name="API_AwsDynamoDbTableSseDescription"></a>

Information about the server-side encryption for the table.

## Contents
<a name="API_AwsDynamoDbTableSseDescription_Contents"></a>

 ** InaccessibleEncryptionDateTime **   <a name="securityhub-Type-AwsDynamoDbTableSseDescription-InaccessibleEncryptionDateTime"></a>
If the key is inaccessible, the date and time when DynamoDB detected that the key was inaccessible.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsMasterKeyArn **   <a name="securityhub-Type-AwsDynamoDbTableSseDescription-KmsMasterKeyArn"></a>
The ARN of the AWS KMS key that is used for the AWS KMS encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SseType **   <a name="securityhub-Type-AwsDynamoDbTableSseDescription-SseType"></a>
The type of server-side encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsDynamoDbTableSseDescription-Status"></a>
The status of the server-side encryption.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableSseDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableSseDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableSseDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableSseDescription)
