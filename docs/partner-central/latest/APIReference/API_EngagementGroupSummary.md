---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementGroupSummary.html
---

# EngagementGroupSummary

A summary of an engagement group: a curated set of engagements that share common characteristics.

## Contents
<a name="API_EngagementGroupSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Id"></a>
The unique identifier of the engagement group. Pass this value to `SearchEngagements` as `GroupId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `eng-grp-[0-9a-z]{14}`
Required: Yes

 ** Arn **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Arn"></a>
The Amazon Resource Name (ARN) of the engagement group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Catalog **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Catalog"></a>
The catalog that the engagement group belongs to.
Type: String
Pattern: `[a-zA-Z]+`
Required: No

 ** Count **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Count"></a>
The number of engagements in the group that are available to you.
Type: Integer
Required: No

 ** Description **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Description"></a>
A description of the engagements that the group targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Name **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-Name"></a>
The name of the engagement group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ReadinessLevel **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-ReadinessLevel"></a>
The readiness level of the engagement group, which indicates the recommended call to action for its leads.
Type: String
Valid Values: `SalesReady | MarketingReady | LowPotential`
Required: No

 ** UpdatedAt **   <a name="AWSPartnerCentral-Type-EngagementGroupSummary-UpdatedAt"></a>
The date and time when the engagement group was last updated, in ISO 8601 format, in Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

## See Also
<a name="API_EngagementGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementGroupSummary)
