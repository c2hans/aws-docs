---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehubv2-system.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::System
<a name="aws-resource-resiliencehubv2-system"></a>

Represents a system in Resilience Hub. A system is a logical grouping of services.

## Syntax
<a name="aws-resource-resiliencehubv2-system-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehubv2-system-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHubV2::System",
  "Properties" : {
      "[Description](#cfn-resiliencehubv2-system-description)" : {{String}},
      "[KmsKeyId](#cfn-resiliencehubv2-system-kmskeyid)" : {{String}},
      "[Name](#cfn-resiliencehubv2-system-name)" : {{String}},
      "[SharingEnabled](#cfn-resiliencehubv2-system-sharingenabled)" : {{Boolean}},
      "[Tags](#cfn-resiliencehubv2-system-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehubv2-system-syntax.yaml"></a>

```
Type: AWS::ResilienceHubV2::System
Properties:
  [Description](#cfn-resiliencehubv2-system-description): {{String}}
  [KmsKeyId](#cfn-resiliencehubv2-system-kmskeyid): {{String}}
  [Name](#cfn-resiliencehubv2-system-name): {{String}}
  [SharingEnabled](#cfn-resiliencehubv2-system-sharingenabled): {{Boolean}}
  [Tags](#cfn-resiliencehubv2-system-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-resiliencehubv2-system-properties"></a>

`Description`  <a name="cfn-resiliencehubv2-system-description"></a>
The description of the event.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-resiliencehubv2-system-kmskeyid"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
*Required*: No
*Type*: String
*Pattern*: `^((arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+))$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-resiliencehubv2-system-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SharingEnabled`  <a name="cfn-resiliencehubv2-system-sharingenabled"></a>
Indicates whether cross-account sharing is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-resiliencehubv2-system-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-resiliencehubv2-system-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-resiliencehubv2-system-return-values"></a>

### Ref
<a name="aws-resource-resiliencehubv2-system-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehubv2-system-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehubv2-system-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the system was created.

`SystemArn`  <a name="SystemArn-fn::getatt"></a>
ARN identifier.

`SystemId`  <a name="SystemId-fn::getatt"></a>
The identifier of the disassociated system.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the system was last updated.
