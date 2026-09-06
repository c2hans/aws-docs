---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-customverificationemailtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::CustomVerificationEmailTemplate
<a name="aws-resource-ses-customverificationemailtemplate"></a>

Represents a request to create a custom verification email template.

## Syntax
<a name="aws-resource-ses-customverificationemailtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-customverificationemailtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::SES::CustomVerificationEmailTemplate",
  "Properties" : {
      "[FailureRedirectionURL](#cfn-ses-customverificationemailtemplate-failureredirectionurl)" : {{String}},
      "[FromEmailAddress](#cfn-ses-customverificationemailtemplate-fromemailaddress)" : {{String}},
      "[SuccessRedirectionURL](#cfn-ses-customverificationemailtemplate-successredirectionurl)" : {{String}},
      "[Tags](#cfn-ses-customverificationemailtemplate-tags)" : {{[ Tag, ... ]}},
      "[TemplateContent](#cfn-ses-customverificationemailtemplate-templatecontent)" : {{String}},
      "[TemplateName](#cfn-ses-customverificationemailtemplate-templatename)" : {{String}},
      "[TemplateSubject](#cfn-ses-customverificationemailtemplate-templatesubject)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-customverificationemailtemplate-syntax.yaml"></a>

```
Type: AWS::SES::CustomVerificationEmailTemplate
Properties:
  [FailureRedirectionURL](#cfn-ses-customverificationemailtemplate-failureredirectionurl): {{String}}
  [FromEmailAddress](#cfn-ses-customverificationemailtemplate-fromemailaddress): {{String}}
  [SuccessRedirectionURL](#cfn-ses-customverificationemailtemplate-successredirectionurl): {{String}}
  [Tags](#cfn-ses-customverificationemailtemplate-tags): {{
    - Tag}}
  [TemplateContent](#cfn-ses-customverificationemailtemplate-templatecontent): {{String}}
  [TemplateName](#cfn-ses-customverificationemailtemplate-templatename): {{String}}
  [TemplateSubject](#cfn-ses-customverificationemailtemplate-templatesubject): {{String}}
```

## Properties
<a name="aws-resource-ses-customverificationemailtemplate-properties"></a>

`FailureRedirectionURL`  <a name="cfn-ses-customverificationemailtemplate-failureredirectionurl"></a>
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromEmailAddress`  <a name="cfn-ses-customverificationemailtemplate-fromemailaddress"></a>
The email address that the custom verification email is sent from.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessRedirectionURL`  <a name="cfn-ses-customverificationemailtemplate-successredirectionurl"></a>
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-customverificationemailtemplate-tags"></a>
An array of objects that define the tags (keys and values) to associate with the custom verification email template.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-customverificationemailtemplate-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateContent`  <a name="cfn-ses-customverificationemailtemplate-templatecontent"></a>
The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see [Custom verification email frequently asked questions](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom-faq) in the *Amazon SES Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-ses-customverificationemailtemplate-templatename"></a>
The name of the custom verification email template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateSubject`  <a name="cfn-ses-customverificationemailtemplate-templatesubject"></a>
The subject line of the custom verification email.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-customverificationemailtemplate-return-values"></a>

### Ref
<a name="aws-resource-ses-customverificationemailtemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the template name. For example:

 `{ "Ref": "MyCustomVerificationEmailTemplate" }`

For the Amazon SES custom verification email template `MyCustomVerificationEmailTemplate`, `Ref` returns the name of the custom verification email template.
