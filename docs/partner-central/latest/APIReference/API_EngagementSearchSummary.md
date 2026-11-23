---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSearchSummary.html
---

# EngagementSearchSummary

A summary of an engagement returned by `SearchEngagements`. It contains the same engagement fields as the `GetEngagement` response.

## Contents
<a name="API_EngagementSearchSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the engagement.
Type: String
Pattern: `arn:.*`
Required: No

 ** Contexts **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-Contexts"></a>
The contexts associated with the engagement, such as prospecting results, lead details, and customer project details.
Type: Array of [EngagementContextDetails](API_EngagementContextDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-CreatedAt"></a>
The date and time when the engagement was created, in ISO 8601 format, in Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-CreatedBy"></a>
The AWS account ID of the user who created the engagement.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** Description **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-Description"></a>
A description of the engagement.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** Id **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-Id"></a>
The unique resource identifier of the engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** MemberCount **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-MemberCount"></a>
The number of members in the engagement.
Type: Integer
Required: No

 ** ModifiedAt **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-ModifiedAt"></a>
The date and time when the engagement was last modified, in ISO 8601 format, in Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** ModifiedBy **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-ModifiedBy"></a>
The AWS account ID of the user who last modified the engagement.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** Title **   <a name="AWSPartnerCentral-Type-EngagementSearchSummary-Title"></a>
The title of the engagement.
Type: String
Pattern: `(?s).{0,40}`
Required: No

## See Also
<a name="API_EngagementSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSearchSummary)
