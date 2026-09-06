---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute.html
---

# AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute
<a name="API_AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute"></a>

 Contains the name and values of a manual Amazon Relational Database Service (RDS) DB cluster snapshot attribute.

## Contents
<a name="API_AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute_Contents"></a>

 ** AttributeName **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute-AttributeName"></a>
 The name of the manual DB cluster snapshot attribute. The attribute named `restore` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AttributeValues **   <a name="securityhub-Type-AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute-AttributeValues"></a>
 The value(s) for the manual DB cluster snapshot attribute. If the `AttributeName` field is set to `restore`, then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of `all` is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute)
