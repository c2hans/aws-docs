---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html
---

# GetStorageLensGroup
<a name="API_control_GetStorageLensGroup"></a>

 Retrieves the Storage Lens group configuration details.

To use this operation, you must have the permission to perform the `s3:GetStorageLensGroup` action. For more information about the required Storage Lens Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions).

For information about Storage Lens groups errors, see [List of Amazon S3 Storage Lens error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList).

## Request Syntax
<a name="API_control_GetStorageLensGroup_RequestSyntax"></a>

```
GET /v20180820/storagelensgroup/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetStorageLensGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-request-uri-uri-Name"></a>
 The name of the Storage Lens group that you're trying to retrieve the configuration details for.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [x-amz-account-id](#API_control_GetStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-request-header-AccountId"></a>
 The AWS account ID associated with the Storage Lens group that you're trying to retrieve the details for.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetStorageLensGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetStorageLensGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StorageLensGroup>
   <Name>string</Name>
   <Filter>
      <And>
         <MatchAnyPrefix>
            <Prefix>string</Prefix>
         </MatchAnyPrefix>
         <MatchAnySuffix>
            <Suffix>string</Suffix>
         </MatchAnySuffix>
         <MatchAnyTag>
            <Tag>
               <Key>string</Key>
               <Value>string</Value>
            </Tag>
         </MatchAnyTag>
         <MatchObjectAge>
            <DaysGreaterThan>integer</DaysGreaterThan>
            <DaysLessThan>integer</DaysLessThan>
         </MatchObjectAge>
         <MatchObjectSize>
            <BytesGreaterThan>long</BytesGreaterThan>
            <BytesLessThan>long</BytesLessThan>
         </MatchObjectSize>
      </And>
      <MatchAnyPrefix>
         <Prefix>string</Prefix>
      </MatchAnyPrefix>
      <MatchAnySuffix>
         <Suffix>string</Suffix>
      </MatchAnySuffix>
      <MatchAnyTag>
         <Tag>
            <Key>string</Key>
            <Value>string</Value>
         </Tag>
      </MatchAnyTag>
      <MatchObjectAge>
         <DaysGreaterThan>integer</DaysGreaterThan>
         <DaysLessThan>integer</DaysLessThan>
      </MatchObjectAge>
      <MatchObjectSize>
         <BytesGreaterThan>long</BytesGreaterThan>
         <BytesLessThan>long</BytesLessThan>
      </MatchObjectSize>
      <Or>
         <MatchAnyPrefix>
            <Prefix>string</Prefix>
         </MatchAnyPrefix>
         <MatchAnySuffix>
            <Suffix>string</Suffix>
         </MatchAnySuffix>
         <MatchAnyTag>
            <Tag>
               <Key>string</Key>
               <Value>string</Value>
            </Tag>
         </MatchAnyTag>
         <MatchObjectAge>
            <DaysGreaterThan>integer</DaysGreaterThan>
            <DaysLessThan>integer</DaysLessThan>
         </MatchObjectAge>
         <MatchObjectSize>
            <BytesGreaterThan>long</BytesGreaterThan>
            <BytesLessThan>long</BytesLessThan>
         </MatchObjectSize>
      </Or>
   </Filter>
   <StorageLensGroupArn>string</StorageLensGroupArn>
</StorageLensGroup>
```

## Response Elements
<a name="API_control_GetStorageLensGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [StorageLensGroup](#API_control_GetStorageLensGroup_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-response-StorageLensGroup"></a>
Root level tag for the StorageLensGroup parameters.
Required: Yes

 ** [Filter](#API_control_GetStorageLensGroup_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-response-Filter"></a>
Sets the criteria for the Storage Lens group data that is displayed. For multiple filter conditions, the `AND` or `OR` logical operator is used.
Type: [StorageLensGroupFilter](API_control_StorageLensGroupFilter.md) data type

 ** [Name](#API_control_GetStorageLensGroup_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-response-Name"></a>
 Contains the name of the Storage Lens group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [StorageLensGroupArn](#API_control_GetStorageLensGroup_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensGroup-response-StorageLensGroupArn"></a>
 Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is read-only.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`

## See Also
<a name="API_control_GetStorageLensGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensGroup)
