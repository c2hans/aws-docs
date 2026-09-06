---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_TargetCloseDateFilter.html
---

# TargetCloseDateFilter
<a name="API_TargetCloseDateFilter"></a>

Filters opportunities based on their target close date.

## Contents
<a name="API_TargetCloseDateFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AfterTargetCloseDate **   <a name="AWSPartnerCentral-Type-TargetCloseDateFilter-AfterTargetCloseDate"></a>
Filters opportunities with a target close date after this date. Use the `YYYY-MM-DD` format.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

 ** BeforeTargetCloseDate **   <a name="AWSPartnerCentral-Type-TargetCloseDateFilter-BeforeTargetCloseDate"></a>
Filters opportunities with a target close date before this date. Use the `YYYY-MM-DD` format.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_TargetCloseDateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/TargetCloseDateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/TargetCloseDateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/TargetCloseDateFilter)
