---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafAtpConfig.html
---

# WafAtpConfig
<a name="API_WafAtpConfig"></a>

Describes the configuration of the account takeover prevention Web Application Firewall (WAF) rule group. The rule group inspects login requests to the login path of your application.

## Contents
<a name="API_WafAtpConfig_Contents"></a>

 ** loginPath **   <a name="Lightsail-Type-WafAtpConfig-loginPath"></a>
The path of the login endpoint of your application (for example, `/login`). Login paths that start with the path that you specify are a match.
Constraints:
+ Must start with a forward slash (`/`).
+ Must contain from 1 to 256 characters.
Type: String
Required: No

 ** passwordField **   <a name="Lightsail-Type-WafAtpConfig-passwordField"></a>
The name of the field in the request body that contains the password (for example, `/password` for `JSON` or `password` for `FORM_ENCODED`).
Constraints:
+ For a `JSON` payload, must be a JSON pointer that starts with a forward slash (`/`).
+ Must contain from 1 to 512 characters.
Type: String
Required: No

 ** payloadType **   <a name="Lightsail-Type-WafAtpConfig-payloadType"></a>
The content type of the request body of login requests.
The following content types are possible:
+  `JSON` – The request body is in JSON format.
+  `FORM_ENCODED` – The request body is form encoded.
Type: String
Valid Values: `JSON | FORM_ENCODED`
Required: No

 ** responseInspection **   <a name="Lightsail-Type-WafAtpConfig-responseInspection"></a>
An object that describes the HTTP status codes that your application returns for successful and failed login attempts.
Type: [WafResponseInspection](API_WafResponseInspection.md) object
Required: No

 ** usernameField **   <a name="Lightsail-Type-WafAtpConfig-usernameField"></a>
The name of the field in the request body that contains the username (for example, `/username` for `JSON` or `username` for `FORM_ENCODED`).
Constraints:
+ For a `JSON` payload, must be a JSON pointer that starts with a forward slash (`/`).
+ Must contain from 1 to 512 characters.
Type: String
Required: No

## See Also
<a name="API_WafAtpConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafAtpConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafAtpConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafAtpConfig)
