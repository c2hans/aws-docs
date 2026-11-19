---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-preevaluationfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule PreEvaluationFilter

A single pre-evaluation filter condition. Specifies a resource type, filter type, key, value, and operator to match against a resource attribute.

## Syntax
<a name="aws-properties-connect-rule-preevaluationfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-preevaluationfilter-syntax.json"></a>

```
{
  "[FilterKey](#cfn-connect-rule-preevaluationfilter-filterkey)" : {{String}},
  "[FilterType](#cfn-connect-rule-preevaluationfilter-filtertype)" : {{String}},
  "[FilterValue](#cfn-connect-rule-preevaluationfilter-filtervalue)" : {{String}},
  "[Operator](#cfn-connect-rule-preevaluationfilter-operator)" : {{String}},
  "[ResourceType](#cfn-connect-rule-preevaluationfilter-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-preevaluationfilter-syntax.yaml"></a>

```
  [FilterKey](#cfn-connect-rule-preevaluationfilter-filterkey): {{String}}
  [FilterType](#cfn-connect-rule-preevaluationfilter-filtertype): {{String}}
  [FilterValue](#cfn-connect-rule-preevaluationfilter-filtervalue): {{String}}
  [Operator](#cfn-connect-rule-preevaluationfilter-operator): {{String}}
  [ResourceType](#cfn-connect-rule-preevaluationfilter-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-preevaluationfilter-properties"></a>

`FilterKey`  <a name="cfn-connect-rule-preevaluationfilter-filterkey"></a>
The key of the attribute to filter on. For tag filters, this is the tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterType`  <a name="cfn-connect-rule-preevaluationfilter-filtertype"></a>
The type of filter to apply. Valid values: `TAG`.
*Required*: Yes
*Type*: String
*Allowed values*: `TAG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterValue`  <a name="cfn-connect-rule-preevaluationfilter-filtervalue"></a>
The value to match against. For tag filters, this is the tag value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-connect-rule-preevaluationfilter-operator"></a>
The comparison operator for the filter condition. Valid values: `EQUALS`.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-connect-rule-preevaluationfilter-resourcetype"></a>
The type of resource to filter on. Valid values:
+ `CONTACT` - Filter on attributes of the contact, such as tags assigned to the contact.
+ `CONTACT_EVALUATION` - Filter on attributes of the contact evaluation, such as tags assigned to the contact evaluation, for rules triggered on the `OnContactEvaluationSubmit` event source.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTACT | CONTACT_EVALUATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
