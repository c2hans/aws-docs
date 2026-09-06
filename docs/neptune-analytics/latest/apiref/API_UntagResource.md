---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes the specified tags from the specified resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="neptunegraph-UntagResource-request-uri-resourceArn"></a>
ARN of the resource whose tag needs to be removed.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="neptunegraph-UntagResource-request-uri-tagKeys"></a>
Tag keys for the tags to be removed.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
A failure occurred on the server.
 ** message **
A message describing the problem.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A specified resource could not be located.
 ** message **
A message describing the problem.
HTTP Status Code: 404

 ** ThrottlingException **
The exception was interrupted by throttling.
 ** message **
A message describing the problem.
HTTP Status Code: 429

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/UntagResource)
