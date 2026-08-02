---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetConnectorV2.html
---

# GetConnectorV2
<a name="API_GetConnectorV2"></a>

Grants permission to retrieve details for a connectorV2 based on connector id.

## Request Syntax
<a name="API_GetConnectorV2_RequestSyntax"></a>

```
GET /connectorsv2/{{ConnectorId+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectorV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorId](#API_GetConnectorV2_RequestSyntax) **   <a name="securityhub-GetConnectorV2-request-uri-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetConnectorV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectorV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorArn": "string",
   "ConnectorId": "string",
   "CreatedAt": "string",
   "Description": "string",
   "EnablementStatus": "string",
   "EnablementStatusReason": "string",
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
   "KmsKeyArn": "string",
   "LastUpdatedAt": "string",
   "Name": "string",
   "ProviderDetail": { ... }
}
```

## Response Elements
<a name="API_GetConnectorV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorArn](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorId](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Type: String
Pattern: `.*\S.*`

 ** [CreatedAt](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-CreatedAt"></a>
ISO 8601 UTC timestamp for the time create the connectorV2.
Type: Timestamp

 ** [Description](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-Description"></a>
The description of the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [EnablementStatus](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-EnablementStatus"></a>
The enablement status of the connector.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | FAILED_TO_ENABLE | PENDING_UPDATE | FAILED_TO_UPDATE | PENDING_DELETION | FAILED_TO_DELETE`

 ** [EnablementStatusReason](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-EnablementStatusReason"></a>
The reason for the current enablement status. Provides additional context when the connector is in a failed state.
Type: String
Pattern: `.*\S.*`

 ** [Health](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-Health"></a>
The current health status for connectorV2
Type: [HealthCheck](API_HealthCheck.md) object

 ** [KmsKeyArn](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of KMS key used for the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [LastUpdatedAt](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-LastUpdatedAt"></a>
ISO 8601 UTC timestamp for the time update the connectorV2 connectorStatus.
Type: Timestamp

 ** [Name](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-Name"></a>
The name of the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [ProviderDetail](#API_GetConnectorV2_ResponseSyntax) **   <a name="securityhub-GetConnectorV2-response-ProviderDetail"></a>
The third-party provider detail for a service configuration.
Type: [ProviderDetail](API_ProviderDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetConnectorV2_Errors"></a>

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
<a name="API_GetConnectorV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetConnectorV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetConnectorV2)
