---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resourceexplorer2-view-searchfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceExplorer2::View SearchFilter
<a name="aws-properties-resourceexplorer2-view-searchfilter"></a>

A search filter defines which resources can be part of a search query result set.

## Syntax
<a name="aws-properties-resourceexplorer2-view-searchfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resourceexplorer2-view-searchfilter-syntax.json"></a>

```
{
  "[FilterString](#cfn-resourceexplorer2-view-searchfilter-filterstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-resourceexplorer2-view-searchfilter-syntax.yaml"></a>

```
  [FilterString](#cfn-resourceexplorer2-view-searchfilter-filterstring): {{
    String}}
```

## Properties
<a name="aws-properties-resourceexplorer2-view-searchfilter-properties"></a>

`FilterString`  <a name="cfn-resourceexplorer2-view-searchfilter-filterstring"></a>
The string that contains the search keywords, prefixes, and operators to control the results that can be returned by a Search operation.
For information about the supported syntax, see [Search query reference](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the *AWS Resource Explorer User Guide*.
This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators). It doesn't support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any AWS Region that begin with the letters `us` and are *not* tagged with a key `Stage` that has the value `prod`.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
