---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetDataGrant.html
---

# GetDataGrant
<a name="API_GetDataGrant"></a>

This operation returns information about a data grant.

## Request Syntax
<a name="API_GetDataGrant_RequestSyntax"></a>

```
GET /v1/data-grants/{{DataGrantId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataGrantId](#API_GetDataGrant_RequestSyntax) **   <a name="dataexchange-GetDataGrant-request-uri-DataGrantId"></a>
The ID of the data grant.
Pattern: `[a-zA-Z0-9]{30,40}$|^arn:aws:dataexchange:[\-a-z0-9]*:(\d{12}):data-grants\/[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_GetDataGrant_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataGrant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AcceptanceState": "string",
   "AcceptedAt": "string",
   "Arn": "string",
   "CreatedAt": "string",
   "DataSetId": "string",
   "Description": "string",
   "EndsAt": "string",
   "GrantDistributionScope": "string",
   "Id": "string",
   "Name": "string",
   "ReceiverPrincipal": "string",
   "SenderPrincipal": "string",
   "SourceDataSetId": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_GetDataGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcceptanceState](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-AcceptanceState"></a>
The acceptance state of the data grant.
Type: String
Valid Values: `PENDING_RECEIVER_ACCEPTANCE | ACCEPTED`

 ** [AcceptedAt](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-AcceptedAt"></a>
The timestamp of when the data grant was accepted.
Type: Timestamp

 ** [Arn](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-Arn"></a>
The Amazon Resource Name (ARN) of the data grant.
Type: String

 ** [CreatedAt](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-CreatedAt"></a>
The timestamp of when the data grant was created.
Type: Timestamp

 ** [DataSetId](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-DataSetId"></a>
The ID of the data set associated to the data grant.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Description](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-Description"></a>
The description of the data grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.

 ** [EndsAt](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-EndsAt"></a>
The timestamp of when access to the associated data set ends.
Type: Timestamp

 ** [GrantDistributionScope](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-GrantDistributionScope"></a>
The distribution scope for the data grant.
Type: String
Valid Values: `AWS_ORGANIZATION | NONE`

 ** [Id](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-Id"></a>
The ID of the data grant.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Name](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-Name"></a>
The name of the data grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ReceiverPrincipal](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-ReceiverPrincipal"></a>
The AWS account ID of the data grant receiver.
Type: String
Pattern: `\d{12}`

 ** [SenderPrincipal](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-SenderPrincipal"></a>
The AWS account ID of the data grant sender.
Type: String
Pattern: `\d{12}`

 ** [SourceDataSetId](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-SourceDataSetId"></a>
The ID of the data set used to create the data grant.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Tags](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-Tags"></a>
The tags associated to the data grant. A tag is a key-value pair.
Type: String to string map

 ** [UpdatedAt](#API_GetDataGrant_ResponseSyntax) **   <a name="dataexchange-GetDataGrant-response-UpdatedAt"></a>
The timestamp of when the data grant was last updated.
Type: Timestamp

## Errors
<a name="API_GetDataGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_GetDataGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/GetDataGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/GetDataGrant)
