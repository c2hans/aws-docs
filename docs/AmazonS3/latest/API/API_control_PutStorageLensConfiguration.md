---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html
---

# PutStorageLensConfiguration
<a name="API_control_PutStorageLensConfiguration"></a>

**Note**
This operation is not supported by directory buckets.

Puts an Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see [Working with Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html) in the *Amazon S3 User Guide*. For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html) in the *Amazon S3 User Guide*.

**Note**
To use this action, you must have permission to perform the `s3:PutStorageLensConfiguration` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html) in the *Amazon S3 User Guide*.

## Request Syntax
<a name="API_control_PutStorageLensConfiguration_RequestSyntax"></a>

```
PUT /v20180820/storagelens/{{storagelensid}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PutStorageLensConfigurationRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <StorageLensConfiguration>
      <AccountLevel>
         <ActivityMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </ActivityMetrics>
         <AdvancedCostOptimizationMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </AdvancedCostOptimizationMetrics>
         <AdvancedDataProtectionMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </AdvancedDataProtectionMetrics>
         <AdvancedPerformanceMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </AdvancedPerformanceMetrics>
         <BucketLevel>
            <ActivityMetrics>
               <IsEnabled>{{boolean}}</IsEnabled>
            </ActivityMetrics>
            <AdvancedCostOptimizationMetrics>
               <IsEnabled>{{boolean}}</IsEnabled>
            </AdvancedCostOptimizationMetrics>
            <AdvancedDataProtectionMetrics>
               <IsEnabled>{{boolean}}</IsEnabled>
            </AdvancedDataProtectionMetrics>
            <AdvancedPerformanceMetrics>
               <IsEnabled>{{boolean}}</IsEnabled>
            </AdvancedPerformanceMetrics>
            <DetailedStatusCodesMetrics>
               <IsEnabled>{{boolean}}</IsEnabled>
            </DetailedStatusCodesMetrics>
            <PrefixLevel>
               <StorageMetrics>
                  <IsEnabled>{{boolean}}</IsEnabled>
                  <SelectionCriteria>
                     <Delimiter>{{string}}</Delimiter>
                     <MaxDepth>{{integer}}</MaxDepth>
                     <MinStorageBytesPercentage>{{double}}</MinStorageBytesPercentage>
                  </SelectionCriteria>
               </StorageMetrics>
            </PrefixLevel>
         </BucketLevel>
         <DetailedStatusCodesMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </DetailedStatusCodesMetrics>
         <StorageLensGroupLevel>
            <SelectionCriteria>
               <Exclude>
                  <Arn>{{string}}</Arn>
               </Exclude>
               <Include>
                  <Arn>{{string}}</Arn>
               </Include>
            </SelectionCriteria>
         </StorageLensGroupLevel>
      </AccountLevel>
      <AwsOrg>
         <Arn>{{string}}</Arn>
      </AwsOrg>
      <DataExport>
         <CloudWatchMetrics>
            <IsEnabled>{{boolean}}</IsEnabled>
         </CloudWatchMetrics>
         <S3BucketDestination>
            <AccountId>{{string}}</AccountId>
            <Arn>{{string}}</Arn>
            <Encryption>
               <SSE-KMS>
                  <KeyId>{{string}}</KeyId>
               </SSE-KMS>
               <SSE-S3>
               </SSE-S3>
            </Encryption>
            <Format>{{string}}</Format>
            <OutputSchemaVersion>{{string}}</OutputSchemaVersion>
            <Prefix>{{string}}</Prefix>
         </S3BucketDestination>
         <StorageLensTableDestination>
            <Encryption>
               <SSE-KMS>
                  <KeyId>{{string}}</KeyId>
               </SSE-KMS>
               <SSE-S3>
               </SSE-S3>
            </Encryption>
            <IsEnabled>{{boolean}}</IsEnabled>
         </StorageLensTableDestination>
      </DataExport>
      <Exclude>
         <Buckets>
            <Arn>{{string}}</Arn>
         </Buckets>
         <Regions>
            <Region>{{string}}</Region>
         </Regions>
      </Exclude>
      <ExpandedPrefixesDataExport>
         <S3BucketDestination>
            <AccountId>{{string}}</AccountId>
            <Arn>{{string}}</Arn>
            <Encryption>
               <SSE-KMS>
                  <KeyId>{{string}}</KeyId>
               </SSE-KMS>
               <SSE-S3>
               </SSE-S3>
            </Encryption>
            <Format>{{string}}</Format>
            <OutputSchemaVersion>{{string}}</OutputSchemaVersion>
            <Prefix>{{string}}</Prefix>
         </S3BucketDestination>
         <StorageLensTableDestination>
            <Encryption>
               <SSE-KMS>
                  <KeyId>{{string}}</KeyId>
               </SSE-KMS>
               <SSE-S3>
               </SSE-S3>
            </Encryption>
            <IsEnabled>{{boolean}}</IsEnabled>
         </StorageLensTableDestination>
      </ExpandedPrefixesDataExport>
      <Id>{{string}}</Id>
      <Include>
         <Buckets>
            <Arn>{{string}}</Arn>
         </Buckets>
         <Regions>
            <Region>{{string}}</Region>
         </Regions>
      </Include>
      <IsEnabled>{{boolean}}</IsEnabled>
      <PrefixDelimiter>{{string}}</PrefixDelimiter>
      <StorageLensArn>{{string}}</StorageLensArn>
   </StorageLensConfiguration>
   <Tags>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </Tags>
</PutStorageLensConfigurationRequest>
```

## URI Request Parameters
<a name="API_control_PutStorageLensConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [storagelensid](#API_control_PutStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutStorageLensConfiguration-request-uri-uri-ConfigId"></a>
The ID of the S3 Storage Lens configuration.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** [x-amz-account-id](#API_control_PutStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutStorageLensConfiguration-request-header-AccountId"></a>
The account ID of the requester.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutStorageLensConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutStorageLensConfigurationRequest](#API_control_PutStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutStorageLensConfiguration-request-PutStorageLensConfigurationRequest"></a>
Root level tag for the PutStorageLensConfigurationRequest parameters.
Required: Yes

 ** [StorageLensConfiguration](#API_control_PutStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutStorageLensConfiguration-request-StorageLensConfiguration"></a>
The S3 Storage Lens configuration.
Type: [StorageLensConfiguration](API_control_StorageLensConfiguration.md) data type
Required: Yes

 ** [Tags](#API_control_PutStorageLensConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutStorageLensConfiguration-request-Tags"></a>
The tag set of the S3 Storage Lens configuration.
You can set up to a maximum of 50 tags.
Type: Array of [StorageLensTag](API_control_StorageLensTag.md) data types
Required: No

## Response Syntax
<a name="API_control_PutStorageLensConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutStorageLensConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_PutStorageLensConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutStorageLensConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutStorageLensConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
