---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html
---

# UpdateStorageLensGroup
<a name="API_control_UpdateStorageLensGroup"></a>

 Updates the existing Storage Lens group.

To use this operation, you must have the permission to perform the `s3:UpdateStorageLensGroup` action. For more information about the required Storage Lens Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions).

For information about Storage Lens groups errors, see [List of Amazon S3 Storage Lens error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList).

## Request Syntax
<a name="API_control_UpdateStorageLensGroup_RequestSyntax"></a>

```
PUT /v20180820/storagelensgroup/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateStorageLensGroupRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <StorageLensGroup>
      <Filter>
         <And>
            <MatchAnyPrefix>
               <Prefix>{{string}}</Prefix>
            </MatchAnyPrefix>
            <MatchAnySuffix>
               <Suffix>{{string}}</Suffix>
            </MatchAnySuffix>
            <MatchAnyTag>
               <Tag>
                  <Key>{{string}}</Key>
                  <Value>{{string}}</Value>
               </Tag>
            </MatchAnyTag>
            <MatchObjectAge>
               <DaysGreaterThan>{{integer}}</DaysGreaterThan>
               <DaysLessThan>{{integer}}</DaysLessThan>
            </MatchObjectAge>
            <MatchObjectSize>
               <BytesGreaterThan>{{long}}</BytesGreaterThan>
               <BytesLessThan>{{long}}</BytesLessThan>
            </MatchObjectSize>
         </And>
         <MatchAnyPrefix>
            <Prefix>{{string}}</Prefix>
         </MatchAnyPrefix>
         <MatchAnySuffix>
            <Suffix>{{string}}</Suffix>
         </MatchAnySuffix>
         <MatchAnyTag>
            <Tag>
               <Key>{{string}}</Key>
               <Value>{{string}}</Value>
            </Tag>
         </MatchAnyTag>
         <MatchObjectAge>
            <DaysGreaterThan>{{integer}}</DaysGreaterThan>
            <DaysLessThan>{{integer}}</DaysLessThan>
         </MatchObjectAge>
         <MatchObjectSize>
            <BytesGreaterThan>{{long}}</BytesGreaterThan>
            <BytesLessThan>{{long}}</BytesLessThan>
         </MatchObjectSize>
         <Or>
            <MatchAnyPrefix>
               <Prefix>{{string}}</Prefix>
            </MatchAnyPrefix>
            <MatchAnySuffix>
               <Suffix>{{string}}</Suffix>
            </MatchAnySuffix>
            <MatchAnyTag>
               <Tag>
                  <Key>{{string}}</Key>
                  <Value>{{string}}</Value>
               </Tag>
            </MatchAnyTag>
            <MatchObjectAge>
               <DaysGreaterThan>{{integer}}</DaysGreaterThan>
               <DaysLessThan>{{integer}}</DaysLessThan>
            </MatchObjectAge>
            <MatchObjectSize>
               <BytesGreaterThan>{{long}}</BytesGreaterThan>
               <BytesLessThan>{{long}}</BytesLessThan>
            </MatchObjectSize>
         </Or>
      </Filter>
      <Name>{{string}}</Name>
      <StorageLensGroupArn>{{string}}</StorageLensGroupArn>
   </StorageLensGroup>
</UpdateStorageLensGroupRequest>
```

## URI Request Parameters
<a name="API_control_UpdateStorageLensGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_UpdateStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_UpdateStorageLensGroup-request-uri-uri-Name"></a>
 The name of the Storage Lens group that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [x-amz-account-id](#API_control_UpdateStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_UpdateStorageLensGroup-request-header-AccountId"></a>
 The AWS account ID of the Storage Lens group owner.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_UpdateStorageLensGroup_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateStorageLensGroupRequest](#API_control_UpdateStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_UpdateStorageLensGroup-request-UpdateStorageLensGroupRequest"></a>
Root level tag for the UpdateStorageLensGroupRequest parameters.
Required: Yes

 ** [StorageLensGroup](#API_control_UpdateStorageLensGroup_RequestSyntax) **   <a name="AmazonS3-control_UpdateStorageLensGroup-request-StorageLensGroup"></a>
 The JSON file that contains the Storage Lens group configuration.
Type: [StorageLensGroup](API_control_StorageLensGroup.md) data type
Required: Yes

## Response Syntax
<a name="API_control_UpdateStorageLensGroup_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_control_UpdateStorageLensGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## See Also
<a name="API_control_UpdateStorageLensGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateStorageLensGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateStorageLensGroup)
