---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails.html
---

# AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails
<a name="API_AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails"></a>

 Provides details about the market (purchasing) options for Spot Instances.

## Contents
<a name="API_AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails_Contents"></a>

 ** BlockDurationMinutes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails-BlockDurationMinutes"></a>
 Deprecated.
Type: Integer
Required: No

 ** InstanceInterruptionBehavior **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails-InstanceInterruptionBehavior"></a>
 The behavior when a Spot Instance is interrupted.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MaxPrice **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails-MaxPrice"></a>
 The maximum hourly price you're willing to pay for the Spot Instances.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SpotInstanceType **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails-SpotInstanceType"></a>
 The Spot Instance request type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ValidUntil **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails-ValidUntil"></a>
 The end date of the request, in UTC format (YYYY-MM-DDTHH:MM:SSZ), for persistent requests.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails)
