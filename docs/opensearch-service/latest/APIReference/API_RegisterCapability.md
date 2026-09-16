---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RegisterCapability.html
---

# RegisterCapability
<a name="API_RegisterCapability"></a>

Registers a capability for an OpenSearch UI application. Use this operation to enable specific capabilities, such as AI features, for a given application. The capability configuration defines the type and settings of the capability to register. For more information about the AI features, see [Agentic AI for OpenSearch UI](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-ai-assistant.html).

## Request Syntax
<a name="API_RegisterCapability_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application/{{ApplicationId}}/capability/register HTTP/1.1
Content-type: application/json

{
   "capabilityConfig": { ... },
   "capabilityName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterCapability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_RegisterCapability_RequestSyntax) **   <a name="opensearchservice-RegisterCapability-request-uri-applicationId"></a>
The unique identifier of the OpenSearch UI application to register the capability for.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_RegisterCapability_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capabilityConfig](#API_RegisterCapability_RequestSyntax) **   <a name="opensearchservice-RegisterCapability-request-capabilityConfig"></a>
The configuration settings for the capability being registered. This includes capability-specific settings such as AI configuration.
Type: [CapabilityBaseRequestConfig](API_CapabilityBaseRequestConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [capabilityName](#API_RegisterCapability_RequestSyntax) **   <a name="opensearchservice-RegisterCapability-request-capabilityName"></a>
The name of the capability to register. Must be between 3 and 30 characters and contain only alphanumeric characters and hyphens. This identifies the type of capability being enabled for the application. For registering AI Assistant capability, use `ai-capability`
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

## Response Syntax
<a name="API_RegisterCapability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "capabilityConfig": { ... },
   "capabilityName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_RegisterCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_RegisterCapability_ResponseSyntax) **   <a name="opensearchservice-RegisterCapability-response-applicationId"></a>
The unique identifier of the OpenSearch UI application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [capabilityConfig](#API_RegisterCapability_ResponseSyntax) **   <a name="opensearchservice-RegisterCapability-response-capabilityConfig"></a>
The configuration settings for the registered capability.
Type: [CapabilityBaseResponseConfig](API_CapabilityBaseResponseConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [capabilityName](#API_RegisterCapability_ResponseSyntax) **   <a name="opensearchservice-RegisterCapability-response-capabilityName"></a>
The name of the registered capability.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [status](#API_RegisterCapability_ResponseSyntax) **   <a name="opensearchservice-RegisterCapability-response-status"></a>
The current status of the capability. Possible values: `creating`, `create_failed`, `active`, `updating`, `update_failed`, `deleting`, `delete_failed`.
Type: String
Valid Values: `creating | create_failed | active | updating | update_failed | deleting | delete_failed`

## Errors
<a name="API_RegisterCapability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
An exception for when a request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_RegisterCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/RegisterCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RegisterCapability)
