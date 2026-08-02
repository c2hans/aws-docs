---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-privateconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection
<a name="aws-resource-devopsagent-privateconnection"></a>

<a name="aws-resource-devopsagent-privateconnection-description"></a>The `AWS::DevOpsAgent::PrivateConnection` resource Property description not available. for DevOpsAgent.

## Syntax
<a name="aws-resource-devopsagent-privateconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-privateconnection-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::PrivateConnection",
  "Properties" : {
      "[Certificate](#cfn-devopsagent-privateconnection-certificate)" : {{String}},
      "[ConnectionConfiguration](#cfn-devopsagent-privateconnection-connectionconfiguration)" : {{ConnectionConfiguration}},
      "[Name](#cfn-devopsagent-privateconnection-name)" : {{String}},
      "[Tags](#cfn-devopsagent-privateconnection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-privateconnection-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::PrivateConnection
Properties:
  [Certificate](#cfn-devopsagent-privateconnection-certificate): {{String}}
  [ConnectionConfiguration](#cfn-devopsagent-privateconnection-connectionconfiguration): {{
    ConnectionConfiguration}}
  [Name](#cfn-devopsagent-privateconnection-name): {{String}}
  [Tags](#cfn-devopsagent-privateconnection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-devopsagent-privateconnection-properties"></a>

`Certificate`  <a name="cfn-devopsagent-privateconnection-certificate"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionConfiguration`  <a name="cfn-devopsagent-privateconnection-connectionconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [ConnectionConfiguration](aws-properties-devopsagent-privateconnection-connectionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-devopsagent-privateconnection-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-devopsagent-privateconnection-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-devopsagent-privateconnection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsagent-privateconnection-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-privateconnection-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-devopsagent-privateconnection-return-values-fn--getatt"></a>

####
<a name="aws-resource-devopsagent-privateconnection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CertificateExpiryTime`  <a name="CertificateExpiryTime-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
