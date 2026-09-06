---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-subscriptiontarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::SubscriptionTarget
<a name="aws-resource-datazone-subscriptiontarget"></a>

The `AWS::DataZone::SubscriptionTarget`resource specifies an Amazon DataZone subscription target. Subscription targets enable you to access the data to which you have subscribed in your projects. A subscription target specifies the location (for example, a database or a schema) and the required permissions (for example, an IAM role) that Amazon DataZone can use to establish a connection with the source data and to create the necessary grants so that members of the Amazon DataZone project can start querying the data to which they have subscribed.

## Syntax
<a name="aws-resource-datazone-subscriptiontarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-subscriptiontarget-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::SubscriptionTarget",
  "Properties" : {
      "[ApplicableAssetTypes](#cfn-datazone-subscriptiontarget-applicableassettypes)" : {{[ String, ... ]}},
      "[AuthorizedPrincipals](#cfn-datazone-subscriptiontarget-authorizedprincipals)" : {{[ String, ... ]}},
      "[DomainIdentifier](#cfn-datazone-subscriptiontarget-domainidentifier)" : {{String}},
      "[EnvironmentIdentifier](#cfn-datazone-subscriptiontarget-environmentidentifier)" : {{String}},
      "[ManageAccessRole](#cfn-datazone-subscriptiontarget-manageaccessrole)" : {{String}},
      "[Name](#cfn-datazone-subscriptiontarget-name)" : {{String}},
      "[Provider](#cfn-datazone-subscriptiontarget-provider)" : {{String}},
      "[SubscriptionTargetConfig](#cfn-datazone-subscriptiontarget-subscriptiontargetconfig)" : {{[ SubscriptionTargetForm, ... ]}},
      "[Type](#cfn-datazone-subscriptiontarget-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-subscriptiontarget-syntax.yaml"></a>

```
Type: AWS::DataZone::SubscriptionTarget
Properties:
  [ApplicableAssetTypes](#cfn-datazone-subscriptiontarget-applicableassettypes): {{
    - String}}
  [AuthorizedPrincipals](#cfn-datazone-subscriptiontarget-authorizedprincipals): {{
    - String}}
  [DomainIdentifier](#cfn-datazone-subscriptiontarget-domainidentifier): {{String}}
  [EnvironmentIdentifier](#cfn-datazone-subscriptiontarget-environmentidentifier): {{String}}
  [ManageAccessRole](#cfn-datazone-subscriptiontarget-manageaccessrole): {{String}}
  [Name](#cfn-datazone-subscriptiontarget-name): {{String}}
  [Provider](#cfn-datazone-subscriptiontarget-provider): {{String}}
  [SubscriptionTargetConfig](#cfn-datazone-subscriptiontarget-subscriptiontargetconfig): {{
    - SubscriptionTargetForm}}
  [Type](#cfn-datazone-subscriptiontarget-type): {{String}}
```

## Properties
<a name="aws-resource-datazone-subscriptiontarget-properties"></a>

`ApplicableAssetTypes`  <a name="cfn-datazone-subscriptiontarget-applicableassettypes"></a>
The asset types included in the subscription target.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizedPrincipals`  <a name="cfn-datazone-subscriptiontarget-authorizedprincipals"></a>
The authorized principals included in the subscription target.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-subscriptiontarget-domainidentifier"></a>
The ID of the Amazon DataZone domain in which subscription target is created.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentIdentifier`  <a name="cfn-datazone-subscriptiontarget-environmentidentifier"></a>
The ID of the environment in which subscription target is created.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManageAccessRole`  <a name="cfn-datazone-subscriptiontarget-manageaccessrole"></a>
The manage access role that is used to create the subscription target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-datazone-subscriptiontarget-name"></a>
The name of the subscription target.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Provider`  <a name="cfn-datazone-subscriptiontarget-provider"></a>
The provider of the subscription target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubscriptionTargetConfig`  <a name="cfn-datazone-subscriptiontarget-subscriptiontargetconfig"></a>
The configuration of the subscription target.
*Required*: Yes
*Type*: Array of [SubscriptionTargetForm](aws-properties-datazone-subscriptiontarget-subscriptiontargetform.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-datazone-subscriptiontarget-type"></a>
The type of the subscription target.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-subscriptiontarget-return-values"></a>

### Ref
<a name="aws-resource-datazone-subscriptiontarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId`, `EnvironmentId` and the `SubscriptionTargetId` that uniquely identify the subscription target. For example: `{ "Ref": "MySubscriptionTarget" }` for the resource with the logical ID `MySubscriptionTarget`, `Ref` returns `DomainId|EnvironmentId|SubscriptionTargetId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-subscriptiontarget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-subscriptiontarget-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the subscription target was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The Amazon DataZone user who created the subscription target.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which the subscription target exists.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The identifier of the environment of the subscription target.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the subscription target.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The identifier of the project specified in the subscription target.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the subscription target was updated.

`UpdatedBy`  <a name="UpdatedBy-fn::getatt"></a>
The Amazon DataZone user who updated the subscription target.
