---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Metadata.html
---

# Metadata
<a name="API_Metadata"></a>

The metadata about the email.

## Contents
<a name="API_Metadata_Contents"></a>

 ** ConfigurationSet **   <a name="sesmailmanager-Type-Metadata-ConfigurationSet"></a>
The name of the configuration set used when sent through a configuration set with archiving enabled.
Type: String
Required: No

 ** IngressPointId **   <a name="sesmailmanager-Type-Metadata-IngressPointId"></a>
The ID of the ingress endpoint through which the email was received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** RuleSetId **   <a name="sesmailmanager-Type-Metadata-RuleSetId"></a>
The ID of the rule set that processed the email.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SenderHostname **   <a name="sesmailmanager-Type-Metadata-SenderHostname"></a>
The name of the host from which the email was received.
Type: String
Required: No

 ** SenderIpAddress **   <a name="sesmailmanager-Type-Metadata-SenderIpAddress"></a>
The IP address of the host from which the email was received.
Type: String
Required: No

 ** SendingMethod **   <a name="sesmailmanager-Type-Metadata-SendingMethod"></a>
The name of the API call used when sent through a configuration set with archiving enabled.
Type: String
Required: No

 ** SendingPool **   <a name="sesmailmanager-Type-Metadata-SendingPool"></a>
The name of the dedicated IP pool used when sent through a configuration set with archiving enabled.
Type: String
Required: No

 ** SourceArn **   <a name="sesmailmanager-Type-Metadata-SourceArn"></a>
Specifies the archived email source, identified by either a Rule Set's ARN with an Archive action, or a Configuration Set's Archive ARN.
Type: String
Required: No

 ** SourceIdentity **   <a name="sesmailmanager-Type-Metadata-SourceIdentity"></a>
The identity name used to authorize the sending action when sent through a configuration set with archiving enabled.
Type: String
Required: No

 ** Timestamp **   <a name="sesmailmanager-Type-Metadata-Timestamp"></a>
The timestamp of when the email was received.
Type: Timestamp
Required: No

 ** TlsCipherSuite **   <a name="sesmailmanager-Type-Metadata-TlsCipherSuite"></a>
The TLS cipher suite used to communicate with the host from which the email was received.
Type: String
Required: No

 ** TlsProtocol **   <a name="sesmailmanager-Type-Metadata-TlsProtocol"></a>
The TLS protocol used to communicate with the host from which the email was received.
Type: String
Required: No

 ** TrafficPolicyId **   <a name="sesmailmanager-Type-Metadata-TrafficPolicyId"></a>
The ID of the traffic policy that was in effect when the email was received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_Metadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Metadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Metadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Metadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
