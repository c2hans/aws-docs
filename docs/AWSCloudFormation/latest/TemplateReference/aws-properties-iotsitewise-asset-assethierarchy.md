---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-asset-assethierarchy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Asset AssetHierarchy
<a name="aws-properties-iotsitewise-asset-assethierarchy"></a>

Describes an asset hierarchy that contains a hierarchy's name and ID.

## Syntax
<a name="aws-properties-iotsitewise-asset-assethierarchy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-asset-assethierarchy-syntax.json"></a>

```
{
  "[ChildAssetId](#cfn-iotsitewise-asset-assethierarchy-childassetid)" : {{String}},
  "[ExternalId](#cfn-iotsitewise-asset-assethierarchy-externalid)" : {{String}},
  "[Id](#cfn-iotsitewise-asset-assethierarchy-id)" : {{String}},
  "[LogicalId](#cfn-iotsitewise-asset-assethierarchy-logicalid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-asset-assethierarchy-syntax.yaml"></a>

```
  [ChildAssetId](#cfn-iotsitewise-asset-assethierarchy-childassetid): {{String}}
  [ExternalId](#cfn-iotsitewise-asset-assethierarchy-externalid): {{String}}
  [Id](#cfn-iotsitewise-asset-assethierarchy-id): {{String}}
  [LogicalId](#cfn-iotsitewise-asset-assethierarchy-logicalid): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-asset-assethierarchy-properties"></a>

`ChildAssetId`  <a name="cfn-iotsitewise-asset-assethierarchy-childassetid"></a>
The Id of the child asset.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-iotsitewise-asset-assethierarchy-externalid"></a>
The external ID of the hierarchy, if it has one. When you update an asset hierarchy, you may assign an external ID if it doesn't already have one. You can't change the external ID of an asset hierarchy that already has one. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotsitewise-asset-assethierarchy-id"></a>
The ID of the hierarchy. This ID is a `hierarchyId`.
This is a return value and can't be set.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalId`  <a name="cfn-iotsitewise-asset-assethierarchy-logicalid"></a>
The ID of the hierarchy. This ID is a `hierarchyId`.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
