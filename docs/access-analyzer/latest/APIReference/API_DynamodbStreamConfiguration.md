---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DynamodbStreamConfiguration.html
---

# DynamodbStreamConfiguration
<a name="API_DynamodbStreamConfiguration"></a>

The proposed access control configuration for a DynamoDB stream. You can propose a configuration for a new DynamoDB stream or an existing DynamoDB stream that you own by specifying the policy for the DynamoDB stream. For more information, see [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html).
+ If the configuration is for an existing DynamoDB stream and you do not specify the DynamoDB policy, then the access preview uses the existing DynamoDB policy for the stream.
+ If the access preview is for a new resource and you do not specify the policy, then the access preview assumes a DynamoDB stream without a policy.
+ To propose deletion of an existing DynamoDB stream policy, you can specify an empty string for the DynamoDB policy.

## Contents
<a name="API_DynamodbStreamConfiguration_Contents"></a>

 ** streamPolicy **   <a name="accessanalyzer-Type-DynamodbStreamConfiguration-streamPolicy"></a>
The proposed resource policy defining who can access or manage the DynamoDB stream.
Type: String
Required: No

## See Also
<a name="API_DynamodbStreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
