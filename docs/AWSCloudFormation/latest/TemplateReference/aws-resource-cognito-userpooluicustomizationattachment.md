---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpooluicustomizationattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolUICustomizationAttachment
<a name="aws-resource-cognito-userpooluicustomizationattachment"></a>

A container for the UI customization information for the hosted UI in a user pool.

## Syntax
<a name="aws-resource-cognito-userpooluicustomizationattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpooluicustomizationattachment-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolUICustomizationAttachment",
  "Properties" : {
      "[ClientId](#cfn-cognito-userpooluicustomizationattachment-clientid)" : {{String}},
      "[CSS](#cfn-cognito-userpooluicustomizationattachment-css)" : {{String}},
      "[UserPoolId](#cfn-cognito-userpooluicustomizationattachment-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpooluicustomizationattachment-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolUICustomizationAttachment
Properties:
  [ClientId](#cfn-cognito-userpooluicustomizationattachment-clientid): {{String}}
  [CSS](#cfn-cognito-userpooluicustomizationattachment-css): {{String}}
  [UserPoolId](#cfn-cognito-userpooluicustomizationattachment-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpooluicustomizationattachment-properties"></a>

`ClientId`  <a name="cfn-cognito-userpooluicustomizationattachment-clientid"></a>
The app client ID for your UI customization. When this value isn't present, the customization applies to all user pool app clients that don't have client-level settings..
*Required*: Yes
*Type*: String
*Pattern*: `[\w+]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CSS`  <a name="cfn-cognito-userpooluicustomizationattachment-css"></a>
A plaintext CSS file that contains the custom fields that you want to apply to your user pool or app client. To download a template, go to the Amazon Cognito console. Navigate to your user pool *App clients* tab, select *Login pages*, edit *Hosted UI (classic) style*, and select the link to `CSS template.css`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-userpooluicustomizationattachment-userpoolid"></a>
The ID of the user pool where you want to apply branding to the classic hosted UI.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-userpooluicustomizationattachment-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpooluicustomizationattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the physicalResourceId, which is “UserPoolUICustomizationAttachment-UserPoolId-ClientId". For example:

 `{ "Ref": "UserPoolUICustomizationAttachment-us-east-1_FAKEPOOLID-2asc123fakeclientidajjulj6bh" }`

For the Amazon Cognito user pool domain `UserPoolUICustomizationAttachment-us-east-1_FAKEPOOLID-2asc123fakeclientidajjulj6bh`, Ref returns the name of the UI customization attachment.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-cognito-userpooluicustomizationattachment--examples"></a>

### Creating a new UI customization attachment for a user pool
<a name="aws-resource-cognito-userpooluicustomizationattachment--examples--Creating_a_new_UI_customization_attachment_for_a_user_pool"></a>

The following example sets UI customization settings in the referenced user pool and client.

#### JSON
<a name="aws-resource-cognito-userpooluicustomizationattachment--examples--Creating_a_new_UI_customization_attachment_for_a_user_pool--json"></a>

```
{
   "UserPoolUICustomization":{
      "Type":"AWS::Cognito::UserPoolUICustomizationAttachment",
      "Properties":{
         "UserPoolId":{
            "Ref":"UserPool"
         },
         "ClientId":{
            "Ref":"Client"
         },
         "CSS":".banner-customizable {\nbackground:
        linear-gradient(#9940B8, #C27BDB)\n}"
      }
   }
}
```

#### YAML
<a name="aws-resource-cognito-userpooluicustomizationattachment--examples--Creating_a_new_UI_customization_attachment_for_a_user_pool--yaml"></a>

```
UserPoolUICustomization:
  Type: AWS::Cognito::UserPoolUICustomizationAttachment
  Properties:
    UserPoolId: !Ref UserPool
    ClientId: !Ref Client
    CSS: ".banner-customizable {
      background: linear-gradient(#9940B8, #C27BDB)
    }"
```
