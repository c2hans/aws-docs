---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksAccessEntry.html
---

# EksAccessEntry
<a name="API_EksAccessEntry"></a>

Configures whether AWS Batch manages an Amazon EKS access entry on the cluster for the compute environment. For information on how the fields interact with the cluster's `authenticationMode` and with other compute environments that share the cluster, see [Amazon EKS access entry authentication](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html) in the * AWS Batch User Guide*.

**Note**
Setting `desiredState=ENABLED` on a single compute environment does not guarantee that AWS Batch creates an access entry, and setting `desiredState=DISABLED` on a single compute environment does not guarantee that AWS Batch deletes one. AWS Batch compares the `desiredState` across all compute environments that target the same cluster. The AWS Batch-managed access entry is created only when all compute environments have `desiredState=ENABLED`, and deleted only when all have `desiredState=DISABLED`. If you have multiple compute environments on the same cluster, set `desiredState` consistently across all of them to avoid uncertainty. For more information, see [Reconciling desiredState across compute environments](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html#eks-access-entries-reconciliation) in the * AWS Batch User Guide*.

## Contents
<a name="API_EksAccessEntry_Contents"></a>

 ** desiredState **   <a name="Batch-Type-EksAccessEntry-desiredState"></a>
The desired access entry state for the compute environment. Valid values:
ENABLED
 AWS Batch manages an access entry on the cluster for the compute environment.
DISABLED
 AWS Batch deletes the AWS Batch-managed access entry for the cluster. This value is rejected if the cluster's `authenticationMode` is `API`, because such a cluster doesn't support the `aws-auth` ConfigMap.
INHERIT\_FROM\_CLUSTER
 AWS Batch defers to the cluster's current access entry `status`. On a cluster whose authentication mode is `API`, AWS Batch creates and manages an access entry. On a cluster whose authentication mode is `API_AND_CONFIG_MAP` or `CONFIG_MAP`, AWS Batch neither adds nor removes an access entry.
Type: String
Valid Values: `ENABLED | DISABLED | INHERIT_FROM_CLUSTER`
Required: Yes

 ** status **   <a name="Batch-Type-EksAccessEntry-status"></a>
The observed state of the access entry on the cluster. `ACTIVE` means that an access entry for the compute environment exists on the cluster and takes precedence over the `aws-auth` ConfigMap. `INACTIVE` means that no AWS Batch-managed access entry is present. This is a read-only field returned by `DescribeComputeEnvironments`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_EksAccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksAccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksAccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksAccessEntry)
