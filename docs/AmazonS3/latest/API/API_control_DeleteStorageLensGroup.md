---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html
---

# DeleteStorageLensGroup
<a name="API_control_DeleteStorageLensGroup"></a>

 Deletes an existing S3 Storage Lens group.

To use this operation, you must have the permission to perform the `s3:DeleteStorageLensGroup` action. For more information about the required Storage Lens Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions).

For information about Storage Lens groups errors, see [List of Amazon S3 Storage Lens error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList).

## Request Syntax
<a name="API_control_DeleteStorageLensGroup_RequestSyntax"></a>

```
DELETE /v20180820/storagelensgroup/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DeleteStorageLensGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_DeleteStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_DeleteStorageLensGroup-request-uri-uri-Name"></a>
 The name of the Storage Lens group that you're trying to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [x-amz-account-id](#API_control_DeleteStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_DeleteStorageLensGroup-request-header-AccountId"></a>
 The AWS account ID used to create the Storage Lens group that you're trying to delete.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DeleteStorageLensGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DeleteStorageLensGroup_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_control_DeleteStorageLensGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## See Also
<a name="API_control_DeleteStorageLensGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteStorageLensGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteStorageLensGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
