---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_FaultRootCauseService.html
---

# FaultRootCauseService
<a name="API_FaultRootCauseService"></a>

A collection of fields identifying the services in a trace summary fault.

## Contents
<a name="API_FaultRootCauseService_Contents"></a>

 ** AccountId **   <a name="xray-Type-FaultRootCauseService-AccountId"></a>
The account ID associated to the service.
Type: String
Required: No

 ** EntityPath **   <a name="xray-Type-FaultRootCauseService-EntityPath"></a>
The path of root cause entities found on the service.
Type: Array of [FaultRootCauseEntity](API_FaultRootCauseEntity.md) objects
Required: No

 ** Inferred **   <a name="xray-Type-FaultRootCauseService-Inferred"></a>
A Boolean value indicating if the service is inferred from the trace.
Type: Boolean
Required: No

 ** Name **   <a name="xray-Type-FaultRootCauseService-Name"></a>
The service name.
Type: String
Required: No

 ** Names **   <a name="xray-Type-FaultRootCauseService-Names"></a>
A collection of associated service names.
Type: Array of strings
Required: No

 ** Type **   <a name="xray-Type-FaultRootCauseService-Type"></a>
The type associated to the service.
Type: String
Required: No

## See Also
<a name="API_FaultRootCauseService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/FaultRootCauseService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/FaultRootCauseService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/FaultRootCauseService)
