---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceQuotaIncreaseRequestInTemplate.html
---

# ServiceQuotaIncreaseRequestInTemplate
<a name="API_ServiceQuotaIncreaseRequestInTemplate"></a>

Information about a quota increase request.

## Contents
<a name="API_ServiceQuotaIncreaseRequestInTemplate_Contents"></a>

 ** AwsRegion **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-AwsRegion"></a>
The AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** DesiredValue **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-DesiredValue"></a>
The new, increased value of the quota.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: No

 ** GlobalQuota **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-GlobalQuota"></a>
Indicates whether the quota is global.
Type: Boolean
Required: No

 ** QuotaCode **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** QuotaName **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-QuotaName"></a>
Specifies the quota name.
Type: String
Required: No

 ** ServiceCode **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** ServiceName **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-ServiceName"></a>
Specifies the service name.
Type: String
Required: No

 ** Unit **   <a name="servicequotas-Type-ServiceQuotaIncreaseRequestInTemplate-Unit"></a>
The unit of measurement.
Type: String
Required: No

## See Also
<a name="API_ServiceQuotaIncreaseRequestInTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/ServiceQuotaIncreaseRequestInTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/ServiceQuotaIncreaseRequestInTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/ServiceQuotaIncreaseRequestInTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
