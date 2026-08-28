---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdMappingTable IdMappingTableInputSource
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource"></a>

The input source of the ID mapping table.

## Syntax
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource-syntax.json"></a>

```
{
  "[IdNamespaceAssociationId](#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-idnamespaceassociationid)" : {{String}},
  "[Type](#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource-syntax.yaml"></a>

```
  [IdNamespaceAssociationId](#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-idnamespaceassociationid): {{String}}
  [Type](#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource-properties"></a>

`IdNamespaceAssociationId`  <a name="cfn-cleanrooms-idmappingtable-idmappingtableinputsource-idnamespaceassociationid"></a>
The unique identifier of the ID namespace association.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-idmappingtable-idmappingtableinputsource-type"></a>
The type of the input source of the ID mapping table.
*Required*: Yes
*Type*: String
*Allowed values*: `SOURCE | TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
