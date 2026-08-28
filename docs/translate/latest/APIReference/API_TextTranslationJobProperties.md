---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_TextTranslationJobProperties.html
---

# TextTranslationJobProperties
<a name="API_TextTranslationJobProperties"></a>

Provides information about a translation job.

## Contents
<a name="API_TextTranslationJobProperties_Contents"></a>

 ** DataAccessRoleArn **   <a name="translate-Type-TextTranslationJobProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the job's input data. For more information, see [Prerequisite permissions](https://docs.aws.amazon.com/translate/latest/dg/async-prereqs.html#async-prereqs-permissions) in the Amazon Translate Developer Guide.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** EndTime **   <a name="translate-Type-TextTranslationJobProperties-EndTime"></a>
The time at which the translation job ended.
Type: Timestamp
Required: No

 ** InputDataConfig **   <a name="translate-Type-TextTranslationJobProperties-InputDataConfig"></a>
The input configuration properties that were specified when the job was requested.
Type: [InputDataConfig](API_InputDataConfig.md) object
Required: No

 ** JobDetails **   <a name="translate-Type-TextTranslationJobProperties-JobDetails"></a>
The number of documents successfully and unsuccessfully processed during the translation job.
Type: [JobDetails](API_JobDetails.md) object
Required: No

 ** JobId **   <a name="translate-Type-TextTranslationJobProperties-JobId"></a>
The ID of the translation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobName **   <a name="translate-Type-TextTranslationJobProperties-JobName"></a>
The user-defined name of the translation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobStatus **   <a name="translate-Type-TextTranslationJobProperties-JobStatus"></a>
The status of the translation job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERROR | FAILED | STOP_REQUESTED | STOPPED`
Required: No

 ** Message **   <a name="translate-Type-TextTranslationJobProperties-Message"></a>
An explanation of any errors that may have occurred during the translation job.
Type: String
Required: No

 ** OutputDataConfig **   <a name="translate-Type-TextTranslationJobProperties-OutputDataConfig"></a>
The output configuration properties that were specified when the job was requested.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: No

 ** ParallelDataNames **   <a name="translate-Type-TextTranslationJobProperties-ParallelDataNames"></a>
A list containing the names of the parallel data resources applied to the translation job.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

 ** Settings **   <a name="translate-Type-TextTranslationJobProperties-Settings"></a>
Settings that modify the translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object
Required: No

 ** SourceLanguageCode **   <a name="translate-Type-TextTranslationJobProperties-SourceLanguageCode"></a>
The language code of the language of the source text. The language must be a language supported by Amazon Translate.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** SubmittedTime **   <a name="translate-Type-TextTranslationJobProperties-SubmittedTime"></a>
The time at which the translation job was submitted.
Type: Timestamp
Required: No

 ** TargetLanguageCodes **   <a name="translate-Type-TextTranslationJobProperties-TargetLanguageCodes"></a>
The language code of the language of the target text. The language must be a language supported by Amazon Translate.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** TerminologyNames **   <a name="translate-Type-TextTranslationJobProperties-TerminologyNames"></a>
A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per [StartTextTranslationJob](API_StartTextTranslationJob.md) request at this time.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

## See Also
<a name="API_TextTranslationJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/TextTranslationJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/TextTranslationJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/TextTranslationJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
