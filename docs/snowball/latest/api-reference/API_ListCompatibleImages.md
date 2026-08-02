---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListCompatibleImages.html
---

# ListCompatibleImages
<a name="API_ListCompatibleImages"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

This action returns a list of the different Amazon EC2-compatible Amazon Machine Images (AMIs) that are owned by your AWS accountthat would be supported for use on a Snow device. Currently, supported AMIs are based on the Amazon Linux-2, Ubuntu 20.04 LTS - Focal, or Ubuntu 22.04 LTS - Jammy images, available on the AWS Marketplace. Ubuntu 16.04 LTS - Xenial (HVM) images are no longer supported in the Market, but still supported for use on devices through Amazon EC2 VM Import/Export and running locally in AMIs.

## Request Syntax
<a name="API_ListCompatibleImages_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCompatibleImages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCompatibleImages_RequestSyntax) **   <a name="Snowball-ListCompatibleImages-request-MaxResults"></a>
The maximum number of results for the list of compatible images. Currently, a Snowball Edge device can store 10 AMIs.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCompatibleImages_RequestSyntax) **   <a name="Snowball-ListCompatibleImages-request-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of compatible images, you can specify a value for `NextToken` as the starting point for your list of returned images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListCompatibleImages_ResponseSyntax"></a>

```
{
   "CompatibleImages": [
      {
         "AmiId": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCompatibleImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompatibleImages](#API_ListCompatibleImages_ResponseSyntax) **   <a name="Snowball-ListCompatibleImages-response-CompatibleImages"></a>
A JSON-formatted object that describes a compatible AMI, including the ID and name for a Snow device AMI.
Type: Array of [CompatibleImage](API_CompatibleImage.md) objects

 ** [NextToken](#API_ListCompatibleImages_ResponseSyntax) **   <a name="Snowball-ListCompatibleImages-response-NextToken"></a>
Because HTTP requests are stateless, this is the starting point for your next list of returned images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListCompatibleImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** Ec2RequestFailedException **
Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListCompatibleImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListCompatibleImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListCompatibleImages)
