---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_AutoScalingConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# AutoScalingConfiguration
<a name="API_AutoScalingConfiguration"></a>

The configuration based on which FinSpace will scale in or scale out nodes in your cluster.

## Contents
<a name="API_AutoScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** autoScalingMetric **   <a name="finspace-Type-AutoScalingConfiguration-autoScalingMetric"></a>
 The metric your cluster will track in order to scale in and out. For example, `CPU_UTILIZATION_PERCENTAGE` is the average CPU usage across all the nodes in a cluster.
Type: String
Valid Values: `CPU_UTILIZATION_PERCENTAGE`
Required: No

 ** maxNodeCount **   <a name="finspace-Type-AutoScalingConfiguration-maxNodeCount"></a>
The highest number of nodes to scale. This value cannot be greater than 5.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** metricTarget **   <a name="finspace-Type-AutoScalingConfiguration-metricTarget"></a>
The desired value of the chosen `autoScalingMetric`. When the metric drops below this value, the cluster will scale in. When the metric goes above this value, the cluster will scale out. You can set the target value between 1 and 100 percent.
Type: Double
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** minNodeCount **   <a name="finspace-Type-AutoScalingConfiguration-minNodeCount"></a>
The lowest number of nodes to scale. This value must be at least 1 and less than the `maxNodeCount`. If the nodes in a cluster belong to multiple availability zones, then `minNodeCount` must be at least 3.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** scaleInCooldownSeconds **   <a name="finspace-Type-AutoScalingConfiguration-scaleInCooldownSeconds"></a>
The duration in seconds that FinSpace will wait after a scale in event before initiating another scaling event.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** scaleOutCooldownSeconds **   <a name="finspace-Type-AutoScalingConfiguration-scaleOutCooldownSeconds"></a>
The duration in seconds that FinSpace will wait after a scale out event before initiating another scaling event.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

## See Also
<a name="API_AutoScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/AutoScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/AutoScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/AutoScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
