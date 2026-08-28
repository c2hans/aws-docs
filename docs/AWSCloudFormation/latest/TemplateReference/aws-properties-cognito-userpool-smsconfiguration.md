---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-smsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool SmsConfiguration
<a name="aws-properties-cognito-userpool-smsconfiguration"></a>

User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account.

## Syntax
<a name="aws-properties-cognito-userpool-smsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-smsconfiguration-syntax.json"></a>

```
{
  "[EumsSms](#cfn-cognito-userpool-smsconfiguration-eumssms)" : {{EumsSmsConfiguration}},
  "[ExternalId](#cfn-cognito-userpool-smsconfiguration-externalid)" : {{String}},
  "[SnsCallerArn](#cfn-cognito-userpool-smsconfiguration-snscallerarn)" : {{String}},
  "[SnsRegion](#cfn-cognito-userpool-smsconfiguration-snsregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-smsconfiguration-syntax.yaml"></a>

```
  [EumsSms](#cfn-cognito-userpool-smsconfiguration-eumssms): {{
    EumsSmsConfiguration}}
  [ExternalId](#cfn-cognito-userpool-smsconfiguration-externalid): {{String}}
  [SnsCallerArn](#cfn-cognito-userpool-smsconfiguration-snscallerarn): {{String}}
  [SnsRegion](#cfn-cognito-userpool-smsconfiguration-snsregion): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-smsconfiguration-properties"></a>

`EumsSms`  <a name="cfn-cognito-userpool-smsconfiguration-eumssms"></a>
Property description not available.
*Required*: No
*Type*: [EumsSmsConfiguration](aws-properties-cognito-userpool-eumssmsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-cognito-userpool-smsconfiguration-externalid"></a>
The external ID provides additional security for your IAM role. You can use an `ExternalId` with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an `ExternalId`, your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the `ExternalID`. If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the `ExternalId`.
For more information about the `ExternalId` of a role, see [How to use an external ID when granting access to your AWS resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsCallerArn`  <a name="cfn-cognito-userpool-smsconfiguration-snscallerarn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your AWS account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a [spending limit](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html).
*Required*: No
*Type*: String
*Pattern*: `(arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?)?`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsRegion`  <a name="cfn-cognito-userpool-smsconfiguration-snsregion"></a>
The AWS Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported **Legacy Amazon SNS alternate Region**.
 Amazon Cognito resources in the Asia Pacific (Seoul) AWS Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html).
*Required*: No
*Type*: String
*Minimum*: `5`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
