---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_iot-secure-tunneling_ListTagsForResource"></a>

Lists the tags for the specified resource.

## Request Syntax
<a name="API_iot-secure-tunneling_ListTagsForResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_iot-secure-tunneling_ListTagsForResource_RequestSyntax) **   <a name="iot-iot-secure-tunneling_ListTagsForResource-request-resourceArn"></a>
The resource ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_iot-secure-tunneling_ListTagsForResource_ResponseSyntax"></a>

```
{
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iot-secure-tunneling_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_iot-secure-tunneling_ListTagsForResource_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_ListTagsForResource-response-tags"></a>
The tags for the specified resource.
Type: Array of [Tag](API_iot-secure-tunneling_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

## Errors
<a name="API_iot-secure-tunneling_ListTagsForResource_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/ListTagsForResource)
