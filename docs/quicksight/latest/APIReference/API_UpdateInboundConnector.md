---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateInboundConnector.html
---

# UpdateInboundConnector

Updates an inbound connector. You can change its name, description, status, and configuration. You can't change the connector type after the connector is created.

## Request Syntax
<a name="API_UpdateInboundConnector_RequestSyntax"></a>

```
PATCH /accounts/{{AwsAccountId}}/inbound-connectors/{{InboundConnectorId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "InboundConnectorConfiguration": {
      "InboundConnectorType": "{{string}}"
   },
   "InboundConnectorStatus": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateInboundConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [InboundConnectorId](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-uri-InboundConnectorId"></a>
The ID of the inbound connector.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateInboundConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-Description"></a>
The new description of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** [InboundConnectorConfiguration](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-InboundConnectorConfiguration"></a>
The new configuration of the inbound connector. You can't change the `InboundConnectorType`.
Type: [InboundConnectorConfig](API_InboundConnectorConfig.md) object
Required: No

 ** [InboundConnectorStatus](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-InboundConnectorStatus"></a>
The new status of the inbound connector.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Name](#API_UpdateInboundConnector_RequestSyntax) **   <a name="QS-UpdateInboundConnector-request-Name"></a>
The new name of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_UpdateInboundConnector_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "InboundConnectorId": "string",
   "InboundConnectorStatus": "string",
   "LastUpdatedTime": number,
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateInboundConnector_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-Arn"></a>
The ARN of the inbound connector.
Type: String

 ** [InboundConnectorId](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-InboundConnectorId"></a>
The ID of the inbound connector.
Type: String

 ** [InboundConnectorStatus](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-InboundConnectorStatus"></a>
The status of the inbound connector.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [LastUpdatedTime](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-LastUpdatedTime"></a>
The time when the inbound connector was last updated.
Type: Timestamp

 ** [RequestId](#API_UpdateInboundConnector_ResponseSyntax) **   <a name="QS-UpdateInboundConnector-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateInboundConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateInboundConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateInboundConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateInboundConnector)
