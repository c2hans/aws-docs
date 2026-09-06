---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensConfiguration.html
---

# StorageLensConfiguration
<a name="API_control_StorageLensConfiguration"></a>

A container for the Amazon S3 Storage Lens configuration.

## Contents
<a name="API_control_StorageLensConfiguration_Contents"></a>

 ** AccountLevel **   <a name="AmazonS3-Type-control_StorageLensConfiguration-AccountLevel"></a>
A container for all the account-level configurations of your S3 Storage Lens configuration.
Type: [AccountLevel](API_control_AccountLevel.md) data type
Required: Yes

 ** Id **   <a name="AmazonS3-Type-control_StorageLensConfiguration-Id"></a>
A container for the Amazon S3 Storage Lens configuration ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_\.]+`
Required: Yes

 ** IsEnabled **   <a name="AmazonS3-Type-control_StorageLensConfiguration-IsEnabled"></a>
A container for whether the S3 Storage Lens configuration is enabled.
Type: Boolean
Required: Yes

 ** AwsOrg **   <a name="AmazonS3-Type-control_StorageLensConfiguration-AwsOrg"></a>
A container for the AWS organization for this S3 Storage Lens configuration.
Type: [StorageLensAwsOrg](API_control_StorageLensAwsOrg.md) data type
Required: No

 ** DataExport **   <a name="AmazonS3-Type-control_StorageLensConfiguration-DataExport"></a>
A container to specify the properties of your S3 Storage Lens metrics export including, the destination, schema and format.
Type: [StorageLensDataExport](API_control_StorageLensDataExport.md) data type
Required: No

 ** Exclude **   <a name="AmazonS3-Type-control_StorageLensConfiguration-Exclude"></a>
A container for what is excluded in this configuration. This container can only be valid if there is no `Include` container submitted, and it's not empty.
Type: [Exclude](API_control_Exclude.md) data type
Required: No

 ** ExpandedPrefixesDataExport **   <a name="AmazonS3-Type-control_StorageLensConfiguration-ExpandedPrefixesDataExport"></a>
A container that configures your S3 Storage Lens expanded prefixes metrics report.
Type: [StorageLensExpandedPrefixesDataExport](API_control_StorageLensExpandedPrefixesDataExport.md) data type
Required: No

 ** Include **   <a name="AmazonS3-Type-control_StorageLensConfiguration-Include"></a>
A container for what is included in this configuration. This container can only be valid if there is no `Exclude` container submitted, and it's not empty.
Type: [Include](API_control_Include.md) data type
Required: No

 ** PrefixDelimiter **   <a name="AmazonS3-Type-control_StorageLensConfiguration-PrefixDelimiter"></a>
A container for all prefix delimiters that are used for object keys in this S3 Storage Lens configuration. The prefix delimiters determine how S3 Storage Lens counts prefix depth, by separating the hierarchical levels in object keys.
+ If either a prefix delimiter or existing delimiter is undefined, Amazon S3 uses the delimiter that’s defined.
+ If both the prefix delimiter and existing delimiter are undefined, S3 uses `/` as the default delimiter.
+ When custom delimiters are used, both the prefix delimiter and existing delimiter must specify the same special character. Otherwise, your request results in an error.
Type: String
Length Constraints: Maximum length of 1.
Required: No

 ** StorageLensArn **   <a name="AmazonS3-Type-control_StorageLensConfiguration-StorageLensArn"></a>
The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only and follows the following format: ` arn:aws:s3:us-east-1:example-account-id:storage-lens/your-dashboard-name `
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`
Required: No

## See Also
<a name="API_control_StorageLensConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensConfiguration)
