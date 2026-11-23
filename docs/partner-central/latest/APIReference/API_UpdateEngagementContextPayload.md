---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateEngagementContextPayload.html
---

# UpdateEngagementContextPayload

Represents the updated payload of an engagement context. The structure of this payload varies based on the context type being updated.

## Contents
<a name="API_UpdateEngagementContextPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CustomerProject **   <a name="AWSPartnerCentral-Type-UpdateEngagementContextPayload-CustomerProject"></a>
Contains the updated details of a customer project when the context type is `CustomerProject`.
Type: [CustomerProjectsContext](API_CustomerProjectsContext.md) object
Required: No

 ** Lead **   <a name="AWSPartnerCentral-Type-UpdateEngagementContextPayload-Lead"></a>
Contains updated information about a lead when the context type is "Lead". This field is present only when updating a lead context within the engagement.
Type: [UpdateLeadContext](API_UpdateLeadContext.md) object
Required: No

 ** ProspectingResult **   <a name="AWSPartnerCentral-Type-UpdateEngagementContextPayload-ProspectingResult"></a>
Contains updated prospecting result data when the context type is "ProspectingResult". This field includes enriched data and insights that the system generates when a partner runs an autonomous prospecting job on leads.
Type: [ProspectingResult](API_ProspectingResult.md) object
Required: No

## See Also
<a name="API_UpdateEngagementContextPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/UpdateEngagementContextPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/UpdateEngagementContextPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/UpdateEngagementContextPayload)
