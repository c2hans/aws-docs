---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-customlineitem-presentationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::CustomLineItem PresentationDetails
<a name="aws-properties-billingconductor-customlineitem-presentationdetails"></a>

An object that defines how custom line item charges are presented in the bill, containing specifications for service presentation.

## Syntax
<a name="aws-properties-billingconductor-customlineitem-presentationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-customlineitem-presentationdetails-syntax.json"></a>

```
{
  "[Service](#cfn-billingconductor-customlineitem-presentationdetails-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-billingconductor-customlineitem-presentationdetails-syntax.yaml"></a>

```
  [Service](#cfn-billingconductor-customlineitem-presentationdetails-service): {{String}}
```

## Properties
<a name="aws-properties-billingconductor-customlineitem-presentationdetails-properties"></a>

`Service`  <a name="cfn-billingconductor-customlineitem-presentationdetails-service"></a>
The service under which the custom line item charges will be presented. Must be a string between 1 and 128 characters matching the pattern `^[a-zA-Z0-9]+$`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
