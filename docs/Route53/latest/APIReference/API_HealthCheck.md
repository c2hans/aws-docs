---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheck.html
---

# HealthCheck
<a name="API_HealthCheck"></a>

A complex type that contains information about one health check that is associated with the current AWS account.

## Contents
<a name="API_HealthCheck_Contents"></a>

 ** CallerReference **   <a name="Route53-Type-HealthCheck-CallerReference"></a>
A unique string that you specified when you created the health check.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** HealthCheckConfig **   <a name="Route53-Type-HealthCheck-HealthCheckConfig"></a>
A complex type that contains detailed information about one health check.
Type: [HealthCheckConfig](API_HealthCheckConfig.md) object
Required: Yes

 ** HealthCheckVersion **   <a name="Route53-Type-HealthCheck-HealthCheckVersion"></a>
The version of the health check. You can optionally pass this value in a call to `UpdateHealthCheck` to prevent overwriting another change to the health check.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** Id **   <a name="Route53-Type-HealthCheck-Id"></a>
The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** CloudWatchAlarmConfiguration **   <a name="Route53-Type-HealthCheck-CloudWatchAlarmConfiguration"></a>
A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.
Type: [CloudWatchAlarmConfiguration](API_CloudWatchAlarmConfiguration.md) object
Required: No

 ** LinkedService **   <a name="Route53-Type-HealthCheck-LinkedService"></a>
If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53.
Type: [LinkedService](API_LinkedService.md) object
Required: No

## See Also
<a name="API_HealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HealthCheck)
