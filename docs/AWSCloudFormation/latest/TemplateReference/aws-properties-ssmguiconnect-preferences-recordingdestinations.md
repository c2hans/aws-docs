---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmguiconnect-preferences-recordingdestinations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMGuiConnect::Preferences RecordingDestinations
<a name="aws-properties-ssmguiconnect-preferences-recordingdestinations"></a>

Determines where recordings of RDP connections are stored.

## Syntax
<a name="aws-properties-ssmguiconnect-preferences-recordingdestinations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmguiconnect-preferences-recordingdestinations-syntax.json"></a>

```
{
  "[S3Buckets](#cfn-ssmguiconnect-preferences-recordingdestinations-s3buckets)" : {{[ S3Bucket, ... ]}}
}
```

### YAML
<a name="aws-properties-ssmguiconnect-preferences-recordingdestinations-syntax.yaml"></a>

```
  [S3Buckets](#cfn-ssmguiconnect-preferences-recordingdestinations-s3buckets): {{
    - S3Bucket}}
```

## Properties
<a name="aws-properties-ssmguiconnect-preferences-recordingdestinations-properties"></a>

`S3Buckets`  <a name="cfn-ssmguiconnect-preferences-recordingdestinations-s3buckets"></a>
The S3 bucket where RDP connection recordings are stored.
*Required*: Yes
*Type*: Array of [S3Bucket](aws-properties-ssmguiconnect-preferences-s3bucket.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
