---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateInboundConnector.html
---

# CreateInboundConnector

Creates an inbound connector in a Quick Sight account. An inbound connector is the endpoint that an external client, such as the Quick Sight desktop application, uses to reach Quick Sight in your account.

Your users authenticate through the access control applications that are associated with the connector. To manage these associations, use `UpdateInboundConnectorApplicationAssociations`.

An account can have one `QUICK_DESKTOP` inbound connector in each Region.

## Request Syntax
<a name="API_CreateInboundConnector_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/inbound-connectors HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "InboundConnectorConfiguration": {
      "InboundConnectorType": "{{string}}"
   },
   "InboundConnectorId": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateInboundConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateInboundConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InboundConnectorConfiguration](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-InboundConnectorConfiguration"></a>
The configuration of the inbound connector.
Type: [InboundConnectorConfig](API_InboundConnectorConfig.md) object
Required: Yes

 ** [InboundConnectorId](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-InboundConnectorId"></a>
The ID for the inbound connector. This ID is unique per AWS Region for each AWS account.
For a `QUICK_DESKTOP` inbound connector, the ID must be `ibc-desktop-` followed by your AWS account ID and the Region that you call, separated by a hyphen. For example, `ibc-desktop-111122223333-us-east-1`. Quick Sight reserves IDs that start with `ibc-desktop-` for `QUICK_DESKTOP` inbound connectors.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [Name](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-Name"></a>
The name of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [Description](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-Description"></a>
The description of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** [Tags](#API_CreateInboundConnector_RequestSyntax) **   <a name="QS-CreateInboundConnector-request-Tags"></a>
The tags to assign to the inbound connector.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateInboundConnector_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "InboundConnectorId": "string",
   "InboundConnectorStatus": "string",
   "RequestId": "string",
   "TenantUrl": "string"
}
```

## Response Elements
<a name="API_CreateInboundConnector_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-Arn"></a>
The ARN of the inbound connector.
Type: String

 ** [CreatedTime](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-CreatedTime"></a>
The time when the inbound connector was created.
Type: Timestamp

 ** [InboundConnectorId](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-InboundConnectorId"></a>
The ID of the inbound connector.
Type: String

 ** [InboundConnectorStatus](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-InboundConnectorStatus"></a>
The status of the inbound connector. A new connector is always `ENABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [RequestId](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TenantUrl](#API_CreateInboundConnector_ResponseSyntax) **   <a name="QS-CreateInboundConnector-response-TenantUrl"></a>
The endpoint URL that clients use to reach Quick Sight through the inbound connector.
Type: String

## Errors
<a name="API_CreateInboundConnector_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

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
<a name="API_CreateInboundConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateInboundConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateInboundConnector)
