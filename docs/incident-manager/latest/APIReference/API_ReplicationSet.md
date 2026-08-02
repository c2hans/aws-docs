---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ReplicationSet.html
---

# ReplicationSet
<a name="API_ReplicationSet"></a>

The set of AWS Region that your Incident Manager data will be replicated to and the AWS KMS key used to encrypt the data.

## Contents
<a name="API_ReplicationSet_Contents"></a>

 ** createdBy **   <a name="IncidentManager-Type-ReplicationSet-createdBy"></a>
Details about who created the replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** createdTime **   <a name="IncidentManager-Type-ReplicationSet-createdTime"></a>
When the replication set was created.
Type: Timestamp
Required: Yes

 ** deletionProtected **   <a name="IncidentManager-Type-ReplicationSet-deletionProtected"></a>
Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last AWS Region in the replication set.
Type: Boolean
Required: Yes

 ** lastModifiedBy **   <a name="IncidentManager-Type-ReplicationSet-lastModifiedBy"></a>
Who last modified the replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

 ** lastModifiedTime **   <a name="IncidentManager-Type-ReplicationSet-lastModifiedTime"></a>
When the replication set was last updated.
Type: Timestamp
Required: Yes

 ** regionMap **   <a name="IncidentManager-Type-ReplicationSet-regionMap"></a>
The map between each AWS Region in your replication set and the AWS KMS key that's used to encrypt the data in that Region.
Type: String to [RegionInfo](API_RegionInfo.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** status **   <a name="IncidentManager-Type-ReplicationSet-status"></a>
The status of the replication set. If the replication set is still pending, you can't use Incident Manager functionality.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | FAILED`
Required: Yes

 ** arn **   <a name="IncidentManager-Type-ReplicationSet-arn"></a>
The Amazon Resource Name (ARN) of the replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_ReplicationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ReplicationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ReplicationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ReplicationSet)
