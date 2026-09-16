---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListBaselines.html
---

# ListBaselines
<a name="API_ListBaselines"></a>

Returns a summary list of all available baselines. For usage examples, see [*the AWS Control Tower User Guide*](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html).

## Request Syntax
<a name="API_ListBaselines_RequestSyntax"></a>

```
POST /list-baselines HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBaselines_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListBaselines_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBaselines_RequestSyntax) **   <a name="controltower-ListBaselines-request-maxResults"></a>
The maximum number of results to be shown.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListBaselines_RequestSyntax) **   <a name="controltower-ListBaselines-request-nextToken"></a>
A pagination token.
Type: String
Required: No

## Response Syntax
<a name="API_ListBaselines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "baselines": [
      {
         "arn": "string",
         "description": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBaselines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baselines](#API_ListBaselines_ResponseSyntax) **   <a name="controltower-ListBaselines-response-baselines"></a>
A list of `Baseline` object details.
Type: Array of [BaselineSummary](API_BaselineSummary.md) objects

 ** [nextToken](#API_ListBaselines_ResponseSyntax) **   <a name="controltower-ListBaselines-response-nextToken"></a>
A pagination token.
Type: String

## Errors
<a name="API_ListBaselines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListBaselines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListBaselines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListBaselines)
