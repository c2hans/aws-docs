---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ComputeLimits.html
---

# ComputeLimits
<a name="API_ComputeLimits"></a>

 The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster can not be above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

## Contents
<a name="API_ComputeLimits_Contents"></a>

 ** MaximumCapacityUnits **   <a name="EMR-Type-ComputeLimits-MaximumCapacityUnits"></a>
 The upper boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
Type: Integer
Required: Yes

 ** MinimumCapacityUnits **   <a name="EMR-Type-ComputeLimits-MinimumCapacityUnits"></a>
 The lower boundary of Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
Type: Integer
Required: Yes

 ** UnitType **   <a name="EMR-Type-ComputeLimits-UnitType"></a>
 The unit type used for specifying a managed scaling policy.
Type: String
Valid Values: `InstanceFleetUnits | Instances | VCPU`
Required: Yes

 ** MaximumCoreCapacityUnits **   <a name="EMR-Type-ComputeLimits-MaximumCoreCapacityUnits"></a>
 The upper boundary of Amazon EC2 units for core node type in a cluster. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.
Type: Integer
Required: No

 ** MaximumOnDemandCapacityUnits **   <a name="EMR-Type-ComputeLimits-MaximumOnDemandCapacityUnits"></a>
 The upper boundary of On-Demand Amazon EC2 units. It is measured through vCPU cores or instances for instance groups and measured through units for instance fleets. The On-Demand units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between On-Demand and Spot Instances.
Type: Integer
Required: No

## See Also
<a name="API_ComputeLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ComputeLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ComputeLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ComputeLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
