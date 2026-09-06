---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-membership.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership
<a name="aws-resource-cleanrooms-membership"></a>

Creates a membership for a specific collaboration identifier and joins the collaboration.

## Syntax
<a name="aws-resource-cleanrooms-membership-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-membership-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::Membership",
  "Properties" : {
      "[CollaborationIdentifier](#cfn-cleanrooms-membership-collaborationidentifier)" : {{String}},
      "[DefaultJobResultConfiguration](#cfn-cleanrooms-membership-defaultjobresultconfiguration)" : {{MembershipProtectedJobResultConfiguration}},
      "[DefaultResultConfiguration](#cfn-cleanrooms-membership-defaultresultconfiguration)" : {{MembershipProtectedQueryResultConfiguration}},
      "[IsMetricsEnabled](#cfn-cleanrooms-membership-ismetricsenabled)" : {{Boolean}},
      "[JobLogStatus](#cfn-cleanrooms-membership-joblogstatus)" : {{String}},
      "[PaymentConfiguration](#cfn-cleanrooms-membership-paymentconfiguration)" : {{MembershipPaymentConfiguration}},
      "[QueryLogStatus](#cfn-cleanrooms-membership-querylogstatus)" : {{String}},
      "[Tags](#cfn-cleanrooms-membership-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-membership-syntax.yaml"></a>

```
Type: AWS::CleanRooms::Membership
Properties:
  [CollaborationIdentifier](#cfn-cleanrooms-membership-collaborationidentifier): {{String}}
  [DefaultJobResultConfiguration](#cfn-cleanrooms-membership-defaultjobresultconfiguration): {{
    MembershipProtectedJobResultConfiguration}}
  [DefaultResultConfiguration](#cfn-cleanrooms-membership-defaultresultconfiguration): {{
    MembershipProtectedQueryResultConfiguration}}
  [IsMetricsEnabled](#cfn-cleanrooms-membership-ismetricsenabled): {{Boolean}}
  [JobLogStatus](#cfn-cleanrooms-membership-joblogstatus): {{String}}
  [PaymentConfiguration](#cfn-cleanrooms-membership-paymentconfiguration): {{
    MembershipPaymentConfiguration}}
  [QueryLogStatus](#cfn-cleanrooms-membership-querylogstatus): {{String}}
  [Tags](#cfn-cleanrooms-membership-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-membership-properties"></a>

`CollaborationIdentifier`  <a name="cfn-cleanrooms-membership-collaborationidentifier"></a>
The unique ID for the associated collaboration.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultJobResultConfiguration`  <a name="cfn-cleanrooms-membership-defaultjobresultconfiguration"></a>
 The default job result configuration for the membership.
*Required*: No
*Type*: [MembershipProtectedJobResultConfiguration](aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResultConfiguration`  <a name="cfn-cleanrooms-membership-defaultresultconfiguration"></a>
The default protected query result configuration as specified by the member who can receive results.
*Required*: No
*Type*: [MembershipProtectedQueryResultConfiguration](aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsMetricsEnabled`  <a name="cfn-cleanrooms-membership-ismetricsenabled"></a>
An indicator as to whether Amazon CloudWatch metrics are enabled for the membership.
When `true`, metrics about query execution are collected in Amazon CloudWatch.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobLogStatus`  <a name="cfn-cleanrooms-membership-joblogstatus"></a>
An indicator as to whether job logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaymentConfiguration`  <a name="cfn-cleanrooms-membership-paymentconfiguration"></a>
The payment responsibilities accepted by the collaboration member.
*Required*: No
*Type*: [MembershipPaymentConfiguration](aws-properties-cleanrooms-membership-membershippaymentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryLogStatus`  <a name="cfn-cleanrooms-membership-querylogstatus"></a>
An indicator as to whether query logging has been enabled or disabled for the membership.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cleanrooms-membership-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-membership-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-membership-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-membership-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `MembershipId`, such as `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. For example:

 `{ "Ref": "MyMembership" }`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-membership-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-membership-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified membership.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified collaboration.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

`CollaborationCreatorAccountId`  <a name="CollaborationCreatorAccountId-fn::getatt"></a>
Returns the unique identifier of the specified collaboration creator account.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

`MembershipIdentifier`  <a name="MembershipIdentifier-fn::getatt"></a>
Returns the unique identifier of the specified membership.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`

## Remarks
<a name="aws-resource-cleanrooms-membership--remarks"></a>

If you are a collaboration owner, ensure that you add `"DeletionPolicy: Retain"` and `"UpdateReplacePolicy: Retain"` to the `Membership` resource in your CloudFormation template.

If your `Membership` resource depends on the collaboration explicitly or implicitly by using a `"Ref"` on the `Collaboration` (`CollaborationIdentifier: !Ref Collaboration`), CloudFormation tries to delete the `Membership` resource before the `Collaboration` resource. However, this attempt will fail because collaboration owners must delete the collaboration before deleting their membership to the collaboration.

For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) and [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html).

## Examples
<a name="aws-resource-cleanrooms-membership--examples"></a>

**Topics**
+ [Membership for a collaboration creator](#aws-resource-cleanrooms-membership--examples--Membership_for_a_collaboration_creator)
+ [Membership for a non-collaboration creator](#aws-resource-cleanrooms-membership--examples--Membership_for_a_non-collaboration_creator)

### Membership for a collaboration creator
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_collaboration_creator"></a>

The following an example of a membership for a collaboration creator. See the Remarks section for notes on the use of the deletion and update replacement policies.

#### JSON
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_collaboration_creator--json"></a>

```
"CollaborationCreatorMembership": {
  "Type" : "AWS::CleanRooms::Membership",
  "DeletionPolicy": "Retain",
  "UpdateReplacePolicy": "Retain",
  "Properties" : {
      "CollaborationIdentifier" : "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "QueryLogStatus" : "ENABLED",
    }
  }
```

#### YAML
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_collaboration_creator--yaml"></a>

```
CollaborationCreatorMembership:
  Type: AWS::CleanRooms::Membership
  DeletionPolicy: Retain
  UpdateReplacePolicy: Retain
  Properties:
    CollaborationIdentifier: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
    QueryLogStatus: ENABLED
```

### Membership for a non-collaboration creator
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_non-collaboration_creator"></a>

The following is an example of a membership for a non-collaboration creator.

#### JSON
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_non-collaboration_creator--json"></a>

```
"ExampleMembership": {
  "Type" : "AWS::CleanRooms::Membership",
  "Properties" : {
      "CollaborationIdentifier" : "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "QueryLogStatus" : "ENABLED",
    }
  }
```

#### YAML
<a name="aws-resource-cleanrooms-membership--examples--Membership_for_a_non-collaboration_creator--yaml"></a>

```
ExampleMembership:
  Type: AWS::CleanRooms::Membership
  Properties:
    CollaborationIdentifier: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
    QueryLogStatus: ENABLED
```
