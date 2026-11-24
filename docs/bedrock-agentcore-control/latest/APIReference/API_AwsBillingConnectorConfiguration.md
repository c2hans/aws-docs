---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_AwsBillingConnectorConfiguration.html
---

# AwsBillingConnectorConfiguration

The configuration for an AWS Billing payment connector. Payments made through an AWS Billing payment connector are charged to the AWS account that owns the payment manager, and appear on that account's AWS bill as AWS Marketplace charges.

## Contents
<a name="API_AwsBillingConnectorConfiguration_Contents"></a>

 ** iamRoleArn **   <a name="bedrockagentcorecontrol-Type-AwsBillingConnectorConfiguration-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Marketplace service-linked role in the account that owns the payment manager. The service sets this value when it creates the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`
Required: Yes

## See Also
<a name="API_AwsBillingConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AwsBillingConnectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AwsBillingConnectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AwsBillingConnectorConfiguration)
