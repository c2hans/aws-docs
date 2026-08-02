---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ServiceInfo.html
---

# ServiceInfo
<a name="API_ServiceInfo"></a>

Information about an AWS service.

## Contents
<a name="API_ServiceInfo_Contents"></a>

 ** ServiceCode **   <a name="servicequotas-Type-ServiceInfo-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** ServiceName **   <a name="servicequotas-Type-ServiceInfo-ServiceName"></a>
Specifies the service name.
Type: String
Required: No

## See Also
<a name="API_ServiceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/ServiceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/ServiceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/ServiceInfo)
