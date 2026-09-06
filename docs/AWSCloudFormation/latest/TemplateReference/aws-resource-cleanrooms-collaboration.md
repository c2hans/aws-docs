---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-collaboration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration
<a name="aws-resource-cleanrooms-collaboration"></a>

Creates a new collaboration.

## Syntax
<a name="aws-resource-cleanrooms-collaboration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-collaboration-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::Collaboration",
  "Properties" : {
      "[AllowedResultRegions](#cfn-cleanrooms-collaboration-allowedresultregions)" : {{[ String, ... ]}},
      "[AnalyticsEngine](#cfn-cleanrooms-collaboration-analyticsengine)" : {{String}},
      "[AutoApprovedChangeTypes](#cfn-cleanrooms-collaboration-autoapprovedchangetypes)" : {{[ String, ... ]}},
      "[CreatorDisplayName](#cfn-cleanrooms-collaboration-creatordisplayname)" : {{String}},
      "[CreatorMemberAbilities](#cfn-cleanrooms-collaboration-creatormemberabilities)" : {{[ String, ... ]}},
      "[CreatorMLMemberAbilities](#cfn-cleanrooms-collaboration-creatormlmemberabilities)" : {{MLMemberAbilities}},
      "[CreatorPaymentConfiguration](#cfn-cleanrooms-collaboration-creatorpaymentconfiguration)" : {{PaymentConfiguration}},
      "[DataEncryptionMetadata](#cfn-cleanrooms-collaboration-dataencryptionmetadata)" : {{DataEncryptionMetadata}},
      "[Description](#cfn-cleanrooms-collaboration-description)" : {{String}},
      "[IsMetricsEnabled](#cfn-cleanrooms-collaboration-ismetricsenabled)" : {{Boolean}},
      "[JobLogStatus](#cfn-cleanrooms-collaboration-joblogstatus)" : {{String}},
      "[Members](#cfn-cleanrooms-collaboration-members)" : {{[ MemberSpecification, ... ]}},
      "[Name](#cfn-cleanrooms-collaboration-name)" : {{String}},
      "[QueryLogStatus](#cfn-cleanrooms-collaboration-querylogstatus)" : {{String}},
      "[Tags](#cfn-cleanrooms-collaboration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-collaboration-syntax.yaml"></a>

```
Type: AWS::CleanRooms::Collaboration
Properties:
  [AllowedResultRegions](#cfn-cleanrooms-collaboration-allowedresultregions): {{
    - String}}
  [AnalyticsEngine](#cfn-cleanrooms-collaboration-analyticsengine): {{String}}
  [AutoApprovedChangeTypes](#cfn-cleanrooms-collaboration-autoapprovedchangetypes): {{
    - String}}
  [CreatorDisplayName](#cfn-cleanrooms-collaboration-creatordisplayname): {{String}}
  [CreatorMemberAbilities](#cfn-cleanrooms-collaboration-creatormemberabilities): {{
    - String}}
  [CreatorMLMemberAbilities](#cfn-cleanrooms-collaboration-creatormlmemberabilities): {{
    MLMemberAbilities}}
  [CreatorPaymentConfiguration](#cfn-cleanrooms-collaboration-creatorpaymentconfiguration): {{
    PaymentConfiguration}}
  [DataEncryptionMetadata](#cfn-cleanrooms-collaboration-dataencryptionmetadata): {{
    DataEncryptionMetadata}}
  [Description](#cfn-cleanrooms-collaboration-description): {{String}}
  [IsMetricsEnabled](#cfn-cleanrooms-collaboration-ismetricsenabled): {{Boolean}}
  [JobLogStatus](#cfn-cleanrooms-collaboration-joblogstatus): {{String}}
  [Members](#cfn-cleanrooms-collaboration-members): {{
    - MemberSpecification}}
  [Name](#cfn-cleanrooms-collaboration-name): {{String}}
  [QueryLogStatus](#cfn-cleanrooms-collaboration-querylogstatus): {{String}}
  [Tags](#cfn-cleanrooms-collaboration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-collaboration-properties"></a>

`AllowedResultRegions`  <a name="cfn-cleanrooms-collaboration-allowedresultregions"></a>
The AWS Regions where collaboration query results can be stored. Returns the list of Region identifiers that were specified when the collaboration was created. This list is used to enforce regional storage policies and compliance requirements.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AnalyticsEngine`  <a name="cfn-cleanrooms-collaboration-analyticsengine"></a>
 The analytics engine for the collaboration.
After July 16, 2025, the `CLEAN_ROOMS_SQL` parameter will no longer be available.
*Required*: No
*Type*: String
*Allowed values*: `CLEAN_ROOMS_SQL | SPARK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoApprovedChangeTypes`  <a name="cfn-cleanrooms-collaboration-autoapprovedchangetypes"></a>
The types of change requests that are automatically approved for this collaboration.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatorDisplayName`  <a name="cfn-cleanrooms-collaboration-creatordisplayname"></a>
A display name of the collaboration creator.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatorMemberAbilities`  <a name="cfn-cleanrooms-collaboration-creatormemberabilities"></a>
The abilities granted to the collaboration creator.
*Allowed values*`CAN_QUERY` \| `CAN_RECEIVE_RESULTS` \| `CAN_RUN_JOB`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatorMLMemberAbilities`  <a name="cfn-cleanrooms-collaboration-creatormlmemberabilities"></a>
The ML member abilities for a collaboration member.
*Required*: No
*Type*: [MLMemberAbilities](aws-properties-cleanrooms-collaboration-mlmemberabilities.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatorPaymentConfiguration`  <a name="cfn-cleanrooms-collaboration-creatorpaymentconfiguration"></a>
An object representing the collaboration member's payment responsibilities set by the collaboration creator.
*Required*: No
*Type*: [PaymentConfiguration](aws-properties-cleanrooms-collaboration-paymentconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataEncryptionMetadata`  <a name="cfn-cleanrooms-collaboration-dataencryptionmetadata"></a>
The settings for client-side encryption for cryptographic computing.
*Required*: No
*Type*: [DataEncryptionMetadata](aws-properties-cleanrooms-collaboration-dataencryptionmetadata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cleanrooms-collaboration-description"></a>
A description of the collaboration provided by the collaboration owner.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsMetricsEnabled`  <a name="cfn-cleanrooms-collaboration-ismetricsenabled"></a>
An indicator as to whether metrics are enabled for the collaboration.
When `true`, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobLogStatus`  <a name="cfn-cleanrooms-collaboration-joblogstatus"></a>
An indicator as to whether job logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Members`  <a name="cfn-cleanrooms-collaboration-members"></a>
A list of initial members, not including the creator. This list is immutable.
*Required*: No
*Type*: Array of [MemberSpecification](aws-properties-cleanrooms-collaboration-memberspecification.md)
*Minimum*: `0`
*Maximum*: `9`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-collaboration-name"></a>
A human-readable identifier provided by the collaboration owner. Display names are not unique.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryLogStatus`  <a name="cfn-cleanrooms-collaboration-querylogstatus"></a>
An indicator as to whether query logging has been enabled or disabled for the collaboration.
When `ENABLED`, AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanrooms-collaboration-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-collaboration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-collaboration-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-collaboration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `CollaborationIdentifier`, such as `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. For example:

 `{ "Ref": "MyCollaboration" }`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-collaboration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-collaboration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified collaboration.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
Returns the unique identifier of the specified collaboration.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

## Examples
<a name="aws-resource-cleanrooms-collaboration--examples"></a>

### Create a collaboration
<a name="aws-resource-cleanrooms-collaboration--examples--Create_a_collaboration"></a>

The following example creates a collaboration with the collaboration creator.

#### JSON
<a name="aws-resource-cleanrooms-collaboration--examples--Create_a_collaboration--json"></a>

```
"ExampleCollaboration": {
  {
    "Type": "AWS::CleanRooms::Collaboration",
    "Properties": {
      "Name": "Example Collaboration",
      "Description": "Example AWS Clean Rooms collaboration",
      "CreatorDisplayName": "Member 1",
      "CreatorMemberAbilities": ["CAN_QUERY", "CAN_RECEIVE_RESULTS"],
      "Members": [
        {
          "AccountId": "111122223333",
          "DisplayName": "Member 2",
          "MemberAbilities": []
        },
        {
          "AccountId": "444455556666",
          "DisplayName": "Member 3",
          "MemberAbilities": []
        }
      ],
      "QueryLogStatus": "ENABLED"
    }
  }
}
```

#### YAML
<a name="aws-resource-cleanrooms-collaboration--examples--Create_a_collaboration--yaml"></a>

```
ExampleCollaboration:
  Type: AWS::CleanRooms::Collaboration
  Properties:
    Name: Example Collaboration
    Description: Example AWS Clean Rooms collaboration
    CreatorDisplayName: Member 1
    CreatorMemberAbilities:
      - CAN_QUERY
      - CAN_RECEIVE_RESULTS
    Members:
      - AccountId: 111122223333
        DisplayName: Member 2
        MemberAbilities: []
      - AccountId: 444455556666
        DisplayName: Member 3
        MemberAbilities: []
    QueryLogStatus: ENABLED
```
