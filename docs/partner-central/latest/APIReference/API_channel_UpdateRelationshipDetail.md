---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_UpdateRelationshipDetail.html
---

# UpdateRelationshipDetail
<a name="API_channel_UpdateRelationshipDetail"></a>

Contains details about an updated relationship.

## Contents
<a name="API_channel_UpdateRelationshipDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_UpdateRelationshipDetail-arn"></a>
The Amazon Resource Name (ARN) of the updated relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** displayName **   <a name="AWSPartnerCentral-Type-channel_UpdateRelationshipDetail-displayName"></a>
The updated display name of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_UpdateRelationshipDetail-id"></a>
The unique identifier of the updated relationship.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `rs-[a-z0-9]{13}`
Required: No

 ** revision **   <a name="AWSPartnerCentral-Type-channel_UpdateRelationshipDetail-revision"></a>
The new revision number of the relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

## See Also
<a name="API_channel_UpdateRelationshipDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/UpdateRelationshipDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/UpdateRelationshipDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/UpdateRelationshipDetail)
