---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-placementconstraint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service PlacementConstraint
<a name="aws-properties-ecs-service-placementconstraint"></a>

An object representing a constraint on task placement. For more information, see [Task placement constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the *Amazon Elastic Container Service Developer Guide*.

**Note**
If you're using the Fargate launch type, task placement constraints aren't supported.

## Syntax
<a name="aws-properties-ecs-service-placementconstraint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-placementconstraint-syntax.json"></a>

```
{
  "[Expression](#cfn-ecs-service-placementconstraint-expression)" : {{String}},
  "[Type](#cfn-ecs-service-placementconstraint-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-placementconstraint-syntax.yaml"></a>

```
  [Expression](#cfn-ecs-service-placementconstraint-expression): {{String}}
  [Type](#cfn-ecs-service-placementconstraint-type): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-placementconstraint-properties"></a>

`Expression`  <a name="cfn-ecs-service-placementconstraint-expression"></a>
A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You can't specify an expression if the constraint type is `distinctInstance`. For more information, see [Cluster query language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ecs-service-placementconstraint-type"></a>
The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.
*Required*: Yes
*Type*: String
*Allowed values*: `distinctInstance | memberOf`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-placementconstraint--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)
