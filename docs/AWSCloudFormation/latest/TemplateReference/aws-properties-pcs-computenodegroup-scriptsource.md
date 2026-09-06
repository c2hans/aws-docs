---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-scriptsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup ScriptSource
<a name="aws-properties-pcs-computenodegroup-scriptsource"></a>

The source location and integrity information for a node lifecycle script.

## Syntax
<a name="aws-properties-pcs-computenodegroup-scriptsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-scriptsource-syntax.json"></a>

```
{
  "[Checksum](#cfn-pcs-computenodegroup-scriptsource-checksum)" : {{String}},
  "[S3VersionId](#cfn-pcs-computenodegroup-scriptsource-s3versionid)" : {{String}},
  "[ScriptLocation](#cfn-pcs-computenodegroup-scriptsource-scriptlocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-scriptsource-syntax.yaml"></a>

```
  [Checksum](#cfn-pcs-computenodegroup-scriptsource-checksum): {{String}}
  [S3VersionId](#cfn-pcs-computenodegroup-scriptsource-s3versionid): {{String}}
  [ScriptLocation](#cfn-pcs-computenodegroup-scriptsource-scriptlocation): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-scriptsource-properties"></a>

`Checksum`  <a name="cfn-pcs-computenodegroup-scriptsource-checksum"></a>
The SHA-256 checksum of the script content, as a 64-character hexadecimal string. This value is optional. When specified, AWS PCS uses this value to verify the integrity of the downloaded script.
*Required*: No
*Type*: String
*Pattern*: `^[a-fA-F0-9]{64}$`
*Minimum*: `64`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3VersionId`  <a name="cfn-pcs-computenodegroup-scriptsource-s3versionid"></a>
The Amazon S3 version ID of the script. Use this value to pin the script to a specific version in a versioned Amazon S3 bucket. This value is only valid when `scriptLocation` is an Amazon S3 URI.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScriptLocation`  <a name="cfn-pcs-computenodegroup-scriptsource-scriptlocation"></a>
The location of the script. Specify either an Amazon S3 URI in the format `s3://bucket-name/key` or an HTTPS URL.
*Required*: Yes
*Type*: String
*Pattern*: `^(s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+|https://.+)$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
