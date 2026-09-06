---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ErrorRootCauseService.html
---

# ErrorRootCauseService
<a name="API_ErrorRootCauseService"></a>

A collection of fields identifying the services in a trace summary error.

## Contents
<a name="API_ErrorRootCauseService_Contents"></a>

 ** AccountId **   <a name="xray-Type-ErrorRootCauseService-AccountId"></a>
The account ID associated to the service.
Type: String
Required: No

 ** EntityPath **   <a name="xray-Type-ErrorRootCauseService-EntityPath"></a>
The path of root cause entities found on the service.
Type: Array of [ErrorRootCauseEntity](API_ErrorRootCauseEntity.md) objects
Required: No

 ** Inferred **   <a name="xray-Type-ErrorRootCauseService-Inferred"></a>
A Boolean value indicating if the service is inferred from the trace.
Type: Boolean
Required: No

 ** Name **   <a name="xray-Type-ErrorRootCauseService-Name"></a>
The service name.
Type: String
Required: No

 ** Names **   <a name="xray-Type-ErrorRootCauseService-Names"></a>
A collection of associated service names.
Type: Array of strings
Required: No

 ** Type **   <a name="xray-Type-ErrorRootCauseService-Type"></a>
The type associated to the service.
Type: String
Required: No

## See Also
<a name="API_ErrorRootCauseService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ErrorRootCauseService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ErrorRootCauseService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ErrorRootCauseService)
