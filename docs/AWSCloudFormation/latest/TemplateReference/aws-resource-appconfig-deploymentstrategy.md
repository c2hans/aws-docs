---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-deploymentstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::DeploymentStrategy
<a name="aws-resource-appconfig-deploymentstrategy"></a>

The `AWS::AppConfig::DeploymentStrategy` resource creates an AWS AppConfig deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

AWS AppConfig requires that you create resources and deploy a configuration in the following order:

1. Create an application

1. Create an environment

1. Create a configuration profile

1. Choose a pre-defined deployment strategy or create your own

1. Deploy the configuration

For more information, see [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) in the *AWS AppConfig User Guide*.

## Syntax
<a name="aws-resource-appconfig-deploymentstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-deploymentstrategy-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::DeploymentStrategy",
  "Properties" : {
      "[DeploymentDurationInMinutes](#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes)" : {{Number}},
      "[Description](#cfn-appconfig-deploymentstrategy-description)" : {{String}},
      "[FinalBakeTimeInMinutes](#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes)" : {{Number}},
      "[GrowthFactor](#cfn-appconfig-deploymentstrategy-growthfactor)" : {{Number}},
      "[GrowthType](#cfn-appconfig-deploymentstrategy-growthtype)" : {{String}},
      "[Name](#cfn-appconfig-deploymentstrategy-name)" : {{String}},
      "[ReplicateTo](#cfn-appconfig-deploymentstrategy-replicateto)" : {{String}},
      "[Tags](#cfn-appconfig-deploymentstrategy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-deploymentstrategy-syntax.yaml"></a>

```
Type: AWS::AppConfig::DeploymentStrategy
Properties:
  [DeploymentDurationInMinutes](#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes): {{Number}}
  [Description](#cfn-appconfig-deploymentstrategy-description): {{String}}
  [FinalBakeTimeInMinutes](#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes): {{Number}}
  [GrowthFactor](#cfn-appconfig-deploymentstrategy-growthfactor): {{Number}}
  [GrowthType](#cfn-appconfig-deploymentstrategy-growthtype): {{String}}
  [Name](#cfn-appconfig-deploymentstrategy-name): {{String}}
  [ReplicateTo](#cfn-appconfig-deploymentstrategy-replicateto): {{String}}
  [Tags](#cfn-appconfig-deploymentstrategy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appconfig-deploymentstrategy-properties"></a>

`DeploymentDurationInMinutes`  <a name="cfn-appconfig-deploymentstrategy-deploymentdurationinminutes"></a>
Total amount of time for a deployment to last.
AWS AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user-based or entity-based gradual deployments](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html#appconfig-entity-based-gradual-deployments)
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appconfig-deploymentstrategy-description"></a>
A description of the deployment strategy.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FinalBakeTimeInMinutes`  <a name="cfn-appconfig-deploymentstrategy-finalbaketimeinminutes"></a>
Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see [Configuring permissions for rollback based on Amazon CloudWatch alarms](https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html) in the *AWS AppConfig User Guide*.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GrowthFactor`  <a name="cfn-appconfig-deploymentstrategy-growthfactor"></a>
The percentage of targets to receive a deployed configuration during each interval.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GrowthType`  <a name="cfn-appconfig-deploymentstrategy-growthtype"></a>
The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:
**Linear**: For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for `Step percentage`. For example, a linear deployment that uses a `Step percentage` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.
**Exponential**: For this type, AWS AppConfig processes the deployment exponentially using the following formula: `G*(2^N)`. In this formula, `G` is the growth factor specified by the user and `N` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:
 `2*(2^0)`
 `2*(2^1)`
 `2*(2^2)`
Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
*Required*: No
*Type*: String
*Allowed values*: `EXPONENTIAL | LINEAR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appconfig-deploymentstrategy-name"></a>
A name for the deployment strategy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReplicateTo`  <a name="cfn-appconfig-deploymentstrategy-replicateto"></a>
Save the deployment strategy to a Systems Manager (SSM) document.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | SSM_DOCUMENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-appconfig-deploymentstrategy-tags"></a>
Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-appconfig-deploymentstrategy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appconfig-deploymentstrategy-return-values"></a>

### Ref
<a name="aws-resource-appconfig-deploymentstrategy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the deployment strategy ID.

### Fn::GetAtt
<a name="aws-resource-appconfig-deploymentstrategy-return-values-fn--getatt"></a>

####
<a name="aws-resource-appconfig-deploymentstrategy-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The deployment strategy ID.

## Examples
<a name="aws-resource-appconfig-deploymentstrategy--examples"></a>

### AWS AppConfig deployment strategy example
<a name="aws-resource-appconfig-deploymentstrategy--examples--deployment_strategy_example"></a>

The following example creates an AWS AppConfig deployment strategy called MyTestDeploymentStrategy. A deployment strategy defines how a configuration is deployed.

#### JSON
<a name="aws-resource-appconfig-deploymentstrategy--examples--deployment_strategy_example--json"></a>

```
Resources": {
    "BasicDeploymentStrategy": {
      "Type": "AWS::AppConfig::DeploymentStrategy",
      "Properties": {
        "Name": "MyTestDeploymentStrategy",
        "Description": "A sample test deployment strategy.",
        "DeploymentDurationInMinutes": 3,
        "FinalBakeTimeInMinutes": 4,
        "GrowthFactor": 10,
        "GrowthType": "LINEAR",
        "ReplicateTo": "NONE",
        "Tags": [
          {
            "Key": "Env",
            "Value": "test"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-appconfig-deploymentstrategy--examples--deployment_strategy_example--yaml"></a>

```
Resources:
  BasicDeploymentStrategy:
    Type: AWS::AppConfig::DeploymentStrategy
    Properties:
      Name: "MyTestDeploymentStrategy"
      Description: "A sample test deployment strategy."
      DeploymentDurationInMinutes: 3
      FinalBakeTimeInMinutes: 4
      GrowthFactor: 10
      GrowthType: LINEAR
      ReplicateTo: NONE
      Tags:
        - Key: Env
          Value: test
```

## See also
<a name="aws-resource-appconfig-deploymentstrategy--seealso"></a>
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
+  [Creating a deployment strategy](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig-creating-deployment-strategy.html)
