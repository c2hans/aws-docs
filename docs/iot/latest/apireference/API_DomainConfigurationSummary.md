---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DomainConfigurationSummary.html
---

# DomainConfigurationSummary
<a name="API_DomainConfigurationSummary"></a>

The summary of a domain configuration. A domain configuration specifies custom IoT-specific information about a domain. A domain configuration can be associated with an AWS-managed domain (for example, dbc123defghijk.iot.us-west-2.amazonaws.com), a customer managed domain, or a default endpoint.
+ Data
+ Jobs
+ CredentialProvider

## Contents
<a name="API_DomainConfigurationSummary_Contents"></a>

 ** domainConfigurationArn **   <a name="iot-Type-DomainConfigurationSummary-domainConfigurationArn"></a>
The ARN of the domain configuration.
Type: String
Required: No

 ** domainConfigurationName **   <a name="iot-Type-DomainConfigurationSummary-domainConfigurationName"></a>
The name of the domain configuration. This value must be unique to a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w.:-]+`
Required: No

 ** serviceType **   <a name="iot-Type-DomainConfigurationSummary-serviceType"></a>
The type of service delivered by the endpoint.
Type: String
Valid Values: `DATA | CREDENTIAL_PROVIDER | JOBS`
Required: No

## See Also
<a name="API_DomainConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DomainConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DomainConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DomainConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
