---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registerednewrelicdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredNewRelicDetails
<a name="aws-properties-devopsagent-service-registerednewrelicdetails"></a>

New Relic service details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registerednewrelicdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registerednewrelicdetails-syntax.json"></a>

```
{
  "[AccountId](#cfn-devopsagent-service-registerednewrelicdetails-accountid)" : {{String}},
  "[Description](#cfn-devopsagent-service-registerednewrelicdetails-description)" : {{String}},
  "[Region](#cfn-devopsagent-service-registerednewrelicdetails-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registerednewrelicdetails-syntax.yaml"></a>

```
  [AccountId](#cfn-devopsagent-service-registerednewrelicdetails-accountid): {{String}}
  [Description](#cfn-devopsagent-service-registerednewrelicdetails-description): {{String}}
  [Region](#cfn-devopsagent-service-registerednewrelicdetails-region): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registerednewrelicdetails-properties"></a>

`AccountId`  <a name="cfn-devopsagent-service-registerednewrelicdetails-accountid"></a>
The New Relic account ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-devopsagent-service-registerednewrelicdetails-description"></a>
A description of the New Relic service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-devopsagent-service-registerednewrelicdetails-region"></a>
The New Relic region.
*Allowed Values*: `US` \| `EU`
*Required*: Yes
*Type*: String
*Allowed values*: `US | EU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
