---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupSummary.html
---

# ComputeNodeGroupSummary
<a name="API_ComputeNodeGroupSummary"></a>

The object returned by the `ListComputeNodeGroups` API action.

## Contents
<a name="API_ComputeNodeGroupSummary_Contents"></a>

 ** arn **   <a name="PCS-Type-ComputeNodeGroupSummary-arn"></a>
The unique Amazon Resource Name (ARN) of the compute node group.
Type: String
Required: Yes

 ** clusterId **   <a name="PCS-Type-ComputeNodeGroupSummary-clusterId"></a>
The ID of the cluster of the compute node group.
Type: String
Required: Yes

 ** createdAt **   <a name="PCS-Type-ComputeNodeGroupSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="PCS-Type-ComputeNodeGroupSummary-id"></a>
The generated unique ID of the compute node group.
Type: String
Required: Yes

 ** modifiedAt **   <a name="PCS-Type-ComputeNodeGroupSummary-modifiedAt"></a>
The date and time the resource was modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="PCS-Type-ComputeNodeGroupSummary-name"></a>
The name that identifies the compute node group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 25.
Pattern: `(?!pcs_)^[A-Za-z][A-Za-z0-9-]+`
Required: Yes

 ** status **   <a name="PCS-Type-ComputeNodeGroupSummary-status"></a>
The provisioning status of the compute node group.
The provisioning status doesn't indicate the overall health of the compute node group.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the * AWS PCS User Guide*.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED | DELETED | SUSPENDING | SUSPENDED | RESUMING`
Required: Yes

## See Also
<a name="API_ComputeNodeGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ComputeNodeGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ComputeNodeGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ComputeNodeGroupSummary)
