---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-userattributeupdatesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool UserAttributeUpdateSettings
<a name="aws-properties-cognito-userpool-userattributeupdatesettings"></a>

The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate`, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see [ Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates).

## Syntax
<a name="aws-properties-cognito-userpool-userattributeupdatesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-userattributeupdatesettings-syntax.json"></a>

```
{
  "[AttributesRequireVerificationBeforeUpdate](#cfn-cognito-userpool-userattributeupdatesettings-attributesrequireverificationbeforeupdate)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-userattributeupdatesettings-syntax.yaml"></a>

```
  [AttributesRequireVerificationBeforeUpdate](#cfn-cognito-userpool-userattributeupdatesettings-attributesrequireverificationbeforeupdate): {{
    - String}}
```

## Properties
<a name="aws-properties-cognito-userpool-userattributeupdatesettings-properties"></a>

`AttributesRequireVerificationBeforeUpdate`  <a name="cfn-cognito-userpool-userattributeupdatesettings-attributesrequireverificationbeforeupdate"></a>
Requires that your user verifies their email address, phone number, or both before Amazon Cognito updates the value of that attribute. When you update a user attribute that has this option activated, Amazon Cognito sends a verification message to the new phone number or email address. Amazon Cognito doesn’t change the value of the attribute until your user responds to the verification message and confirms the new value.
When `AttributesRequireVerificationBeforeUpdate` is false, your user pool doesn't require that your users verify attribute changes before Amazon Cognito updates them. In a user pool where `AttributesRequireVerificationBeforeUpdate` is false, API operations that change attribute values can immediately update a user’s `email` or `phone_number` attribute.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
