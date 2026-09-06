---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html
---

# DeleteStorageLensConfigurationTagging
<a name="API_control_DeleteStorageLensConfigurationTagging"></a>

**Note**
This operation is not supported by directory buckets.

Deletes the Amazon S3 Storage Lens configuration tags. For more information about S3 Storage Lens, see [Assessing your storage activity and usage with Amazon S3 Storage Lens ](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html) in the *Amazon S3 User Guide*.

**Note**
To use this action, you must have permission to perform the `s3:DeleteStorageLensConfigurationTagging` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html) in the *Amazon S3 User Guide*.

## Request Syntax
<a name="API_control_DeleteStorageLensConfigurationTagging_RequestSyntax"></a>

```
DELETE /v20180820/storagelens/{{storagelensid}}/tagging HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DeleteStorageLensConfigurationTagging_RequestParameters"></a>

The request uses the following URI parameters.

 ** [storagelensid](#API_control_DeleteStorageLensConfigurationTagging_RequestSyntax) **   <a name="AmazonS3-control_DeleteStorageLensConfigurationTagging-request-uri-uri-ConfigId"></a>
The ID of the S3 Storage Lens configuration.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** [x-amz-account-id](#API_control_DeleteStorageLensConfigurationTagging_RequestSyntax) **   <a name="AmazonS3-control_DeleteStorageLensConfigurationTagging-request-header-AccountId"></a>
The account ID of the requester.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DeleteStorageLensConfigurationTagging_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DeleteStorageLensConfigurationTagging_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_DeleteStorageLensConfigurationTagging_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_DeleteStorageLensConfigurationTagging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteStorageLensConfigurationTagging)
