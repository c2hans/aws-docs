---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxAttachedCluster.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxAttachedCluster
<a name="API_KxAttachedCluster"></a>

The structure containing the metadata of the attached clusters.

## Contents
<a name="API_KxAttachedCluster_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clusterName **   <a name="finspace-Type-KxAttachedCluster-clusterName"></a>
A unique name for the attached cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** clusterStatus **   <a name="finspace-Type-KxAttachedCluster-clusterStatus"></a>
The status of the attached cluster.
+ PENDING – The cluster is pending creation.
+ CREATING – The cluster creation process is in progress.
+ CREATE\_FAILED – The cluster creation process has failed.
+ RUNNING – The cluster creation process is running.
+ UPDATING – The cluster is in the process of being updated.
+ DELETING – The cluster is in the process of being deleted.
+ DELETED – The cluster has been deleted.
+ DELETE\_FAILED – The cluster failed to delete.
Type: String
Valid Values: `PENDING | CREATING | CREATE_FAILED | RUNNING | UPDATING | DELETING | DELETED | DELETE_FAILED`
Required: No

 ** clusterType **   <a name="finspace-Type-KxAttachedCluster-clusterType"></a>
Specifies the type of cluster. The volume for TP and RDB cluster types will be used for TP logs.
Type: String
Valid Values: `HDB | RDB | GATEWAY | GP | TICKERPLANT`
Required: No

## See Also
<a name="API_KxAttachedCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxAttachedCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxAttachedCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxAttachedCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
