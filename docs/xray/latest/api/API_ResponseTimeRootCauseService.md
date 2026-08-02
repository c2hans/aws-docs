---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ResponseTimeRootCauseService.html
---

# ResponseTimeRootCauseService
<a name="API_ResponseTimeRootCauseService"></a>

A collection of fields identifying the service in a response time warning.

## Contents
<a name="API_ResponseTimeRootCauseService_Contents"></a>

 ** AccountId **   <a name="xray-Type-ResponseTimeRootCauseService-AccountId"></a>
The account ID associated to the service.
Type: String
Required: No

 ** EntityPath **   <a name="xray-Type-ResponseTimeRootCauseService-EntityPath"></a>
The path of root cause entities found on the service.
Type: Array of [ResponseTimeRootCauseEntity](API_ResponseTimeRootCauseEntity.md) objects
Required: No

 ** Inferred **   <a name="xray-Type-ResponseTimeRootCauseService-Inferred"></a>
A Boolean value indicating if the service is inferred from the trace.
Type: Boolean
Required: No

 ** Name **   <a name="xray-Type-ResponseTimeRootCauseService-Name"></a>
The service name.
Type: String
Required: No

 ** Names **   <a name="xray-Type-ResponseTimeRootCauseService-Names"></a>
A collection of associated service names.
Type: Array of strings
Required: No

 ** Type **   <a name="xray-Type-ResponseTimeRootCauseService-Type"></a>
The type associated to the service.
Type: String
Required: No

## See Also
<a name="API_ResponseTimeRootCauseService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ResponseTimeRootCauseService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ResponseTimeRootCauseService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ResponseTimeRootCauseService)
