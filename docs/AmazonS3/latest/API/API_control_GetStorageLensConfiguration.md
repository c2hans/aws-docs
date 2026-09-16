---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html
---

# GetStorageLensConfiguration
<a name="API_control_GetStorageLensConfiguration"></a>

**Note**
This operation is not supported by directory buckets.

Gets the Amazon S3 Storage Lens configuration. For more information, see [Assessing your storage activity and usage with Amazon S3 Storage Lens ](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html) in the *Amazon S3 User Guide*. For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html) in the *Amazon S3 User Guide*.

**Note**
To use this action, you must have permission to perform the `s3:GetStorageLensConfiguration` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html) in the *Amazon S3 User Guide*.

## Request Syntax
<a name="API_control_GetStorageLensConfiguration_RequestSyntax"></a>

```
GET /v20180820/storagelens/{{storagelensid}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetStorageLensConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [storagelensid](#API_control_GetStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-request-uri-uri-ConfigId"></a>
The ID of the Amazon S3 Storage Lens configuration.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** [x-amz-account-id](#API_control_GetStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-request-header-AccountId"></a>
The account ID of the requester.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetStorageLensConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetStorageLensConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<StorageLensConfiguration>
   <Id>string</Id>
   <AccountLevel>
      <ActivityMetrics>
         <IsEnabled>boolean</IsEnabled>
      </ActivityMetrics>
      <AdvancedCostOptimizationMetrics>
         <IsEnabled>boolean</IsEnabled>
      </AdvancedCostOptimizationMetrics>
      <AdvancedDataProtectionMetrics>
         <IsEnabled>boolean</IsEnabled>
      </AdvancedDataProtectionMetrics>
      <AdvancedPerformanceMetrics>
         <IsEnabled>boolean</IsEnabled>
      </AdvancedPerformanceMetrics>
      <BucketLevel>
         <ActivityMetrics>
            <IsEnabled>boolean</IsEnabled>
         </ActivityMetrics>
         <AdvancedCostOptimizationMetrics>
            <IsEnabled>boolean</IsEnabled>
         </AdvancedCostOptimizationMetrics>
         <AdvancedDataProtectionMetrics>
            <IsEnabled>boolean</IsEnabled>
         </AdvancedDataProtectionMetrics>
         <AdvancedPerformanceMetrics>
            <IsEnabled>boolean</IsEnabled>
         </AdvancedPerformanceMetrics>
         <DetailedStatusCodesMetrics>
            <IsEnabled>boolean</IsEnabled>
         </DetailedStatusCodesMetrics>
         <PrefixLevel>
            <StorageMetrics>
               <IsEnabled>boolean</IsEnabled>
               <SelectionCriteria>
                  <Delimiter>string</Delimiter>
                  <MaxDepth>integer</MaxDepth>
                  <MinStorageBytesPercentage>double</MinStorageBytesPercentage>
               </SelectionCriteria>
            </StorageMetrics>
         </PrefixLevel>
      </BucketLevel>
      <DetailedStatusCodesMetrics>
         <IsEnabled>boolean</IsEnabled>
      </DetailedStatusCodesMetrics>
      <StorageLensGroupLevel>
         <SelectionCriteria>
            <Exclude>
               <Arn>string</Arn>
            </Exclude>
            <Include>
               <Arn>string</Arn>
            </Include>
         </SelectionCriteria>
      </StorageLensGroupLevel>
   </AccountLevel>
   <Include>
      <Buckets>
         <Arn>string</Arn>
      </Buckets>
      <Regions>
         <Region>string</Region>
      </Regions>
   </Include>
   <Exclude>
      <Buckets>
         <Arn>string</Arn>
      </Buckets>
      <Regions>
         <Region>string</Region>
      </Regions>
   </Exclude>
   <DataExport>
      <CloudWatchMetrics>
         <IsEnabled>boolean</IsEnabled>
      </CloudWatchMetrics>
      <S3BucketDestination>
         <AccountId>string</AccountId>
         <Arn>string</Arn>
         <Encryption>
            <SSE-KMS>
               <KeyId>string</KeyId>
            </SSE-KMS>
            <SSE-S3>
            </SSE-S3>
         </Encryption>
         <Format>string</Format>
         <OutputSchemaVersion>string</OutputSchemaVersion>
         <Prefix>string</Prefix>
      </S3BucketDestination>
      <StorageLensTableDestination>
         <Encryption>
            <SSE-KMS>
               <KeyId>string</KeyId>
            </SSE-KMS>
            <SSE-S3>
            </SSE-S3>
         </Encryption>
         <IsEnabled>boolean</IsEnabled>
      </StorageLensTableDestination>
   </DataExport>
   <ExpandedPrefixesDataExport>
      <S3BucketDestination>
         <AccountId>string</AccountId>
         <Arn>string</Arn>
         <Encryption>
            <SSE-KMS>
               <KeyId>string</KeyId>
            </SSE-KMS>
            <SSE-S3>
            </SSE-S3>
         </Encryption>
         <Format>string</Format>
         <OutputSchemaVersion>string</OutputSchemaVersion>
         <Prefix>string</Prefix>
      </S3BucketDestination>
      <StorageLensTableDestination>
         <Encryption>
            <SSE-KMS>
               <KeyId>string</KeyId>
            </SSE-KMS>
            <SSE-S3>
            </SSE-S3>
         </Encryption>
         <IsEnabled>boolean</IsEnabled>
      </StorageLensTableDestination>
   </ExpandedPrefixesDataExport>
   <IsEnabled>boolean</IsEnabled>
   <AwsOrg>
      <Arn>string</Arn>
   </AwsOrg>
   <StorageLensArn>string</StorageLensArn>
   <PrefixDelimiter>string</PrefixDelimiter>
</StorageLensConfiguration>
```

