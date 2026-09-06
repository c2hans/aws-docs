---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetClustersForImage.html
---

# GetClustersForImage
<a name="API_GetClustersForImage"></a>

Returns a list of clusters and metadata associated with an image.

## Request Syntax
<a name="API_GetClustersForImage_RequestSyntax"></a>

```
POST /cluster/get HTTP/1.1
Content-type: application/json

{
   "filter": {
      "resourceId": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetClustersForImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetClustersForImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_GetClustersForImage_RequestSyntax) **   <a name="inspector2-GetClustersForImage-request-filter"></a>
The resource Id for the Amazon ECR image.
Type: [ClusterForImageFilterCriteria](API_ClusterForImageFilterCriteria.md) object
Required: Yes

 ** [maxResults](#API_GetClustersForImage_RequestSyntax) **   <a name="inspector2-GetClustersForImage-request-maxResults"></a>
The maximum number of results to be returned in a single page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetClustersForImage_RequestSyntax) **   <a name="inspector2-GetClustersForImage-request-nextToken"></a>
The pagination token from a previous request used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

## Response Syntax
<a name="API_GetClustersForImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cluster": [
      {
         "clusterArn": "string",
         "clusterDetails": [
            {
               "clusterMetadata": { ... },
               "lastInUse": number,
               "runningUnitCount": number,
               "stoppedUnitCount": number
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetClustersForImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_GetClustersForImage_ResponseSyntax) **   <a name="inspector2-GetClustersForImage-response-cluster"></a>
A unit of work inside of a cluster, which can include metadata about the cluster.
Type: Array of [ClusterInformation](API_ClusterInformation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [nextToken](#API_GetClustersForImage_ResponseSyntax) **   <a name="inspector2-GetClustersForImage-response-nextToken"></a>
The pagination token from a previous request used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.

## Errors
<a name="API_GetClustersForImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetClustersForImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetClustersForImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetClustersForImage)
