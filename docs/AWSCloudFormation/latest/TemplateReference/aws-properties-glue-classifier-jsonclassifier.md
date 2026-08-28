---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-classifier-jsonclassifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Classifier JsonClassifier
<a name="aws-properties-glue-classifier-jsonclassifier"></a>

A classifier for `JSON` content.

## Syntax
<a name="aws-properties-glue-classifier-jsonclassifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-classifier-jsonclassifier-syntax.json"></a>

```
{
  "[JsonPath](#cfn-glue-classifier-jsonclassifier-jsonpath)" : {{String}},
  "[Name](#cfn-glue-classifier-jsonclassifier-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-classifier-jsonclassifier-syntax.yaml"></a>

```
  [JsonPath](#cfn-glue-classifier-jsonclassifier-jsonpath): {{String}}
  [Name](#cfn-glue-classifier-jsonclassifier-name): {{String}}
```

## Properties
<a name="aws-properties-glue-classifier-jsonclassifier-properties"></a>

`JsonPath`  <a name="cfn-glue-classifier-jsonclassifier-jsonpath"></a>
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-classifier-jsonclassifier-name"></a>
The name of the classifier.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-glue-classifier-jsonclassifier--seealso"></a>
+ [JsonClassifier Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-JsonClassifier) in the *AWS Glue Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
