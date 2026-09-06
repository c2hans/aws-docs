---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rum-appmonitor-javascriptsourcemaps.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RUM::AppMonitor JavaScriptSourceMaps
<a name="aws-properties-rum-appmonitor-javascriptsourcemaps"></a>

 A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps.

## Syntax
<a name="aws-properties-rum-appmonitor-javascriptsourcemaps-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rum-appmonitor-javascriptsourcemaps-syntax.json"></a>

```
{
  "[S3Uri](#cfn-rum-appmonitor-javascriptsourcemaps-s3uri)" : {{String}},
  "[Status](#cfn-rum-appmonitor-javascriptsourcemaps-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-rum-appmonitor-javascriptsourcemaps-syntax.yaml"></a>

```
  [S3Uri](#cfn-rum-appmonitor-javascriptsourcemaps-s3uri): {{String}}
  [Status](#cfn-rum-appmonitor-javascriptsourcemaps-status): {{String}}
```

## Properties
<a name="aws-properties-rum-appmonitor-javascriptsourcemaps-properties"></a>

`S3Uri`  <a name="cfn-rum-appmonitor-javascriptsourcemaps-s3uri"></a>
 The S3Uri of the bucket or folder that stores the source map files. It is required if status is ENABLED.
*Required*: No
*Type*: String
*Pattern*: `^s3://[a-z0-9][-.a-z0-9]{1,62}(?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-rum-appmonitor-javascriptsourcemaps-status"></a>
 Specifies whether JavaScript error stack traces should be unminified for this app monitor. The default is for JavaScript error stack trace unminification to be `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
