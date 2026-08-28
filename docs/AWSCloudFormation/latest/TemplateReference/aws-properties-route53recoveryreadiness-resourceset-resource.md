---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53recoveryreadiness-resourceset-resource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53RecoveryReadiness::ResourceSet Resource
<a name="aws-properties-route53recoveryreadiness-resourceset-resource"></a>

The resource element of a resource set.

## Syntax
<a name="aws-properties-route53recoveryreadiness-resourceset-resource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53recoveryreadiness-resourceset-resource-syntax.json"></a>

```
{
  "[ComponentId](#cfn-route53recoveryreadiness-resourceset-resource-componentid)" : {{String}},
  "[DnsTargetResource](#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource)" : {{DNSTargetResource}},
  "[ReadinessScopes](#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes)" : {{[ String, ... ]}},
  "[ResourceArn](#cfn-route53recoveryreadiness-resourceset-resource-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53recoveryreadiness-resourceset-resource-syntax.yaml"></a>

```
  [ComponentId](#cfn-route53recoveryreadiness-resourceset-resource-componentid): {{String}}
  [DnsTargetResource](#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource): {{
    DNSTargetResource}}
  [ReadinessScopes](#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes): {{
    - String}}
  [ResourceArn](#cfn-route53recoveryreadiness-resourceset-resource-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-route53recoveryreadiness-resourceset-resource-properties"></a>

`ComponentId`  <a name="cfn-route53recoveryreadiness-resourceset-resource-componentid"></a>
The component identifier of the resource, generated when DNS target resource is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsTargetResource`  <a name="cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource"></a>
A component for DNS/routing control readiness checks. This is a required setting when `ResourceSet``ResourceSetType` is set to `AWS::Route53RecoveryReadiness::DNSTargetResource`. Do not set it for any other `ResourceSetType` setting.
*Required*: Conditional
*Type*: [DNSTargetResource](aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadinessScopes`  <a name="cfn-route53recoveryreadiness-resourceset-resource-readinessscopes"></a>
The recovery group Amazon Resource Name (ARN) or the cell ARN that the readiness checks for this resource set are scoped to.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-route53recoveryreadiness-resourceset-resource-resourcearn"></a>
The Amazon Resource Name (ARN) of the AWS resource. This is a required setting for all `ResourceSet``ResourceSetType` settings except `AWS::Route53RecoveryReadiness::DNSTargetResource`. Do not set this when `ResourceSetType` is set to `AWS::Route53RecoveryReadiness::DNSTargetResource`.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
