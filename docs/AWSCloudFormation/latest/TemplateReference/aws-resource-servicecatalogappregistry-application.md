---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalogappregistry-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalogAppRegistry::Application
<a name="aws-resource-servicecatalogappregistry-application"></a>

Represents a AWS Service Catalog AppRegistry application that is the top-level node in a hierarchy of related cloud resource abstractions.

## Syntax
<a name="aws-resource-servicecatalogappregistry-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalogappregistry-application-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalogAppRegistry::Application",
  "Properties" : {
      "[Description](#cfn-servicecatalogappregistry-application-description)" : {{String}},
      "[Name](#cfn-servicecatalogappregistry-application-name)" : {{String}},
      "[Tags](#cfn-servicecatalogappregistry-application-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalogappregistry-application-syntax.yaml"></a>

```
Type: AWS::ServiceCatalogAppRegistry::Application
Properties:
  [Description](#cfn-servicecatalogappregistry-application-description): {{String}}
  [Name](#cfn-servicecatalogappregistry-application-name): {{String}}
  [Tags](#cfn-servicecatalogappregistry-application-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-servicecatalogappregistry-application-properties"></a>

`Description`  <a name="cfn-servicecatalogappregistry-application-description"></a>
The description of the application.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-servicecatalogappregistry-application-name"></a>
The name of the application. The name must be unique in the region in which you are creating the application.
*Required*: Yes
*Type*: String
*Pattern*: `\w+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-servicecatalogappregistry-application-tags"></a>
Key-value pairs you can use to associate with the application.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z+-=._:/]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-servicecatalogappregistry-application-return-values"></a>

### Ref
<a name="aws-resource-servicecatalogappregistry-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application Id.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicecatalogappregistry-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-servicecatalogappregistry-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationName`  <a name="ApplicationName-fn::getatt"></a>
The name of the application. The name must be unique in the region in which you are creating the application.

`ApplicationTagKey`  <a name="ApplicationTagKey-fn::getatt"></a>
 The key of the AWS application tag, which is `awsApplication`. Applications created before 11/13/2023 or applications without the `AppTag` linked resource group return no value.

`ApplicationTagValue`  <a name="ApplicationTagValue-fn::getatt"></a>
 The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11/13/2023 or applications without the `AppTag` linked resource group return no value.

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon resource name (ARN) that specifies the application across services.

`Id`  <a name="Id-fn::getatt"></a>
 The identifier of the application.
