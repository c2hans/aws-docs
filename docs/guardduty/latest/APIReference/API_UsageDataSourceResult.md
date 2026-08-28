---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageDataSourceResult.html
---

# UsageDataSourceResult
<a name="API_UsageDataSourceResult"></a>

Contains information on the result of usage based on data source type.

## Contents
<a name="API_UsageDataSourceResult_Contents"></a>

 ** dataSource **   <a name="guardduty-Type-UsageDataSourceResult-dataSource"></a>
The data source type that generated usage.
Type: String
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_LOGS | KUBERNETES_AUDIT_LOGS | EC2_MALWARE_SCAN`
Required: No

 ** total **   <a name="guardduty-Type-UsageDataSourceResult-total"></a>
Represents the total of usage for the specified data source.
Type: [Total](API_Total.md) object
Required: No

## See Also
<a name="API_UsageDataSourceResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageDataSourceResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageDataSourceResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageDataSourceResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
