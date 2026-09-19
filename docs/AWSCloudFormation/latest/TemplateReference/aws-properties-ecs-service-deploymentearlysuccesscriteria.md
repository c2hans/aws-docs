---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentearlysuccesscriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service DeploymentEarlySuccessCriteria
<a name="aws-properties-ecs-service-deploymentearlysuccesscriteria"></a>

**Note**
You can use early success criteria only with rolling deployment strategy.

The configuration that determines when a rolling update deployment is considered successful. Early success criteria defines the percentage of tasks that must be healthy before a deployment completes. It also controls whether Amazon ECS must remove the previous tasks before a deployment completes.

## Syntax
<a name="aws-properties-ecs-service-deploymentearlysuccesscriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-deploymentearlysuccesscriteria-syntax.json"></a>

```
{
  "[Enable](#cfn-ecs-service-deploymentearlysuccesscriteria-enable)" : {{Boolean}},
  "[HealthyPercent](#cfn-ecs-service-deploymentearlysuccesscriteria-healthypercent)" : {{Integer}},
  "[SourceServiceRevisionCleanup](#cfn-ecs-service-deploymentearlysuccesscriteria-sourceservicerevisioncleanup)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-deploymentearlysuccesscriteria-syntax.yaml"></a>

```
  [Enable](#cfn-ecs-service-deploymentearlysuccesscriteria-enable): {{Boolean}}
  [HealthyPercent](#cfn-ecs-service-deploymentearlysuccesscriteria-healthypercent): {{Integer}}
  [SourceServiceRevisionCleanup](#cfn-ecs-service-deploymentearlysuccesscriteria-sourceservicerevisioncleanup): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-deploymentearlysuccesscriteria-properties"></a>

`Enable`  <a name="cfn-ecs-service-deploymentearlysuccesscriteria-enable"></a>
Specifies whether to use the early success criteria for the service deployment. When set to `false`, the deployment uses the default behavior, where Amazon ECS considers the deployment successful when the target service revision fully stabilizes and the previous tasks are removed. The default value is `false`.
When set to `true`, Amazon ECS monitors the deployment to meet early success criteria. You must also specify `healthyPercent` and `sourceServiceRevisionCleanup`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthyPercent`  <a name="cfn-ecs-service-deploymentearlysuccesscriteria-healthypercent"></a>
The percentage of healthy tasks that the target service revision must reach before Amazon ECS considers the deployment successful. This percentage is relative to the service's `desiredCount` and must be an integer between `0` and `100`. This value must be greater than or equal to the `minimumHealthyPercent` value.
After this percentage of tasks is healthy and the bake time elapses, Amazon ECS completes the deployment. Amazon ECS continues to scale the target service revision to 100 percent in the background.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceServiceRevisionCleanup`  <a name="cfn-ecs-service-deploymentearlysuccesscriteria-sourceservicerevisioncleanup"></a>
The time when Amazon ECS removes the source revisions' tasks relative to deployment completion. The valid values are:
+ `BLOCKING`—Amazon ECS removes the previous tasks before it marks the deployment as successful.
+ `DEFERRED`—Amazon ECS marks the deployment successful, and then removes the previous tasks in the background.
*Required*: No
*Type*: String
*Allowed values*: `BLOCKING | DEFERRED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
