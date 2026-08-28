---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-fleetproxyrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet FleetProxyRule
<a name="aws-properties-codebuild-fleet-fleetproxyrule"></a>

Information about the proxy rule for your reserved capacity instances.

## Syntax
<a name="aws-properties-codebuild-fleet-fleetproxyrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-fleetproxyrule-syntax.json"></a>

```
{
  "[Effect](#cfn-codebuild-fleet-fleetproxyrule-effect)" : {{String}},
  "[Entities](#cfn-codebuild-fleet-fleetproxyrule-entities)" : {{[ String, ... ]}},
  "[Type](#cfn-codebuild-fleet-fleetproxyrule-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-fleetproxyrule-syntax.yaml"></a>

```
  [Effect](#cfn-codebuild-fleet-fleetproxyrule-effect): {{String}}
  [Entities](#cfn-codebuild-fleet-fleetproxyrule-entities): {{
    - String}}
  [Type](#cfn-codebuild-fleet-fleetproxyrule-type): {{String}}
```

## Properties
<a name="aws-properties-codebuild-fleet-fleetproxyrule-properties"></a>

`Effect`  <a name="cfn-codebuild-fleet-fleetproxyrule-effect"></a>
The behavior of the proxy rule.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Entities`  <a name="cfn-codebuild-fleet-fleetproxyrule-entities"></a>
The destination of the proxy rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-codebuild-fleet-fleetproxyrule-type"></a>
The type of proxy rule.
*Required*: No
*Type*: String
*Allowed values*: `DOMAIN | IP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
