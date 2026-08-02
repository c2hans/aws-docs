---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SystemStatus.html
---

# SystemStatus
<a name="API_SystemStatus"></a>

CPU utilization and load average metrics for an Amazon EC2 instance.

## Contents
<a name="API_SystemStatus_Contents"></a>

 ** CPUUtilization **
CPU utilization metrics for the instance.
Type: [CPUUtilization](API_CPUUtilization.md) object
Required: No

 ** LoadAverage.member.N **
Load average in the last 1-minute, 5-minute, and 15-minute periods. For more information, see [Operating System Metrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os).
Type: Array of doubles
Required: No

## See Also
<a name="API_SystemStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/SystemStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/SystemStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/SystemStatus)
