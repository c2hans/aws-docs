---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_BestOutreachWindow.html
---

# BestOutreachWindow

A single recommended outreach window for one day, expressed in Coordinated Universal Time (UTC).

## Contents
<a name="API_BestOutreachWindow_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Day **   <a name="AWSPartnerCentral-Type-BestOutreachWindow-Day"></a>
The day of the week that this outreach window applies to. Valid values are `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY`.
Type: String
Valid Values: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
Required: Yes

 ** EndTimeUtc **   <a name="AWSPartnerCentral-Type-BestOutreachWindow-EndTimeUtc"></a>
The exclusive end of the outreach window, in Coordinated Universal Time (UTC), in 24-hour `HH:mm` format.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `(?:[01][0-9]|2[0-3]):[0-5][0-9]`
Required: Yes

 ** StartTimeUtc **   <a name="AWSPartnerCentral-Type-BestOutreachWindow-StartTimeUtc"></a>
The inclusive start of the outreach window, in Coordinated Universal Time (UTC), in 24-hour `HH:mm` format.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `(?:[01][0-9]|2[0-3]):[0-5][0-9]`
Required: Yes

## See Also
<a name="API_BestOutreachWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/BestOutreachWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/BestOutreachWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/BestOutreachWindow)
