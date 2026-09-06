---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html
---

# BatchUpdateRecommendationResourceExclusion
<a name="API_BatchUpdateRecommendationResourceExclusion"></a>

Update one or more exclusion statuses for a list of recommendation resources. This API supports up to 25 unique recommendation resource ARNs per request. This API currently doesn't support prioritized recommendation resources. This API updates global recommendations, eliminating the need to call the API in each AWS Region. After submitting an exclusion update, note that it might take a few minutes for the changes to be reflected in the system.

## Request Syntax
<a name="API_BatchUpdateRecommendationResourceExclusion_RequestSyntax"></a>

```
PUT /v1/batch-update-recommendation-resource-exclusion HTTP/1.1
Content-type: application/json

{
   "recommendationResourceExclusions": [
      {
         "arn": "{{string}}",
         "isExcluded": {{boolean}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateRecommendationResourceExclusion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateRecommendationResourceExclusion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recommendationResourceExclusions](#API_BatchUpdateRecommendationResourceExclusion_RequestSyntax) **   <a name="ta-BatchUpdateRecommendationResourceExclusion-request-recommendationResourceExclusions"></a>
A list of recommendation resource ARNs and exclusion status to update
Type: Array of [RecommendationResourceExclusion](API_RecommendationResourceExclusion.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateRecommendationResourceExclusion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchUpdateRecommendationResourceExclusionErrors": [
      {
         "arn": "string",
         "errorCode": "string",
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateRecommendationResourceExclusion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchUpdateRecommendationResourceExclusionErrors](#API_BatchUpdateRecommendationResourceExclusion_ResponseSyntax) **   <a name="ta-BatchUpdateRecommendationResourceExclusion-response-batchUpdateRecommendationResourceExclusionErrors"></a>
A list of recommendation resource ARNs whose exclusion status failed to update, if any
Type: Array of [UpdateRecommendationResourceExclusionError](API_UpdateRecommendationResourceExclusionError.md) objects

## Errors
<a name="API_BatchUpdateRecommendationResourceExclusion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Exception that access has been denied due to insufficient access
HTTP Status Code: 403

 ** ConflictException **
Exception that the request was denied due to conflictions in state
HTTP Status Code: 409

 ** InternalServerException **
Exception to notify that an unexpected internal error occurred during processing of the request
HTTP Status Code: 500

 ** ThrottlingException **
Exception to notify that requests are being throttled
HTTP Status Code: 429

 ** ValidationException **
Exception that the request failed to satisfy service constraints
HTTP Status Code: 400

## Examples
<a name="API_BatchUpdateRecommendationResourceExclusion_Examples"></a>

### Update one or more exclusion status for a list of recommendation resources
<a name="API_BatchUpdateRecommendationResourceExclusion_Example_1"></a>

Batch update one or more exclusion status for a list of recommendation resources

#### Sample Request
<a name="API_BatchUpdateRecommendationResourceExclusion_Example_1_Request"></a>

```
{
                    "recommendationResourceExclusions": [
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010",
                    "isExcluded": true
                    }
                    ]
                    }
```

#### Sample Response
<a name="API_BatchUpdateRecommendationResourceExclusion_Example_1_Response"></a>

```
{
                    "batchUpdateRecommendationResourceExclusionErrors": [
                    {
                    "arn": "arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010",
                    "errorCode": "404",
                    "errorMessage": "Exception that the requested resource has not been found"
                    }
                    ]
                    }
```

## See Also
<a name="API_BatchUpdateRecommendationResourceExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion)
