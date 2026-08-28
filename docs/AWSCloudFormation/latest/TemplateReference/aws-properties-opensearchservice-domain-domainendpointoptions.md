---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-domainendpointoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain DomainEndpointOptions
<a name="aws-properties-opensearchservice-domain-domainendpointoptions"></a>

Specifies additional options for the domain endpoint, such as whether to require HTTPS for all traffic or whether to use a custom endpoint rather than the default endpoint.

## Syntax
<a name="aws-properties-opensearchservice-domain-domainendpointoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-domainendpointoptions-syntax.json"></a>

```
{
  "[CustomEndpoint](#cfn-opensearchservice-domain-domainendpointoptions-customendpoint)" : {{String}},
  "[CustomEndpointCertificateArn](#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn)" : {{String}},
  "[CustomEndpointEnabled](#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled)" : {{Boolean}},
  "[EnforceHTTPS](#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps)" : {{Boolean}},
  "[TLSSecurityPolicy](#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-domainendpointoptions-syntax.yaml"></a>

```
  [CustomEndpoint](#cfn-opensearchservice-domain-domainendpointoptions-customendpoint): {{String}}
  [CustomEndpointCertificateArn](#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn): {{String}}
  [CustomEndpointEnabled](#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled): {{Boolean}}
  [EnforceHTTPS](#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps): {{Boolean}}
  [TLSSecurityPolicy](#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-domainendpointoptions-properties"></a>

`CustomEndpoint`  <a name="cfn-opensearchservice-domain-domainendpointoptions-customendpoint"></a>
The fully qualified URL for your custom endpoint. Required if you enabled a custom endpoint for the domain.
*Required*: Conditional
*Type*: String
*Pattern*: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomEndpointCertificateArn`  <a name="cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn"></a>
The AWS Certificate Manager ARN for your domain's SSL/TLS certificate. Required if you enabled a custom endpoint for the domain.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomEndpointEnabled`  <a name="cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled"></a>
True to enable a custom endpoint for the domain. If enabled, you must also provide values for `CustomEndpoint` and `CustomEndpointCertificateArn`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnforceHTTPS`  <a name="cfn-opensearchservice-domain-domainendpointoptions-enforcehttps"></a>
True to require that all traffic to the domain arrive over HTTPS. Required if you enable fine-grained access control in [AdvancedSecurityOptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).
*Required*: Conditional
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`TLSSecurityPolicy`  <a name="cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy"></a>
The minimum TLS version required for traffic to the domain. The policy can be one of the following values:
+ **Policy-Min-TLS-1-0-2019-07:** TLS security policy that supports TLS version 1.0 to TLS version 1.2
+ **Policy-Min-TLS-1-2-2019-07:** TLS security policy that supports only TLS version 1.2
+ **Policy-Min-TLS-1-2-PFS-2023-10:** TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites
*Required*: No
*Type*: String
*Allowed values*: `Policy-Min-TLS-1-0-2019-07 | Policy-Min-TLS-1-2-2019-07 | Policy-Min-TLS-1-2-PFS-2023-10 | Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
