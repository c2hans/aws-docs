---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-detective-memberinvitation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Detective::MemberInvitation
<a name="aws-resource-detective-memberinvitation"></a>

The `AWS::Detective::MemberInvitation` resource is an Amazon Detective resource type that creates an invitation to join a Detective behavior graph. The administrator account can choose whether to send an email notification of the invitation to the root user email address of the AWS account.

## Syntax
<a name="aws-resource-detective-memberinvitation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-detective-memberinvitation-syntax.json"></a>

```
{
  "Type" : "AWS::Detective::MemberInvitation",
  "Properties" : {
      "[DisableEmailNotification](#cfn-detective-memberinvitation-disableemailnotification)" : {{Boolean}},
      "[GraphArn](#cfn-detective-memberinvitation-grapharn)" : {{String}},
      "[MemberEmailAddress](#cfn-detective-memberinvitation-memberemailaddress)" : {{String}},
      "[MemberId](#cfn-detective-memberinvitation-memberid)" : {{String}},
      "[Message](#cfn-detective-memberinvitation-message)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-detective-memberinvitation-syntax.yaml"></a>

```
Type: AWS::Detective::MemberInvitation
Properties:
  [DisableEmailNotification](#cfn-detective-memberinvitation-disableemailnotification): {{Boolean}}
  [GraphArn](#cfn-detective-memberinvitation-grapharn): {{String}}
  [MemberEmailAddress](#cfn-detective-memberinvitation-memberemailaddress): {{String}}
  [MemberId](#cfn-detective-memberinvitation-memberid): {{String}}
  [Message](#cfn-detective-memberinvitation-message): {{String}}
```

## Properties
<a name="aws-resource-detective-memberinvitation-properties"></a>

`DisableEmailNotification`  <a name="cfn-detective-memberinvitation-disableemailnotification"></a>
Whether to send an invitation email to the member account. If set to true, the member account does not receive an invitation email.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GraphArn`  <a name="cfn-detective-memberinvitation-grapharn"></a>
The ARN of the behavior graph to invite the account to contribute data to.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:detective:(([a-z]+-)+[0-9]+):[0-9]{12}:graph:[0-9a-f]{32}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemberEmailAddress`  <a name="cfn-detective-memberinvitation-memberemailaddress"></a>
The root user email address of the invited account. If the email address provided is not the root user email address for the provided account, the invitation creation fails.
*Required*: Yes
*Type*: String
*Pattern*: `.*@.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemberId`  <a name="cfn-detective-memberinvitation-memberid"></a>
The AWS account identifier of the invited account
*Required*: Yes
*Type*: String
*Pattern*: `[0-9]{12}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Message`  <a name="cfn-detective-memberinvitation-message"></a>
Customized text to include in the invitation email message.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-detective-memberinvitation-return-values"></a>

### Ref
<a name="aws-resource-detective-memberinvitation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the behavior graph and the member account identifier, separated by a pipe character ('\|').

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-detective-memberinvitation--examples"></a>

**Topics**
+ [Sending a behavior graph invitation to a member account](#aws-resource-detective-memberinvitation--examples--Sending_a_behavior_graph_invitation_to_a_member_account)
+ [Blocking the email notification of an invitation to a member account](#aws-resource-detective-memberinvitation--examples--Blocking_the_email_notification_of_an_invitation_to_a_member_account)

### Sending a behavior graph invitation to a member account
<a name="aws-resource-detective-memberinvitation--examples--Sending_a_behavior_graph_invitation_to_a_member_account"></a>

This example shows how to declare a new `AWS:Detective:MemberInvitation` resource to create a new invitation to a member account and send an email notification.

#### JSON
<a name="aws-resource-detective-memberinvitation--examples--Sending_a_behavior_graph_invitation_to_a_member_account--json"></a>

```
"MemberInvitation": {
    "Type": "AWS::Detective::MemberInvitation",
    "Properties": {
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
        "MemberId": "444455556666",
        "MemberEmailAddress": "mmajor@example.com",
        "Message": "This is Paul Santos. I need to add your account to the data we use for security investigation in Detective. If you have any questions, contact me at psantos@example.com."
     }
}
```

#### YAML
<a name="aws-resource-detective-memberinvitation--examples--Sending_a_behavior_graph_invitation_to_a_member_account--yaml"></a>

```
MemberInvitation:
    Type: AWS::Detective::MemberInvitation
    Properties:
      GraphArn: "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
      MemberId: 444455556666
      MemberEmailAddress: mmajor@example.com
      Message: This is Paul Santos. I need to add your account to the data we use for security investigation in Detective. If you have any questions, contact me at psantos@example.com.
```

### Blocking the email notification of an invitation to a member account
<a name="aws-resource-detective-memberinvitation--examples--Blocking_the_email_notification_of_an_invitation_to_a_member_account"></a>

This example shows how to declare a new `AWS:Detective:MemberInvitation` resource to create a new invitation to a member account. The email notification is blocked.

#### JSON
<a name="aws-resource-detective-memberinvitation--examples--Blocking_the_email_notification_of_an_invitation_to_a_member_account--json"></a>

```
"MemberInvitation": {
    "Type": "AWS::Detective::MemberInvitation",
    "Properties": {
        "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
        "MemberId": "444455556666",
        "MemberEmailAddress": "mmajor@example.com",
        "DisableEmailNotification": "true"
     }
}
```

#### YAML
<a name="aws-resource-detective-memberinvitation--examples--Blocking_the_email_notification_of_an_invitation_to_a_member_account--yaml"></a>

```
MemberInvitation:
    Type: AWS::Detective::MemberInvitation
    Properties:
      GraphArn: "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
      MemberId: 444455556666
      MemberEmailAddress: mmajor@example.com
      DisableEmailNotification: true
```
