---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html
---

# DomainEndpointOptions
<a name="API_DomainEndpointOptions"></a>

## Description
<a name="API_DomainEndpointOptions_Description"></a>

Whether to require that all requests to the domain arrive over HTTPS. We recommend `Policy-Min-TLS-1-2-2019-07` for `TLSSecurityPolicy`. For compatibility with older clients, the default is `Policy-Min-TLS-1-0-2019-07`.

## Contents
<a name="API_DomainEndpointOptions_Contents"></a>

 **EnforceHTTPS**
Enables or disables the requirement that all requests to the domain arrive over HTTPS.
Type: Boolean
Valid Values: `true | false`
Required: No

 **TLSSecurityPolicy**
The minimum required TLS version.
Type: String
Valid Values: `Policy-Min-TLS-1-2-2019-07 | Policy-Min-TLS-1-0-2019-07`
Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
