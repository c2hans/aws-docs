---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceFleetResizingSpecifications.html
---

# InstanceFleetResizingSpecifications
<a name="API_InstanceFleetResizingSpecifications"></a>

The resize specification for On-Demand and Spot Instances in the fleet.

## Contents
<a name="API_InstanceFleetResizingSpecifications_Contents"></a>

 ** OnDemandResizeSpecification **   <a name="EMR-Type-InstanceFleetResizingSpecifications-OnDemandResizeSpecification"></a>
The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period.
Type: [OnDemandResizingSpecification](API_OnDemandResizingSpecification.md) object
Required: No

 ** SpotResizeSpecification **   <a name="EMR-Type-InstanceFleetResizingSpecifications-SpotResizeSpecification"></a>
The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period.
Type: [SpotResizingSpecification](API_SpotResizingSpecification.md) object
Required: No

## See Also
<a name="API_InstanceFleetResizingSpecifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetResizingSpecifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
