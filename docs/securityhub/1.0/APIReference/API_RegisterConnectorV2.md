---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RegisterConnectorV2.html
---

# RegisterConnectorV2
<a name="API_RegisterConnectorV2"></a>

Grants permission to complete the authorization based on input parameters.

## Request Syntax
<a name="API_RegisterConnectorV2_RequestSyntax"></a>

```
POST /connectorsv2/register HTTP/1.1
Content-type: application/json

{
   "AuthCode": "{{string}}",
   "AuthState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterConnectorV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterConnectorV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthCode](#API_RegisterConnectorV2_RequestSyntax) **   <a name="securityhub-RegisterConnectorV2-request-AuthCode"></a>
The authCode retrieved from authUrl to complete the OAuth 2.0 authorization code flow.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [AuthState](#API_RegisterConnectorV2_RequestSyntax) **   <a name="securityhub-RegisterConnectorV2-request-AuthState"></a>
The authState retrieved from authUrl to complete the OAuth 2.0 authorization code flow.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_RegisterConnectorV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorArn": "string",
   "ConnectorId": "string"
}
```

## Response Elements
<a name="API_RegisterConnectorV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorArn](#API_RegisterConnectorV2_ResponseSyntax) **   <a name="securityhub-RegisterConnectorV2-response-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorId](#API_RegisterConnectorV2_ResponseSyntax) **   <a name="securityhub-RegisterConnectorV2-response-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_RegisterConnectorV2_Errors"></a>

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
<a name="API_RegisterConnectorV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/RegisterConnectorV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RegisterConnectorV2)
