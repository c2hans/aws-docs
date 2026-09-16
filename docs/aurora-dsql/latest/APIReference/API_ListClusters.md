---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListClusters.html
---

# ListClusters
<a name="API_ListClusters"></a>

Retrieves information about a list of clusters.

## Request Syntax
<a name="API_ListClusters_RequestSyntax"></a>

```
GET /cluster?max-results={{maxResults}}&next-token={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListClusters_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListClusters_RequestSyntax) **   <a name="auroradsql-ListClusters-request-uri-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListClusters_RequestSyntax) **   <a name="auroradsql-ListClusters-request-uri-nextToken"></a>
If your initial ListClusters operation returns a nextToken, you can include the returned nextToken in following ListClusters operations, which returns results in the next page.

## Request Body
<a name="API_ListClusters_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListClusters_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clusters": [
      {
         "arn": "string",
         "identifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusters](#API_ListClusters_ResponseSyntax) **   <a name="auroradsql-ListClusters-response-clusters"></a>
An array of the returned clusters.
Type: Array of [ClusterSummary](API_ClusterSummary.md) objects

 ** [nextToken](#API_ListClusters_ResponseSyntax) **   <a name="auroradsql-ListClusters-response-nextToken"></a>
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.
Type: String

## Errors
<a name="API_ListClusters_Errors"></a>

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
<a name="API_ListClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dsql-2018-05-10/ListClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dsql-2018-05-10/ListClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/ListClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dsql-2018-05-10/ListClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/ListClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dsql-2018-05-10/ListClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dsql-2018-05-10/ListClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dsql-2018-05-10/ListClusters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dsql-2018-05-10/ListClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/ListClusters)
