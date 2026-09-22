---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageScanFindingAggregations.html
---

# ListImageScanFindingAggregations
<a name="API_ListImageScanFindingAggregations"></a>

Returns a list of image scan aggregations for your account. You can filter by the type of key that Image Builder uses to group results. For example, if you want to get a list of findings by severity level for one of your pipelines, you might specify your pipeline with the `imagePipelineArn` filter. If you don't specify a filter, Image Builder returns an aggregation for your account.

To streamline results, you can use the following filters in your request:
+  `imageBuildVersionArn`
+  `imagePipelineArn`
+  `vulnerabilityId`

## Request Syntax
<a name="API_ListImageScanFindingAggregations_RequestSyntax"></a>

```
POST /ListImageScanFindingAggregations HTTP/1.1
Content-type: application/json

{
   "filter": {
      "name": "{{string}}",
      "values": [ "{{string}}" ]
   },
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImageScanFindingAggregations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImageScanFindingAggregations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListImageScanFindingAggregations_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-request-filter"></a>
A filter name and value pair that determines the type of aggregation that Image Builder returns. Use one of the following filter names:
+  `imageBuildVersionArn`
+  `imagePipelineArn`
+  `vulnerabilityId`
If you don't specify a filter, Image Builder returns an aggregation for your account.
Type: [Filter](API_Filter.md) object
Required: No

 ** [nextToken](#API_ListImageScanFindingAggregations_RequestSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListImageScanFindingAggregations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationType": "string",
   "nextToken": "string",
   "requestId": "string",
   "responses": [
      {
         "accountAggregation": {
            "accountId": "string",
            "severityCounts": {
               "all": number,
               "critical": number,
               "high": number,
               "medium": number
            }
         },
         "imageAggregation": {
            "imageBuildVersionArn": "string",
            "severityCounts": {
               "all": number,
               "critical": number,
               "high": number,
               "medium": number
            }
         },
         "imagePipelineAggregation": {
            "imagePipelineArn": "string",
            "severityCounts": {
               "all": number,
               "critical": number,
               "high": number,
               "medium": number
            }
         },
         "vulnerabilityIdAggregation": {
            "severityCounts": {
               "all": number,
               "critical": number,
               "high": number,
               "medium": number
            },
            "vulnerabilityId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListImageScanFindingAggregations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationType](#API_ListImageScanFindingAggregations_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-response-aggregationType"></a>
The aggregation type specifies what type of key is used to group the image scan findings. Image Builder returns results based on the request filter. If you didn't specify a filter in the request, the type defaults to `accountId`.

**Aggregation types**
+ accountId
+ imageBuildVersionArn
+ imagePipelineArn
+ vulnerabilityId
Each aggregation includes counts by severity level for medium severity and higher level findings, plus a total for all of the findings for each key value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [nextToken](#API_ListImageScanFindingAggregations_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListImageScanFindingAggregations_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [responses](#API_ListImageScanFindingAggregations_ResponseSyntax) **   <a name="imagebuilder-ListImageScanFindingAggregations-response-responses"></a>
An array of image scan finding aggregations that match the filter criteria.
Type: Array of [ImageScanFindingAggregation](API_ImageScanFindingAggregation.md) objects

## Errors
<a name="API_ListImageScanFindingAggregations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListImageScanFindingAggregations_Examples"></a>

### List image scan finding aggregations for an image pipeline
<a name="API_ListImageScanFindingAggregations_Example_1"></a>

The following example aggregates vulnerability findings for images that the specified pipeline created, with counts grouped by severity level.

#### Sample Request
<a name="API_ListImageScanFindingAggregations_Example_1_Request"></a>

```
POST /ListImageScanFindingAggregations HTTP/1.1
Content-type: application/json

{
    "filter": {
        "name": "imagePipelineArn",
        "values": [
            "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline"
        ]
    }
}
```

#### Sample Response
<a name="API_ListImageScanFindingAggregations_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "b1c9dd23-7a9c-4a52-a1f7-3b8e9e17b2c4",
    "aggregationType": "imagePipelineArn",
    "responses": [
        {
            "imagePipelineAggregation": {
                "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
                "severityCounts": {
                    "all": 25,
                    "critical": 1,
                    "high": 7,
                    "medium": 12
                }
            }
        }
    ]
}
```

## See Also
<a name="API_ListImageScanFindingAggregations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListImageScanFindingAggregations)
