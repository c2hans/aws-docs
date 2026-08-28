---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-observabilityadmin-telemetryenrichment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryEnrichment
<a name="aws-resource-observabilityadmin-telemetryenrichment"></a>

 Enables the Resource tags for telemetry feature for your account. When enabled, CloudWatch creates an AWS Resource Explorer index and managed view so that it can discover resources and tags in your account. CloudWatch uses this information to enrich your telemetry with related AWS resource tags. For more information, see [Resource tags for telemetry documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-tags-for-telemetry.html).

## Syntax
<a name="aws-resource-observabilityadmin-telemetryenrichment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-observabilityadmin-telemetryenrichment-syntax.json"></a>

```
{
  "Type" : "AWS::ObservabilityAdmin::TelemetryEnrichment",
  "Properties" : {
      "[Scope](#cfn-observabilityadmin-telemetryenrichment-scope)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-observabilityadmin-telemetryenrichment-syntax.yaml"></a>

```
Type: AWS::ObservabilityAdmin::TelemetryEnrichment
Properties:
  [Scope](#cfn-observabilityadmin-telemetryenrichment-scope): {{String}}
```

## Properties
<a name="aws-resource-observabilityadmin-telemetryenrichment-properties"></a>

`Scope`  <a name="cfn-observabilityadmin-telemetryenrichment-scope"></a>
The scope of the telemetry enrichment. Currently, the only supported value is `ACCOUNT`.
*Required*: Yes
*Type*: String
*Allowed values*: `ACCOUNT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-observabilityadmin-telemetryenrichment-return-values"></a>

### Ref
<a name="aws-resource-observabilityadmin-telemetryenrichment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the scope of the telemetry enrichment.

### Fn::GetAtt
<a name="aws-resource-observabilityadmin-telemetryenrichment-return-values-fn--getatt"></a>

####
<a name="aws-resource-observabilityadmin-telemetryenrichment-return-values-fn--getatt-fn--getatt"></a>

`Status`  <a name="Status-fn::getatt"></a>
The current status of the Resource tags for telemetry feature. Valid values are `RUNNING`, `STOPPED`, and `IMPAIRED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
