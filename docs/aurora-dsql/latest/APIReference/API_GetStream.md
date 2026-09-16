---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetStream.html
---

# GetStream
<a name="API_GetStream"></a>

Retrieves information about a stream.

## Request Syntax
<a name="API_GetStream_RequestSyntax"></a>

```
GET /stream/{{clusterIdentifier}}/{{streamIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterIdentifier](#API_GetStream_RequestSyntax) **   <a name="auroradsql-GetStream-request-uri-clusterIdentifier"></a>
The ID of the cluster containing the stream to retrieve.
Pattern: `[a-z0-9]{26}`
Required: Yes

 ** [streamIdentifier](#API_GetStream_RequestSyntax) **   <a name="auroradsql-GetStream-request-uri-streamIdentifier"></a>
The ID of the stream to retrieve.
Pattern: `[a-z0-9]{26}`
Required: Yes

## Request Body
<a name="API_GetStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "clusterIdentifier": "string",
   "creationTime": number,
   "format": "string",
   "ordering": "string",
   "status": "string",
   "statusReason": {
      "error": "string",
      "updatedAt": number
   },
   "streamIdentifier": "string",
   "tags": {
      "string" : "string"
   },
   "targetDefinition": { ... }
}
```

## Response Elements
<a name="API_GetStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-arn"></a>
The ARN of the retrieved stream.
Type: String
Pattern: `arn:aws(-[^:]+)?:dsql:[a-z0-9-]{1,20}:[0-9]{12}:cluster/[a-z0-9]{26}/stream/[a-z0-9]{26}`

 ** [clusterIdentifier](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-clusterIdentifier"></a>
The ID of the cluster for the retrieved stream.
Type: String
Pattern: `[a-z0-9]{26}`

 ** [creationTime](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-creationTime"></a>
The time when the stream was created.
Type: Timestamp

 ** [format](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-format"></a>
The format of the stream records.
Type: String
Valid Values: `JSON`

 ** [ordering](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-ordering"></a>
The ordering mode of the stream.
Type: String
Valid Values: `UNORDERED`

 ** [status](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-status"></a>
The current status of the retrieved stream.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | FAILED | IMPAIRED`

 ** [statusReason](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-statusReason"></a>
Stream status reason with error code and timestamp (if applicable).
Type: [StatusReason](API_StatusReason.md) object

 ** [streamIdentifier](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-streamIdentifier"></a>
The ID of the retrieved stream.
Type: String
Pattern: `[a-z0-9]{26}`

 ** [tags](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-tags"></a>
A map of tags associated with the stream.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.:/=+\-@ ]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9_.:/=+\-@ ]*`

 ** [targetDefinition](#API_GetStream_ResponseSyntax) **   <a name="auroradsql-GetStream-response-targetDefinition"></a>
The target definition for the stream destination.
Type: [TargetDefinition](API_TargetDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
Retry after seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceId **
The resource ID could not be found.
 ** resourceType **
The resource type could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
The message that the request was denied due to request throttling.
 ** quotaCode **
The request exceeds a request rate quota.
 ** retryAfterSeconds **
The request exceeds a request rate quota. Retry after seconds.
 ** serviceCode **
The request exceeds a service quota.
HTTP Status Code: 429

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/GetStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/GetStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/GetStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/GetStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/GetStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/GetStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/GetStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/GetStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/GetStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/GetStream)
