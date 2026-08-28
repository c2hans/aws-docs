---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-contactmethod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ContactMethod
<a name="aws-resource-lightsail-contactmethod"></a>

Describes a contact method.

A contact method is a way to send you notifications. For more information, see [Notifications in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications).

## Syntax
<a name="aws-resource-lightsail-contactmethod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-contactmethod-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::ContactMethod",
  "Properties" : {
      "[ContactEndpoint](#cfn-lightsail-contactmethod-contactendpoint)" : {{String}},
      "[Protocol](#cfn-lightsail-contactmethod-protocol)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-contactmethod-syntax.yaml"></a>

```
Type: AWS::Lightsail::ContactMethod
Properties:
  [ContactEndpoint](#cfn-lightsail-contactmethod-contactendpoint): {{String}}
  [Protocol](#cfn-lightsail-contactmethod-protocol): {{String}}
```

## Properties
<a name="aws-resource-lightsail-contactmethod-properties"></a>

`ContactEndpoint`  <a name="cfn-lightsail-contactmethod-contactendpoint"></a>
The destination of the contact method, such as an email address or a mobile phone number.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-lightsail-contactmethod-protocol"></a>
The protocol of the contact method, such as email or SMS (text messaging).
*Required*: Yes
*Type*: String
*Allowed values*: `Email | SMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lightsail-contactmethod-return-values"></a>

### Ref
<a name="aws-resource-lightsail-contactmethod-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-contactmethod-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-contactmethod-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the contact method.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the contact method was created.

`Name`  <a name="Name-fn::getatt"></a>
The name of the contact method.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The Lightsail resource type of the contact method.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the contact method.
A contact method has the following possible status:
+ `PendingVerification` - The contact method has not yet been verified, and the verification has not yet expired.
+ `Valid` - The contact method has been verified.
+ `InValid` - An attempt was made to verify the contact method, but the verification has expired.

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail contact method. This code enables our support team to look up your Lightsail information more easily.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
