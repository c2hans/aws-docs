---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-domainunit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DomainUnit
<a name="aws-resource-datazone-domainunit"></a>

The summary of the domain unit.

## Syntax
<a name="aws-resource-datazone-domainunit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-domainunit-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::DomainUnit",
  "Properties" : {
      "[Description](#cfn-datazone-domainunit-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-domainunit-domainidentifier)" : {{String}},
      "[Name](#cfn-datazone-domainunit-name)" : {{String}},
      "[ParentDomainUnitIdentifier](#cfn-datazone-domainunit-parentdomainunitidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-domainunit-syntax.yaml"></a>

```
Type: AWS::DataZone::DomainUnit
Properties:
  [Description](#cfn-datazone-domainunit-description): {{String}}
  [DomainIdentifier](#cfn-datazone-domainunit-domainidentifier): {{String}}
  [Name](#cfn-datazone-domainunit-name): {{String}}
  [ParentDomainUnitIdentifier](#cfn-datazone-domainunit-parentdomainunitidentifier): {{String}}
```

## Properties
<a name="aws-resource-datazone-domainunit-properties"></a>

`Description`  <a name="cfn-datazone-domainunit-description"></a>
The description of the domain unit.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-domainunit-domainidentifier"></a>
The ID of the domain where you want to crate a domain unit.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-domainunit-name"></a>
The name of the domain unit.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentDomainUnitIdentifier`  <a name="cfn-datazone-domainunit-parentdomainunitidentifier"></a>
The ID of the parent domain unit.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-domainunit-return-values"></a>

### Ref
<a name="aws-resource-datazone-domainunit-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `DomainUnitId`, which uniquely identifies a domain unit. For example: { `"Ref": "MyDomainUnit"` } for the resource with the logical ID MyDomainUnit, Ref returns `DomainId|DomainUnitId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-domainunit-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-domainunit-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time stamp at which the domain unit was created.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The ID of the domain in which the domain unit lives.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the domain unit.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The identifier of the domain unit that you want to get.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp at which the domain unit was last updated.

`ParentDomainUnitId`  <a name="ParentDomainUnitId-fn::getatt"></a>
The ID of the parent domain unit.
