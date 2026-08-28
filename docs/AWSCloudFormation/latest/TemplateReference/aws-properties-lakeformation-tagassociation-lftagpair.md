---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-tagassociation-lftagpair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::TagAssociation LFTagPair
<a name="aws-properties-lakeformation-tagassociation-lftagpair"></a>

 A structure containing the catalog ID, tag key, and tag values of an LF-tag key-value pair.

## Syntax
<a name="aws-properties-lakeformation-tagassociation-lftagpair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-tagassociation-lftagpair-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-tagassociation-lftagpair-catalogid)" : {{String}},
  "[TagKey](#cfn-lakeformation-tagassociation-lftagpair-tagkey)" : {{String}},
  "[TagValues](#cfn-lakeformation-tagassociation-lftagpair-tagvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lakeformation-tagassociation-lftagpair-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-tagassociation-lftagpair-catalogid): {{String}}
  [TagKey](#cfn-lakeformation-tagassociation-lftagpair-tagkey): {{String}}
  [TagValues](#cfn-lakeformation-tagassociation-lftagpair-tagvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-lakeformation-tagassociation-lftagpair-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-tagassociation-lftagpair-catalogid"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagKey`  <a name="cfn-lakeformation-tagassociation-lftagpair-tagkey"></a>
The key-name for the LF-tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagValues`  <a name="cfn-lakeformation-tagassociation-lftagpair-tagvalues"></a>
 A list of possible values of the corresponding `TagKey` of an LF-tag key-value pair.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
