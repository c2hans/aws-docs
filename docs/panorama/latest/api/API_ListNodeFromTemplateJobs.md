---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListNodeFromTemplateJobs.html
---

# ListNodeFromTemplateJobs
<a name="API_ListNodeFromTemplateJobs"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of camera stream node jobs.

## Request Syntax
<a name="API_ListNodeFromTemplateJobs_RequestSyntax"></a>

```
GET /packages/template-job?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNodeFromTemplateJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListNodeFromTemplateJobs_RequestSyntax) **   <a name="panorama-ListNodeFromTemplateJobs-request-uri-MaxResults"></a>
The maximum number of node from template jobs to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NextToken](#API_ListNodeFromTemplateJobs_RequestSyntax) **   <a name="panorama-ListNodeFromTemplateJobs-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Request Body
<a name="API_ListNodeFromTemplateJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNodeFromTemplateJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "NodeFromTemplateJobs": [
      {
         "CreatedTime": number,
         "JobId": "string",
         "NodeName": "string",
         "Status": "string",
         "StatusMessage": "string",
         "TemplateType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNodeFromTemplateJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNodeFromTemplateJobs_ResponseSyntax) **   <a name="panorama-ListNodeFromTemplateJobs-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [NodeFromTemplateJobs](#API_ListNodeFromTemplateJobs_ResponseSyntax) **   <a name="panorama-ListNodeFromTemplateJobs-response-NodeFromTemplateJobs"></a>
A list of jobs.
Type: Array of [NodeFromTemplateJob](API_NodeFromTemplateJob.md) objects

## Errors
<a name="API_ListNodeFromTemplateJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListNodeFromTemplateJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListNodeFromTemplateJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListNodeFromTemplateJobs)
