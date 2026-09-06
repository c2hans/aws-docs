---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeregisterCapability.html
---

# DeregisterCapability
<a name="API_DeregisterCapability"></a>

Deregisters a capability from an OpenSearch UI application. This operation removes the capability and its associated configuration.

## Request Syntax
<a name="API_DeregisterCapability_RequestSyntax"></a>

```
DELETE /2021-01-01/opensearch/application/{{ApplicationId}}/capability/deregister/{{CapabilityName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeregisterCapability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_DeregisterCapability_RequestSyntax) **   <a name="opensearchservice-DeregisterCapability-request-uri-applicationId"></a>
The unique identifier of the OpenSearch UI application to deregister the capability from.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

 ** [CapabilityName](#API_DeregisterCapability_RequestSyntax) **   <a name="opensearchservice-DeregisterCapability-request-uri-capabilityName"></a>
The name of the capability to deregister.
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

## Request Body
<a name="API_DeregisterCapability_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeregisterCapability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_DeregisterCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeregisterCapability_ResponseSyntax) **   <a name="opensearchservice-DeregisterCapability-response-status"></a>
The status of the deregistration operation. Returns `deleting` when the capability is being removed.
Type: String
Valid Values: `creating | create_failed | active | updating | update_failed | deleting | delete_failed`

## Errors
<a name="API_DeregisterCapability_Errors"></a>

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

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DeregisterCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeregisterCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeregisterCapability)
