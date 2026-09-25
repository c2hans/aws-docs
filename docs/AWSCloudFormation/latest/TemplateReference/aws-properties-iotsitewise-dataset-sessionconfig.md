---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-sessionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset SessionConfig
<a name="aws-properties-iotsitewise-dataset-sessionconfig"></a>

Contains the session configuration for a `SESSION` dataset, which defines the time range of time-series data the session covers.

## Syntax
<a name="aws-properties-iotsitewise-dataset-sessionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-sessionconfig-syntax.json"></a>

```
{
  "[SessionEndTime](#cfn-iotsitewise-dataset-sessionconfig-sessionendtime)" : {{String}},
  "[SessionStartTime](#cfn-iotsitewise-dataset-sessionconfig-sessionstarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-sessionconfig-syntax.yaml"></a>

```
  [SessionEndTime](#cfn-iotsitewise-dataset-sessionconfig-sessionendtime): {{String}}
  [SessionStartTime](#cfn-iotsitewise-dataset-sessionconfig-sessionstarttime): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-sessionconfig-properties"></a>

`SessionEndTime`  <a name="cfn-iotsitewise-dataset-sessionconfig-sessionendtime"></a>
The end time of the session as an ISO 8601 UTC instant, for example `2024-12-31T23:59:59Z`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionStartTime`  <a name="cfn-iotsitewise-dataset-sessionconfig-sessionstarttime"></a>
The start time of the session as an ISO 8601 UTC instant, for example `2024-01-01T00:00:00Z`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
