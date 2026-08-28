---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds or overwrites one or more tags for the specified resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "identifier": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_TagResource_RequestSyntax) **   <a name="diagnostictools-TagResource-request-identifier"></a>
The resource ID you want to tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="diagnostictools-TagResource-request-tags"></a>
One or more tags. The value parameter is required.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Throttle error message.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal error. Try your request again later
 ** message **
Error Message
 ** retryAfterSeconds **
Second after which client can retry the transaction
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request failed because it references a resource that doesn't exist.
 ** message **
Reason for the resource not found.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 400

 ** ThrottlingException **
The request failed because it exceeded a throttling quota.
 ** message **
Throttle error message.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Second after which client can retry the transaction
 ** serviceCode **
The code for the AWS-service; that owns the quota.
HTTP Status Code: 400

 ** TooManyTagsException **
Request exceeded maximum number of tag allowed..
 ** message **
Reason for failure.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable. If more than one field caused the error, pick one and elaborate in the message.
 ** message **
Description of the error.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_TagResource_Examples"></a>

This example illustrates one usage of `TagResource`.

### Example
<a name="API_TagResource_Example_1"></a>

 **Using AWS JSON protocol (default)**

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ts.us-east-2.amazonaws.com
X-Amz-Target: Troubleshooting.TagResource
Content-Type: application/x-amz-json-1.0
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "identifier": "e-aaaaaaaaaa"
    "tags": [{
        "key": "department",
        "value": "support"
    }]
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
{}
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/troubleshooting-2023-01-01/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Diagnostic Tools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query diagnostic-tools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
