---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConnector.html
---

# GetConnector
<a name="API_GetConnector"></a>

Retrieves details for a CSPM connector based on the connector ID.

## Request Syntax
<a name="API_GetConnector_RequestSyntax"></a>

```
GET /connectors/{{ConnectorId+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorId](#API_GetConnector_RequestSyntax) **   <a name="securityhub-GetConnector-request-uri-ConnectorId"></a>
The unique identifier of the connector to retrieve.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorArn": "string",
   "ConnectorId": "string",
   "CreatedAt": "string",
   "CreatedBy": "string",
   "Description": "string",
   "EnablementStatus": "string",
   "Health": {
      "ConnectorStatus": "string",
      "Issues": [
         {
            "Code": "string",
            "Message": "string"
         }
      ],
      "LastCheckedAt": "string",
      "Message": "string"
   },
   "LastUpdatedAt": "string",
   "Name": "string",
   "ProviderDetail": { ... }
}
```

## Response Elements
<a name="API_GetConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorArn](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorId](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-ConnectorId"></a>
The unique identifier of the connector.
Type: String
Pattern: `.*\S.*`

 ** [CreatedAt](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-CreatedAt"></a>
The ISO 8601 UTC timestamp indicating when the connector was created.
Type: Timestamp

 ** [CreatedBy](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-CreatedBy"></a>
The service principal that created the connector.
Type: String
Pattern: `.*\S.*`

 ** [Description](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-Description"></a>
The description of the connector.
Type: String
Pattern: `.*\S.*`

 ** [EnablementStatus](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-EnablementStatus"></a>
The enablement status of the connector.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`

 ** [Health](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-Health"></a>
The health status of the connector, including connectivity status and last check time.
Type: [CspmHealthCheck](API_CspmHealthCheck.md) object

 ** [LastUpdatedAt](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-LastUpdatedAt"></a>
The ISO 8601 UTC timestamp indicating when the connector was last updated.
Type: Timestamp

 ** [Name](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-Name"></a>
The name of the connector.
Type: String
Pattern: `.*\S.*`

 ** [ProviderDetail](#API_GetConnector_ResponseSyntax) **   <a name="securityhub-GetConnector-response-ProviderDetail"></a>
The cloud provider configuration details for the connector.
Type: [CspmProviderDetail](API_CspmProviderDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetConnector_Errors"></a>

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
<a name="API_GetConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetConnector)
