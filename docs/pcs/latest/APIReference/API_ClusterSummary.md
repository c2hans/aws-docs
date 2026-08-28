---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSummary.html
---

# ClusterSummary
<a name="API_ClusterSummary"></a>

The object returned by the `ListClusters` API action.

## Contents
<a name="API_ClusterSummary_Contents"></a>

 ** arn **   <a name="PCS-Type-ClusterSummary-arn"></a>
The unique Amazon Resource Name (ARN) of the cluster.
Type: String
Required: Yes

 ** createdAt **   <a name="PCS-Type-ClusterSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="PCS-Type-ClusterSummary-id"></a>
The generated unique ID of the cluster.
Type: String
Required: Yes

 ** modifiedAt **   <a name="PCS-Type-ClusterSummary-modifiedAt"></a>
The date and time the resource was modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="PCS-Type-ClusterSummary-name"></a>
The name that identifies the cluster.
Type: String
Required: Yes

 ** status **   <a name="PCS-Type-ClusterSummary-status"></a>
The provisioning status of the cluster.
The provisioning status doesn't indicate the overall health of the cluster.
The resource enters the `SUSPENDING` and `SUSPENDED` states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is `SUSPENDED`. For more information, see [Frequently asked questions about Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html) in the * AWS PCS User Guide*.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED | SUSPENDING | SUSPENDED | RESUMING`
Required: Yes

## See Also
<a name="API_ClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ClusterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ClusterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ClusterSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
