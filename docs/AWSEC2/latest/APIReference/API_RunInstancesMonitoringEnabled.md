---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstancesMonitoringEnabled.html
---

# RunInstancesMonitoringEnabled

Describes the monitoring of an instance.

## Contents
<a name="API_RunInstancesMonitoringEnabled_Contents"></a>

 ** Enabled ** (request), ** enabled ** (response)
Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
Type: Boolean
Required: Yes

 ** MetricCategoryId.N **
The IDs of the metric categories to associate with the instance. To specify metric categories, you must also enable detailed monitoring.
Type: Array of strings
Required: No

## See Also
<a name="API_RunInstancesMonitoringEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RunInstancesMonitoringEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RunInstancesMonitoringEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RunInstancesMonitoringEnabled)
