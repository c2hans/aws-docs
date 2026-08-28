---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_InferenceConfig.html
---

# InferenceConfig
<a name="API_connect-customer-profiles_InferenceConfig"></a>

Configuration settings for inference behavior of the recommender.

## Contents
<a name="API_connect-customer-profiles_InferenceConfig_Contents"></a>

 ** MinProvisionedTPS **   <a name="connect-Type-connect-customer-profiles_InferenceConfig-MinProvisionedTPS"></a>
The minimum provisioned transactions per second (TPS) that the recommender supports. The default value is 1. A high MinProvisionedTPS will increase your cost.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

## See Also
<a name="API_connect-customer-profiles_InferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/InferenceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/InferenceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/InferenceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
