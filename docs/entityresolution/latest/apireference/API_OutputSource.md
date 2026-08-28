---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_OutputSource.html
---

# OutputSource
<a name="API_OutputSource"></a>

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed`. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

## Contents
<a name="API_OutputSource_Contents"></a>

 ** output **   <a name="API-Type-OutputSource-output"></a>
A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed`. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.
Type: Array of [OutputAttribute](API_OutputAttribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 750 items.
Required: Yes

 ** applyNormalization **   <a name="API-Type-OutputSource-applyNormalization"></a>
Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER`, and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.
Type: Boolean
Required: No

 ** customerProfilesIntegrationConfig **   <a name="API-Type-OutputSource-customerProfilesIntegrationConfig"></a>
Specifies the Customer Profiles integration configuration for sending matched output directly to Customer Profiles. When configured, AWS Entity Resolution automatically creates and updates customer profiles based on match clusters, eliminating the need for manual Amazon S3 integration setup.
Type: [CustomerProfilesIntegrationConfig](API_CustomerProfilesIntegrationConfig.md) object
Required: No

 ** KMSArn **   <a name="API-Type-OutputSource-KMSArn"></a>
Customer KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.
Type: String
Pattern: `arn:aws:kms:.*:[0-9]+:.*`
Required: No

 ** outputS3Path **   <a name="API-Type-OutputSource-outputS3Path"></a>
The S3 path to which AWS Entity Resolution will write the output table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: No

## See Also
<a name="API_OutputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/OutputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/OutputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/OutputSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
