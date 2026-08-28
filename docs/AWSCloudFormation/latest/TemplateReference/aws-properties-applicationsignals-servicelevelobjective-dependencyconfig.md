---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-servicelevelobjective-dependencyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::ServiceLevelObjective DependencyConfig
<a name="aws-properties-applicationsignals-servicelevelobjective-dependencyconfig"></a>

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.

## Syntax
<a name="aws-properties-applicationsignals-servicelevelobjective-dependencyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-servicelevelobjective-dependencyconfig-syntax.json"></a>

```
{
  "[DependencyKeyAttributes](#cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencykeyattributes)" : {{String}},
  "[DependencyOperationName](#cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencyoperationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-servicelevelobjective-dependencyconfig-syntax.yaml"></a>

```
  [DependencyKeyAttributes](#cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencykeyattributes): {{String}}
  [DependencyOperationName](#cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencyoperationname): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-servicelevelobjective-dependencyconfig-properties"></a>

`DependencyKeyAttributes`  <a name="cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencykeyattributes"></a>
If this SLO is related to a metric collected by Application Signals, you must use this field to specify which dependency the SLO metric is related to.
+ `Type` designates the type of object this is.
+ `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+ `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+ `Environment` specifies the location where this object is hosted, or what it belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependencyOperationName`  <a name="cfn-applicationsignals-servicelevelobjective-dependencyconfig-dependencyoperationname"></a>
When the SLO monitors a specific operation of the dependency, this field specifies the name of that operation in the dependency.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
