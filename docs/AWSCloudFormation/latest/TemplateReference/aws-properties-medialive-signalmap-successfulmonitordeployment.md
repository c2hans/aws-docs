---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-signalmap-successfulmonitordeployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::SignalMap SuccessfulMonitorDeployment
<a name="aws-properties-medialive-signalmap-successfulmonitordeployment"></a>

Represents the latest successful monitor deployment of a signal map.

## Syntax
<a name="aws-properties-medialive-signalmap-successfulmonitordeployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-signalmap-successfulmonitordeployment-syntax.json"></a>

```
{
  "[DetailsUri](#cfn-medialive-signalmap-successfulmonitordeployment-detailsuri)" : {{String}},
  "[Status](#cfn-medialive-signalmap-successfulmonitordeployment-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-signalmap-successfulmonitordeployment-syntax.yaml"></a>

```
  [DetailsUri](#cfn-medialive-signalmap-successfulmonitordeployment-detailsuri): {{String}}
  [Status](#cfn-medialive-signalmap-successfulmonitordeployment-status): {{String}}
```

## Properties
<a name="aws-properties-medialive-signalmap-successfulmonitordeployment-properties"></a>

`DetailsUri`  <a name="cfn-medialive-signalmap-successfulmonitordeployment-detailsuri"></a>
URI associated with a signal map's monitor deployment.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-medialive-signalmap-successfulmonitordeployment-status"></a>
A signal map's monitor deployment status.
*Required*: Yes
*Type*: String
*Allowed values*: `NOT_DEPLOYED | DRY_RUN_DEPLOYMENT_COMPLETE | DRY_RUN_DEPLOYMENT_FAILED | DRY_RUN_DEPLOYMENT_IN_PROGRESS | DEPLOYMENT_COMPLETE | DEPLOYMENT_FAILED | DEPLOYMENT_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED | DELETE_IN_PROGRESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
