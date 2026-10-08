---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-otelenrichment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::OTelEnrichment
<a name="aws-resource-cloudwatch-otelenrichment"></a>

Enables OpenTelemetry (OTel) metric enrichment in Amazon CloudWatch, allowing CloudWatch vended metrics to be available for PromQL querying enriched with AWS resource tags and metadata.

This is a singleton resource — only one `OTelEnrichment` resource can exist per AWS account. Creating the resource starts enrichment, and deleting it stops enrichment.

By default, enrichment applies to every namespace that CloudWatch supports. To limit enrichment to a subset of metrics, specify `IncludeFilters`, `ExcludeFilters`, or both. You can change the filters without interrupting enrichment. CloudFormation applies the change by calling `UpdateOTelEnrichment`.

Before creating this resource, you must enable resource tags on telemetry for your account. For more information, see [Supported AWS infrastructure metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-cloudwatch-otelenrichment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-otelenrichment-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::OTelEnrichment",
  "Properties" : {
      "[ExcludeFilters](#cfn-cloudwatch-otelenrichment-excludefilters)" : {{[ OTelEnrichmentMetricSelector, ... ]}},
      "[IncludeFilters](#cfn-cloudwatch-otelenrichment-includefilters)" : {{[ OTelEnrichmentMetricSelector, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-otelenrichment-syntax.yaml"></a>

```
Type: AWS::CloudWatch::OTelEnrichment
Properties:
  [ExcludeFilters](#cfn-cloudwatch-otelenrichment-excludefilters): {{
    - OTelEnrichmentMetricSelector}}
  [IncludeFilters](#cfn-cloudwatch-otelenrichment-includefilters): {{
    - OTelEnrichmentMetricSelector}}
```

## Properties
<a name="aws-resource-cloudwatch-otelenrichment-properties"></a>

`ExcludeFilters`  <a name="cfn-cloudwatch-otelenrichment-excludefilters"></a>
The metric namespaces, and the metric names, to leave unenriched. If this parameter is omitted, nothing is excluded.
Amazon CloudWatch applies `ExcludeFilters` after `IncludeFilters`, so a metric that both parameters match is not enriched.
A maximum of 100 filters is allowed across `IncludeFilters` and `ExcludeFilters` combined.
*Required*: No
*Type*: Array of [OTelEnrichmentMetricSelector](aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeFilters`  <a name="cfn-cloudwatch-otelenrichment-includefilters"></a>
The metric namespaces, and the metric names, to enrich. If this parameter is omitted, every namespace that Amazon CloudWatch supports for enrichment is in scope.
A maximum of 100 filters is allowed across `IncludeFilters` and `ExcludeFilters` combined.
*Required*: No
*Type*: Array of [OTelEnrichmentMetricSelector](aws-properties-cloudwatch-otelenrichment-otelenrichmentmetricselector.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-otelenrichment-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-otelenrichment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns AWS account ID.

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-otelenrichment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-otelenrichment-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The AWS account ID. This is the primary identifier for this singleton resource.

`Status`  <a name="Status-fn::getatt"></a>
The current status of OTel enrichment for the account. Valid values are `RUNNING` (enrichment is enabled) and `STOPPED` (enrichment is disabled).
