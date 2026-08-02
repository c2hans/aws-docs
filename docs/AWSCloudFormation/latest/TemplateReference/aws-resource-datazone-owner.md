---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-owner.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Owner
<a name="aws-resource-datazone-owner"></a>

The owner that you want to add to the entity.

## Syntax
<a name="aws-resource-datazone-owner-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-owner-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::Owner",
  "Properties" : {
      "[DomainIdentifier](#cfn-datazone-owner-domainidentifier)" : {{String}},
      "[EntityIdentifier](#cfn-datazone-owner-entityidentifier)" : {{String}},
      "[EntityType](#cfn-datazone-owner-entitytype)" : {{String}},
      "[Owner](#cfn-datazone-owner-owner)" : {{OwnerProperties}}
    }
}
```

### YAML
<a name="aws-resource-datazone-owner-syntax.yaml"></a>

```
Type: AWS::DataZone::Owner
Properties:
  [DomainIdentifier](#cfn-datazone-owner-domainidentifier): {{String}}
  [EntityIdentifier](#cfn-datazone-owner-entityidentifier): {{String}}
  [EntityType](#cfn-datazone-owner-entitytype): {{String}}
  [Owner](#cfn-datazone-owner-owner): {{
    OwnerProperties}}
```

## Properties
<a name="aws-resource-datazone-owner-properties"></a>

`DomainIdentifier`  <a name="cfn-datazone-owner-domainidentifier"></a>
The ID of the domain in which you want to add the entity owner.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityIdentifier`  <a name="cfn-datazone-owner-entityidentifier"></a>
The ID of the entity to which you want to add an owner.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityType`  <a name="cfn-datazone-owner-entitytype"></a>
The type of an entity.
*Required*: Yes
*Type*: String
*Allowed values*: `DOMAIN_UNIT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Owner`  <a name="cfn-datazone-owner-owner"></a>
The owner that you want to add to the entity.
*Required*: Yes
*Type*: [OwnerProperties](aws-properties-datazone-owner-ownerproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-owner-return-values"></a>

### Ref
<a name="aws-resource-datazone-owner-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId`, `EntityType`, `EntityId`, `OwnerType`, and `OwnerId`, which uniquely identifies an owner. For example: `{ "Ref": "MyOwner" }` for the resource with the logical ID MyOwner, Ref returns `DomainId|EntityType|EntityId|OwnerType|OwnerId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-owner-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-owner-return-values-fn--getatt-fn--getatt"></a>

`OwnerIdentifier`  <a name="OwnerIdentifier-fn::getatt"></a>
The ID of the entity to which you want to add an owner.

`OwnerType`  <a name="OwnerType-fn::getatt"></a>
The owner that you want to add to the entity.
