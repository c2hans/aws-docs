---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetupRequest.html
---

# SetupRequest
<a name="API_SetupRequest"></a>

Returns information that was submitted during the `SetupInstanceHttps` request. Email information is redacted for privacy.

## Contents
<a name="API_SetupRequest_Contents"></a>

 ** certificateProvider **   <a name="Lightsail-Type-SetupRequest-certificateProvider"></a>
The Certificate Authority (CA) that issues the SSL/TLS certificate.
Type: String
Valid Values: `LetsEncrypt`
Required: No

 ** domainNames **   <a name="Lightsail-Type-SetupRequest-domainNames"></a>
The name of the domain and subdomains that the SSL/TLS certificate secures.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 4. Maximum length of 253.
Pattern: `^[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z0-9\-]{1,63}){0,8}(\.[a-zA-Z]{2,63})$`
Required: No

 ** instanceName **   <a name="Lightsail-Type-SetupRequest-instanceName"></a>
The name of the Lightsail instance.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## See Also
<a name="API_SetupRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetupRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetupRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetupRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
