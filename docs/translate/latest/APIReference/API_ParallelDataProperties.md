---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_ParallelDataProperties.html
---

# ParallelDataProperties
<a name="API_ParallelDataProperties"></a>

The properties of a parallel data resource.

## Contents
<a name="API_ParallelDataProperties_Contents"></a>

 ** Arn **   <a name="translate-Type-ParallelDataProperties-Arn"></a>
The Amazon Resource Name (ARN) of the parallel data resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** CreatedAt **   <a name="translate-Type-ParallelDataProperties-CreatedAt"></a>
The time at which the parallel data resource was created.
Type: Timestamp
Required: No

 ** Description **   <a name="translate-Type-ParallelDataProperties-Description"></a>
The description assigned to the parallel data resource.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\P{M}\p{M}]{0,256}`
Required: No

 ** EncryptionKey **   <a name="translate-Type-ParallelDataProperties-EncryptionKey"></a>
The encryption key used to encrypt this object.
Type: [EncryptionKey](API_EncryptionKey.md) object
Required: No

 ** FailedRecordCount **   <a name="translate-Type-ParallelDataProperties-FailedRecordCount"></a>
The number of records unsuccessfully imported from the parallel data input file.
Type: Long
Required: No

 ** ImportedDataSize **   <a name="translate-Type-ParallelDataProperties-ImportedDataSize"></a>
The number of UTF-8 characters that Amazon Translate imported from the parallel data input file. This number includes only the characters in your translation examples. It does not include characters that are used to format your file. For example, if you provided a Translation Memory Exchange (.tmx) file, this number does not include the tags.
Type: Long
Required: No

 ** ImportedRecordCount **   <a name="translate-Type-ParallelDataProperties-ImportedRecordCount"></a>
The number of records successfully imported from the parallel data input file.
Type: Long
Required: No

 ** LastUpdatedAt **   <a name="translate-Type-ParallelDataProperties-LastUpdatedAt"></a>
The time at which the parallel data resource was last updated.
Type: Timestamp
Required: No

 ** LatestUpdateAttemptAt **   <a name="translate-Type-ParallelDataProperties-LatestUpdateAttemptAt"></a>
The time that the most recent update was attempted.
Type: Timestamp
Required: No

 ** LatestUpdateAttemptStatus **   <a name="translate-Type-ParallelDataProperties-LatestUpdateAttemptStatus"></a>
The status of the most recent update attempt for the parallel data resource.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | DELETING | FAILED`
Required: No

 ** Message **   <a name="translate-Type-ParallelDataProperties-Message"></a>
Additional information from Amazon Translate about the parallel data resource.
Type: String
Required: No

 ** Name **   <a name="translate-Type-ParallelDataProperties-Name"></a>
The custom name assigned to the parallel data resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

 ** ParallelDataConfig **   <a name="translate-Type-ParallelDataProperties-ParallelDataConfig"></a>
Specifies the format and S3 location of the parallel data input file.
Type: [ParallelDataConfig](API_ParallelDataConfig.md) object
Required: No

 ** SkippedRecordCount **   <a name="translate-Type-ParallelDataProperties-SkippedRecordCount"></a>
The number of items in the input file that Amazon Translate skipped when you created or updated the parallel data resource. For example, Amazon Translate skips empty records, empty target texts, and empty lines.
Type: Long
Required: No

 ** SourceLanguageCode **   <a name="translate-Type-ParallelDataProperties-SourceLanguageCode"></a>
The source language of the translations in the parallel data file.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** Status **   <a name="translate-Type-ParallelDataProperties-Status"></a>
The status of the parallel data resource. When the parallel data is ready for you to use, the status is `ACTIVE`.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | DELETING | FAILED`
Required: No

 ** TargetLanguageCodes **   <a name="translate-Type-ParallelDataProperties-TargetLanguageCodes"></a>
The language codes for the target languages available in the parallel data file. All possible target languages are returned as an array.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

## See Also
<a name="API_ParallelDataProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/ParallelDataProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/ParallelDataProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/ParallelDataProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
