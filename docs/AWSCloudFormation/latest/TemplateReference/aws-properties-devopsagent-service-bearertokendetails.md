---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-bearertokendetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service BearerTokenDetails
<a name="aws-properties-devopsagent-service-bearertokendetails"></a>

Bearer token authentication details.

## Syntax
<a name="aws-properties-devopsagent-service-bearertokendetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-bearertokendetails-syntax.json"></a>

```
{
  "[AuthorizationHeader](#cfn-devopsagent-service-bearertokendetails-authorizationheader)" : {{String}},
  "[TokenName](#cfn-devopsagent-service-bearertokendetails-tokenname)" : {{String}},
  "[TokenValue](#cfn-devopsagent-service-bearertokendetails-tokenvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-bearertokendetails-syntax.yaml"></a>

```
  [AuthorizationHeader](#cfn-devopsagent-service-bearertokendetails-authorizationheader): {{String}}
  [TokenName](#cfn-devopsagent-service-bearertokendetails-tokenname): {{String}}
  [TokenValue](#cfn-devopsagent-service-bearertokendetails-tokenvalue): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-bearertokendetails-properties"></a>

`AuthorizationHeader`  <a name="cfn-devopsagent-service-bearertokendetails-authorizationheader"></a>
The HTTP header name used to send the bearer token. Defaults to `Authorization`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenName`  <a name="cfn-devopsagent-service-bearertokendetails-tokenname"></a>
A friendly name for the bearer token.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\s-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenValue`  <a name="cfn-devopsagent-service-bearertokendetails-tokenvalue"></a>
The bearer token value.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
