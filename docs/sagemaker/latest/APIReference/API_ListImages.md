---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListImages.html
---

# ListImages
<a name="API_ListImages"></a>

Lists the images in your account and their properties. The list can be filtered by creation time or modified time, and whether the image name contains a specified string.

## Request Syntax
<a name="API_ListImages_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListImages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListImages_RequestSyntax) **   <a name="sagemaker-ListImages-request-MaxResults"></a>
The maximum number of images to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListImages_RequestSyntax) **   <a name="sagemaker-ListImages-request-NameContains"></a>
A filter that returns only images whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-.]+`
Required: No

 ** [NextToken](#API_ListImages_RequestSyntax) **   <a name="sagemaker-ListImages-request-NextToken"></a>
If the previous call to `ListImages` didn't return the full set of images, the call returns a token for getting the next set of images.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListImages_RequestSyntax) **   <a name="sagemaker-ListImages-request-SortBy"></a>
The property used to sort results. The default value is `CREATION_TIME`.
Type: String
Valid Values: `CREATION_TIME | LAST_MODIFIED_TIME | IMAGE_NAME`
Required: No

 ** [SortOrder](#API_ListImages_RequestSyntax) **   <a name="sagemaker-ListImages-request-SortOrder"></a>
The sort order. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListImages_ResponseSyntax"></a>

```
{
   "Images": [
      {
         "Description": "string",
         "DisplayName": "string",
         "FailureReason": "string",
         "ImageArn": "string",
         "ImageName": "string",
         "ImageStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Images](#API_ListImages_ResponseSyntax) **   <a name="sagemaker-ListImages-response-Images"></a>
A list of images and their properties.
Type: Array of [Image](API_Image.md) objects

 ** [NextToken](#API_ListImages_ResponseSyntax) **   <a name="sagemaker-ListImages-response-NextToken"></a>
A token for getting the next set of images, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListImages)
