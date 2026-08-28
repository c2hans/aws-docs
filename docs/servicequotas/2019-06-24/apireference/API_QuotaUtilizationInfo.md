---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaUtilizationInfo.html
---

# QuotaUtilizationInfo
<a name="API_QuotaUtilizationInfo"></a>

Information about a quota's utilization, including the quota code, service information, current usage, and applied limits.

## Contents
<a name="API_QuotaUtilizationInfo_Contents"></a>

 ** Adjustable **   <a name="servicequotas-Type-QuotaUtilizationInfo-Adjustable"></a>
Indicates whether the quota value can be increased.
Type: Boolean
Required: No

 ** AppliedValue **   <a name="servicequotas-Type-QuotaUtilizationInfo-AppliedValue"></a>
The applied value of the quota, which may be higher than the default value if a quota increase has been requested and approved.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: No

 ** DefaultValue **   <a name="servicequotas-Type-QuotaUtilizationInfo-DefaultValue"></a>
The default value of the quota.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: No

 ** Namespace **   <a name="servicequotas-Type-QuotaUtilizationInfo-Namespace"></a>
The namespace of the metric used to track quota usage.
Type: String
Required: No

 ** QuotaCode **   <a name="servicequotas-Type-QuotaUtilizationInfo-QuotaCode"></a>
The quota identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** QuotaName **   <a name="servicequotas-Type-QuotaUtilizationInfo-QuotaName"></a>
The quota name.
Type: String
Required: No

 ** ServiceCode **   <a name="servicequotas-Type-QuotaUtilizationInfo-ServiceCode"></a>
The service identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** ServiceName **   <a name="servicequotas-Type-QuotaUtilizationInfo-ServiceName"></a>
The service name.
Type: String
Required: No

 ** Utilization **   <a name="servicequotas-Type-QuotaUtilizationInfo-Utilization"></a>
The utilization percentage of the quota, calculated as (current usage / applied value) × 100. Values range from 0.0 to 100.0 or higher if usage exceeds the quota limit.
Type: Double
Required: No

## See Also
<a name="API_QuotaUtilizationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/QuotaUtilizationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/QuotaUtilizationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/QuotaUtilizationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
