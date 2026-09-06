---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementContextDetails.html
---

# EngagementContextDetails
<a name="API_EngagementContextDetails"></a>

Provides detailed context information for an Engagement. This structure allows for specifying the type of context and its associated payload.

## Contents
<a name="API_EngagementContextDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="AWSPartnerCentral-Type-EngagementContextDetails-Type"></a>
Specifies the type of Engagement context. Valid values are "CustomerProject" or "Document", indicating whether the context relates to a customer project or a document respectively.
Type: String
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-EngagementContextDetails-Id"></a>
The unique identifier of the engagement context. This ID is used to reference and manage the specific context within the engagement.
Type: String
Pattern: `(?s).{1,3}`
Required: No

 ** Payload **   <a name="AWSPartnerCentral-Type-EngagementContextDetails-Payload"></a>
Contains the specific details of the Engagement context. The structure of this payload varies depending on the Type field.
Type: [EngagementContextPayload](API_EngagementContextPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_EngagementContextDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementContextDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementContextDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementContextDetails)
