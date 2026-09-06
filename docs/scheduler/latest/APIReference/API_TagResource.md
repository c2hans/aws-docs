---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Assigns one or more tags (key-value pairs) to the specified EventBridge Scheduler resource. You can only assign tags to schedule groups.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="scheduler-TagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the schedule group that you are adding tags to.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="scheduler-TagResource-request-Tags"></a>
The list of tags to associate with the schedule group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/TagResource)
