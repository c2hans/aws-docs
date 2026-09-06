---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CPUUtilization.html
---

# CPUUtilization
<a name="API_CPUUtilization"></a>

CPU utilization metrics for an instance.

## Contents
<a name="API_CPUUtilization_Contents"></a>

 ** Idle **
Percentage of time that the CPU has spent in the `Idle` state over the last 10 seconds.
Type: Double
Required: No

 ** IOWait **
Available on Linux environments only.
Percentage of time that the CPU has spent in the `I/O Wait` state over the last 10 seconds.
Type: Double
Required: No

 ** IRQ **
Available on Linux environments only.
Percentage of time that the CPU has spent in the `IRQ` state over the last 10 seconds.
Type: Double
Required: No

 ** Nice **
Available on Linux environments only.
Percentage of time that the CPU has spent in the `Nice` state over the last 10 seconds.
Type: Double
Required: No

 ** Privileged **
Available on Windows environments only.
Percentage of time that the CPU has spent in the `Privileged` state over the last 10 seconds.
Type: Double
Required: No

 ** SoftIRQ **
Available on Linux environments only.
Percentage of time that the CPU has spent in the `SoftIRQ` state over the last 10 seconds.
Type: Double
Required: No

 ** System **
Available on Linux environments only.
Percentage of time that the CPU has spent in the `System` state over the last 10 seconds.
Type: Double
Required: No

 ** User **
Percentage of time that the CPU has spent in the `User` state over the last 10 seconds.
Type: Double
Required: No

## See Also
<a name="API_CPUUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CPUUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CPUUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CPUUtilization)
