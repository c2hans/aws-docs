---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_S3BucketTranscriptSource.html
---

# S3BucketTranscriptSource
<a name="API_S3BucketTranscriptSource"></a>

The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.

## Contents
<a name="API_S3BucketTranscriptSource_Contents"></a>

 ** s3BucketName **   <a name="lexv2-Type-S3BucketTranscriptSource-s3BucketName"></a>
The name of the bucket containing the transcript and the associated metadata.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
Required: Yes

 ** transcriptFormat **   <a name="lexv2-Type-S3BucketTranscriptSource-transcriptFormat"></a>
The format of the transcript content. Currently, Genie only supports the Amazon Lex transcript format.
Type: String
Valid Values: `Lex`
Required: Yes

 ** kmsKeyArn **   <a name="lexv2-Type-S3BucketTranscriptSource-kmsKeyArn"></a>
The ARN of the KMS key that customer use to encrypt their Amazon S3 bucket. Only use this field if your bucket is encrypted using a customer managed KMS key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
Required: No

 ** pathFormat **   <a name="lexv2-Type-S3BucketTranscriptSource-pathFormat"></a>
The object that contains a path format that will be applied when Amazon Lex reads the transcript file in the bucket you provide. Specify this object if you only want Lex to read a subset of files in your Amazon S3 bucket.
Type: [PathFormat](API_PathFormat.md) object
Required: No

 ** transcriptFilter **   <a name="lexv2-Type-S3BucketTranscriptSource-transcriptFilter"></a>
The object that contains the filter which will be applied when Amazon Lex reads through the Amazon S3 bucket. Specify this object if you want Amazon Lex to read only a subset of the Amazon S3 bucket based on the filter you provide.
Type: [TranscriptFilter](API_TranscriptFilter.md) object
Required: No

## See Also
<a name="API_S3BucketTranscriptSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/S3BucketTranscriptSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/S3BucketTranscriptSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/S3BucketTranscriptSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
