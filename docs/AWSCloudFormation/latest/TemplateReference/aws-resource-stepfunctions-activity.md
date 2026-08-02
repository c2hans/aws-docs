---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-activity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::Activity
<a name="aws-resource-stepfunctions-activity"></a>

An activity is a task that you write in any programming language and host on any machine that has access to AWS Step Functions. Activities must poll Step Functions using the `GetActivityTask` API action and respond using `SendTask*` API actions. This function makes Step Functions aware of your activity and returns an identifier for use in a state machine and when polling from the activity.

For information about creating an activity, see [Creating an Activity State Machine](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-activity-state-machine.html) in the *AWS Step Functions Developer Guide* and [CreateActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateActivity.html) in the *AWS Step Functions API Reference*.

## Syntax
<a name="aws-resource-stepfunctions-activity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-stepfunctions-activity-syntax.json"></a>

```
{
  "Type" : "AWS::StepFunctions::Activity",
  "Properties" : {
      "[EncryptionConfiguration](#cfn-stepfunctions-activity-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Name](#cfn-stepfunctions-activity-name)" : {{String}},
      "[Tags](#cfn-stepfunctions-activity-tags)" : {{[ TagsEntry, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-stepfunctions-activity-syntax.yaml"></a>

```
Type: AWS::StepFunctions::Activity
Properties:
  [EncryptionConfiguration](#cfn-stepfunctions-activity-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Name](#cfn-stepfunctions-activity-name): {{String}}
  [Tags](#cfn-stepfunctions-activity-tags): {{
    - TagsEntry}}
```

## Properties
<a name="aws-resource-stepfunctions-activity-properties"></a>

`EncryptionConfiguration`  <a name="cfn-stepfunctions-activity-encryptionconfiguration"></a>
Encryption configuration for the activity.
Activity configuration is immutable, and resource names must be unique. To set customer managed keys for encryption, you must create a **new Activity**. If you attempt to change the configuration in your CFN template for an existing activity, you will receive an `ActivityAlreadyExists` exception.
 To update your activity to include customer managed keys, set a new activity name within your CloudFormation template.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-stepfunctions-activity-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-stepfunctions-activity-name"></a>
The name of the activity.
A name must *not* contain:
+ white space
+ brackets `< > { } [ ]`
+ wildcard characters `? *`
+ special characters `" # % \ ^ | ~ ` $ & , ; : /`
+ control characters (`U+0000-001F`, `U+007F-009F`, `U+FFFE-FFFF`)
+ surrogates (`U+D800-DFFF`)
+ invalid characters (` U+10FFFF`)
To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and \_.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-stepfunctions-activity-tags"></a>
The list of tags to add to a resource.
Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @`.
*Required*: No
*Type*: Array of [TagsEntry](aws-properties-stepfunctions-activity-tagsentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-stepfunctions-activity-return-values"></a>

### Ref
<a name="aws-resource-stepfunctions-activity-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, `Ref` returns the ARN of the created activity. For example:

 `{ "Ref": "MyActivity" }`

Returns a value similar to the following:

 `arn:aws:states:us-east-1:111122223333:activity:myActivity`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-stepfunctions-activity-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-stepfunctions-activity-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the ARN of the resource.

`Name`  <a name="Name-fn::getatt"></a>
Returns the name of the activity. For example:
 `{ "Fn::GetAtt": ["MyActivity", "Name"] }`
Returns a value similar to the following:
 `myActivity`
For more information about using `Fn::GetAtt`, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-stepfunctions-activity--examples"></a>

The following examples create Step Functions activities.

Note that Activity configuration is immutable, and resource names must be unique. To set customer managed keys for encryption, you must create a **new Activity**. If you attempt to change the configuration in your CFN template for an existing activity, you will receive an `ActivityAlreadyExists` exception.

 To update your activity to include customer managed keys, set a new activity name within your CFN template. The following shows an example that creates a new activity with a customer managed key configuration:

**Topics**
+ [Create an activity](#aws-resource-stepfunctions-activity--examples--Create_an_activity)
+ [Create an activity with a customer managed AWS KMS key](#aws-resource-stepfunctions-activity--examples--Create_an_activity_with_a_customer_managed_key)

### Create an activity
<a name="aws-resource-stepfunctions-activity--examples--Create_an_activity"></a>

#### YAML
<a name="aws-resource-stepfunctions-activity--examples--Create_an_activity--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: An example template for a new Activity.
Resources:
    Activity:
    Type: AWS::StepFunctions::Activity
    Properties:
        Name: myActivity
        EncryptionConfiguration:
            Type: AWS_OWNED_KEY
        Tags:
        -
          Key: "keyname1"
          Value: "value1"
        -
          Key: "keyname2"
          Value: "value2"
```

#### JSON
<a name="aws-resource-stepfunctions-activity--examples--Create_an_activity--json"></a>

```
{
"AWSTemplateFormatVersion" : "2010-09-09",
"Description" : "An example template for a Step Functions activity.",
"Resources" : {
    "MyActivity" : {
        "Type" : "AWS::StepFunctions::Activity",
        "Properties" : {
            "Name" : "myActivity",
            "EncryptionConfiguration" : {
                "Type": "AWS_OWNED_KEY",
            }
            "Tags": [
                    {
                        "Key": "keyname1",
                        "Value": "value1"
                    },
                    {
                        "Key": "keyname2",
                        "Value": "value2"
                    }
                ]
            }
        }
    }
}
```

### Create an activity with a customer managed AWS KMS key
<a name="aws-resource-stepfunctions-activity--examples--Create_an_activity_with_a_customer_managed_key"></a>

#### YAML
<a name="aws-resource-stepfunctions-activity--examples--Create_an_activity_with_a_customer_managed_key--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: An example template for an Activity with customer managed key encryption.
Resources:
    Activity:
    Type: AWS::StepFunctions::Activity
    Properties:
        Name: ActivityWithKmsEncryption
        EncryptionConfiguration:
            Type: CUSTOMER_MANAGED_KMS_KEY
            KmsKeyId: !Ref MyKmsKey
            KmsDataKeyReusePeriodSeconds: 100
        Tags:
          -
            Key: "keyname1"
            Value: "value1"
          -
            Key: "keyname2"
            Value: "value2"

    MyKmsKey:
        Type: AWS::KMS::Key
        Properties:
            Description: Symmetric KMS key used for encryption/decryption
```
