---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentalarms.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service DeploymentAlarms
<a name="aws-properties-ecs-service-deploymentalarms"></a>

One of the methods which provide a way for you to quickly identify when a deployment has failed, and then to optionally roll back the failure to the last working deployment.

When the alarms are generated, Amazon ECS sets the service deployment to failed. Set the rollback parameter to have Amazon ECS to roll back your service to the last completed deployment after a failure.

You can only use the `DeploymentAlarms` method to detect failures when the `DeploymentController` is set to `ECS`.

For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the * *Amazon Elastic Container Service Developer Guide* *.

## Syntax
<a name="aws-properties-ecs-service-deploymentalarms-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-deploymentalarms-syntax.json"></a>

```
{
  "[AlarmNames](#cfn-ecs-service-deploymentalarms-alarmnames)" : {{[ String, ... ]}},
  "[Enable](#cfn-ecs-service-deploymentalarms-enable)" : {{Boolean}},
  "[Rollback](#cfn-ecs-service-deploymentalarms-rollback)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ecs-service-deploymentalarms-syntax.yaml"></a>

```
  [AlarmNames](#cfn-ecs-service-deploymentalarms-alarmnames): {{
    - String}}
  [Enable](#cfn-ecs-service-deploymentalarms-enable): {{Boolean}}
  [Rollback](#cfn-ecs-service-deploymentalarms-rollback): {{Boolean}}
```

## Properties
<a name="aws-properties-ecs-service-deploymentalarms-properties"></a>

`AlarmNames`  <a name="cfn-ecs-service-deploymentalarms-alarmnames"></a>
One or more CloudWatch alarm names. Use a "," to separate the alarms.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enable`  <a name="cfn-ecs-service-deploymentalarms-enable"></a>
Determines whether to use the CloudWatch alarm option in the service deployment process.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rollback`  <a name="cfn-ecs-service-deploymentalarms-rollback"></a>
Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-deploymentalarms--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
