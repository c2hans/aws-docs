---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-migrationproject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::MigrationProject
<a name="aws-resource-dms-migrationproject"></a>

Provides information that defines a migration project.

## Syntax
<a name="aws-resource-dms-migrationproject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-migrationproject-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::MigrationProject",
  "Properties" : {
      "[Description](#cfn-dms-migrationproject-description)" : {{String}},
      "[InstanceProfileArn](#cfn-dms-migrationproject-instanceprofilearn)" : {{String}},
      "[InstanceProfileIdentifier](#cfn-dms-migrationproject-instanceprofileidentifier)" : {{String}},
      "[InstanceProfileName](#cfn-dms-migrationproject-instanceprofilename)" : {{String}},
      "[MigrationProjectIdentifier](#cfn-dms-migrationproject-migrationprojectidentifier)" : {{String}},
      "[MigrationProjectName](#cfn-dms-migrationproject-migrationprojectname)" : {{String}},
      "[SchemaConversionApplicationAttributes](#cfn-dms-migrationproject-schemaconversionapplicationattributes)" : {{SchemaConversionApplicationAttributes}},
      "[SourceDataProviderDescriptors](#cfn-dms-migrationproject-sourcedataproviderdescriptors)" : {{[ DataProviderDescriptor, ... ]}},
      "[Tags](#cfn-dms-migrationproject-tags)" : {{[ Tag, ... ]}},
      "[TargetDataProviderDescriptors](#cfn-dms-migrationproject-targetdataproviderdescriptors)" : {{[ DataProviderDescriptor, ... ]}},
      "[TransformationRules](#cfn-dms-migrationproject-transformationrules)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dms-migrationproject-syntax.yaml"></a>

```
Type: AWS::DMS::MigrationProject
Properties:
  [Description](#cfn-dms-migrationproject-description): {{String}}
  [InstanceProfileArn](#cfn-dms-migrationproject-instanceprofilearn): {{String}}
  [InstanceProfileIdentifier](#cfn-dms-migrationproject-instanceprofileidentifier): {{String}}
  [InstanceProfileName](#cfn-dms-migrationproject-instanceprofilename): {{String}}
  [MigrationProjectIdentifier](#cfn-dms-migrationproject-migrationprojectidentifier): {{String}}
  [MigrationProjectName](#cfn-dms-migrationproject-migrationprojectname): {{String}}
  [SchemaConversionApplicationAttributes](#cfn-dms-migrationproject-schemaconversionapplicationattributes): {{
    SchemaConversionApplicationAttributes}}
  [SourceDataProviderDescriptors](#cfn-dms-migrationproject-sourcedataproviderdescriptors): {{
    - DataProviderDescriptor}}
  [Tags](#cfn-dms-migrationproject-tags): {{
    - Tag}}
  [TargetDataProviderDescriptors](#cfn-dms-migrationproject-targetdataproviderdescriptors): {{
    - DataProviderDescriptor}}
  [TransformationRules](#cfn-dms-migrationproject-transformationrules): {{String}}
```

## Properties
<a name="aws-resource-dms-migrationproject-properties"></a>

`Description`  <a name="cfn-dms-migrationproject-description"></a>
A user-friendly description of the migration project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileArn`  <a name="cfn-dms-migrationproject-instanceprofilearn"></a>
The Amazon Resource Name (ARN) of the instance profile for your migration project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileIdentifier`  <a name="cfn-dms-migrationproject-instanceprofileidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileName`  <a name="cfn-dms-migrationproject-instanceprofilename"></a>
The name of the associated instance profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MigrationProjectIdentifier`  <a name="cfn-dms-migrationproject-migrationprojectidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MigrationProjectName`  <a name="cfn-dms-migrationproject-migrationprojectname"></a>
The name of the migration project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaConversionApplicationAttributes`  <a name="cfn-dms-migrationproject-schemaconversionapplicationattributes"></a>
The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.
*Required*: No
*Type*: [SchemaConversionApplicationAttributes](aws-properties-dms-migrationproject-schemaconversionapplicationattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceDataProviderDescriptors`  <a name="cfn-dms-migrationproject-sourcedataproviderdescriptors"></a>
Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.
*Required*: No
*Type*: Array of [DataProviderDescriptor](aws-properties-dms-migrationproject-dataproviderdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-migrationproject-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-migrationproject-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetDataProviderDescriptors`  <a name="cfn-dms-migrationproject-targetdataproviderdescriptors"></a>
Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.
*Required*: No
*Type*: Array of [DataProviderDescriptor](aws-properties-dms-migrationproject-dataproviderdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformationRules`  <a name="cfn-dms-migrationproject-transformationrules"></a>
The transformation rules for the migration project in JSON format. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see [Transformation rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html).
Homogeneous data migrations do not support transformation rules.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-migrationproject-return-values"></a>

### Ref
<a name="aws-resource-dms-migrationproject-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-migrationproject-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dms-migrationproject-return-values-fn--getatt-fn--getatt"></a>

`MigrationProjectArn`  <a name="MigrationProjectArn-fn::getatt"></a>
The ARN string that uniquely identifies the migration project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
