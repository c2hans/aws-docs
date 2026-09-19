---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Application
<a name="aws-resource-iotsitewise-application"></a>

<a name="aws-resource-iotsitewise-application-description"></a>The `AWS::IoTSiteWise::Application` resource Property description not available. for IoTSiteWise.

## Syntax
<a name="aws-resource-iotsitewise-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-application-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Application",
  "Properties" : {
      "[Description](#cfn-iotsitewise-application-description)" : {{String}},
      "[IdcInstanceArn](#cfn-iotsitewise-application-idcinstancearn)" : {{String}},
      "[Name](#cfn-iotsitewise-application-name)" : {{String}},
      "[Tags](#cfn-iotsitewise-application-tags)" : {{[ Tag, ... ]}},
      "[WorkspaceName](#cfn-iotsitewise-application-workspacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-application-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Application
Properties:
  [Description](#cfn-iotsitewise-application-description): {{String}}
  [IdcInstanceArn](#cfn-iotsitewise-application-idcinstancearn): {{String}}
  [Name](#cfn-iotsitewise-application-name): {{String}}
  [Tags](#cfn-iotsitewise-application-tags): {{
    - Tag}}
  [WorkspaceName](#cfn-iotsitewise-application-workspacename): {{String}}
```

## Properties
<a name="aws-resource-iotsitewise-application-properties"></a>

`Description`  <a name="cfn-iotsitewise-application-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdcInstanceArn`  <a name="cfn-iotsitewise-application-idcinstancearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-iotsitewise-application-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9](?:[A-Za-z0-9 ._()\-]*[A-Za-z0-9._()\-])?$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotsitewise-application-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-application-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceName`  <a name="cfn-iotsitewise-application-workspacename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotsitewise-application-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-application-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iotsitewise-application-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotsitewise-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`DnsSubdomain`  <a name="DnsSubdomain-fn::getatt"></a>
Property description not available.

`IdcApplicationArn`  <a name="IdcApplicationArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
