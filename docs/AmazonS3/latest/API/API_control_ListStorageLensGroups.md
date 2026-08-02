---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html
---

# ListStorageLensGroups
<a name="API_control_ListStorageLensGroups"></a>

 Lists all the Storage Lens groups in the specified home Region.

To use this operation, you must have the permission to perform the `s3:ListStorageLensGroups` action. For more information about the required Storage Lens Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions).

For information about Storage Lens groups errors, see [List of Amazon S3 Storage Lens error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList).

## Request Syntax
<a name="API_control_ListStorageLensGroups_RequestSyntax"></a>

```
GET /v20180820/storagelensgroup?nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListStorageLensGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_control_ListStorageLensGroups_RequestSyntax) **   <a name="AmazonS3-control_ListStorageLensGroups-request-uri-querystring-NextToken"></a>
The token for the next set of results, or `null` if there are no more results.

 ** [x-amz-account-id](#API_control_ListStorageLensGroups_RequestSyntax) **   <a name="AmazonS3-control_ListStorageLensGroups-request-header-AccountId"></a>
 The AWS account ID that owns the Storage Lens groups.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListStorageLensGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListStorageLensGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListStorageLensGroupsResult>
   <NextToken>string</NextToken>
   <StorageLensGroup>
      <HomeRegion>string</HomeRegion>
      <Name>string</Name>
      <StorageLensGroupArn>string</StorageLensGroupArn>
   </StorageLensGroup>
   ...
</ListStorageLensGroupsResult>
```

## Response Elements
<a name="API_control_ListStorageLensGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListStorageLensGroupsResult](#API_control_ListStorageLensGroups_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensGroups-response-ListStorageLensGroupsResult"></a>
Root level tag for the ListStorageLensGroupsResult parameters.
Required: Yes

 ** [NextToken](#API_control_ListStorageLensGroups_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensGroups-response-NextToken"></a>
 If `NextToken` is returned, there are more Storage Lens groups results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String

 ** [StorageLensGroup](#API_control_ListStorageLensGroups_ResponseSyntax) **   <a name="AmazonS3-control_ListStorageLensGroups-response-StorageLensGroupList"></a>
 The list of Storage Lens groups that exist in the specified home Region.
Type: Array of [ListStorageLensGroupEntry](API_control_ListStorageLensGroupEntry.md) data types

## See Also
<a name="API_control_ListStorageLensGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListStorageLensGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListStorageLensGroups)
