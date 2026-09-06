---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registereddynatracedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredDynatraceDetails
<a name="aws-properties-devopsagent-service-registereddynatracedetails"></a>

Dynatrace service details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registereddynatracedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registereddynatracedetails-syntax.json"></a>

```
{
  "[AccountUrn](#cfn-devopsagent-service-registereddynatracedetails-accounturn)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registereddynatracedetails-syntax.yaml"></a>

```
  [AccountUrn](#cfn-devopsagent-service-registereddynatracedetails-accounturn): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registereddynatracedetails-properties"></a>

`AccountUrn`  <a name="cfn-devopsagent-service-registereddynatracedetails-accounturn"></a>
The Dynatrace account URN.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
