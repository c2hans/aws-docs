---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-otelenrichment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::OTelEnrichment
<a name="aws-resource-cloudwatch-otelenrichment"></a>

Enables OpenTelemetry (OTel) metric enrichment in Amazon CloudWatch, allowing CloudWatch vended metrics to be available for PromQL querying enriched with AWS resource tags and metadata.

This is a singleton resource — only one `OTelEnrichment` resource can exist per AWS account. The resource has no configurable properties. Creating the resource starts enrichment, and deleting it stops enrichment.

Before creating this resource, you must enable resource tags on telemetry for your account. For more information, see [Supported AWS infrastructure metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-resource-cloudwatch-otelenrichment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-otelenrichment-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::OTelEnrichment"
}
```

### YAML
<a name="aws-resource-cloudwatch-otelenrichment-syntax.yaml"></a>

```
Type: AWS::CloudWatch::OTelEnrichment
```

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
