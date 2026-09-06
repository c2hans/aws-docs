---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition TaskDefinitionPlacementConstraint
<a name="aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint"></a>

The constraint on task placement in the task definition. For more information, see [Task placement constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the *Amazon Elastic Container Service Developer Guide*.

**Note**
Task placement constraints aren't supported for tasks run on AWS Fargate.

## Syntax
<a name="aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint-syntax.json"></a>

```
{
  "[Expression](#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression)" : {{String}},
  "[Type](#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint-syntax.yaml"></a>

```
  [Expression](#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression): {{String}}
  [Type](#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint-properties"></a>

`Expression`  <a name="cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression"></a>
A cluster query language expression to apply to the constraint. For more information, see [Cluster query language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type"></a>
The type of constraint. The `MemberOf` constraint restricts selection to be from a group of valid candidates.
*Required*: Yes
*Type*: String
*Allowed values*: `memberOf`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
