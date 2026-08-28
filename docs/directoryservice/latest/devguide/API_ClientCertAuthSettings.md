---
source_url: https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ClientCertAuthSettings.html
---

# ClientCertAuthSettings
<a name="API_ClientCertAuthSettings"></a>

Contains information about the client certificate authentication settings for the `RegisterCertificate` and `DescribeCertificate` operations.

## Contents
<a name="API_ClientCertAuthSettings_Contents"></a>

 ** OCSPUrl **   <a name="DirectoryService-Type-ClientCertAuthSettings-OCSPUrl"></a>
Specifies the URL of the default OCSP server used to check for revocation status. A secondary value to any OCSP address found in the AIA extension of the user certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(https?|ftp|file|ldaps?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;()]*[-a-zA-Z0-9+&@#/%=~_|()]`
Required: No

## See Also
<a name="API_ClientCertAuthSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ClientCertAuthSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ClientCertAuthSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ClientCertAuthSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
