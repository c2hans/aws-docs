---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Remove tags from a resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="braket-UntagResource-request-uri-resourceArn"></a>
Specify the `resourceArn` for the resource from which to remove the tags.
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="braket-UntagResource-request-uri-tagKeys"></a>
Specify the keys for the tags to remove from the resource.
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

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/UntagResource)
