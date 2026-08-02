---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-formtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::FormType
<a name="aws-resource-datazone-formtype"></a>

The details of the metadata form type.

## Syntax
<a name="aws-resource-datazone-formtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-formtype-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::FormType",
  "Properties" : {
      "[Description](#cfn-datazone-formtype-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-formtype-domainidentifier)" : {{String}},
      "[Model](#cfn-datazone-formtype-model)" : {{Model}},
      "[Name](#cfn-datazone-formtype-name)" : {{String}},
      "[OwningProjectIdentifier](#cfn-datazone-formtype-owningprojectidentifier)" : {{String}},
      "[Status](#cfn-datazone-formtype-status)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-formtype-syntax.yaml"></a>

```
Type: AWS::DataZone::FormType
Properties:
  [Description](#cfn-datazone-formtype-description): {{String}}
  [DomainIdentifier](#cfn-datazone-formtype-domainidentifier): {{String}}
  [Model](#cfn-datazone-formtype-model): {{
    Model}}
  [Name](#cfn-datazone-formtype-name): {{String}}
  [OwningProjectIdentifier](#cfn-datazone-formtype-owningprojectidentifier): {{String}}
  [Status](#cfn-datazone-formtype-status): {{String}}
```

## Properties
<a name="aws-resource-datazone-formtype-properties"></a>

`Description`  <a name="cfn-datazone-formtype-description"></a>
The description of the metadata form type.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-formtype-domainidentifier"></a>
The identifier of the Amazon DataZone domain in which the form type exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Model`  <a name="cfn-datazone-formtype-model"></a>
The model of the form type.
*Required*: Yes
*Type*: [Model](aws-properties-datazone-formtype-model.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Name`  <a name="cfn-datazone-formtype-name"></a>
The name of the form type.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OwningProjectIdentifier`  <a name="cfn-datazone-formtype-owningprojectidentifier"></a>
The identifier of the project that owns the form type.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Status`  <a name="cfn-datazone-formtype-status"></a>
The status of the form type.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-datazone-formtype-return-values"></a>

### Ref
<a name="aws-resource-datazone-formtype-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainIdentifier` and `FormTypeIdentifier`, which uniquely identifies a form type. For example: `{"Ref": "MyFormType" }` for the resource with the logical ID `MyFormType`, `Ref` returns `DomainIdentifier|FormTypeIdentifier`.

### Fn::GetAtt
<a name="aws-resource-datazone-formtype-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-formtype-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the metadata form type was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The Amazon DataZone user who created teh metadata form type.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which the form type exists.

`FormTypeIdentifier`  <a name="FormTypeIdentifier-fn::getatt"></a>
The ID of the metadata form type.

`OwningProjectId`  <a name="OwningProjectId-fn::getatt"></a>
The identifier of the project that owns the form type.

`Revision`  <a name="Revision-fn::getatt"></a>
The revision of the form type.
