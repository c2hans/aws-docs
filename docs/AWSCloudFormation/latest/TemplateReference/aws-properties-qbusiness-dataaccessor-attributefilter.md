---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-attributefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor AttributeFilter
<a name="aws-properties-qbusiness-dataaccessor-attributefilter"></a>

Enables filtering of responses based on document attributes or metadata fields.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-attributefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-attributefilter-syntax.json"></a>

```
{
  "[AndAllFilters](#cfn-qbusiness-dataaccessor-attributefilter-andallfilters)" : {{[ AttributeFilter, ... ]}},
  "[ContainsAll](#cfn-qbusiness-dataaccessor-attributefilter-containsall)" : {{DocumentAttribute}},
  "[ContainsAny](#cfn-qbusiness-dataaccessor-attributefilter-containsany)" : {{DocumentAttribute}},
  "[EqualsTo](#cfn-qbusiness-dataaccessor-attributefilter-equalsto)" : {{DocumentAttribute}},
  "[GreaterThan](#cfn-qbusiness-dataaccessor-attributefilter-greaterthan)" : {{DocumentAttribute}},
  "[GreaterThanOrEquals](#cfn-qbusiness-dataaccessor-attributefilter-greaterthanorequals)" : {{DocumentAttribute}},
  "[LessThan](#cfn-qbusiness-dataaccessor-attributefilter-lessthan)" : {{DocumentAttribute}},
  "[LessThanOrEquals](#cfn-qbusiness-dataaccessor-attributefilter-lessthanorequals)" : {{DocumentAttribute}},
  "[NotFilter](#cfn-qbusiness-dataaccessor-attributefilter-notfilter)" : {{AttributeFilter}},
  "[OrAllFilters](#cfn-qbusiness-dataaccessor-attributefilter-orallfilters)" : {{[ AttributeFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-attributefilter-syntax.yaml"></a>

```
  [AndAllFilters](#cfn-qbusiness-dataaccessor-attributefilter-andallfilters): {{
    - AttributeFilter}}
  [ContainsAll](#cfn-qbusiness-dataaccessor-attributefilter-containsall): {{
    DocumentAttribute}}
  [ContainsAny](#cfn-qbusiness-dataaccessor-attributefilter-containsany): {{
    DocumentAttribute}}
  [EqualsTo](#cfn-qbusiness-dataaccessor-attributefilter-equalsto): {{
    DocumentAttribute}}
  [GreaterThan](#cfn-qbusiness-dataaccessor-attributefilter-greaterthan): {{
    DocumentAttribute}}
  [GreaterThanOrEquals](#cfn-qbusiness-dataaccessor-attributefilter-greaterthanorequals): {{
    DocumentAttribute}}
  [LessThan](#cfn-qbusiness-dataaccessor-attributefilter-lessthan): {{
    DocumentAttribute}}
  [LessThanOrEquals](#cfn-qbusiness-dataaccessor-attributefilter-lessthanorequals): {{
    DocumentAttribute}}
  [NotFilter](#cfn-qbusiness-dataaccessor-attributefilter-notfilter): {{
    AttributeFilter}}
  [OrAllFilters](#cfn-qbusiness-dataaccessor-attributefilter-orallfilters): {{
    - AttributeFilter}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-attributefilter-properties"></a>

`AndAllFilters`  <a name="cfn-qbusiness-dataaccessor-attributefilter-andallfilters"></a>
Performs a logical `AND` operation on all supplied filters.
*Required*: No
*Type*: Array of [AttributeFilter](#aws-properties-qbusiness-dataaccessor-attributefilter)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainsAll`  <a name="cfn-qbusiness-dataaccessor-attributefilter-containsall"></a>
Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainsAny`  <a name="cfn-qbusiness-dataaccessor-attributefilter-containsany"></a>
Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EqualsTo`  <a name="cfn-qbusiness-dataaccessor-attributefilter-equalsto"></a>
Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue`, `longValue`, `stringListValue` and `stringValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GreaterThan`  <a name="cfn-qbusiness-dataaccessor-attributefilter-greaterthan"></a>
Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GreaterThanOrEquals`  <a name="cfn-qbusiness-dataaccessor-attributefilter-greaterthanorequals"></a>
Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LessThan`  <a name="cfn-qbusiness-dataaccessor-attributefilter-lessthan"></a>
Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LessThanOrEquals`  <a name="cfn-qbusiness-dataaccessor-attributefilter-lessthanorequals"></a>
Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
*Required*: No
*Type*: [DocumentAttribute](aws-properties-qbusiness-dataaccessor-documentattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotFilter`  <a name="cfn-qbusiness-dataaccessor-attributefilter-notfilter"></a>
Performs a logical `NOT` operation on all supplied filters.
*Required*: No
*Type*: [AttributeFilter](#aws-properties-qbusiness-dataaccessor-attributefilter)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrAllFilters`  <a name="cfn-qbusiness-dataaccessor-attributefilter-orallfilters"></a>
 Performs a logical `OR` operation on all supplied filters.
*Required*: No
*Type*: Array of [AttributeFilter](#aws-properties-qbusiness-dataaccessor-attributefilter)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
