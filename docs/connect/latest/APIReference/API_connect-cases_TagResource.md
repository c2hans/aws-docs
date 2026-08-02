---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_TagResource.html
---

# TagResource
<a name="API_connect-cases_TagResource"></a>

Adds tags to a resource.

## Request Syntax
<a name="API_connect-cases_TagResource_RequestSyntax"></a>

```
POST /tags/{{arn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-cases_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_connect-cases_TagResource_RequestSyntax) **   <a name="connect-connect-cases_TagResource-request-uri-arn"></a>
The Amazon Resource Name (ARN)
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_connect-cases_TagResource_RequestSyntax) **   <a name="connect-connect-cases_TagResource-request-tags"></a>
A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Required: Yes

## Response Syntax
<a name="API_connect-cases_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_TagResource_Examples"></a>

### Request and Response example
<a name="API_connect-cases_TagResource_Example_1"></a>

This example illustrates one usage of TagResource.

```
{
  "tags": {
  "some_key": "some_value"
  }
}
```

```
{ }
```

## See Also
<a name="API_connect-cases_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/TagResource)
