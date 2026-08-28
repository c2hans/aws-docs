---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-proxyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet ProxyConfiguration
<a name="aws-properties-codebuild-fleet-proxyconfiguration"></a>

Information about the proxy configurations that apply network access control to your reserved capacity instances.

## Syntax
<a name="aws-properties-codebuild-fleet-proxyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-proxyconfiguration-syntax.json"></a>

```
{
  "[DefaultBehavior](#cfn-codebuild-fleet-proxyconfiguration-defaultbehavior)" : {{String}},
  "[OrderedProxyRules](#cfn-codebuild-fleet-proxyconfiguration-orderedproxyrules)" : {{[ FleetProxyRule, ... ]}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-proxyconfiguration-syntax.yaml"></a>

```
  [DefaultBehavior](#cfn-codebuild-fleet-proxyconfiguration-defaultbehavior): {{String}}
  [OrderedProxyRules](#cfn-codebuild-fleet-proxyconfiguration-orderedproxyrules): {{
    - FleetProxyRule}}
```

## Properties
<a name="aws-properties-codebuild-fleet-proxyconfiguration-properties"></a>

`DefaultBehavior`  <a name="cfn-codebuild-fleet-proxyconfiguration-defaultbehavior"></a>
The default behavior of outgoing traffic.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW_ALL | DENY_ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrderedProxyRules`  <a name="cfn-codebuild-fleet-proxyconfiguration-orderedproxyrules"></a>
An array of `FleetProxyRule` objects that represent the specified destination domains or IPs to allow or deny network access control to.
*Required*: No
*Type*: Array of [FleetProxyRule](aws-properties-codebuild-fleet-fleetproxyrule.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
