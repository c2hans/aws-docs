---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CertificateConfiguration.html
---

# CertificateConfiguration
<a name="API_CertificateConfiguration"></a>

Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the [Amazon GameLift Servers Server SDK](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html) operation `GetInstanceCertificate`.

## Contents
<a name="API_CertificateConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CertificateType **   <a name="gameliftservers-Type-CertificateConfiguration-CertificateType"></a>
Indicates whether a TLS/SSL certificate is generated for a fleet.
Valid values include:
+  **GENERATED** - Generate a TLS/SSL certificate for this fleet.
+  **DISABLED** - (default) Do not generate a TLS/SSL certificate for this fleet.
Type: String
Valid Values: `DISABLED | GENERATED`
Required: Yes

## See Also
<a name="API_CertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CertificateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CertificateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CertificateConfiguration)
