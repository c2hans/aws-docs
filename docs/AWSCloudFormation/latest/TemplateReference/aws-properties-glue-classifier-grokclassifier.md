---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-classifier-grokclassifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Classifier GrokClassifier
<a name="aws-properties-glue-classifier-grokclassifier"></a>

A classifier that uses `grok` patterns.

## Syntax
<a name="aws-properties-glue-classifier-grokclassifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-classifier-grokclassifier-syntax.json"></a>

```
{
  "[Classification](#cfn-glue-classifier-grokclassifier-classification)" : {{String}},
  "[CustomPatterns](#cfn-glue-classifier-grokclassifier-custompatterns)" : {{String}},
  "[GrokPattern](#cfn-glue-classifier-grokclassifier-grokpattern)" : {{String}},
  "[Name](#cfn-glue-classifier-grokclassifier-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-classifier-grokclassifier-syntax.yaml"></a>

```
  [Classification](#cfn-glue-classifier-grokclassifier-classification): {{String}}
  [CustomPatterns](#cfn-glue-classifier-grokclassifier-custompatterns): {{String}}
  [GrokPattern](#cfn-glue-classifier-grokclassifier-grokpattern): {{String}}
  [Name](#cfn-glue-classifier-grokclassifier-name): {{String}}
```

## Properties
<a name="aws-properties-glue-classifier-grokclassifier-properties"></a>

`Classification`  <a name="cfn-glue-classifier-grokclassifier-classification"></a>
An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPatterns`  <a name="cfn-glue-classifier-grokclassifier-custompatterns"></a>
Optional custom grok patterns defined by this classifier. For more information, see custom patterns in [Writing Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html).
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `16000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GrokPattern`  <a name="cfn-glue-classifier-grokclassifier-grokpattern"></a>
The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in [Writing Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html).
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\t]*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-classifier-grokclassifier-name"></a>
The name of the classifier.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
