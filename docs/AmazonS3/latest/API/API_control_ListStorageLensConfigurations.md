---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html
---

# ListStorageLensConfigurations
<a name="API_control_ListStorageLensConfigurations"></a>

**Note**
This operation is not supported by directory buckets.

Gets a list of Amazon S3 Storage Lens configurations. For more information about S3 Storage Lens, see [Assessing your storage activity and usage with Amazon S3 Storage Lens ](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html) in the *Amazon S3 User Guide*.

**Note**
To use this action, you must have permission to perform the `s3:ListStorageLensConfigurations` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html) in the *Amazon S3 User Guide*.

## Request Syntax
<a name="API_control_ListStorageLensConfigurations_RequestSyntax"></a>

```
GET /v20180820/storagelens?nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListStorageLensConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_control_ListStorageLensConfigurations_RequestSyntax) **   <a name="AmazonS3-control_ListStorageLensConfigurations-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results.

 ** [x-amz-account-id](#API_control_ListStorageLensConfigurations_RequestSyntax) **   <a name="AmazonS3-control_ListStorageLensConfigurations-request-header-AccountId"></a>
The account ID of the requester.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListStorageLensConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListStorageLensConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListStorageLensConfigurationsResult>
   <NextToken>string</NextToken>
   <StorageLensConfiguration>
      <HomeRegion>string</HomeRegion>
      <Id>string</Id>
      <IsEnabled>boolean</IsEnabled>
      <StorageLensArn>string</StorageLensArn>
   </StorageLensConfiguration>
   ...
</ListStorageLensConfigurationsResult>
```

## Response Elements
<a name="API_control_ListStorageLensConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListStorageLensConfigurationsResult](#API_control_ListStorageLensConfigurations_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensConfigurations-response-ListStorageLensConfigurationsResult"></a>
Root level tag for the ListStorageLensConfigurationsResult parameters.
Required: Yes

 ** [NextToken](#API_control_ListStorageLensConfigurations_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensConfigurations-response-NextToken"></a>
If the request produced more than the maximum number of S3 Storage Lens configuration results, you can pass this value into a subsequent request to retrieve the next page of results.
Type: String

 ** [StorageLensConfiguration](#API_control_ListStorageLensConfigurations_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensConfigurations-response-StorageLensConfigurationList"></a>
A list of S3 Storage Lens configurations.
Type: Array of [ListStorageLensConfigurationEntry](API_control_ListStorageLensConfigurationEntry.md) data types

## See Also
<a name="API_control_ListStorageLensConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListStorageLensConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListStorageLensConfigurations)
