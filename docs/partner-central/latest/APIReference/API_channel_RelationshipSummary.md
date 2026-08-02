---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_RelationshipSummary.html
---

# RelationshipSummary
<a name="API_channel_RelationshipSummary"></a>

Summary information about a partner relationship.

## Contents
<a name="API_channel_RelationshipSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-arn"></a>
The Amazon Resource Name (ARN) of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** associatedAccountId **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-associatedAccountId"></a>
The AWS account ID associated in this relationship.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** associationType **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-associationType"></a>
The type of association for the relationship.
Type: String
Valid Values: `DOWNSTREAM_SELLER | END_CUSTOMER | INTERNAL`
Required: No

 ** catalog **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-catalog"></a>
The catalog identifier associated with the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: No

 ** createdAt **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-createdAt"></a>
The timestamp when the relationship was created.
Type: Timestamp
Required: No

 ** displayName **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-displayName"></a>
The display name of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-id"></a>
The unique identifier of the relationship.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `rs-[a-z0-9]{13}`
Required: No

 ** programManagementAccountId **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-programManagementAccountId"></a>
The identifier of the program management account.
Type: String
Length Constraints: Fixed length of 17.
Pattern: `pma-[a-z0-9]{13}`
Required: No

 ** revision **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-revision"></a>
The current revision number of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

 ** sector **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-sector"></a>
The business sector for the relationship.
Type: String
Valid Values: `COMMERCIAL | GOVERNMENT | GOVERNMENT_EXCEPTION`
Required: No

 ** startDate **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-startDate"></a>
The start date of the relationship.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="AWSPartnerCentral-Type-channel_RelationshipSummary-updatedAt"></a>
The timestamp when the relationship was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_RelationshipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/RelationshipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/RelationshipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/RelationshipSummary)
