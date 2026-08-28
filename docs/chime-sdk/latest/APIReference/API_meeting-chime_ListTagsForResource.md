---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_meeting-chime_ListTagsForResource"></a>

Returns a list of the tags available for the specified resource.

## Request Syntax
<a name="API_meeting-chime_ListTagsForResource_RequestSyntax"></a>

```
GET /tags?arn={{ResourceARN}} HTTP/1.1
```

## URI Request Parameters
<a name="API_meeting-chime_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceARN](#API_meeting-chime_ListTagsForResource_RequestSyntax) **   <a name="chimesdk-meeting-chime_ListTagsForResource-request-uri-ResourceARN"></a>
The ARN of the resource.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.*`
Required: Yes

## Request Body
<a name="API_meeting-chime_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_meeting-chime_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_meeting-chime_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_meeting-chime_ListTagsForResource_ResponseSyntax) **   <a name="chimesdk-meeting-chime_ListTagsForResource-response-Tags"></a>
The tags requested for the specified resource.
Type: Array of [Tag](API_meeting-chime_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_meeting-chime_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** LimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource that you want to tag couldn't be found.
 ** RequestId **
The ID of the resource that couldn't be found.
 ** ResourceName **
The name of the resource that couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The ID of the failed request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request id associated with the call responsible for the exception.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 503

 ** ThrottlingException **
The number of customer requests exceeds the request rate limit.
 ** RequestId **
The ID of the request that exceeded the throttling limit.
HTTP Status Code: 429

 ** UnauthorizedException **
The user isn't authorized to request a resource.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 401

## See Also
<a name="API_meeting-chime_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/ListTagsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
