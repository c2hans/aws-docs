---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_StartTextTranslationJob.html
---

# StartTextTranslationJob
<a name="API_StartTextTranslationJob"></a>

Starts an asynchronous batch translation job. Use batch translation jobs to translate large volumes of text across multiple documents at once. For batch translation, you can input documents with different source languages (specify `auto` as the source language). You can specify one or more target languages. Batch translation translates each input document into each of the target languages. For more information, see [Asynchronous batch processing](https://docs.aws.amazon.com/translate/latest/dg/async.html) in the Amazon Translate Developer Guide.

Batch translation jobs can be described with the [DescribeTextTranslationJob](API_DescribeTextTranslationJob.md) operation, listed with the [ListTextTranslationJobs](API_ListTextTranslationJobs.md) operation, and stopped with the [StopTextTranslationJob](API_StopTextTranslationJob.md) operation.

## Request Syntax
<a name="API_StartTextTranslationJob_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "InputDataConfig": {
      "ContentType": "{{string}}",
      "S3Uri": "{{string}}"
   },
   "JobName": "{{string}}",
   "OutputDataConfig": {
      "EncryptionKey": {
         "Id": "{{string}}",
         "Type": "{{string}}"
      },
      "S3Uri": "{{string}}"
   },
   "ParallelDataNames": [ "{{string}}" ],
   "Settings": {
      "Brevity": "{{string}}",
      "Formality": "{{string}}",
      "Profanity": "{{string}}"
   },
   "SourceLanguageCode": "{{string}}",
   "TargetLanguageCodes": [ "{{string}}" ],
   "TerminologyNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StartTextTranslationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-ClientToken"></a>
A unique identifier for the request. This token is generated for you when using the Amazon Translate SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [DataAccessRoleArn](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that grants Amazon Translate read access to your input data. For more information, see [Prerequisite permissions](https://docs.aws.amazon.com/translate/latest/dg/async-prereqs.html#async-prereqs-permissions) in the Amazon Translate Developer Guide.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [InputDataConfig](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-InputDataConfig"></a>
Specifies the format and location of the input documents for the translation job.
Type: [InputDataConfig](API_InputDataConfig.md) object
Required: Yes

 ** [JobName](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-JobName"></a>
The name of the batch translation job to be performed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** [OutputDataConfig](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-OutputDataConfig"></a>
Specifies the S3 folder to which your job output will be saved.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

 ** [ParallelDataNames](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-ParallelDataNames"></a>
The name of a parallel data resource to add to the translation job. This resource consists of examples that show how you want segments of text to be translated. If you specify multiple target languages for the job, the parallel data file must include translations for all the target languages.
When you add parallel data to a translation job, you create an *Active Custom Translation* job.
This parameter accepts only one parallel data resource.
Active Custom Translation jobs are priced at a higher rate than other jobs that don't use parallel data. For more information, see [Amazon Translate pricing](http://aws.amazon.com/translate/pricing/).
For a list of available parallel data resources, use the [ListParallelData](API_ListParallelData.md) operation.
For more information, see [ Customizing your translations with parallel data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html) in the Amazon Translate Developer Guide.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

 ** [Settings](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-Settings"></a>
Settings to configure your translation output. You can configure the following options:
+ Brevity: not supported.
+ Formality: sets the formality level of the output text.
+ Profanity: masks profane words and phrases in your translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object
Required: No

 ** [SourceLanguageCode](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-SourceLanguageCode"></a>
The language code of the input language. Specify the language if all input documents share the same language. If you don't know the language of the source files, or your input documents contains different source languages, select `auto`. Amazon Translate auto detects the source language for each input document. For a list of supported language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TargetLanguageCodes](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-TargetLanguageCodes"></a>
The target languages of the translation job. Enter up to 10 language codes. Each input file is translated into each target language.
Each language code is 2 or 5 characters long. For a list of language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TerminologyNames](#API_StartTextTranslationJob_RequestSyntax) **   <a name="translate-StartTextTranslationJob-request-TerminologyNames"></a>
The name of a custom terminology resource to add to the translation job. This resource lists examples source terms and the desired translation for each term.
This parameter accepts only one custom terminology resource.
If you specify multiple target languages for the job, translate uses the designated terminology for each requested target language that has an entry for the source term in the terminology file.
For a list of available custom terminology resources, use the [ListTerminologies](API_ListTerminologies.md) operation.
For more information, see [Custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) in the Amazon Translate Developer Guide.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

## Response Syntax
<a name="API_StartTextTranslationJob_ResponseSyntax"></a>

```
{
   "JobId": "string",
   "JobStatus": "string"
}
```

## Response Elements
<a name="API_StartTextTranslationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartTextTranslationJob_ResponseSyntax) **   <a name="translate-StartTextTranslationJob-response-JobId"></a>
The identifier generated for the job. To get the status of a job, use this ID with the [DescribeTextTranslationJob](API_DescribeTextTranslationJob.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`

 ** [JobStatus](#API_StartTextTranslationJob_ResponseSyntax) **   <a name="translate-StartTextTranslationJob-response-JobStatus"></a>
The status of the job. Possible values include:
+  `SUBMITTED` - The job has been received and is queued for processing.
+  `IN_PROGRESS` - Amazon Translate is processing the job.
+  `COMPLETED` - The job was successfully completed and the output is available.
+  `COMPLETED_WITH_ERROR` - The job was completed with errors. The errors can be analyzed in the job's output.
+  `FAILED` - The job did not complete. To get details, use the [DescribeTextTranslationJob](API_DescribeTextTranslationJob.md) operation.
+  `STOP_REQUESTED` - The user who started the job has requested that it be stopped.
+  `STOPPED` - The job has been stopped.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERROR | FAILED | STOP_REQUESTED | STOPPED`

## Errors
<a name="API_StartTextTranslationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value of the parameter is not valid. Review the value of the parameter you are using to correct it, and then retry your operation.
HTTP Status Code: 400

 ** InvalidRequestException **
 The request that you made is not valid. Check your request to determine why it's not valid and then retry the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource you are looking for has not been found. Review the resource you're looking for and see if a different resource will accomplish your needs before retrying the revised request.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again.
HTTP Status Code: 400

 ** UnsupportedLanguagePairException **
Amazon Translate does not support translation from the language of the source text into the requested target language. For more information, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
 ** SourceLanguageCode **
The language code for the language of the input text.
 ** TargetLanguageCode **
The language code for the language of the translated text.
HTTP Status Code: 400

## See Also
<a name="API_StartTextTranslationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/StartTextTranslationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/StartTextTranslationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
