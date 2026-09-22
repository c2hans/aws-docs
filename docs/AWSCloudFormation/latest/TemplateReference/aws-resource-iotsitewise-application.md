---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Application
<a name="aws-resource-iotsitewise-application"></a>

Specifies a new application for the provided workspace and IAM Identity Center instance. For more information, see [CreateApplication](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateApplication.html) in the *AWS IoT SiteWise API Reference*.

A workspace supports at most one application.

**Important**
Changing `WorkspaceName`, `Name`, `Description`, or `IdcInstanceArn` replaces the application. CloudFormation deletes the existing application, then creates a replacement. This interrupts access to the application during the replacement. You can update `Tags` without replacing the application.

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
A description of the application's purpose or intended use.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdcInstanceArn`  <a name="cfn-iotsitewise-application-idcinstancearn"></a>
The ARN of the IAM Identity Center instance to associate with the application.
You must provide this value when creating an application.
You use this property only when creating the application. Neither `Ref` nor `Fn::GetAtt` returns this value.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-iotsitewise-application-name"></a>
A name that identifies the application in the workspace. The name must start with a letter or digit and can't end with a space.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9](?:[A-Za-z0-9 ._()\-]*[A-Za-z0-9._()\-])?$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotsitewise-application-tags"></a>
Metadata that you can assign to the application in the form of key-value pairs. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-application-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceName`  <a name="cfn-iotsitewise-application-workspacename"></a>
The name of the existing workspace in which to create the application. Specify the workspace name, not its ARN.
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

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the application.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The unique identifier of the application.

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the application.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the application was created, in ISO 8601 format.

`DnsSubdomain`  <a name="DnsSubdomain-fn::getatt"></a>
The DNS subdomain label assigned to the application.

`IdcApplicationArn`  <a name="IdcApplicationArn-fn::getatt"></a>
The ARN of the IAM Identity Center application associated with this application.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the application. Valid values are:
+ `CREATING` - AWS IoT SiteWise is creating the application.
+ `ACTIVE` - You can use the application.
+ `DELETING` - AWS IoT SiteWise is deleting the application.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the application was last updated, in ISO 8601 format.

## Examples
<a name="aws-resource-iotsitewise-application--examples"></a>

The following example specifies an application in an existing workspace.

### Specify an application with IAM Identity Center
<a name="aws-resource-iotsitewise-application--examples--Specify_an_application_with_IAM_Identity_Center"></a>

Provide the name of an existing workspace that doesn't already contain an application, a name for the application, and the ARN of an enabled IAM Identity Center instance. The outputs return the application's ARN and identifier.

#### YAML
<a name="aws-resource-iotsitewise-application--examples--Specify_an_application_with_IAM_Identity_Center--yaml"></a>

```
Parameters:
  WorkspaceName:
    Type: String
  ApplicationName:
    Type: String
  IdcInstanceArn:
    Type: String
Resources:
  Application:
    Type: AWS::IoTSiteWise::Application
    Properties:
      WorkspaceName: !Ref WorkspaceName
      Name: !Ref ApplicationName
      IdcInstanceArn: !Ref IdcInstanceArn
      Tags:
        - Key: Environment
          Value: Example
Outputs:
  ApplicationArn:
    Value: !Ref Application
  ApplicationId:
    Value: !GetAtt Application.ApplicationId
```
