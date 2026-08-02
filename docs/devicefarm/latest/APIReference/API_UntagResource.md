---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Deletes the specified tags from a resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_UntagResource_RequestSyntax) **   <a name="devicefarm-UntagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource or resources from which to delete tags. You can associate tags with the following Device Farm resources: `PROJECT`, `TESTGRID_PROJECT`, `RUN`, `NETWORK_PROFILE`, `INSTANCE_PROFILE`, `DEVICE_INSTANCE`, `SESSION`, `DEVICE_POOL`, `DEVICE`, and `VPCE_CONFIGURATION`.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="devicefarm-UntagResource-request-TagKeys"></a>
The keys of the tags to be removed.
Type: Array of strings
Array Members: Maximum number of 150 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** TagOperationException **
The operation was not successful. Try again.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UntagResource)
