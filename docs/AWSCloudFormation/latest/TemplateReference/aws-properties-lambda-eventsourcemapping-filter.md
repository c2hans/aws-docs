---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping Filter

 A structure within a `FilterCriteria` object that defines an event filtering pattern.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-filter-syntax.json"></a>

```json
{
  "[Pattern](#cfn-lambda-eventsourcemapping-filter-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-filter-syntax.yaml"></a>

```yaml
  [Pattern](#cfn-lambda-eventsourcemapping-filter-pattern): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-filter-properties"></a>

`Pattern`  <a name="cfn-lambda-eventsourcemapping-filter-pattern"></a>
 A filter pattern. For more information on the syntax of a filter pattern, see [ Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
