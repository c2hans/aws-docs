---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-schema-schemaversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Schema SchemaVersion
<a name="aws-properties-glue-schema-schemaversion"></a>

Specifies the version of a schema.

## Syntax
<a name="aws-properties-glue-schema-schemaversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-schema-schemaversion-syntax.json"></a>

```
{
  "[IsLatest](#cfn-glue-schema-schemaversion-islatest)" : {{Boolean}},
  "[VersionNumber](#cfn-glue-schema-schemaversion-versionnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-schema-schemaversion-syntax.yaml"></a>

```
  [IsLatest](#cfn-glue-schema-schemaversion-islatest): {{Boolean}}
  [VersionNumber](#cfn-glue-schema-schemaversion-versionnumber): {{Integer}}
```

## Properties
<a name="aws-properties-glue-schema-schemaversion-properties"></a>

`IsLatest`  <a name="cfn-glue-schema-schemaversion-islatest"></a>
Indicates if this version is the latest version of the schema.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionNumber`  <a name="cfn-glue-schema-schemaversion-versionnumber"></a>
The version number of the schema.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
