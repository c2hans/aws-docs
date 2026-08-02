---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-eventbuspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::EventBusPolicy
<a name="aws-resource-events-eventbuspolicy"></a>

Running `PutPermission` permits the specified AWS account or AWS organization to put events to the specified *event bus*. Amazon EventBridge rules in your account are triggered by these events arriving to an event bus in your account.

For another account to send events to your account, that external account must have an EventBridge rule with your account's event bus as a target.

To enable multiple AWS accounts to put events to your event bus, run `PutPermission` once for each of these accounts. Or, if all the accounts are members of the same AWS organization, you can run `PutPermission` once specifying `Principal` as "\*" and specifying the AWS organization ID in `Condition`, to grant permissions to all accounts in that organization.

If you grant permissions using an organization, then accounts in that organization must specify a `RoleArn` with proper permissions when they use `PutTarget` to add your account's event bus as a target. For more information, see [Sending and Receiving Events Between AWS Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide*.

The permission policy on the event bus cannot exceed 10 KB in size.

## Syntax
<a name="aws-resource-events-eventbuspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-events-eventbuspolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Events::EventBusPolicy",
  "Properties" : {
      "[EventBusName](#cfn-events-eventbuspolicy-eventbusname)" : {{String}},
      "[Statement](#cfn-events-eventbuspolicy-statement)" : {{Json}},
      "[StatementId](#cfn-events-eventbuspolicy-statementid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-events-eventbuspolicy-syntax.yaml"></a>

```
Type: AWS::Events::EventBusPolicy
Properties:
  [EventBusName](#cfn-events-eventbuspolicy-eventbusname): {{String}}
  [Statement](#cfn-events-eventbuspolicy-statement): {{Json}}
  [StatementId](#cfn-events-eventbuspolicy-statementid): {{String}}
```

## Properties
<a name="aws-resource-events-eventbuspolicy-properties"></a>

`EventBusName`  <a name="cfn-events-eventbuspolicy-eventbusname"></a>
The name of the event bus associated with the rule. If you omit this, the default event bus is used.
*Required*: No
*Type*: String
*Pattern*: `[\.\-_A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Statement`  <a name="cfn-events-eventbuspolicy-statement"></a>
A JSON string that describes the permission policy statement. You can include a `Policy` parameter in the request instead of using the `StatementId`, `Action`, `Principal`, or `Condition` parameters.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatementId`  <a name="cfn-events-eventbuspolicy-statementid"></a>
An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this `StatementId` when you run [RemovePermission](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html).
Each `StatementId` must be unique.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-events-eventbuspolicy-return-values"></a>

### Ref
<a name="aws-resource-events-eventbuspolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the event bus policy ID, such as `EventBusPolicy-1aBCdeFGh2J3`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-events-eventbuspolicy--examples"></a>

**Topics**
+ [Grant Permission to One Account](#aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_One_Account)
+ [Grant Permission to an Organization](#aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization)
+ [Deny policy using multiple principals and actions](#aws-resource-events-eventbuspolicy--examples--Deny_policy_using_multiple_principals_and_actions)
+ [Grant Permission to an Organization using a custom event bus](#aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization_using_a_custom_event_bus)

### Grant Permission to One Account
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_One_Account"></a>

The following example grants permission to one AWS account with an account ID of `111122223333`.

#### JSON
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_One_Account--json"></a>

```
"SampleEventBusPolicy": {
    "Type": "AWS::Events::EventBusPolicy",
    "Properties": {
        "StatementId": "MyStatement",
        "Statement": {
            "Effect": "Allow",
            "Principal" : {"AWS" : "arn:aws:iam::111122223333:root"},
            "Action": "events:PutEvents",
            "Resource": "arn:aws:events:us-east-1:111122223333:event-bus/default"
        }
    }
}
```

#### YAML
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_One_Account--yaml"></a>

```
SampleEventBusPolicy:
    Type: AWS::Events::EventBusPolicy
    Properties:
        StatementId: "MyStatement"
        Statement:
            Effect: "Allow"
            Principal:
                AWS: "arn:aws:iam::111122223333:root"
            Action: "events:PutEvents"
            Resource: "arn:aws:events:us-east-1:111122223333:event-bus/default"
```

### Grant Permission to an Organization
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization"></a>

The following example grants permission to all AWS accounts in the organization with an organization ID of `o-1234567890`.

#### JSON
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization--json"></a>

```
"SampleEventBusPolicy": {
    "Type": "AWS::Events::EventBusPolicy",
    "Properties": {
        "StatementId": "MyStatement",
        "Statement": {
            "Effect": "Allow",
            "Principal" : "*",
            "Action": "events:PutEvents",
            "Resource": "arn:aws:events:us-east-1:111122223333:event-bus/default",
            "Condition": {
                "StringEquals": {"aws:PrincipalOrgID": "o-1234567890"}
             }
        }
    }
}
```

#### YAML
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization--yaml"></a>

```
SampleEventBusPolicy:
    Type: AWS::Events::EventBusPolicy
    Properties:
        StatementId: "MyStatement"
        Statement:
            Effect: "Allow"
            Principal: "*"
            Action: "events:PutEvents"
            Resource: "arn:aws:events:us-east-1:111122223333:event-bus/default"
            Condition:
                StringEquals:
                    "aws:PrincipalOrgID": "o-1234567890"
```

### Deny policy using multiple principals and actions
<a name="aws-resource-events-eventbuspolicy--examples--Deny_policy_using_multiple_principals_and_actions"></a>

The following example demonstrates a deny policy statement using multiple principals and actions.

#### JSON
<a name="aws-resource-events-eventbuspolicy--examples--Deny_policy_using_multiple_principals_and_actions--json"></a>

```
"SampleDenyEventBusPolicy": {
    "Type": "AWS::Events::EventBusPolicy",
    "Properties": {
        "StatementId": "MyDenyStatement",
        "Statement": {
            "Effect": "Deny",
            "Principal" :
                {"AWS" : ["arn:aws:iam::111122223333:user/alice", "arn:aws:iam::111122223333:user/bob"]},
            "Action": [
                "events:PutEvents",
                "events:PutRule"
            ],
            "Resource": "arn:aws:events:us-east-1:111122223333:event-bus/default"
        }
    }
}
```

#### YAML
<a name="aws-resource-events-eventbuspolicy--examples--Deny_policy_using_multiple_principals_and_actions--yaml"></a>

```
SampleDenyEventBusPolicy:
    Type: AWS::Events::EventBusPolicy
    Properties:
        StatementId: "MyDenyStatement"
        Statement:
            Effect: "Deny"
            Principal:
                AWS:
                    - "arn:aws:iam::111122223333:user/alice"
                    - "arn:aws:iam::111122223333:user/bob"
            Action:
                - "events:PutEvents"
                - "events:PutRule"
            Resource: "arn:aws:events:us-east-1:111122223333:event-bus/default"
```

### Grant Permission to an Organization using a custom event bus
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization_using_a_custom_event_bus"></a>

The following example grants permission to all AWS accounts in the organization with an organization ID of `o-1234567890` using a custom event bus.

#### JSON
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization_using_a_custom_event_bus--json"></a>

```
"SampleCustomEventBus": {
    "Type": "AWS::Events::EventBus",
    "Properties": {
        "Name": "MyCustomEventBus"
     }
},
"SampleCustomEventBusPolicy": {
    "Type": "AWS::Events::EventBusPolicy",
    "Properties": {
        "EventBusName": {
            "Ref": "SampleCustomEventBus"
        },
        "StatementId": "MyCustomEventBusStatement",
        "Statement": {
            "Effect": "Allow",
            "Principal" : "*",
            "Action": "events:PutEvents",
            "Resource": {
                "Fn::GetAtt": [
                    "SampleCustomEventBus",
                    "Arn"
                ]
            },
            "Condition": {
                "StringEquals": {"aws:PrincipalOrgID": "o-1234567890"}
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-events-eventbuspolicy--examples--Grant_Permission_to_an_Organization_using_a_custom_event_bus--yaml"></a>

```
SampleCustomEventBus:
    Type: AWS::Events::EventBus
    Properties:
        Name: "MyCustomEventBus"

SampleCustomEventBusPolicy:
    Type: AWS::Events::EventBusPolicy
    Properties:
        EventBusName:
            Ref: "SampleCustomEventBus"
        StatementId: "MyCustomEventBusStatement"
        Statement:
            Effect: "Allow"
            Principal: "*"
            Action: "events:PutEvents"
            Resource: !GetAtt "SampleCustomEventBus.Arn"
            Condition:
                StringEquals:
                    "aws:PrincipalOrgID": "o-1234567890"
```
