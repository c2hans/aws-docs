---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective CompositeSliComponent
<a name="aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent"></a>

Identifies a single operation to include in a composite SLI for a service-level SLO. Used as an element of the `Components` list in `CompositeSliConfig`.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent-syntax.json"></a>

```
{
  "[OperationName](#cfn-applicationsignals-servicelevelobjective-compositeslicomponent-operationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent-syntax.yaml"></a>

```
  [OperationName](#cfn-applicationsignals-servicelevelobjective-compositeslicomponent-operationname): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-compositeslicomponent-properties"></a>

`OperationName`  <a name="cfn-applicationsignals-servicelevelobjective-compositeslicomponent-operationname"></a>
The name of the operation to include in the composite SLI.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
