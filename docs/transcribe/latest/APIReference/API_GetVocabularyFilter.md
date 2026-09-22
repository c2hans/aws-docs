---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_GetVocabularyFilter.html
---

# GetVocabularyFilter
<a name="API_GetVocabularyFilter"></a>

Provides information about the specified custom vocabulary filter.

To get a list of your custom vocabulary filters, use the [ListVocabularyFilters](API_ListVocabularyFilters.md) operation.

## Request Syntax
<a name="API_GetVocabularyFilter_RequestSyntax"></a>

```
{
   "VocabularyFilterName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetVocabularyFilter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VocabularyFilterName](#API_GetVocabularyFilter_RequestSyntax) **   <a name="transcribe-GetVocabularyFilter-request-VocabularyFilterName"></a>
The name of the custom vocabulary filter you want information about. Custom vocabulary filter names are case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

## Response Syntax
<a name="API_GetVocabularyFilter_ResponseSyntax"></a>

```
{
   "DataAccessRoleArn": "string",
   "DownloadUri": "string",
   "EncryptionConfiguration": {
      "KMSEncryptionContext": {
         "string" : "string"
      },
      "KMSKey": "string"
   },
   "LanguageCode": "string",
   "LastModifiedTime": number,
   "VocabularyFilterName": "string"
}
```

## Response Elements
<a name="API_GetVocabularyFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataAccessRoleArn](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used to access the Amazon S3 bucket that contains your input files and, if applicable, the AWS KMS key specified in `EncryptionConfiguration`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{0,63}:role/[A-Za-z0-9:_/+=,@.-]{0,1024}$`

 ** [DownloadUri](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-DownloadUri"></a>
The Amazon S3 location where the custom vocabulary filter is stored; use this URI to view or download the custom vocabulary filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|http(s*)://).+`

 ** [EncryptionConfiguration](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-EncryptionConfiguration"></a>
The encryption configuration used for your custom vocabulary filter.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [LanguageCode](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-LanguageCode"></a>
The language code you selected for your custom vocabulary filter.
Type: String
Valid Values: `af-ZA | ar-AE | ar-SA | am-ET | cy-GB | da-DK | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-MX | es-US | fa-AF | fa-IR | fr-CA | fr-FR | ga-IE | gd-GB | he-IL | hi-IN | ht-HT | id-ID | it-IT | ja-JP | jv-ID | km-KH | ko-KR | my-MM | ms-MY | nl-NL | pt-BR | pt-PT | ru-RU | ta-IN | te-IN | tr-TR | zh-CN | zh-TW | th-TH | en-ZA | en-NZ | vi-VN | sv-SE | ab-GE | ast-ES | az-AZ | ba-RU | be-BY | bg-BG | bn-IN | bs-BA | ca-ES | ckb-IQ | ckb-IR | cs-CZ | cy-WL | el-GR | et-EE | et-ET | eu-ES | fi-FI | gl-ES | gu-IN | ha-NG | hr-HR | hu-HU | hy-AM | is-IS | ka-GE | kab-DZ | kk-KZ | kn-IN | ky-KG | lg-IN | lt-LT | lv-LV | mhr-RU | mi-NZ | mk-MK | ml-IN | mn-MN | mr-IN | mt-MT | no-NO | ne-NP | or-IN | pa-IN | pl-PL | ps-AF | ro-RO | rw-RW | si-LK | sk-SK | sl-SI | so-SO | sq-AL | sr-RS | su-ID | sw-BI | sw-KE | sw-RW | sw-TZ | sw-UG | tl-PH | tt-RU | ug-CN | uk-UA | uz-UZ | wo-SN | zh-HK | zu-ZA`

 ** [LastModifiedTime](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-LastModifiedTime"></a>
The date and time the specified custom vocabulary filter was last modified.
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.
Type: Timestamp

 ** [VocabularyFilterName](#API_GetVocabularyFilter_ResponseSyntax) **   <a name="transcribe-GetVocabularyFilter-response-VocabularyFilterName"></a>
The name of the custom vocabulary filter you requested information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`

## Errors
<a name="API_GetVocabularyFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.
HTTP Status Code: 400

 ** InternalFailureException **
There was an internal error. Check the error message, correct the issue, and try your request again.
HTTP Status Code: 500

 ** LimitExceededException **
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.
HTTP Status Code: 400

 ** NotFoundException **
We can't find the requested resource. Check that the specified name is correct and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_GetVocabularyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/GetVocabularyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/GetVocabularyFilter)
