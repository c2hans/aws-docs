---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCapability.html
---

# GetCapability
<a name="API_GetCapability"></a>

Retrieves information about a registered capability for an OpenSearch UI application, including its configuration and current status.

## Request Syntax
<a name="API_GetCapability_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/application/{{ApplicationId}}/capability/{{CapabilityName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCapability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_GetCapability_RequestSyntax) **   <a name="opensearchservice-GetCapability-request-uri-applicationId"></a>
The unique identifier of the OpenSearch UI application.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

 ** [CapabilityName](#API_GetCapability_RequestSyntax) **   <a name="opensearchservice-GetCapability-request-uri-capabilityName"></a>
The name of the capability to retrieve information about.
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

## Request Body
<a name="API_GetCapability_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCapability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "capabilityConfig": { ... },
   "capabilityName": "string",
   "failures": [
      {
         "details": "string",
         "reason": "string"
      }
   ],
   "status": "string"
}
```

## Response Elements
<a name="API_GetCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetCapability_ResponseSyntax) **   <a name="opensearchservice-GetCapability-response-applicationId"></a>
The unique identifier of the OpenSearch UI application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [capabilityConfig](#API_GetCapability_ResponseSyntax) **   <a name="opensearchservice-GetCapability-response-capabilityConfig"></a>
The configuration settings for the capability, including capability-specific settings such as AI configuration.
Type: [CapabilityExtendedResponseConfig](API_CapabilityExtendedResponseConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [capabilityName](#API_GetCapability_ResponseSyntax) **   <a name="opensearchservice-GetCapability-response-capabilityName"></a>
The name of the capability.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [failures](#API_GetCapability_ResponseSyntax) **   <a name="opensearchservice-GetCapability-response-failures"></a>
A list of failures associated with the capability, if any. Each failure includes a reason and details about what went wrong.
Type: Array of [CapabilityFailure](API_CapabilityFailure.md) objects

 ** [status](#API_GetCapability_ResponseSyntax) **   <a name="opensearchservice-GetCapability-response-status"></a>
The current status of the capability. Possible values: `creating`, `create_failed`, `active`, `updating`, `update_failed`, `deleting`, `delete_failed`.
Type: String
Valid Values: `creating | create_failed | active | updating | update_failed | deleting | delete_failed`

## Errors
<a name="API_GetCapability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetCapability)
