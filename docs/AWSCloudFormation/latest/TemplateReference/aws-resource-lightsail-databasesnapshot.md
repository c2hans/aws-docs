---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-databasesnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::DatabaseSnapshot
<a name="aws-resource-lightsail-databasesnapshot"></a>

Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database.

The `create relational database snapshot` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Syntax
<a name="aws-resource-lightsail-databasesnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-databasesnapshot-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::DatabaseSnapshot",
  "Properties" : {
      "[RelationalDatabaseName](#cfn-lightsail-databasesnapshot-relationaldatabasename)" : {{String}},
      "[RelationalDatabaseSnapshotName](#cfn-lightsail-databasesnapshot-relationaldatabasesnapshotname)" : {{String}},
      "[Tags](#cfn-lightsail-databasesnapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-databasesnapshot-syntax.yaml"></a>

```
Type: AWS::Lightsail::DatabaseSnapshot
Properties:
  [RelationalDatabaseName](#cfn-lightsail-databasesnapshot-relationaldatabasename): {{String}}
  [RelationalDatabaseSnapshotName](#cfn-lightsail-databasesnapshot-relationaldatabasesnapshotname): {{String}}
  [Tags](#cfn-lightsail-databasesnapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lightsail-databasesnapshot-properties"></a>

`RelationalDatabaseName`  <a name="cfn-lightsail-databasesnapshot-relationaldatabasename"></a>
The unique name of the database resource in Lightsail.
*Required*: Yes
*Type*: String
*Pattern*: `^\w[\w\-]*\w$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RelationalDatabaseSnapshotName`  <a name="cfn-lightsail-databasesnapshot-relationaldatabasesnapshotname"></a>
The name of the database snapshot.
*Required*: Yes
*Type*: String
*Pattern*: `^\w[\w\-]*\w$`
*Minimum*: `2`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lightsail-databasesnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
*Required*: No
*Type*: Array of [Tag](aws-properties-lightsail-databasesnapshot-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-databasesnapshot-return-values"></a>

### Ref
<a name="aws-resource-lightsail-databasesnapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-databasesnapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-databasesnapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the database snapshot.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the database snapshot was created.

`Engine`  <a name="Engine-fn::getatt"></a>
The software of the database snapshot (for example, `MySQL`)

`EngineVersion`  <a name="EngineVersion-fn::getatt"></a>
The database engine version for the database snapshot (for example, `5.7.23`).

`FromRelationalDatabaseArn`  <a name="FromRelationalDatabaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the database from which the database snapshot was created.

`FromRelationalDatabaseBlueprintId`  <a name="FromRelationalDatabaseBlueprintId-fn::getatt"></a>
The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.

`FromRelationalDatabaseBundleId`  <a name="FromRelationalDatabaseBundleId-fn::getatt"></a>
The bundle ID of the database from which the database snapshot was created.

`FromRelationalDatabaseName`  <a name="FromRelationalDatabaseName-fn::getatt"></a>
The name of the source database from which the database snapshot was created.

`Name`  <a name="Name-fn::getatt"></a>
The name of the database snapshot.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The Lightsail resource type.

`SizeInGb`  <a name="SizeInGb-fn::getatt"></a>
The size of the disk in GB (for example, `32`) for the database snapshot.

`State`  <a name="State-fn::getatt"></a>
The state of the database snapshot.

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
