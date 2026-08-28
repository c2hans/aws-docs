---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-collectionscheme.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign CollectionScheme
<a name="aws-properties-iotfleetwise-campaign-collectionscheme"></a>

Specifies what data to collect and how often or when to collect it.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-collectionscheme-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-collectionscheme-syntax.json"></a>

```
{
  "[ConditionBasedCollectionScheme](#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme)" : {{ConditionBasedCollectionScheme}},
  "[TimeBasedCollectionScheme](#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme)" : {{TimeBasedCollectionScheme}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-collectionscheme-syntax.yaml"></a>

```
  [ConditionBasedCollectionScheme](#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme): {{
    ConditionBasedCollectionScheme}}
  [TimeBasedCollectionScheme](#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme): {{
    TimeBasedCollectionScheme}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-collectionscheme-properties"></a>

`ConditionBasedCollectionScheme`  <a name="cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme"></a>
 Information about a collection scheme that uses a simple logical expression to recognize what data to collect.
*Required*: No
*Type*: [ConditionBasedCollectionScheme](aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeBasedCollectionScheme`  <a name="cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme"></a>
 Information about a collection scheme that uses a time period to decide how often to collect data.
*Required*: No
*Type*: [TimeBasedCollectionScheme](aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
