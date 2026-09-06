---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_TagResource.html
---

# TagResource
<a name="API_iot-secure-tunneling_TagResource"></a>

A resource tag.

## Request Syntax
<a name="API_iot-secure-tunneling_TagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_iot-secure-tunneling_TagResource_RequestSyntax) **   <a name="iot-iot-secure-tunneling_TagResource-request-resourceArn"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** [tags](#API_iot-secure-tunneling_TagResource_RequestSyntax) **   <a name="iot-iot-secure-tunneling_TagResource-request-tags"></a>
The tags for the resource.
Type: Array of [Tag](API_iot-secure-tunneling_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_iot-secure-tunneling_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iot-secure-tunneling_TagResource_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/TagResource)
