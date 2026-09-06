---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds the specified tags to the specified resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="savingsplans-TagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Pattern: `arn:aws:[a-z]+:([a-z]{2}-[a-z]+-\d{1}|):(\d{12}):savingsplan\/([0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})$`
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="savingsplans-TagResource-request-tags"></a>
One or more tags. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
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
An unexpected error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
HTTP Status Code: 402

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/TagResource)
