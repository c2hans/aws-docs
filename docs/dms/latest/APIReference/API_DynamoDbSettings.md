---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DynamoDbSettings.html
---

# DynamoDbSettings
<a name="API_DynamoDbSettings"></a>

Provides the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role used to define an Amazon DynamoDB target endpoint.

## Contents
<a name="API_DynamoDbSettings_Contents"></a>

 ** ServiceAccessRoleArn **   <a name="DMS-Type-DynamoDbSettings-ServiceAccessRoleArn"></a>
 The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.
Type: String
Required: Yes

## See Also
<a name="API_DynamoDbSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DynamoDbSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DynamoDbSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DynamoDbSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
