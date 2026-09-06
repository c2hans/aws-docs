---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConnectorV2.html
---

# CreateConnectorV2
<a name="API_CreateConnectorV2"></a>

Grants permission to create a connectorV2 based on input parameters.

## Request Syntax
<a name="API_CreateConnectorV2_RequestSyntax"></a>

```
POST /connectorsv2 HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "Name": "{{string}}",
   "Provider": { ... },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConnectorV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnectorV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-ClientToken"></a>
A unique identifier used to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[\x21-\x7E]{1,64}$`
Required: No

 ** [Description](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-Description"></a>
The description of the connectorV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [KmsKeyArn](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of KMS key used to encrypt secrets for the connectorV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-Name"></a>
The unique name of the connectorV2.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Provider](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-Provider"></a>
The third-party provider’s service configuration.
Type: [ProviderConfiguration](API_ProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Tags](#API_CreateConnectorV2_RequestSyntax) **   <a name="securityhub-CreateConnectorV2-request-Tags"></a>
The tags to add to the connectorV2 when you create.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnectorV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthUrl": "string",
   "ConnectorArn": "string",
   "ConnectorId": "string",
   "ConnectorStatus": "string",
   "EnablementStatus": "string"
}
```

## Response Elements
<a name="API_CreateConnectorV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthUrl](#API_CreateConnectorV2_ResponseSyntax) **   <a name="securityhub-CreateConnectorV2-response-AuthUrl"></a>
The Url provide to customers for OAuth auth code flow.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorArn](#API_CreateConnectorV2_ResponseSyntax) **   <a name="securityhub-CreateConnectorV2-response-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connectorV2.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorId](#API_CreateConnectorV2_ResponseSyntax) **   <a name="securityhub-CreateConnectorV2-response-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorStatus](#API_CreateConnectorV2_ResponseSyntax) **   <a name="securityhub-CreateConnectorV2-response-ConnectorStatus"></a>
The current status of the connectorV2.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`

 ** [EnablementStatus](#API_CreateConnectorV2_ResponseSyntax) **   <a name="securityhub-CreateConnectorV2-response-EnablementStatus"></a>
The enablement status of the connector after creation.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | FAILED_TO_ENABLE | PENDING_UPDATE | FAILED_TO_UPDATE | PENDING_DELETION | FAILED_TO_DELETE`

## Errors
<a name="API_CreateConnectorV2_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed the service quota limit.
HTTP Status Code: 402

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnectorV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateConnectorV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateConnectorV2)
