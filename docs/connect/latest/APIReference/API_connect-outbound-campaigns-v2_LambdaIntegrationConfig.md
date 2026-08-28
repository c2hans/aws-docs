---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_LambdaIntegrationConfig.html
---

# LambdaIntegrationConfig
<a name="API_connect-outbound-campaigns-v2_LambdaIntegrationConfig"></a>

The integration configuration to integrate Lambda with an Connect Customer instance.

## Contents
<a name="API_connect-outbound-campaigns-v2_LambdaIntegrationConfig_Contents"></a>

 ** functionArn **   <a name="connect-Type-connect-outbound-campaigns-v2_LambdaIntegrationConfig-functionArn"></a>
The Amazon Resource Name (ARN) of the Lambda function to invoke during campaign execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:function:([a-zA-Z0-9-_]+)(:([a-zA-Z0-9-_]+))?`
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns-v2_LambdaIntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/LambdaIntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/LambdaIntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/LambdaIntegrationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
