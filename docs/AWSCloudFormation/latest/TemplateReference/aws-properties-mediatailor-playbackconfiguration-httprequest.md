---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-httprequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration HttpRequest
<a name="aws-properties-mediatailor-playbackconfiguration-httprequest"></a>

HTTP request configuration parameters that define how MediaTailor communicates with the ad decision server.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-httprequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-httprequest-syntax.json"></a>

```
{
  "[Body](#cfn-mediatailor-playbackconfiguration-httprequest-body)" : {{String}},
  "[CompressRequest](#cfn-mediatailor-playbackconfiguration-httprequest-compressrequest)" : {{String}},
  "[Headers](#cfn-mediatailor-playbackconfiguration-httprequest-headers)" : {{{{{Key}}: {{Value}}, ...}}},
  "[HttpMethod](#cfn-mediatailor-playbackconfiguration-httprequest-httpmethod)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-httprequest-syntax.yaml"></a>

```
  [Body](#cfn-mediatailor-playbackconfiguration-httprequest-body): {{String}}
  [CompressRequest](#cfn-mediatailor-playbackconfiguration-httprequest-compressrequest): {{String}}
  [Headers](#cfn-mediatailor-playbackconfiguration-httprequest-headers): {{
    {{Key}}: {{Value}}}}
  [HttpMethod](#cfn-mediatailor-playbackconfiguration-httprequest-httpmethod): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-httprequest-properties"></a>

`Body`  <a name="cfn-mediatailor-playbackconfiguration-httprequest-body"></a>
The request body content to send with HTTP requests to the ad decision server. This value is only eligible for `POST` requests.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompressRequest`  <a name="cfn-mediatailor-playbackconfiguration-httprequest-compressrequest"></a>
The compression method to apply to requests sent to the ad decision server. Supported values are `NONE` and `GZIP`. This value is only eligible for `POST` requests.
*Required*: No
*Type*: String
*Allowed values*: `NONE | GZIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-mediatailor-playbackconfiguration-httprequest-headers"></a>
Custom HTTP headers to include in requests to the ad decision server. Specify headers as key-value pairs. This value is only eligible for `POST` requests.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpMethod`  <a name="cfn-mediatailor-playbackconfiguration-httprequest-httpmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
