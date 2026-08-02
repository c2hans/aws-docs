---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicecatalog-launchnotificationconstraint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::LaunchNotificationConstraint
<a name="aws-resource-servicecatalog-launchnotificationconstraint"></a>

Specifies a notification constraint.

## Syntax
<a name="aws-resource-servicecatalog-launchnotificationconstraint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-servicecatalog-launchnotificationconstraint-syntax.json"></a>

```
{
  "Type" : "AWS::ServiceCatalog::LaunchNotificationConstraint",
  "Properties" : {
      "[AcceptLanguage](#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage)" : {{String}},
      "[Description](#cfn-servicecatalog-launchnotificationconstraint-description)" : {{String}},
      "[NotificationArns](#cfn-servicecatalog-launchnotificationconstraint-notificationarns)" : {{[ String, ... ]}},
      "[PortfolioId](#cfn-servicecatalog-launchnotificationconstraint-portfolioid)" : {{String}},
      "[ProductId](#cfn-servicecatalog-launchnotificationconstraint-productid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-servicecatalog-launchnotificationconstraint-syntax.yaml"></a>

```
Type: AWS::ServiceCatalog::LaunchNotificationConstraint
Properties:
  [AcceptLanguage](#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage): {{String}}
  [Description](#cfn-servicecatalog-launchnotificationconstraint-description): {{String}}
  [NotificationArns](#cfn-servicecatalog-launchnotificationconstraint-notificationarns): {{
    - String}}
  [PortfolioId](#cfn-servicecatalog-launchnotificationconstraint-portfolioid): {{String}}
  [ProductId](#cfn-servicecatalog-launchnotificationconstraint-productid): {{String}}
```

## Properties
<a name="aws-resource-servicecatalog-launchnotificationconstraint-properties"></a>

`AcceptLanguage`  <a name="cfn-servicecatalog-launchnotificationconstraint-acceptlanguage"></a>
The language code.
+ `jp` - Japanese
+ `zh` - Chinese
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-servicecatalog-launchnotificationconstraint-description"></a>
The description of the constraint.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationArns`  <a name="cfn-servicecatalog-launchnotificationconstraint-notificationarns"></a>
The notification ARNs.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortfolioId`  <a name="cfn-servicecatalog-launchnotificationconstraint-portfolioid"></a>
The portfolio identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProductId`  <a name="cfn-servicecatalog-launchnotificationconstraint-productid"></a>
The product identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-servicecatalog-launchnotificationconstraint-return-values"></a>

### Ref
<a name="aws-resource-servicecatalog-launchnotificationconstraint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the identifier of the constraint.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-servicecatalog-launchnotificationconstraint-return-values-fn--getatt"></a>

## See also
<a name="aws-resource-servicecatalog-launchnotificationconstraint--seealso"></a>
+ [CreateConstraint](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CreateConstraint.html) in the *AWS Service Catalog API Reference*
