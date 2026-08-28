---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-service-urlendpointinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Service UrlEndpointInput
<a name="aws-properties-refactorspaces-service-urlendpointinput"></a>

The configuration for the URL endpoint type.

## Syntax
<a name="aws-properties-refactorspaces-service-urlendpointinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-service-urlendpointinput-syntax.json"></a>

```
{
  "[HealthUrl](#cfn-refactorspaces-service-urlendpointinput-healthurl)" : {{String}},
  "[Url](#cfn-refactorspaces-service-urlendpointinput-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-service-urlendpointinput-syntax.yaml"></a>

```
  [HealthUrl](#cfn-refactorspaces-service-urlendpointinput-healthurl): {{String}}
  [Url](#cfn-refactorspaces-service-urlendpointinput-url): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-service-urlendpointinput-properties"></a>

`HealthUrl`  <a name="cfn-refactorspaces-service-urlendpointinput-healthurl"></a>
The health check URL of the URL endpoint type. If the URL is a public endpoint, the `HealthUrl` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.
*Required*: No
*Type*: String
*Pattern*: `^https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Url`  <a name="cfn-refactorspaces-service-urlendpointinput-url"></a>
The URL to route traffic to. The URL must be an [rfc3986-formatted URL](https://datatracker.ietf.org/doc/html/rfc3986). If the host is a domain name, the name must be resolvable over the public internet. If the scheme is `https`, the top level domain of the host must be listed in the [IANA root zone database](https://www.iana.org/domains/root/db).
*Required*: Yes
*Type*: String
*Pattern*: `^https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
