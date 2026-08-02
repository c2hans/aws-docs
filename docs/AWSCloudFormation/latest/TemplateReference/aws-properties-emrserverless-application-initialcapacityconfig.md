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
