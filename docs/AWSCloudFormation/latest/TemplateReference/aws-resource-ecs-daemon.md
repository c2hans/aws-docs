---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-daemon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Daemon
<a name="aws-resource-ecs-daemon"></a>

Information about a daemon resource.

## Syntax
<a name="aws-resource-ecs-daemon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-daemon-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::Daemon",
  "Properties" : {
      "[CapacityProviderArns](#cfn-ecs-daemon-capacityproviderarns)" : {{[ String, ... ]}},
      "[ClusterArn](#cfn-ecs-daemon-clusterarn)" : {{String}},
      "[DaemonName](#cfn-ecs-daemon-daemonname)" : {{String}},
      "[DaemonTaskDefinitionArn](#cfn-ecs-daemon-daemontaskdefinitionarn)" : {{String}},
      "[DeploymentConfiguration](#cfn-ecs-daemon-deploymentconfiguration)" : {{DaemonDeploymentConfiguration}},
      "[EnableECSManagedTags](#cfn-ecs-daemon-enableecsmanagedtags)" : {{Boolean}},
      "[EnableExecuteCommand](#cfn-ecs-daemon-enableexecutecommand)" : {{Boolean}},
      "[PropagateTags](#cfn-ecs-daemon-propagatetags)" : {{String}},
      "[Tags](#cfn-ecs-daemon-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecs-daemon-syntax.yaml"></a>

```
Type: AWS::ECS::Daemon
Properties:
  [CapacityProviderArns](#cfn-ecs-daemon-capacityproviderarns): {{
    - String}}
  [ClusterArn](#cfn-ecs-daemon-clusterarn): {{String}}
  [DaemonName](#cfn-ecs-daemon-daemonname): {{String}}
  [DaemonTaskDefinitionArn](#cfn-ecs-daemon-daemontaskdefinitionarn): {{String}}
  [DeploymentConfiguration](#cfn-ecs-daemon-deploymentconfiguration): {{
    DaemonDeploymentConfiguration}}
  [EnableECSManagedTags](#cfn-ecs-daemon-enableecsmanagedtags): {{Boolean}}
  [EnableExecuteCommand](#cfn-ecs-daemon-enableexecutecommand): {{Boolean}}
  [PropagateTags](#cfn-ecs-daemon-propagatetags): {{String}}
  [Tags](#cfn-ecs-daemon-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ecs-daemon-properties"></a>

`CapacityProviderArns`  <a name="cfn-ecs-daemon-capacityproviderarns"></a>
The Amazon Resource Names (ARNs) of the capacity providers associated with the daemon.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterArn`  <a name="cfn-ecs-daemon-clusterarn"></a>
The Amazon Resource Name (ARN) of the cluster that the daemon is running in.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DaemonName`  <a name="cfn-ecs-daemon-daemonname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DaemonTaskDefinitionArn`  <a name="cfn-ecs-daemon-daemontaskdefinitionarn"></a>
The Amazon Resource Name (ARN) of the daemon task definition used by this revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentConfiguration`  <a name="cfn-ecs-daemon-deploymentconfiguration"></a>
The deployment configuration used for this daemon deployment.
*Required*: No
*Type*: [DaemonDeploymentConfiguration](aws-properties-ecs-daemon-daemondeploymentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableECSManagedTags`  <a name="cfn-ecs-daemon-enableecsmanagedtags"></a>
Specifies whether Amazon ECS managed tags are turned on for the daemon tasks.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableExecuteCommand`  <a name="cfn-ecs-daemon-enableexecutecommand"></a>
Specifies whether the execute command functionality is turned on for the daemon tasks.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-ecs-daemon-propagatetags"></a>
Specifies whether tags are propagated from the daemon to the daemon tasks.
*Required*: No
*Type*: String
*Allowed values*: `DAEMON | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ecs-daemon-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-daemon-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecs-daemon-return-values"></a>

### Ref
<a name="aws-resource-ecs-daemon-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-daemon-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-daemon-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp for the time when the daemon was created.

`DaemonArn`  <a name="DaemonArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the daemon.

`DaemonStatus`  <a name="DaemonStatus-fn::getatt"></a>
The status of the daemon.

`DeploymentArn`  <a name="DeploymentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the most recent daemon deployment.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp for the time when the daemon was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
