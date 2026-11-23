---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RouterContentQualityAnalysisConfiguration

The content quality analysis configuration for the router input.

**Important**
The content quality analysis feature only monitors the first video stream and the first audio stream it encounters within the router input source.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-syntax.json"></a>

```json
{
  "[ContentLevel](#cfn-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-contentlevel)" : {{ContentQualityAnalysisFeatureConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-syntax.yaml"></a>

```yaml
  [ContentLevel](#cfn-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-contentlevel): {{
    ContentQualityAnalysisFeatureConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-properties"></a>

`ContentLevel`  <a name="cfn-mediaconnect-routerinput-routercontentqualityanalysisconfiguration-contentlevel"></a>
The content quality analysis configuration.
*Required*: Yes
*Type*: [ContentQualityAnalysisFeatureConfiguration](aws-properties-mediaconnect-routerinput-contentqualityanalysisfeatureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
