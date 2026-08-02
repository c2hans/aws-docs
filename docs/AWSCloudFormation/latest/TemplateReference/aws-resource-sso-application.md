---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sso-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::Application
<a name="aws-resource-sso-application"></a>

Creates an OAuth 2.0 customer managed application in IAM Identity Center for the given application provider.

**Note**
This API does not support creating SAML 2.0 customer managed applications or AWS managed applications. To learn how to create an AWS managed application, see the application user guide. You can create a SAML 2.0 customer managed application in the AWS Management Console only. See [Setting up customer managed SAML 2.0 applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html). For more information on these application types, see [AWS managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html).

## Syntax
<a name="aws-resource-sso-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sso-application-syntax.json"></a>

```
{
  "Type" : "AWS::SSO::Application",
  "Properties" : {
      "[ApplicationProviderArn](#cfn-sso-application-applicationproviderarn)" : {{String}},
      "[Description](#cfn-sso-application-description)" : {{String}},
      "[InstanceArn](#cfn-sso-application-instancearn)" : {{String}},
      "[Name](#cfn-sso-application-name)" : {{String}},
      "[PortalOptions](#cfn-sso-application-portaloptions)" : {{PortalOptionsConfiguration}},
      "[Status](#cfn-sso-application-status)" : {{String}},
      "[Tags](#cfn-sso-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sso-application-syntax.yaml"></a>

```
Type: AWS::SSO::Application
Properties:
  [ApplicationProviderArn](#cfn-sso-application-applicationproviderarn): {{String}}
  [Description](#cfn-sso-application-description): {{String}}
  [InstanceArn](#cfn-sso-application-instancearn): {{String}}
  [Name](#cfn-sso-application-name): {{String}}
  [PortalOptions](#cfn-sso-application-portaloptions): {{
    PortalOptionsConfiguration}}
  [Status](#cfn-sso-application-status): {{String}}
  [Tags](#cfn-sso-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sso-application-properties"></a>

`ApplicationProviderArn`  <a name="cfn-sso-application-applicationproviderarn"></a>
The ARN of the application provider for this application.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-sso-application-description"></a>
The description of the application.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-sso-application-instancearn"></a>
The ARN of the instance of IAM Identity Center that is configured with this application.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `10`
*Maximum*: `1224`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-sso-application-name"></a>
The name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalOptions`  <a name="cfn-sso-application-portaloptions"></a>
A structure that describes the options for the access portal associated with this application.
*Required*: No
*Type*: [PortalOptionsConfiguration](aws-properties-sso-application-portaloptionsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-sso-application-status"></a>
The current status of the application in this instance of IAM Identity Center.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sso-application-tags"></a>
Specifies tags to be attached to the application.
*Required*: No
*Type*: Array of [Tag](aws-properties-sso-application-tag.md)
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sso-application-return-values"></a>

### Ref
<a name="aws-resource-sso-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a generated ID, combined by all fields with the delimiter `|`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sso-application-return-values-fn--getatt"></a>

####
<a name="aws-resource-sso-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
The ARN of the application.

`IdentityStoreArn`  <a name="IdentityStoreArn-fn::getatt"></a>
The ARN of the identity store that is connected to the instance of IAM Identity Center.

## Examples
<a name="aws-resource-sso-application--examples"></a>

### Creating an application in IAM Identity Center
<a name="aws-resource-sso-application--examples--Creating_an_application_in"></a>

The following example creates a new custom application with an Application URL sign-in option.

#### JSON
<a name="aws-resource-sso-application--examples--Creating_an_application_in--json"></a>

```
{
  "Type" : "AWS::SSO::Application",
  "Properties" : {
    "ApplicationProviderArn" : "arn:sso::aws:applicationProvider/example",
    "Description" : "This is a sample application",
    "InstanceArn" : "arn:aws:sso:::instance/ssoins-instanceId",
    "Name" : "Application",
    "PortalOptions" : {
      "SignInOptions" : {
        "ApplicationUrl" : "http://www.example.com",
        "Origin" : "APPLICATION"
      },
      "Visibility" : "ENABLED"
    },
    "Status" : "ENABLED",
    "Tags": [
      {
        "Key": "tagKey",
        "Value": "tagValue"
      }
    ]
  }
}
```

#### YAML
<a name="aws-resource-sso-application--examples--Creating_an_application_in--yaml"></a>

```
Type: AWS::SSO::Application
Properties:
  ApplicationProviderArn: arn:sso::aws:applicationProvider/example
  Description: This is a sample application
  InstanceArn: arn:aws:sso:::instance/ssoins-instanceId
  Name: Application
  PortalOptions:
    SignInOptions:
      ApplicationUrl: http://www.example.com
      Origin: APPLICATION
    Visibility: ENABLED
  Status: ENABLED
  Tags:
  - Key: tagKey
    Value: tagValue
```
