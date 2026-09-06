---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds tags to a Lambda MicroVM resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /2017-03-31/tags/{{Resource}} HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Resource](#API_TagResource_RequestSyntax) **   <a name="lambdamicrovm-TagResource-request-uri-Resource"></a>
The ARN of the resource to tag.
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:(function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?|layer:([a-zA-Z0-9-_]+)|code-signing-config:csc-[a-z0-9]{17}|event-source-mapping:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}|(capacity-provider|network-connector|microvm-image):[a-zA-Z0-9-_]+)`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="lambdamicrovm-TagResource-request-Tags"></a>
The key-value pairs of tags to add to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda MicroVMs service encountered an internal error.
 ** Type **
The exception type.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. Retry the request later.
 ** Type **
The exception type.
HTTP Status Code: 429

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/TagResource)
