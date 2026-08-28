---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-initialcapacityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application InitialCapacityConfig
<a name="aws-properties-emrserverless-application-initialcapacityconfig"></a>

The initial capacity configuration per worker.

## Syntax
<a name="aws-properties-emrserverless-application-initialcapacityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-initialcapacityconfig-syntax.json"></a>

```
{
  "[WorkerConfiguration](#cfn-emrserverless-application-initialcapacityconfig-workerconfiguration)" : {{WorkerConfiguration}},
  "[WorkerCount](#cfn-emrserverless-application-initialcapacityconfig-workercount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-initialcapacityconfig-syntax.yaml"></a>

```
  [WorkerConfiguration](#cfn-emrserverless-application-initialcapacityconfig-workerconfiguration): {{
    WorkerConfiguration}}
  [WorkerCount](#cfn-emrserverless-application-initialcapacityconfig-workercount): {{Integer}}
```

## Properties
<a name="aws-properties-emrserverless-application-initialcapacityconfig-properties"></a>

`WorkerConfiguration`  <a name="cfn-emrserverless-application-initialcapacityconfig-workerconfiguration"></a>
The resource configuration of the initial capacity configuration.
*Required*: Yes
*Type*: [WorkerConfiguration](aws-properties-emrserverless-application-workerconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`WorkerCount`  <a name="cfn-emrserverless-application-initialcapacityconfig-workercount"></a>
The number of workers in the initial capacity configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000000`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
