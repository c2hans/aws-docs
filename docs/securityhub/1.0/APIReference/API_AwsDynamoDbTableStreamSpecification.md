---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableStreamSpecification.html
---

# AwsDynamoDbTableStreamSpecification
<a name="API_AwsDynamoDbTableStreamSpecification"></a>

The current DynamoDB Streams configuration for the table.

## Contents
<a name="API_AwsDynamoDbTableStreamSpecification_Contents"></a>

 ** StreamEnabled **   <a name="securityhub-Type-AwsDynamoDbTableStreamSpecification-StreamEnabled"></a>
Indicates whether DynamoDB Streams is enabled on the table.
Type: Boolean
Required: No

 ** StreamViewType **   <a name="securityhub-Type-AwsDynamoDbTableStreamSpecification-StreamViewType"></a>
Determines the information that is written to the table.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableStreamSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableStreamSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableStreamSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableStreamSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
