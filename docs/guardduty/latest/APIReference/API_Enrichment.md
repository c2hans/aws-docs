---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Enrichment.html
---

# Enrichment
<a name="API_Enrichment"></a>

Contains additional context about activity, such as geolocation and threat intelligence information. Not every member is set.

## Contents
<a name="API_Enrichment_Contents"></a>

 ** asnOrg **   <a name="guardduty-Type-Enrichment-asnOrg"></a>
The name of the organization that owns the autonomous system number (ASN).
Type: String
Required: No

 ** countryName **   <a name="guardduty-Type-Enrichment-countryName"></a>
The name of the country associated with the activity.
Type: String
Required: No

 ** threatListName **   <a name="guardduty-Type-Enrichment-threatListName"></a>
The name of the threat list that contains the indicator.
Type: String
Required: No

 ** threatName **   <a name="guardduty-Type-Enrichment-threatName"></a>
The name of the threat.
Type: String
Required: No

## See Also
<a name="API_Enrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Enrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Enrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Enrichment)
