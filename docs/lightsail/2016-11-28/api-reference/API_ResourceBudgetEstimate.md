---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ResourceBudgetEstimate.html
---

# ResourceBudgetEstimate
<a name="API_ResourceBudgetEstimate"></a>

Describes the estimated cost or usage that a budget tracks.

## Contents
<a name="API_ResourceBudgetEstimate_Contents"></a>

 ** costEstimates **   <a name="Lightsail-Type-ResourceBudgetEstimate-costEstimates"></a>
The cost estimate for the specified budget.
Type: Array of [CostEstimate](API_CostEstimate.md) objects
Required: No

 ** endTime **   <a name="Lightsail-Type-ResourceBudgetEstimate-endTime"></a>
The estimate end time.
Type: Timestamp
Required: No

 ** resourceName **   <a name="Lightsail-Type-ResourceBudgetEstimate-resourceName"></a>
The resource name.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-ResourceBudgetEstimate-resourceType"></a>
The type of resource the budget will track.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** startTime **   <a name="Lightsail-Type-ResourceBudgetEstimate-startTime"></a>
The estimate start time.
Type: Timestamp
Required: No

## See Also
<a name="API_ResourceBudgetEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ResourceBudgetEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ResourceBudgetEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ResourceBudgetEstimate)
