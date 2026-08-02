---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CapacityProviderLoggingConfig.html
---

# CapacityProviderLoggingConfig
<a name="API_CapacityProviderLoggingConfig"></a>

The capacity provider's Amazon CloudWatch Logs configuration settings.

## Contents
<a name="API_CapacityProviderLoggingConfig_Contents"></a>

 ** LogGroup **   <a name="lambda-Type-CapacityProviderLoggingConfig-LogGroup"></a>
The name of the Amazon CloudWatch log group the capacity provider sends logs to. By default, Lambda capacity providers send logs to a default log group named `/aws/lambda/capacity-provider/<capacity provider name>`. To use a different log group, enter an existing log group or enter a new log group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** SystemLogLevel **   <a name="lambda-Type-CapacityProviderLoggingConfig-SystemLogLevel"></a>
Set this property to filter the system logs for your capacity provider that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.
Type: String
Valid Values: `DEBUG | INFO | WARN`
Required: No

## See Also
<a name="API_CapacityProviderLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CapacityProviderLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CapacityProviderLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CapacityProviderLoggingConfig)
