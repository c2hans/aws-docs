---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingLaunchConfigurationMetadataOptions.html
---

# AwsAutoScalingLaunchConfigurationMetadataOptions
<a name="API_AwsAutoScalingLaunchConfigurationMetadataOptions"></a>

The metadata options for the instances.

## Contents
<a name="API_AwsAutoScalingLaunchConfigurationMetadataOptions_Contents"></a>

 ** HttpEndpoint **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationMetadataOptions-HttpEndpoint"></a>
Enables or disables the HTTP metadata endpoint on your instances. By default, the metadata endpoint is enabled.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpPutResponseHopLimit **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationMetadataOptions-HttpPutResponseHopLimit"></a>
The HTTP `PUT` response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.
Type: Integer
Required: No

 ** HttpTokens **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationMetadataOptions-HttpTokens"></a>
Indicates whether token usage is `required` or `optional` for metadata requests. By default, token usage is `optional`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingLaunchConfigurationMetadataOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationMetadataOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationMetadataOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationMetadataOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