## Response Elements
<a name="API_control_GetStorageLensConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [StorageLensConfiguration](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-StorageLensConfiguration"></a>
Root level tag for the StorageLensConfiguration parameters.
Required: Yes

 ** [AccountLevel](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-AccountLevel"></a>
A container for all the account-level configurations of your S3 Storage Lens configuration.
Type: [AccountLevel](API_control_AccountLevel.md) data type

 ** [AwsOrg](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-AwsOrg"></a>
A container for the AWS organization for this S3 Storage Lens configuration.
Type: [StorageLensAwsOrg](API_control_StorageLensAwsOrg.md) data type

 ** [DataExport](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-DataExport"></a>
A container to specify the properties of your S3 Storage Lens metrics export including, the destination, schema and format.
Type: [StorageLensDataExport](API_control_StorageLensDataExport.md) data type

 ** [Exclude](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-Exclude"></a>
A container for what is excluded in this configuration. This container can only be valid if there is no `Include` container submitted, and it's not empty.
Type: [Exclude](API_control_Exclude.md) data type

 ** [ExpandedPrefixesDataExport](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-ExpandedPrefixesDataExport"></a>
A container that configures your S3 Storage Lens expanded prefixes metrics report.
Type: [StorageLensExpandedPrefixesDataExport](API_control_StorageLensExpandedPrefixesDataExport.md) data type

 ** [Id](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-Id"></a>
A container for the Amazon S3 Storage Lens configuration ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`

 ** [Include](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-Include"></a>
A container for what is included in this configuration. This container can only be valid if there is no `Exclude` container submitted, and it's not empty.
Type: [Include](API_control_Include.md) data type

 ** [IsEnabled](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-IsEnabled"></a>
A container for whether the S3 Storage Lens configuration is enabled.
Type: Boolean

 ** [PrefixDelimiter](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-PrefixDelimiter"></a>
A container for all prefix delimiters that are used for object keys in this S3 Storage Lens configuration. The prefix delimiters determine how S3 Storage Lens counts prefix depth, by separating the hierarchical levels in object keys.
+ If either a prefix delimiter or existing delimiter is undefined, Amazon S3 uses the delimiter that’s defined.
+ If both the prefix delimiter and existing delimiter are undefined, S3 uses `/` as the default delimiter.
+ When custom delimiters are used, both the prefix delimiter and existing delimiter must specify the same special character. Otherwise, your request results in an error.
Type: String
Length Constraints: Maximum length of 1.

 ** [StorageLensArn](#API_control_GetStorageLensConfiguration_ResponseSyntax) **   <a name="AmazonS3-control_GetStorageLensConfiguration-response-StorageLensArn"></a>
The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only and follows the following format: ` arn:aws:s3:us-east-1:example-account-id:storage-lens/your-dashboard-name `
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`

## See Also
<a name="API_control_GetStorageLensConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensConfiguration)
