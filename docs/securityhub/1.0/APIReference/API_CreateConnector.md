---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateConnector.html
---

# CreateConnector
<a name="API_CreateConnector"></a>

Creates a connector to a third-party cloud provider in Security Hub CSPM. A connector establishes a connection between Security Hub CSPM and a third-party cloud provider, enabling Security Hub CSPM to ingest security findings and resource data from the connected environment.

## Request Syntax
<a name="API_CreateConnector_RequestSyntax"></a>

```
POST /connectors HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Provider": { ... },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateConnector_RequestSyntax) **   <a name="securityhub-CreateConnector-request-ClientToken"></a>
A unique identifier used to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[\x21-\x7E]{1,64}$`
Required: No

 ** [Description](#API_CreateConnector_RequestSyntax) **   <a name="securityhub-CreateConnector-request-Description"></a>
The description of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_CreateConnector_RequestSyntax) **   <a name="securityhub-CreateConnector-request-Name"></a>
The name of the connector. Must be unique within the account.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Provider](#API_CreateConnector_RequestSyntax) **   <a name="securityhub-CreateConnector-request-Provider"></a>
The configuration for the cloud provider to connect to. Currently supports Azure.
Type: [CspmProviderConfiguration](API_CspmProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Tags](#API_CreateConnector_RequestSyntax) **   <a name="securityhub-CreateConnector-request-Tags"></a>
The tags to add to the connector resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectorArn": "string",
   "ConnectorId": "string",
   "ConnectorStatus": "string",
   "EnablementStatus": "string"
}
```

## Response Elements
<a name="API_CreateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorArn](#API_CreateConnector_ResponseSyntax) **   <a name="securityhub-CreateConnector-response-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorId](#API_CreateConnector_ResponseSyntax) **   <a name="securityhub-CreateConnector-response-ConnectorId"></a>
The unique identifier of the connector.
Type: String
Pattern: `.*\S.*`

 ** [ConnectorStatus](#API_CreateConnector_ResponseSyntax) **   <a name="securityhub-CreateConnector-response-ConnectorStatus"></a>
The connectivity status of the connector.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | UNKNOWN`

 ** [EnablementStatus](#API_CreateConnector_ResponseSyntax) **   <a name="securityhub-CreateConnector-response-EnablementStatus"></a>
The enablement status of the connector.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`

## Errors
<a name="API_CreateConnector_Errors"></a>

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
<a name="API_CreateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateConnector)
