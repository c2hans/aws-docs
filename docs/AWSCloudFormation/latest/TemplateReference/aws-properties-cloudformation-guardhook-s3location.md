---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GuardHook S3Location
<a name="aws-properties-cloudformation-guardhook-s3location"></a>

Specifies the S3 location where your Guard rules or input parameters are located.

## Syntax
<a name="aws-properties-cloudformation-guardhook-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-guardhook-s3location-syntax.json"></a>

```
{
  "[Uri](#cfn-cloudformation-guardhook-s3location-uri)" : {{String}},
  "[VersionId](#cfn-cloudformation-guardhook-s3location-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-guardhook-s3location-syntax.yaml"></a>

```
  [Uri](#cfn-cloudformation-guardhook-s3location-uri): {{String}}
  [VersionId](#cfn-cloudformation-guardhook-s3location-versionid): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-guardhook-s3location-properties"></a>

`Uri`  <a name="cfn-cloudformation-guardhook-s3location-uri"></a>
Specifies the S3 path to the file that contains your Guard rules or input parameters (in the form `s3://<bucket name>/<file name>`).
For Guard rules, the object stored in S3 must have one of the following file extensions: `.guard`, `.zip`, or `.tar.gz`.
For input parameters, the object stored in S3 must have one of the following file extensions: `.yaml`, `.json`, `.zip`, or `.tar.gz`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-cloudformation-guardhook-s3location-versionid"></a>
For S3 buckets with versioning enabled, specifies the unique ID of the S3 object version to download your Guard rules or input parameters from.
The Guard Hook downloads files from S3 every time the Hook is invoked. To prevent accidental changes or deletions, we recommend using a version when configuring your Guard Hook.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
