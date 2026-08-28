---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateSpotMarketOptions.html
---

# LaunchTemplateSpotMarketOptions
<a name="API_LaunchTemplateSpotMarketOptions"></a>

The options for Spot Instances.

## Contents
<a name="API_LaunchTemplateSpotMarketOptions_Contents"></a>

 ** blockDurationMinutes **
The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
Type: Integer
Required: No

 ** instanceInterruptionBehavior **
The behavior when a Spot Instance is interrupted.
Type: String
Valid Values: `hibernate | stop | terminate`
Required: No

 ** maxPrice **
The maximum hourly price you're willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. If you do specify this parameter, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message when the launch template is used to launch an instance.
Type: String
Required: No

 ** spotInstanceType **
The Spot Instance request type.
Type: String
Valid Values: `one-time | persistent`
Required: No

 ** validUntil **
The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.
Type: Timestamp
Required: No

## See Also
<a name="API_LaunchTemplateSpotMarketOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateSpotMarketOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateSpotMarketOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateSpotMarketOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
