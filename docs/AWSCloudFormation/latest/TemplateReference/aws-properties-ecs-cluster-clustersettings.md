---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-clustersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster ClusterSettings
<a name="aws-properties-ecs-cluster-clustersettings"></a>

The settings to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights with enhanced observability or CloudWatch Container Insights for a cluster.

Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up.

For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-cluster-clustersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-cluster-clustersettings-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-cluster-clustersettings-name)" : {{String}},
  "[Value](#cfn-ecs-cluster-clustersettings-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-cluster-clustersettings-syntax.yaml"></a>

```
  [Name](#cfn-ecs-cluster-clustersettings-name): {{String}}
  [Value](#cfn-ecs-cluster-clustersettings-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-cluster-clustersettings-properties"></a>

`Name`  <a name="cfn-ecs-cluster-clustersettings-name"></a>
The name of the cluster setting. The value is `containerInsights`.
*Required*: No
*Type*: String
*Allowed values*: `containerInsights`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ecs-cluster-clustersettings-value"></a>
The value to set for the cluster setting. The supported values are `enhanced`, `enabled`, and `disabled`.
To use Container Insights with enhanced observability, set the `containerInsights` account setting to `enhanced`.
To use Container Insights, set the `containerInsights` account setting to `enabled`.
If a cluster value is specified, it will override the `containerInsights` value set with [PutAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html) or [PutAccountSettingDefault](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-cluster-clustersettings--seealso"></a>
+  [Define an empty cluster with CloudWatch Container Insights enabled and defined tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#ws-resource-ecs-cluster--examples--Define_an_empty_cluster_with_CloudWatch_Container_Insights_enabled_and_defined_tags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
