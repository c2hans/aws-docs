---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds tags to the specified resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="neptunegraph-TagResource-request-uri-resourceArn"></a>
ARN of the resource for which tags need to be added.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="neptunegraph-TagResource-request-tags"></a>
The tags to be assigned to the Neptune Analytics resource.
The tags are metadata that are specified as a list of key-value pairs:
 **Key** (string)   –   A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length. It can't be prefixed with `aws:` and can only contain the set of Unicode characters specified by this Java regular expression: `"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")`.
 **Value** (string)   –   A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. It can't be prefixed with `aws:` and can only contain the set of Unicode characters specified by this Java regular expression: `"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
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
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/TagResource)
