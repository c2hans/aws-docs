---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConnector.html
---

# UpdateConnector
<a name="API_UpdateConnector"></a>

Updates a CSPM connector's configuration, such as the scope or regions for the connected cloud provider.

## Request Syntax
<a name="API_UpdateConnector_RequestSyntax"></a>

```
PATCH /connectors/{{ConnectorId+}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Provider": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorId](#API_UpdateConnector_RequestSyntax) **   <a name="securityhub-UpdateConnector-request-uri-ConnectorId"></a>
The unique identifier of the connector to update.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateConnector_RequestSyntax) **   <a name="securityhub-UpdateConnector-request-Description"></a>
The updated description of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Provider](#API_UpdateConnector_RequestSyntax) **   <a name="securityhub-UpdateConnector-request-Provider"></a>
The updated cloud provider configuration for the connector.
Type: [CspmProviderUpdateConfiguration](API_CspmProviderUpdateConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorStatus": "string",
   "EnablementStatus": "string"
}
```

## Response Elements
<a name="API_UpdateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorStatus](#API_UpdateConnector_ResponseSyntax) **   <a name="securityhub-UpdateConnector-response-ConnectorStatus"></a>
The connectivity status of the connector after the update.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | UNKNOWN`

 ** [EnablementStatus](#API_UpdateConnector_ResponseSyntax) **   <a name="securityhub-UpdateConnector-response-EnablementStatus"></a>
The enablement status of the connector after the update.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`

## Errors
<a name="API_UpdateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateConnector)
