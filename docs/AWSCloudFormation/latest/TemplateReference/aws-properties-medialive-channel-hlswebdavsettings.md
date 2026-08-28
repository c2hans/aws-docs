---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-hlswebdavsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel HlsWebdavSettings
<a name="aws-properties-medialive-channel-hlswebdavsettings"></a>

The configuration of a WebDav server as the downstream system for an HLS output.

The parent of this entity is HlsCdnSettings.

## Syntax
<a name="aws-properties-medialive-channel-hlswebdavsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-hlswebdavsettings-syntax.json"></a>

```
{
  "[ConnectionRetryInterval](#cfn-medialive-channel-hlswebdavsettings-connectionretryinterval)" : {{Integer}},
  "[FilecacheDuration](#cfn-medialive-channel-hlswebdavsettings-filecacheduration)" : {{Integer}},
  "[HttpTransferMode](#cfn-medialive-channel-hlswebdavsettings-httptransfermode)" : {{String}},
  "[NumRetries](#cfn-medialive-channel-hlswebdavsettings-numretries)" : {{Integer}},
  "[RestartDelay](#cfn-medialive-channel-hlswebdavsettings-restartdelay)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-hlswebdavsettings-syntax.yaml"></a>

```
  [ConnectionRetryInterval](#cfn-medialive-channel-hlswebdavsettings-connectionretryinterval): {{Integer}}
  [FilecacheDuration](#cfn-medialive-channel-hlswebdavsettings-filecacheduration): {{Integer}}
  [HttpTransferMode](#cfn-medialive-channel-hlswebdavsettings-httptransfermode): {{String}}
  [NumRetries](#cfn-medialive-channel-hlswebdavsettings-numretries): {{Integer}}
  [RestartDelay](#cfn-medialive-channel-hlswebdavsettings-restartdelay): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-hlswebdavsettings-properties"></a>

`ConnectionRetryInterval`  <a name="cfn-medialive-channel-hlswebdavsettings-connectionretryinterval"></a>
The number of seconds to wait before retrying a connection to the CDN if the connection is lost.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilecacheDuration`  <a name="cfn-medialive-channel-hlswebdavsettings-filecacheduration"></a>
The size, in seconds, of the file cache for streaming outputs.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpTransferMode`  <a name="cfn-medialive-channel-hlswebdavsettings-httptransfermode"></a>
Specifies whether to use chunked transfer encoding to WebDAV.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumRetries`  <a name="cfn-medialive-channel-hlswebdavsettings-numretries"></a>
The number of retry attempts that are made before the channel is put into an error state.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestartDelay`  <a name="cfn-medialive-channel-hlswebdavsettings-restartdelay"></a>
If a streaming output fails, the number of seconds to wait until a restart is initiated. A value of 0 means never restart.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
