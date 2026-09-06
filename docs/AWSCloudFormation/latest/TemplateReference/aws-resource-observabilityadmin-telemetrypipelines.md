---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-telemetrypipelines.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryPipelines
<a name="aws-resource-observabilityadmin-telemetrypipelines"></a>

Creates a telemetry pipeline for processing and transforming telemetry data. The pipeline defines how data flows from sources through processors to destinations, enabling data transformation and delivering capabilities.

## Syntax
<a name="aws-resource-observabilityadmin-telemetrypipelines-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-telemetrypipelines-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::TelemetryPipelines",
  "Properties" : {
      "[Configuration](#cfn-observabilityadmin-telemetrypipelines-configuration)" : {{TelemetryPipelineConfiguration}},
      "[Name](#cfn-observabilityadmin-telemetrypipelines-name)" : {{String}},
      "[Tags](#cfn-observabilityadmin-telemetrypipelines-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-telemetrypipelines-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::TelemetryPipelines
Properties:
  [Configuration](#cfn-observabilityadmin-telemetrypipelines-configuration): {{
    TelemetryPipelineConfiguration}}
  [Name](#cfn-observabilityadmin-telemetrypipelines-name): {{String}}
  [Tags](#cfn-observabilityadmin-telemetrypipelines-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-observabilityadmin-telemetrypipelines-properties"></a>

`Configuration`  <a name="cfn-observabilityadmin-telemetrypipelines-configuration"></a>
The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html).
*Required*: Yes
*Type*: [TelemetryPipelineConfiguration](aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-observabilityadmin-telemetrypipelines-name"></a>
The name of the telemetry pipeline to create. The name must be unique within your account.
*Required*: No
*Type*: String
*Pattern*: `[a-z][a-z0-9\-]+`
*Minimum*: `3`
*Maximum*: `28`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-observabilityadmin-telemetrypipelines-tags"></a>
The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.
*Required*: No
*Type*: Array of [Tag](aws-properties-observabilityadmin-telemetrypipelines-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-observabilityadmin-telemetrypipelines-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-telemetrypipelines-return-values-ref"></a>

The Amazon Resource Name (ARN) of the created telemetry pipeline.

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-telemetrypipelines-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-telemetrypipelines-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the created telemetry pipeline.

`PipelineIdentifier`  <a name="PipelineIdentifier-fn::getatt"></a>
The Amazon Resource Name (ARN) of the telemetry pipeline.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the telemetry pipeline.

## Examples
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples"></a>

**Topics**
+ [Using CloudWatch as a pipeline source](#aws-resource-observabilityadmin-telemetrypipelines--examples--Using_CloudWatch_as_a_pipeline_source)
+ [Using Amazon S3 as a pipeline source](#aws-resource-observabilityadmin-telemetrypipelines--examples--Using_Amazon_S3_as_a_pipeline_source)

### Using CloudWatch as a pipeline source
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_CloudWatch_as_a_pipeline_source"></a>

The following is an example of a `Body` property value for the `Configuration` object.

#### JSON
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_CloudWatch_as_a_pipeline_source--json"></a>

```
{
  "Type": "AWS::ObservabilityAdmin::TelemetryPipelines",
  "Properties": {
    "Configuration": {
      "Body": "pipeline:\n  source:\n    cloudwatch_logs:\n      log_event_metadata:\n        data_source_name: \"my_data_source\"\n        data_source_type: \"default\"\n      aws:\n        sts_role_arn: \"arn:aws:iam::123456789012:role/MyPipelineAccessRole\"\n  processor:\n    - parse_json: {}\n  sink:\n    - cloudwatch_logs:\n        log_group: \"@original\""
    }
  }
}
```

#### YAML
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_CloudWatch_as_a_pipeline_source--yaml"></a>

```
Type: AWS::ObservabilityAdmin::TelemetryPipelines
Properties:
  Configuration:
    Body: |
      pipeline:
        source:
          cloudwatch_logs:
            log_event_metadata:
              data_source_name: "my_data_source"
              data_source_type: "default"
            aws:
              sts_role_arn: "arn:aws:iam::123456789012:role/MyPipelineAccessRole"
        processor:
          - parse_json: {}
        sink:
          - cloudwatch_logs:
              log_group: "@original"
```

### Using Amazon S3 as a pipeline source
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_Amazon_S3_as_a_pipeline_source"></a>

The following is an example of a `Body` property value for the `Configuration` object.

#### JSON
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_Amazon_S3_as_a_pipeline_source--json"></a>

```
{
  "Type": "AWS::ObservabilityAdmin::TelemetryPipelines",
  "Properties": {
    "Configuration": {
      "Body": "pipeline:\n  source:\n    s3:\n      sqs:\n        visibility_timeout: \"PT60S\"\n        visibility_duplication_protection: true\n        maximum_messages: 10\n        queue_url: \"https://sqs.us-east-1.amazonaws.com/123456789012/my-sqs-queue\"\n      notification_type: \"sqs\"\n      codec:\n        ndjson: {}\n      aws:\n        region: \"us-east-1\"\n        sts_role_arn: \"arn:aws:iam::123456789012:role/MyAccessRole\"\n      data_source_name: \"crowdstrike_falcon\"\n  processor:\n    - ocsf:\n        version: \"1.5\"\n        mapping_version: \"1.5.0\"\n        schema:\n          crowdstrike_falcon:\n  sink:\n    - cloudwatch_logs:\n        log_group: \"my-log-group\""
    }
  }
}
```

#### YAML
<a name="aws-resource-observabilityadmin-telemetrypipelines--examples--Using_Amazon_S3_as_a_pipeline_source--yaml"></a>

```
Type: AWS::ObservabilityAdmin::TelemetryPipelines
Properties:
  Configuration:
    Body: |
      pipeline:
        source:
          s3:
            sqs:
              visibility_timeout: "PT60S"
              visibility_duplication_protection: true
              maximum_messages: 10
              queue_url: "https://sqs.us-east-1.amazonaws.com/123456789012/my-sqs-queue"
            notification_type: "sqs"
            codec:
              ndjson: {}
            aws:
              region: "us-east-1"
              sts_role_arn: "arn:aws:iam::123456789012:role/MyAccessRole"
            data_source_name: "crowdstrike_falcon"
        processor:
          - ocsf:
              version: "1.5"
              mapping_version: "1.5.0"
              schema:
                crowdstrike_falcon:
        sink:
          - cloudwatch_logs:
              log_group: "my-log-group"
```
