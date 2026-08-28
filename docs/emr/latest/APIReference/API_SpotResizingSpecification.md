---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_SpotResizingSpecification.html
---

# SpotResizingSpecification
<a name="API_SpotResizingSpecification"></a>

The resize specification for Spot Instances in the instance fleet, which contains the resize timeout period.

## Contents
<a name="API_SpotResizingSpecification_Contents"></a>

 ** AllocationStrategy **   <a name="EMR-Type-SpotResizingSpecification-AllocationStrategy"></a>
Specifies the allocation strategy to use to launch Spot instances during a resize. If you run Amazon EMR releases 6.9.0 or higher, the default is `price-capacity-optimized`. If you run Amazon EMR releases 6.8.0 or lower, the default is `capacity-optimized`.
Type: String
Valid Values: `capacity-optimized | price-capacity-optimized | lowest-price | diversified | capacity-optimized-prioritized`
Required: No

 ** TimeoutDurationMinutes **   <a name="EMR-Type-SpotResizingSpecification-TimeoutDurationMinutes"></a>
Spot resize timeout in minutes. If Spot Instances are not provisioned within this time, the resize workflow will stop provisioning of Spot instances. Minimum value is 5 minutes and maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_SpotResizingSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SpotResizingSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SpotResizingSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SpotResizingSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
