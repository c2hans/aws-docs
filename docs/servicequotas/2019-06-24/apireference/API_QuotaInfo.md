---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaInfo.html
---

# QuotaInfo
<a name="API_QuotaInfo"></a>

Information on your Service Quotas for [Service Quotas Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html). Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.

## Contents
<a name="API_QuotaInfo_Contents"></a>

 ** QuotaCode **   <a name="servicequotas-Type-QuotaInfo-QuotaCode"></a>
The Service Quotas code for the AWS service monitored with Automatic Management.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** QuotaName **   <a name="servicequotas-Type-QuotaInfo-QuotaName"></a>
The Service Quotas name for the AWS service monitored with Automatic Management.
Type: String
Required: No

## See Also
<a name="API_QuotaInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/QuotaInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/QuotaInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/QuotaInfo)
