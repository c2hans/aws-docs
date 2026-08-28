---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ExascaleDbStorageVault.html
---

# ExascaleDbStorageVault
<a name="API_ExascaleDbStorageVault"></a>

Information about an Exascale storage vault.

## Contents
<a name="API_ExascaleDbStorageVault_Contents"></a>

 ** exascaleDbStorageVaultId **   <a name="odb-Type-ExascaleDbStorageVault-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** additionalFlashCacheInPercent **   <a name="odb-Type-ExascaleDbStorageVault-additionalFlashCacheInPercent"></a>
The additional flash cache percentage for the Exascale storage vault.
Type: Integer
Required: No

 ** attachedShapeAttributes **   <a name="odb-Type-ExascaleDbStorageVault-attachedShapeAttributes"></a>
The list of shape attributes attached to the Exascale storage vault.
Type: Array of strings
Valid Values: `SMART_STORAGE | BLOCK_STORAGE`
Required: No

 ** autoscaleLimitInGBs **   <a name="odb-Type-ExascaleDbStorageVault-autoscaleLimitInGBs"></a>
The autoscale limit in gigabytes (GB) for the Exascale storage vault.
Type: Integer
Required: No

 ** availabilityZone **   <a name="odb-Type-ExascaleDbStorageVault-availabilityZone"></a>
The Availability Zone for the Exascale storage vault.
Type: String
Required: No

 ** availabilityZoneId **   <a name="odb-Type-ExascaleDbStorageVault-availabilityZoneId"></a>
The Availability Zone ID for the Exascale storage vault.
Type: String
Required: No

 ** createdAt **   <a name="odb-Type-ExascaleDbStorageVault-createdAt"></a>
The date and time when the Exascale storage vault was created.
Type: Timestamp
Required: No

 ** description **   <a name="odb-Type-ExascaleDbStorageVault-description"></a>
The description of the Exascale storage vault.
Type: String
Required: No

 ** displayName **   <a name="odb-Type-ExascaleDbStorageVault-displayName"></a>
The user-friendly name for the Exascale storage vault.
Type: String
Required: No

 ** exascaleDbStorageVaultArn **   <a name="odb-Type-ExascaleDbStorageVault-exascaleDbStorageVaultArn"></a>
The Amazon Resource Name (ARN) of the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** highCapacityDatabaseStorage **   <a name="odb-Type-ExascaleDbStorageVault-highCapacityDatabaseStorage"></a>
The high-capacity database storage details for the Exascale storage vault.
Type: [ExascaleDbStorageDetails](API_ExascaleDbStorageDetails.md) object
Required: No

 ** isAutoscaleEnabled **   <a name="odb-Type-ExascaleDbStorageVault-isAutoscaleEnabled"></a>
Specifies whether autoscaling is enabled for the Exascale storage vault.
Type: Boolean
Required: No

 ** ocid **   <a name="odb-Type-ExascaleDbStorageVault-ocid"></a>
The OCID of the Exascale storage vault.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-ExascaleDbStorageVault-ociResourceAnchorName"></a>
The name of the OCI resource anchor for the Exascale storage vault.
Type: String
Required: No

 ** ociUrl **   <a name="odb-Type-ExascaleDbStorageVault-ociUrl"></a>
The HTTPS link to the Exascale storage vault in Oracle Cloud Infrastructure (OCI).
Type: String
Required: No

 ** percentProgress **   <a name="odb-Type-ExascaleDbStorageVault-percentProgress"></a>
The amount of progress made on the current operation on the Exascale storage vault, expressed as a percentage.
Type: Float
Required: No

 ** status **   <a name="odb-Type-ExascaleDbStorageVault-status"></a>
The current status of the Exascale storage vault.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-ExascaleDbStorageVault-statusReason"></a>
Additional information about the status of the Exascale storage vault.
Type: String
Required: No

 ** timeZone **   <a name="odb-Type-ExascaleDbStorageVault-timeZone"></a>
The time zone of the Exascale storage vault.
Type: String
Required: No

 ** vmClusterArns **   <a name="odb-Type-ExascaleDbStorageVault-vmClusterArns"></a>
The list of Amazon Resource Names (ARNs) of the VM clusters associated with this Exascale storage vault.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** vmClusterCount **   <a name="odb-Type-ExascaleDbStorageVault-vmClusterCount"></a>
The number of VM clusters associated with this Exascale storage vault.
Type: Integer
Required: No

 ** vmClusterIds **   <a name="odb-Type-ExascaleDbStorageVault-vmClusterIds"></a>
The list of unique identifiers of the VM clusters associated with this Exascale storage vault.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

## See Also
<a name="API_ExascaleDbStorageVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ExascaleDbStorageVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ExascaleDbStorageVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ExascaleDbStorageVault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
