---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_AlarmIdentifier.html
---

# AlarmIdentifier
<a name="API_AlarmIdentifier"></a>

A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

## Contents
<a name="API_AlarmIdentifier_Contents"></a>

 ** Name **   <a name="Route53-Type-AlarmIdentifier-Name"></a>
The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
Route 53 supports CloudWatch alarms with the following features:
+ Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User Guide*.
+ Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Region **   <a name="Route53-Type-AlarmIdentifier-Region"></a>
For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
For the current list of CloudWatch regions, see [Amazon CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html) in the *Amazon Web Services General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | ca-central-1 | eu-central-1 | eu-central-2 | eu-west-1 | eu-west-2 | eu-west-3 | ap-east-1 | me-south-1 | me-central-1 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | eu-north-1 | sa-east-1 | cn-northwest-1 | cn-north-1 | af-south-1 | eu-south-1 | eu-south-2 | us-gov-west-1 | us-gov-east-1 | us-iso-east-1 | us-iso-west-1 | us-isob-east-1 | ap-southeast-4 | il-central-1 | ca-west-1 | ap-southeast-5 | mx-central-1 | us-isof-south-1 | us-isof-east-1 | ap-southeast-7 | ap-east-2 | eu-isoe-west-1 | ap-southeast-6 | us-isob-west-1`
Required: Yes

## See Also
<a name="API_AlarmIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/AlarmIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/AlarmIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/AlarmIdentifier)
