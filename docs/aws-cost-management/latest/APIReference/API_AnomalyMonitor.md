---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html
---

# AnomalyMonitor
<a name="API_AnomalyMonitor"></a>

This object continuously inspects your account's cost data for anomalies. It's based on `MonitorType` and `MonitorSpecification`. The content consists of detailed metadata and the current status of the monitor object.

## Contents
<a name="API_AnomalyMonitor_Contents"></a>

 ** MonitorName **   <a name="awscostmanagement-Type-AnomalyMonitor-MonitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** MonitorType **   <a name="awscostmanagement-Type-AnomalyMonitor-MonitorType"></a>
The type of the monitor.
Set this to `DIMENSIONAL` for an AWS managed monitor. AWS managed monitors automatically track up to the top 5,000 values by cost within a dimension of your choosing. Each dimension value is evaluated independently. If you start incurring cost in a new value of your chosen dimension, it will automatically be analyzed by an AWS managed monitor.
Set this to `CUSTOM` for a customer managed monitor. Customer managed monitors let you select specific dimension values that get monitored in aggregate.
For more information about monitor types, see [Monitor types](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html#monitor-type-def) in the *Billing and Cost Management User Guide*.
Type: String
Valid Values: `DIMENSIONAL | CUSTOM`
Required: Yes

 ** CreationDate **   <a name="awscostmanagement-Type-AnomalyMonitor-CreationDate"></a>
The date when the monitor was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

 ** DimensionalValueCount **   <a name="awscostmanagement-Type-AnomalyMonitor-DimensionalValueCount"></a>
The value for evaluated dimensions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** LastEvaluatedDate **   <a name="awscostmanagement-Type-AnomalyMonitor-LastEvaluatedDate"></a>
The date when the monitor last evaluated for anomalies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

 ** LastUpdatedDate **   <a name="awscostmanagement-Type-AnomalyMonitor-LastUpdatedDate"></a>
The date when the monitor was last updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

 ** MonitorArn **   <a name="awscostmanagement-Type-AnomalyMonitor-MonitorArn"></a>
The Amazon Resource Name (ARN) value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MonitorDimension **   <a name="awscostmanagement-Type-AnomalyMonitor-MonitorDimension"></a>
For customer managed monitors, do not specify this field.
For AWS managed monitors, this field controls which cost dimension is automatically analyzed by the monitor. For `TAG` and `COST_CATEGORY ` dimensions, you must also specify MonitorSpecification to configure the specific tag or cost category key to analyze.
Type: String
Valid Values: `SERVICE | LINKED_ACCOUNT | TAG | COST_CATEGORY`
Required: No

 ** MonitorSpecification **   <a name="awscostmanagement-Type-AnomalyMonitor-MonitorSpecification"></a>
An [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object used to control what costs the monitor analyzes for anomalies.
For AWS managed monitors:
+ If MonitorDimension is `SERVICE` or `LINKED_ACCOUNT`, do not specify this field
+ If MonitorDimension is `TAG`, set this field to `{ "Tags": { "Key": "your tag key" } }`
+ If MonitorDimension is `COST_CATEGORY`, set this field to `{ "CostCategories": { "Key": "your cost category key" } }`
For customer managed monitors:
+ To track linked accounts, set this field to `{ "Dimensions": { "Key": "LINKED_ACCOUNT", "Values": [ "your list of up to 10 account IDs" ] } } `
+ To track cost allocation tags, set this field to `{ "Tags": { "Key": "your tag key", "Values": [ "your list of up to 10 tag values" ] } } `
+ To track cost categories, set this field to`{ "CostCategories": { "Key": "your cost category key", "Values": [ "your cost category value" ] } } `
Type: [Expression](API_Expression.md) object
Required: No

## See Also
<a name="API_AnomalyMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/AnomalyMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/AnomalyMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/AnomalyMonitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
