---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolregionalconfigurationattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRegionalConfigurationAttachment
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment"></a>

The Regional settings for a user pool replica, including email configuration, SMS configuration, AWS Lambda triggers, tags, and replica status. Create this resource in the secondary (replica) Region. The replica must be in `ACTIVE` or `INACTIVE` status before you create this resource.

## Syntax
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolRegionalConfigurationAttachment",
  "Properties" : {
      "[EmailConfiguration](#cfn-cognito-userpoolregionalconfigurationattachment-emailconfiguration)" : {{EmailConfiguration}},
      "[LambdaConfig](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig)" : {{LambdaConfig}},
      "[SmsConfiguration](#cfn-cognito-userpoolregionalconfigurationattachment-smsconfiguration)" : {{SmsConfiguration}},
      "[Status](#cfn-cognito-userpoolregionalconfigurationattachment-status)" : {{String}},
      "[UserPoolId](#cfn-cognito-userpoolregionalconfigurationattachment-userpoolid)" : {{String}},
      "[UserPoolTags](#cfn-cognito-userpoolregionalconfigurationattachment-userpooltags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolRegionalConfigurationAttachment
Properties:
  [EmailConfiguration](#cfn-cognito-userpoolregionalconfigurationattachment-emailconfiguration): {{
    EmailConfiguration}}
  [LambdaConfig](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig): {{
    LambdaConfig}}
  [SmsConfiguration](#cfn-cognito-userpoolregionalconfigurationattachment-smsconfiguration): {{
    SmsConfiguration}}
  [Status](#cfn-cognito-userpoolregionalconfigurationattachment-status): {{String}}
  [UserPoolId](#cfn-cognito-userpoolregionalconfigurationattachment-userpoolid): {{String}}
  [UserPoolTags](#cfn-cognito-userpoolregionalconfigurationattachment-userpooltags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-properties"></a>

`EmailConfiguration`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-emailconfiguration"></a>
The email configuration of your user pool. The email configuration type sets your preferred sending method, AWS Region, and sender for email invitation and verification messages from your user pool.
*Required*: No
*Type*: [EmailConfiguration](aws-properties-cognito-userpoolregionalconfigurationattachment-emailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaConfig`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig"></a>
A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.
*Required*: No
*Type*: [LambdaConfig](aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsConfiguration`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-smsconfiguration"></a>
The SMS configuration with the settings for your Amazon Cognito user pool to send SMS message with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account. For more information see [SMS message settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html).
*Required*: No
*Type*: [SmsConfiguration](aws-properties-cognito-userpoolregionalconfigurationattachment-smsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-status"></a>
The status of the replica. Valid values are `ACTIVE` and `INACTIVE`. If you don't specify a value, the default is `INACTIVE`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-userpoolid"></a>
The ID of the user pool. The user pool must have a replica in the Region where you create this resource.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserPoolTags`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-userpooltags"></a>
The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpoolregionalconfigurationattachment-return-values-ref"></a>
