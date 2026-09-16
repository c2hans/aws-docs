---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListStreams.html
---

# ListStreams
<a name="API_ListStreams"></a>

Retrieves information about a list of streams for a cluster.

## Request Syntax
<a name="API_ListStreams_RequestSyntax"></a>

```
GET /stream/{{clusterIdentifier}}?max-results={{maxResults}}&next-token={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStreams_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterIdentifier](#API_ListStreams_RequestSyntax) **   <a name="auroradsql-ListStreams-request-uri-clusterIdentifier"></a>
The ID of the cluster for which to list streams.
Pattern: `[a-z0-9]{26}`
Required: Yes

 ** [maxResults](#API_ListStreams_RequestSyntax) **   <a name="auroradsql-ListStreams-request-uri-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results. Default: 10.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListStreams_RequestSyntax) **   <a name="auroradsql-ListStreams-request-uri-nextToken"></a>
If your initial ListStreams operation returns a nextToken, you can include the returned nextToken in following ListStreams operations, which returns results in the next page.

## Request Body
<a name="API_ListStreams_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStreams_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "streams": [
      {
         "arn": "string",
         "clusterIdentifier": "string",
         "creationTime": number,
         "status": "string",
         "streamIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStreams_ResponseSyntax) **   <a name="auroradsql-ListStreams-response-nextToken"></a>
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.
Type: String

 ** [streams](#API_ListStreams_ResponseSyntax) **   <a name="auroradsql-ListStreams-response-streams"></a>
An array of the returned streams.
Type: Array of [StreamSummary](API_StreamSummary.md) objects

## Errors
<a name="API_ListStreams_Errors"></a>

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
<a name="API_ListStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/ListStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/ListStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/ListStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/ListStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/ListStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/ListStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/ListStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/ListStreams)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/ListStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/ListStreams)
