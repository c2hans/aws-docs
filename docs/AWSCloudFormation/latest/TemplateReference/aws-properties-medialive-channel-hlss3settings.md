---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-hlss3settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel HlsS3Settings
<a name="aws-properties-medialive-channel-hlss3settings"></a>

Sets up Amazon S3 as the destination for this HLS output.

The parent of this entity is HlsCdnSettings.

## Syntax
<a name="aws-properties-medialive-channel-hlss3settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-hlss3settings-syntax.json"></a>

```
{
  "[CannedAcl](#cfn-medialive-channel-hlss3settings-cannedacl)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-hlss3settings-syntax.yaml"></a>

```
  [CannedAcl](#cfn-medialive-channel-hlss3settings-cannedacl): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-hlss3settings-properties"></a>

`CannedAcl`  <a name="cfn-medialive-channel-hlss3settings-cannedacl"></a>
Specify the canned ACL to apply to each S3 request. Defaults to none.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
