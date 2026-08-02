---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceQuota.html
---

# ServiceQuota
<a name="API_ServiceQuota"></a>

Information about a quota.

## Contents
<a name="API_ServiceQuota_Contents"></a>

 ** Adjustable **   <a name="servicequotas-Type-ServiceQuota-Adjustable"></a>
Indicates whether the quota value can be increased.
Type: Boolean
Required: No

 ** Description **   <a name="servicequotas-Type-ServiceQuota-Description"></a>
The quota description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `^.{0,350}$`
Required: No

 ** ErrorReason **   <a name="servicequotas-Type-ServiceQuota-ErrorReason"></a>
The error code and error reason.
Type: [ErrorReason](API_ErrorReason.md) object
Required: No

 ** GlobalQuota **   <a name="servicequotas-Type-ServiceQuota-GlobalQuota"></a>
Indicates whether the quota is global.
Type: Boolean
Required: No

 ** Period **   <a name="servicequotas-Type-ServiceQuota-Period"></a>
The period of time.
Type: [QuotaPeriod](API_QuotaPeriod.md) object
Required: No

 ** QuotaAppliedAtLevel **   <a name="servicequotas-Type-ServiceQuota-QuotaAppliedAtLevel"></a>
Filters the response to return applied quota values for the `ACCOUNT`, `RESOURCE`, or `ALL` levels. `ACCOUNT` is the default.
Type: String
Valid Values: `ACCOUNT | RESOURCE | ALL`
Required: No

 ** QuotaArn **   <a name="servicequotas-Type-ServiceQuota-QuotaArn"></a>
The Amazon Resource Name (ARN) of the quota.
Type: String
Required: No

 ** QuotaCode **   <a name="servicequotas-Type-ServiceQuota-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** QuotaContext **   <a name="servicequotas-Type-ServiceQuota-QuotaContext"></a>
The context for this service quota.
Type: [QuotaContextInfo](API_QuotaContextInfo.md) object
Required: No

 ** QuotaName **   <a name="servicequotas-Type-ServiceQuota-QuotaName"></a>
Specifies the quota name.
Type: String
Required: No

 ** ServiceCode **   <a name="servicequotas-Type-ServiceQuota-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** ServiceName **   <a name="servicequotas-Type-ServiceQuota-ServiceName"></a>
Specifies the service name.
Type: String
Required: No

 ** Unit **   <a name="servicequotas-Type-ServiceQuota-Unit"></a>
The unit of measurement.
Type: String
Required: No

 ** UsageMetric **   <a name="servicequotas-Type-ServiceQuota-UsageMetric"></a>
Information about the measurement.
Type: [MetricInfo](API_MetricInfo.md) object
Required: No

 ** Value **   <a name="servicequotas-Type-ServiceQuota-Value"></a>
The quota value.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: No

## See Also
<a name="API_ServiceQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/ServiceQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/ServiceQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/ServiceQuota)
