---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IdNamespaceAssociation IdNamespaceAssociationInputReferenceConfig
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig"></a>

Provides the information for the ID namespace association input reference configuration.

## Syntax
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-syntax.json"></a>

```
{
  "[InputReferenceArn](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-inputreferencearn)" : {{String}},
  "[ManageResourcePolicies](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-manageresourcepolicies)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-syntax.yaml"></a>

```
  [InputReferenceArn](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-inputreferencearn): {{String}}
  [ManageResourcePolicies](#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-manageresourcepolicies): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-properties"></a>

`InputReferenceArn`  <a name="cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-inputreferencearn"></a>
The Amazon Resource Name (ARN) of the AWS Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManageResourcePolicies`  <a name="cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-manageresourcepolicies"></a>
When `TRUE`, AWS Clean Rooms manages permissions for the ID namespace association resource.
When `FALSE`, the resource owner manages permissions for the ID namespace association resource.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
