---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AudioLogDestination.html
---

# AudioLogDestination
<a name="API_AudioLogDestination"></a>

The location of audio log files collected when conversation logging is enabled for a bot.

## Contents
<a name="API_AudioLogDestination_Contents"></a>

 ** s3Bucket **   <a name="lexv2-Type-AudioLogDestination-s3Bucket"></a>
The Amazon S3 bucket where the audio log files are stored. The IAM role specified in the `roleArn` parameter of the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation must have permission to write to this bucket.
Type: [S3BucketLogDestination](API_S3BucketLogDestination.md) object
Required: Yes

## See Also
<a name="API_AudioLogDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AudioLogDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AudioLogDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AudioLogDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
