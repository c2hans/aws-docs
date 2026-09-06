---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SingleInstanceHealth.html
---

# SingleInstanceHealth
<a name="API_SingleInstanceHealth"></a>

Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk environment.

## Contents
<a name="API_SingleInstanceHealth_Contents"></a>

 ** ApplicationMetrics **
Request metrics from your application.
Type: [ApplicationMetrics](API_ApplicationMetrics.md) object
Required: No

 ** AvailabilityZone **
The availability zone in which the instance runs.
Type: String
Required: No

 ** Causes.member.N **
Represents the causes, which provide more information about the current health status.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Color **
Represents the color indicator that gives you information about the health of the EC2 instance. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html).
Type: String
Required: No

 ** Deployment **
Information about the most recent deployment to an instance.
Type: [Deployment](API_Deployment.md) object
Required: No

 ** HealthStatus **
Returns the health status of the specified instance. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html).
Type: String
Required: No

 ** InstanceId **
The ID of the Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** InstanceType **
The instance's type.
Type: String
Required: No

 ** LaunchedAt **
The time at which the EC2 instance was launched.
Type: Timestamp
Required: No

 ** System **
Operating system metrics from the instance.
Type: [SystemStatus](API_SystemStatus.md) object
Required: No

## See Also
<a name="API_SingleInstanceHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/SingleInstanceHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/SingleInstanceHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/SingleInstanceHealth)
