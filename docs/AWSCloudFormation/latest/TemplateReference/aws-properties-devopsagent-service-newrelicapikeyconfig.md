---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-newrelicapikeyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service NewRelicApiKeyConfig
<a name="aws-properties-devopsagent-service-newrelicapikeyconfig"></a>

The API key configuration for a New Relic service.

## Syntax
<a name="aws-properties-devopsagent-service-newrelicapikeyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-newrelicapikeyconfig-syntax.json"></a>

```
{
  "[AccountId](#cfn-devopsagent-service-newrelicapikeyconfig-accountid)" : {{String}},
  "[AlertPolicyIds](#cfn-devopsagent-service-newrelicapikeyconfig-alertpolicyids)" : {{[ String, ... ]}},
  "[ApiKey](#cfn-devopsagent-service-newrelicapikeyconfig-apikey)" : {{String}},
  "[ApplicationIds](#cfn-devopsagent-service-newrelicapikeyconfig-applicationids)" : {{[ String, ... ]}},
  "[EntityGuids](#cfn-devopsagent-service-newrelicapikeyconfig-entityguids)" : {{[ String, ... ]}},
  "[Region](#cfn-devopsagent-service-newrelicapikeyconfig-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-newrelicapikeyconfig-syntax.yaml"></a>

```
  [AccountId](#cfn-devopsagent-service-newrelicapikeyconfig-accountid): {{String}}
  [AlertPolicyIds](#cfn-devopsagent-service-newrelicapikeyconfig-alertpolicyids): {{
    - String}}
  [ApiKey](#cfn-devopsagent-service-newrelicapikeyconfig-apikey): {{String}}
  [ApplicationIds](#cfn-devopsagent-service-newrelicapikeyconfig-applicationids): {{
    - String}}
  [EntityGuids](#cfn-devopsagent-service-newrelicapikeyconfig-entityguids): {{
    - String}}
  [Region](#cfn-devopsagent-service-newrelicapikeyconfig-region): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-newrelicapikeyconfig-properties"></a>

`AccountId`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-accountid"></a>
The New Relic account ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlertPolicyIds`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-alertpolicyids"></a>
List of New Relic alert policy IDs.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKey`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-apikey"></a>
The New Relic User API key. Must match the pattern `^NRAK-[A-Z0-9]+$`.
*Required*: Yes
*Type*: String
*Pattern*: `^NRAK-[A-Z0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationIds`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-applicationids"></a>
List of New Relic APM application IDs to monitor.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityGuids`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-entityguids"></a>
List of globally unique IDs for New Relic resources.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-devopsagent-service-newrelicapikeyconfig-region"></a>
The New Relic region.
*Allowed Values*: `US` \| `EU`
*Required*: Yes
*Type*: String
*Allowed values*: `US | EU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
