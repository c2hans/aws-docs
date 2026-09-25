---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eventsv2-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::ResourcePolicy
<a name="aws-resource-eventsv2-resourcepolicy"></a>

Resource type definition for `AWS::EventsV2::ResourcePolicy`, the resource policy of an Amazon EventBridge event bus. This manages only the resource policy named "default", which the bus owner writes. It does not manage the policy named "AWS\_RAM", which AWS Resource Access Manager owns on behalf of the bus owner. If the bus already has a default policy, creating this resource fails. Deleting this resource removes all permissions granted by it. An explicit Deny in this policy takes precedence over an Allow in the "AWS\_RAM" policy, so deleting this resource can widen access. Set DeletionPolicy: Retain if the policy carries a Deny that you rely on. Required permissions: events:PutResourcePolicy, events:GetResourcePolicy, and events:DeleteResourcePolicy. Listing resources of this type also requires events:ListEventBuses and events:ListResourcePolicies.

## Syntax
<a name="aws-resource-eventsv2-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eventsv2-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::EventsV2::ResourcePolicy",
  "Properties" : {
      "[EventBusArn](#cfn-eventsv2-resourcepolicy-eventbusarn)" : {{String}},
      "[PolicyDocument](#cfn-eventsv2-resourcepolicy-policydocument)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-eventsv2-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::EventsV2::ResourcePolicy
Properties:
  [EventBusArn](#cfn-eventsv2-resourcepolicy-eventbusarn): {{String}}
  [PolicyDocument](#cfn-eventsv2-resourcepolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-resource-eventsv2-resourcepolicy-properties"></a>

`EventBusArn`  <a name="cfn-eventsv2-resourcepolicy-eventbusarn"></a>
The Amazon Resource Name (ARN) of the event bus whose resource policy this is. The bus must already exist. This resource does not create it.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-eventsv2-resourcepolicy-policydocument"></a>
The resource policy document, as a JSON object. The document can be up to 20 KB. This quota is adjustable. An empty object is not a valid policy. To remove the policy, delete this resource. The principals in the document must exist and be visible to the service when the policy is written. When you create a new IAM role or user, that principal might not be immediately visible to the service. You might need to enforce a delay before you include it in the document. For more information, see "Changes that I make are not always immediately visible" in the IAM User Guide. Declare Version. Write AWS account and role principals as ARNs rather than as account IDs. Write a single Action, Resource, or principal value as a scalar rather than as a one-element list. The service returns these forms as you wrote them. It normalizes other forms, and a normalized value can appear as drift. A stack update replaces the whole policy with this document, including any change made outside CloudFormation. For more information about event bus resource policies, see the Amazon EventBridge User Guide.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-eventsv2-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-eventsv2-resourcepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the event bus that this resource policy applies to, such as `arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eventsv2-resourcepolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eventsv2-resourcepolicy-return-values-fn--getatt-fn--getatt"></a>

`RevisionId`  <a name="RevisionId-fn::getatt"></a>
The revision identifier that the service assigned to the stored policy. The identifier changes on every successful write.

## Examples
<a name="aws-resource-eventsv2-resourcepolicy--examples"></a>

The following examples manage the default resource policy of an event bus.

**Topics**
+ [Grant an organization permission to send events](#aws-resource-eventsv2-resourcepolicy--examples--Grant_an_organization_permission_to_send_events)
+ [Grant a single account permission to send events](#aws-resource-eventsv2-resourcepolicy--examples--Grant_a_single_account_permission_to_send_events)

### Grant an organization permission to send events
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_an_organization_permission_to_send_events"></a>

The following example grants accounts in an organization permission to send events to the event bus.

#### JSON
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_an_organization_permission_to_send_events--json"></a>

```
{
  "Resources": {
    "OrdersBusPolicy": {
      "Type": "AWS::EventsV2::ResourcePolicy",
      "Properties": {
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "AllowOrganizationToPutEvents",
              "Effect": "Allow",
              "Principal": "*",
              "Action": "events:PutEvents",
              "Resource": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
              "Condition": {
                "StringEquals": {
                  "aws:PrincipalOrgID": "o-a1b2c3d4e5"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_an_organization_permission_to_send_events--yaml"></a>

```
Resources:
  OrdersBusPolicy:
    Type: AWS::EventsV2::ResourcePolicy
    Properties:
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Sid: AllowOrganizationToPutEvents
            Effect: Allow
            Principal: '*'
            Action: events:PutEvents
            Resource: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
            Condition:
              StringEquals:
                aws:PrincipalOrgID: o-a1b2c3d4e5
```

### Grant a single account permission to send events
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_a_single_account_permission_to_send_events"></a>

The following example grants one account permission to send events to the event bus by matching the source account in a condition.

#### JSON
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_a_single_account_permission_to_send_events--json"></a>

```
{
  "Resources": {
    "OrdersBusPolicy": {
      "Type": "AWS::EventsV2::ResourcePolicy",
      "Properties": {
        "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "AllowSourceAccountToPutEvents",
              "Effect": "Allow",
              "Principal": "*",
              "Action": "events:PutEvents",
              "Resource": "arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m",
              "Condition": {
                "StringEquals": {
                  "aws:SourceAccount": "210987654321"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-eventsv2-resourcepolicy--examples--Grant_a_single_account_permission_to_send_events--yaml"></a>

```
Resources:
  OrdersBusPolicy:
    Type: AWS::EventsV2::ResourcePolicy
    Properties:
      EventBusArn: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Sid: AllowSourceAccountToPutEvents
            Effect: Allow
            Principal: '*'
            Action: events:PutEvents
            Resource: arn:aws:events:us-east-1:123456789012:event-busv2/orders-event-bus/a1b2c3d4e5f6g7h8i9j0k1l2m
            Condition:
              StringEquals:
                aws:SourceAccount: '210987654321'
```
