---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_DescribeTextTranslationJob.html
---

# DescribeTextTranslationJob
<a name="API_DescribeTextTranslationJob"></a>

Gets the properties associated with an asynchronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.

## Request Syntax
<a name="API_DescribeTextTranslationJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTextTranslationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeTextTranslationJob_RequestSyntax) **   <a name="translate-DescribeTextTranslationJob-request-JobId"></a>
The identifier that Amazon Translate generated for the job. The [StartTextTranslationJob](API_StartTextTranslationJob.md) operation returns this identifier in its response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: Yes

## Response Syntax
<a name="API_DescribeTextTranslationJob_ResponseSyntax"></a>

```
{
   "TextTranslationJobProperties": {
      "DataAccessRoleArn": "string",
      "EndTime": number,
      "InputDataConfig": {
         "ContentType": "string",
         "S3Uri": "string"
      },
      "JobDetails": {
         "DocumentsWithErrorsCount": number,
         "InputDocumentsCount": number,
         "TranslatedDocumentsCount": number
      },
      "JobId": "string",
      "JobName": "string",
      "JobStatus": "string",
      "Message": "string",
      "OutputDataConfig": {
         "EncryptionKey": {
            "Id": "string",
            "Type": "string"
         },
         "S3Uri": "string"
      },
      "ParallelDataNames": [ "string" ],
      "Settings": {
         "Brevity": "string",
         "Formality": "string",
         "Profanity": "string"
      },
      "SourceLanguageCode": "string",
      "SubmittedTime": number,
      "TargetLanguageCodes": [ "string" ],
      "TerminologyNames": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeTextTranslationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TextTranslationJobProperties](#API_DescribeTextTranslationJob_ResponseSyntax) **   <a name="translate-DescribeTextTranslationJob-response-TextTranslationJobProperties"></a>
An object that contains the properties associated with an asynchronous batch translation job.
Type: [TextTranslationJobProperties](API_TextTranslationJobProperties.md) object

## Errors
<a name="API_DescribeTextTranslationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource you are looking for has not been found. Review the resource you're looking for and see if a different resource will accomplish your needs before retrying the revised request.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTextTranslationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/DescribeTextTranslationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/DescribeTextTranslationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
