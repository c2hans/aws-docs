---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_ParallelDataConfig.html
---

# ParallelDataConfig
<a name="API_ParallelDataConfig"></a>

Specifies the format and S3 location of the parallel data input file.

## Contents
<a name="API_ParallelDataConfig_Contents"></a>

 ** Format **   <a name="translate-Type-ParallelDataConfig-Format"></a>
The format of the parallel data input file.
Type: String
Valid Values: `TSV | CSV | TMX`
Required: No

 ** S3Uri **   <a name="translate-Type-ParallelDataConfig-S3Uri"></a>
The URI of the Amazon S3 folder that contains the parallel data input file. The folder must be in the same Region as the API endpoint you are calling.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: No

## See Also
<a name="API_ParallelDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/ParallelDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/ParallelDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/ParallelDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
