---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-route-defaultrouteinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Route DefaultRouteInput
<a name="aws-properties-refactorspaces-route-defaultrouteinput"></a>

 The configuration for the default route type.

## Syntax
<a name="aws-properties-refactorspaces-route-defaultrouteinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-route-defaultrouteinput-syntax.json"></a>

```
{
  "[ActivationState](#cfn-refactorspaces-route-defaultrouteinput-activationstate)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-route-defaultrouteinput-syntax.yaml"></a>

```
  [ActivationState](#cfn-refactorspaces-route-defaultrouteinput-activationstate): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-route-defaultrouteinput-properties"></a>

`ActivationState`  <a name="cfn-refactorspaces-route-defaultrouteinput-activationstate"></a>
If set to `ACTIVE`, traffic is forwarded to this route’s service after the route is created.
*Required*: Yes
*Type*: String
*Allowed values*: `INACTIVE | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
