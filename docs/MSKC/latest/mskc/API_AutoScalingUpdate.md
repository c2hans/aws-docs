---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_AutoScalingUpdate.html
---

# AutoScalingUpdate
<a name="API_AutoScalingUpdate"></a>

The updates to the auto scaling parameters for the connector.

## Contents
<a name="API_AutoScalingUpdate_Contents"></a>

 ** maxWorkerCount **   <a name="MSKC-Type-AutoScalingUpdate-maxWorkerCount"></a>
The target maximum number of workers allocated to the connector.
Type: Integer
Required: Yes

 ** mcuCount **   <a name="MSKC-Type-AutoScalingUpdate-mcuCount"></a>
The target number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8.
Required: Yes

 ** minWorkerCount **   <a name="MSKC-Type-AutoScalingUpdate-minWorkerCount"></a>
The target minimum number of workers allocated to the connector.
Type: Integer
Required: Yes

 ** scaleInPolicy **   <a name="MSKC-Type-AutoScalingUpdate-scaleInPolicy"></a>
The target scale-in policy for the connector.
Type: [ScaleInPolicyUpdate](API_ScaleInPolicyUpdate.md) object
Required: Yes

 ** scaleOutPolicy **   <a name="MSKC-Type-AutoScalingUpdate-scaleOutPolicy"></a>
The target scale-out policy for the connector.
Type: [ScaleOutPolicyUpdate](API_ScaleOutPolicyUpdate.md) object
Required: Yes

 ** maxAutoscalingTaskCount **   <a name="MSKC-Type-AutoScalingUpdate-maxAutoscalingTaskCount"></a>
The maximum number of tasks allocated to the connector during autoscaling operations. Must be at least equal to maxWorkerCount.
Type: Integer
Required: No

## See Also
<a name="API_AutoScalingUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/AutoScalingUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/AutoScalingUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/AutoScalingUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
