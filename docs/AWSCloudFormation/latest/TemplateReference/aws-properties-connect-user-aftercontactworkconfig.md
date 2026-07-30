---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-aftercontactworkconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User AfterContactWorkConfig
<a name="aws-properties-connect-user-aftercontactworkconfig"></a>

Configuration settings for after contact work (ACW) timeout.

## Syntax
<a name="aws-properties-connect-user-aftercontactworkconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-aftercontactworkconfig-syntax.json"></a>

```
{
  "[AfterContactWorkMode](#cfn-connect-user-aftercontactworkconfig-aftercontactworkmode)" : {{String}},
  "[AfterContactWorkTimeLimit](#cfn-connect-user-aftercontactworkconfig-aftercontactworktimelimit)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-user-aftercontactworkconfig-syntax.yaml"></a>

```
  [AfterContactWorkMode](#cfn-connect-user-aftercontactworkconfig-aftercontactworkmode): {{String}}
  [AfterContactWorkTimeLimit](#cfn-connect-user-aftercontactworkconfig-aftercontactworktimelimit): {{Integer}}
```

## Properties
<a name="aws-properties-connect-user-aftercontactworkconfig-properties"></a>

`AfterContactWorkMode`  <a name="cfn-connect-user-aftercontactworkconfig-aftercontactworkmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ON | OFF | ON_DEMAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AfterContactWorkTimeLimit`  <a name="cfn-connect-user-aftercontactworkconfig-aftercontactworktimelimit"></a>
The ACW timeout duration in seconds. Minimum: 1 second. Maximum: 2,000,000 seconds (24 days). Enter 0 for indefinite ACW time.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
