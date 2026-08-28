---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdMappingTable IdMappingTableInputReferenceConfig
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig"></a>

Provides the input reference configuration for the ID mapping table.

## Syntax
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-syntax.json"></a>

```
{
  "[InputReferenceArn](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-inputreferencearn)" : {{String}},
  "[ManageResourcePolicies](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-manageresourcepolicies)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-syntax.yaml"></a>

```
  [InputReferenceArn](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-inputreferencearn): {{String}}
  [ManageResourcePolicies](#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-manageresourcepolicies): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-properties"></a>

`InputReferenceArn`  <a name="cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-inputreferencearn"></a>
The Amazon Resource Name (ARN) of the referenced resource in AWS Entity Resolution. Valid values are ID mapping workflow ARNs.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManageResourcePolicies`  <a name="cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-manageresourcepolicies"></a>
When `TRUE`, AWS Clean Rooms manages permissions for the ID mapping table resource.
When `FALSE`, the resource owner manages permissions for the ID mapping table resource.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
