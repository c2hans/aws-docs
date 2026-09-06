---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteConnector.html
---

# DeleteConnector
<a name="API_DeleteConnector"></a>

Deletes a CSPM connector. When you delete a connector, Security Hub CSPM stops ingesting findings and resource data from the connected cloud provider environment.

## Request Syntax
<a name="API_DeleteConnector_RequestSyntax"></a>

```
DELETE /connectors/{{ConnectorId+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorId](#API_DeleteConnector_RequestSyntax) **   <a name="securityhub-DeleteConnector-request-uri-ConnectorId"></a>
The unique identifier of the connector to delete.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DeleteConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EnablementStatus": "string"
}
```

## Response Elements
<a name="API_DeleteConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnablementStatus](#API_DeleteConnector_ResponseSyntax) **   <a name="securityhub-DeleteConnector-response-EnablementStatus"></a>
The enablement status of the connector after the delete request.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`

## Errors
<a name="API_DeleteConnector_Errors"></a>

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
<a name="API_DeleteConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DeleteConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DeleteConnector)
