---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ResourceSnapshotSummary.html
---

# ResourceSnapshotSummary
<a name="API_ResourceSnapshotSummary"></a>

 Provides a concise summary of a resource snapshot, including its unique identifier and version information. This structure is used to quickly reference and identify specific versions of resource snapshots.

## Contents
<a name="API_ResourceSnapshotSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-Arn"></a>
 The Amazon Resource Name (ARN) of the snapshot. This globally unique identifier can be used for cross-service references and in IAM policies.
Type: String
Pattern: `arn:.*`
Required: No

 ** CreatedBy **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-CreatedBy"></a>
The AWS account ID of the entity that owns the resource from which the snapshot was created.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** ResourceId **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-ResourceId"></a>
The identifier of the specific resource snapshotted. The format might vary depending on the ResourceType.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** ResourceSnapshotTemplateName **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-ResourceSnapshotTemplateName"></a>
The name of the template used to create the snapshot.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`
Required: No

 ** ResourceType **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-ResourceType"></a>
The type of resource snapshotted.
Type: String
Valid Values: `Opportunity`
Required: No

 ** Revision **   <a name="AWSPartnerCentral-Type-ResourceSnapshotSummary-Revision"></a>
The revision number of the snapshot. This integer value is incremented each time the snapshot is updated, allowing for version tracking of the resource snapshot.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ResourceSnapshotSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ResourceSnapshotSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ResourceSnapshotSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ResourceSnapshotSummary)
