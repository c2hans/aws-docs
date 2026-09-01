---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentConfig
<a name="aws-resource-codedeploy-deploymentconfig"></a>

 The `AWS::CodeDeploy::DeploymentConfig` resource creates a set of deployment rules, deployment success conditions, and deployment failure conditions that AWS CodeDeploy uses during a deployment. The deployment configuration specifies the number or percentage of instances that must remain available at any time during a deployment.

## Syntax
<a name="aws-resource-codedeploy-deploymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codedeploy-deploymentconfig-syntax.json"></a>

```
{
  "Type" : "AWS::CodeDeploy::DeploymentConfig",
  "Properties" : {
      "[ComputePlatform](#cfn-codedeploy-deploymentconfig-computeplatform)" : {{String}},
      "[DeploymentConfigName](#cfn-codedeploy-deploymentconfig-deploymentconfigname)" : {{String}},
      "[MinimumHealthyHosts](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts)" : {{MinimumHealthyHosts}},
      "[TrafficRoutingConfig](#cfn-codedeploy-deploymentconfig-trafficroutingconfig)" : {{TrafficRoutingConfig}},
      "[ZonalConfig](#cfn-codedeploy-deploymentconfig-zonalconfig)" : {{ZonalConfig}}
    }
}
```

### YAML
<a name="aws-resource-codedeploy-deploymentconfig-syntax.yaml"></a>

```
Type: AWS::CodeDeploy::DeploymentConfig
Properties:
  [ComputePlatform](#cfn-codedeploy-deploymentconfig-computeplatform): {{String}}
  [DeploymentConfigName](#cfn-codedeploy-deploymentconfig-deploymentconfigname): {{String}}
  [MinimumHealthyHosts](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts): {{
    MinimumHealthyHosts}}
  [TrafficRoutingConfig](#cfn-codedeploy-deploymentconfig-trafficroutingconfig): {{
    TrafficRoutingConfig}}
  [ZonalConfig](#cfn-codedeploy-deploymentconfig-zonalconfig): {{
    ZonalConfig}}
```

## Properties
<a name="aws-resource-codedeploy-deploymentconfig-properties"></a>

`ComputePlatform`  <a name="cfn-codedeploy-deploymentconfig-computeplatform"></a>
The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
*Required*: No
*Type*: String
*Allowed values*: `Server | Lambda | ECS | Kubernetes`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeploymentConfigName`  <a name="cfn-codedeploy-deploymentconfig-deploymentconfigname"></a>
 A name for the deployment configuration. If you don't specify a name, CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
 If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9+=,.@_-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinimumHealthyHosts`  <a name="cfn-codedeploy-deploymentconfig-minimumhealthyhosts"></a>
The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
The type parameter takes either of the following values:
+ HOST\_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.
+ FLEET\_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET\_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
The value parameter takes an integer.
For example, to set a minimum of 95% healthy instance, specify a type of FLEET\_PERCENT and a value of 95.
 For more information about instance health, see [CodeDeploy Instance Health](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html) in the AWS CodeDeploy User Guide.
*Required*: No
*Type*: [MinimumHealthyHosts](aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficRoutingConfig`  <a name="cfn-codedeploy-deploymentconfig-trafficroutingconfig"></a>
The configuration that specifies how the deployment traffic is routed.
*Required*: No
*Type*: [TrafficRoutingConfig](aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ZonalConfig`  <a name="cfn-codedeploy-deploymentconfig-zonalconfig"></a>
Configure the `ZonalConfig` object if you want AWS CodeDeploy to deploy your application to one [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) at a time, within an AWS Region.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
*Required*: No
*Type*: [ZonalConfig](aws-properties-codedeploy-deploymentconfig-zonalconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codedeploy-deploymentconfig-return-values"></a>

### Ref
<a name="aws-resource-codedeploy-deploymentconfig-return-values-ref"></a>

When you pass the logical ID of an `AWS::CodeDeploy::DeploymentConfig` resource to the intrinsic `Ref` function, the function returns the deployment configuration name, such as `mydeploymentconfig-a123d0d1`.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-codedeploy-deploymentconfig--examples"></a>

### Specifying minimum healthy hosts
<a name="aws-resource-codedeploy-deploymentconfig--examples--Specifying_minimum_healthy_hosts"></a>

The following example requires at least 75% of the fleet to be healthy. For example, if you had a fleet of four instances, the deployment proceeds one instance at a time.

#### JSON
<a name="aws-resource-codedeploy-deploymentconfig--examples--Specifying_minimum_healthy_hosts--json"></a>

```
"TwentyFivePercentAtATime" : {
    "Type" : "AWS::CodeDeploy::DeploymentConfig",
    "Properties" : {
        "MinimumHealthyHosts" : {
            "Type" : "FLEET_PERCENT",
            "Value" : "75"
        }
    }
}
```

#### YAML
<a name="aws-resource-codedeploy-deploymentconfig--examples--Specifying_minimum_healthy_hosts--yaml"></a>

```
TwentyFivePercentAtATime:
  Type: AWS::CodeDeploy::DeploymentConfig
  Properties:
    MinimumHealthyHosts:
      Type: "FLEET_PERCENT"
      Value: 75
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
