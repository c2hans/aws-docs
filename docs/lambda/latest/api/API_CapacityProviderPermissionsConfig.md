---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CapacityProviderPermissionsConfig.html
---

# CapacityProviderPermissionsConfig
<a name="API_CapacityProviderPermissionsConfig"></a>

Configuration that specifies the permissions required for the capacity provider to manage compute resources.

## Contents
<a name="API_CapacityProviderPermissionsConfig_Contents"></a>

 ** CapacityProviderOperatorRoleArn **   <a name="lambda-Type-CapacityProviderPermissionsConfig-CapacityProviderOperatorRoleArn"></a>
The ARN of the IAM role that the capacity provider uses to manage compute instances and other AWS resources.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_CapacityProviderPermissionsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CapacityProviderPermissionsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CapacityProviderPermissionsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CapacityProviderPermissionsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
