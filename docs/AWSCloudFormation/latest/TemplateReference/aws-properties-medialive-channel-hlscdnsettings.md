---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-hlscdnsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel HlsCdnSettings
<a name="aws-properties-medialive-channel-hlscdnsettings"></a>

The settings for the CDN of an HLS output.

The parent of this entity is HlsGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-hlscdnsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-hlscdnsettings-syntax.json"></a>

```
{
  "[HlsAkamaiSettings](#cfn-medialive-channel-hlscdnsettings-hlsakamaisettings)" : {{HlsAkamaiSettings}},
  "[HlsBasicPutSettings](#cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings)" : {{HlsBasicPutSettings}},
  "[HlsMediaStoreSettings](#cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings)" : {{HlsMediaStoreSettings}},
  "[HlsS3Settings](#cfn-medialive-channel-hlscdnsettings-hlss3settings)" : {{HlsS3Settings}},
  "[HlsWebdavSettings](#cfn-medialive-channel-hlscdnsettings-hlswebdavsettings)" : {{HlsWebdavSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-hlscdnsettings-syntax.yaml"></a>

```
  [HlsAkamaiSettings](#cfn-medialive-channel-hlscdnsettings-hlsakamaisettings): {{
    HlsAkamaiSettings}}
  [HlsBasicPutSettings](#cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings): {{
    HlsBasicPutSettings}}
  [HlsMediaStoreSettings](#cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings): {{
    HlsMediaStoreSettings}}
  [HlsS3Settings](#cfn-medialive-channel-hlscdnsettings-hlss3settings): {{
    HlsS3Settings}}
  [HlsWebdavSettings](#cfn-medialive-channel-hlscdnsettings-hlswebdavsettings): {{
    HlsWebdavSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-hlscdnsettings-properties"></a>

`HlsAkamaiSettings`  <a name="cfn-medialive-channel-hlscdnsettings-hlsakamaisettings"></a>
Sets up Akamai as the downstream system for the HLS output group.
*Required*: No
*Type*: [HlsAkamaiSettings](aws-properties-medialive-channel-hlsakamaisettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsBasicPutSettings`  <a name="cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings"></a>
The settings for Basic Put for the HLS output.
*Required*: No
*Type*: [HlsBasicPutSettings](aws-properties-medialive-channel-hlsbasicputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsMediaStoreSettings`  <a name="cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings"></a>
Sets up MediaStore as the destination for the HLS output.
*Required*: No
*Type*: [HlsMediaStoreSettings](aws-properties-medialive-channel-hlsmediastoresettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsS3Settings`  <a name="cfn-medialive-channel-hlscdnsettings-hlss3settings"></a>
Sets up Amazon S3 as the destination for this HLS output.
*Required*: No
*Type*: [HlsS3Settings](aws-properties-medialive-channel-hlss3settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsWebdavSettings`  <a name="cfn-medialive-channel-hlscdnsettings-hlswebdavsettings"></a>
The settings for Web VTT captions in the HLS output group.
The parent of this entity is HlsGroupSettings.
*Required*: No
*Type*: [HlsWebdavSettings](aws-properties-medialive-channel-hlswebdavsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
