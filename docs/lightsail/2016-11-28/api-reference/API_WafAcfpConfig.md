---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafAcfpConfig.html
---

# WafAcfpConfig
<a name="API_WafAcfpConfig"></a>

Describes the configuration of the account creation fraud prevention Web Application Firewall (WAF) rule group. The rule group inspects account creation requests to your application.

## Contents
<a name="API_WafAcfpConfig_Contents"></a>

 ** creationPath **   <a name="Lightsail-Type-WafAcfpConfig-creationPath"></a>
The path of the endpoint that accepts completed account creation forms (for example, `/signup/submit`). This endpoint must accept `POST` requests.
Constraints:
+ Must start with a forward slash (`/`).
+ Must contain from 1 to 256 characters.
Type: String
Required: No

 ** payloadType **   <a name="Lightsail-Type-WafAcfpConfig-payloadType"></a>
The content type of the request body of account creation requests.
The following content types are possible:
+  `JSON` – The request body is in JSON format.
+  `FORM_ENCODED` – The request body is form encoded.
Type: String
Valid Values: `JSON | FORM_ENCODED`
Required: No

 ** registrationPagePath **   <a name="Lightsail-Type-WafAcfpConfig-registrationPagePath"></a>
The path of the page that displays the account creation form (for example, `/signup`).
Constraints:
+ Must start with a forward slash (`/`).
+ Must contain from 1 to 256 characters.
Type: String
Required: No

 ** responseInspection **   <a name="Lightsail-Type-WafAcfpConfig-responseInspection"></a>
An object that describes the HTTP status codes that your application returns for successful and failed account creation attempts.
Type: [WafResponseInspection](API_WafResponseInspection.md) object
Required: No

## See Also
<a name="API_WafAcfpConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafAcfpConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafAcfpConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafAcfpConfig)
