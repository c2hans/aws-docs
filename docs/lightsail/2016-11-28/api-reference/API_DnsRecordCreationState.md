---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DnsRecordCreationState.html
---

# DnsRecordCreationState
<a name="API_DnsRecordCreationState"></a>

Describes the creation state of the canonical name (CNAME) records that are automatically added by Amazon Lightsail to the DNS of a domain to validate domain ownership for an SSL/TLS certificate.

When you create an SSL/TLS certificate for a Lightsail resource, you must add a set of CNAME records to the DNS of the domains for the certificate to validate that you own the domains. Lightsail can automatically add the CNAME records to the DNS of the domain if the DNS zone for the domain exists within your Lightsail account. If automatic record addition fails, or if you manage the DNS of your domain using a third-party service, then you must manually add the CNAME records to the DNS of your domain. For more information, see [Verify an SSL/TLS certificate in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/verify-tls-ssl-certificate-using-dns-cname-https) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_DnsRecordCreationState_Contents"></a>

 ** code **   <a name="Lightsail-Type-DnsRecordCreationState-code"></a>
The status code for the automated DNS record creation.
Following are the possible values:
+  `SUCCEEDED` - The validation records were successfully added to the domain.
+  `STARTED` - The automatic DNS record creation has started.
+  `FAILED` - The validation records failed to be added to the domain.
Type: String
Valid Values: `SUCCEEDED | STARTED | FAILED`
Required: No

 ** message **   <a name="Lightsail-Type-DnsRecordCreationState-message"></a>
The message that describes the reason for the status code.
Type: String
Required: No

## See Also
<a name="API_DnsRecordCreationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DnsRecordCreationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DnsRecordCreationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DnsRecordCreationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
