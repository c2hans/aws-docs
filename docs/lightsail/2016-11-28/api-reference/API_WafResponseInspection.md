---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafResponseInspection.html
---

# WafResponseInspection
<a name="API_WafResponseInspection"></a>

Describes the HTTP status codes that your application returns to indicate successful and failed attempts. The Web Application Firewall (WAF) rule group uses these status codes to track successful and failed attempts.

## Contents
<a name="API_WafResponseInspection_Contents"></a>

 ** failureCodes **   <a name="Lightsail-Type-WafResponseInspection-failureCodes"></a>
The HTTP status codes that indicate a failed attempt (for example, `401`).
Constraints:
+ Must contain from 1 to 10 status codes.
+ Each status code must be from `0` to `999`.
+ Can't contain a status code that is also in `successCodes`.
Type: Array of integers
Required: No

 ** successCodes **   <a name="Lightsail-Type-WafResponseInspection-successCodes"></a>
The HTTP status codes that indicate a successful attempt (for example, `200`).
Constraints:
+ Must contain from 1 to 10 status codes.
+ Each status code must be from `0` to `999`.
+ Can't contain a status code that is also in `failureCodes`.
Type: Array of integers
Required: No

## See Also
<a name="API_WafResponseInspection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafResponseInspection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafResponseInspection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafResponseInspection)
