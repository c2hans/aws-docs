---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificateDnsRecordCreationState.html
---

# LoadBalancerTlsCertificateDnsRecordCreationState
<a name="API_LoadBalancerTlsCertificateDnsRecordCreationState"></a>

An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of the domain to validate domain ownership.

## Contents
<a name="API_LoadBalancerTlsCertificateDnsRecordCreationState_Contents"></a>

 ** code **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDnsRecordCreationState-code"></a>
The status code for the automated DNS record creation.
Following are the possible values:
+  `SUCCEEDED` - The validation records were successfully added.
+  `STARTED` - The automatic DNS record creation has started.
+  `FAILED` - The validation record addition failed.
Type: String
Valid Values: `SUCCEEDED | STARTED | FAILED`
Required: No

 ** message **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDnsRecordCreationState-message"></a>
The message that describes the reason for the status code.
Type: String
Required: No

## See Also
<a name="API_LoadBalancerTlsCertificateDnsRecordCreationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsCertificateDnsRecordCreationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsCertificateDnsRecordCreationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsCertificateDnsRecordCreationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
