---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalogappregistry-attributegroupassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation"></a>

 Associates an attribute group with an application to augment the application's metadata with the group's attributes. This feature enables applications to be described with user-defined details that are machine-readable, such as third-party integrations.

## Syntax
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation",
  "Properties" : {
      "[Application](#cfn-servicecatalogappregistry-attributegroupassociation-application)" : {{String}},
      "[AttributeGroup](#cfn-servicecatalogappregistry-attributegroupassociation-attributegroup)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-syntax.yaml"></a>

```
Type: AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation
Properties:
  [Application](#cfn-servicecatalogappregistry-attributegroupassociation-application): {{String}}
  [AttributeGroup](#cfn-servicecatalogappregistry-attributegroupassociation-attributegroup): {{String}}
```

## Properties
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-properties"></a>

`Application`  <a name="cfn-servicecatalogappregistry-attributegroupassociation-application"></a>
 The name or ID of the application.
*Required*: Yes
*Type*: String
*Pattern*: `\w+|[a-z0-9]{12}`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttributeGroup`  <a name="cfn-servicecatalogappregistry-attributegroupassociation-attributegroup"></a>
 The name or ID of the attribute group which holds the attributes that describe the application.
*Required*: Yes
*Type*: String
*Pattern*: `\w+|[a-z0-9]{12}`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-return-values"></a>

### Ref
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application Id.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-servicecatalogappregistry-attributegroupassociation-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
 The Amazon resource name (ARN) of the application that was augmented with attributes.

`AttributeGroupArn`  <a name="AttributeGroupArn-fn::getatt"></a>
 The Amazon resource name (ARN) of the attribute group which contains the application's new attributes.
