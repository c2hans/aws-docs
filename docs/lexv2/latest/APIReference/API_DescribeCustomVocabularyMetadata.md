---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeCustomVocabularyMetadata.html
---

# DescribeCustomVocabularyMetadata
<a name="API_DescribeCustomVocabularyMetadata"></a>

Provides metadata information about a custom vocabulary.

## Request Syntax
<a name="API_DescribeCustomVocabularyMetadata_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/customvocabulary/DEFAULT/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCustomVocabularyMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeCustomVocabularyMetadata_RequestSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-request-uri-botId"></a>
The unique identifier of the bot that contains the custom vocabulary.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeCustomVocabularyMetadata_RequestSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-request-uri-botVersion"></a>
The bot version of the bot to return metadata for.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_DescribeCustomVocabularyMetadata_RequestSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-request-uri-localeId"></a>
The locale to return the custom vocabulary information for. The locale must be `en_GB`.
Required: Yes

## Request Body
<a name="API_DescribeCustomVocabularyMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCustomVocabularyMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "customVocabularyStatus": "string",
   "lastUpdatedDateTime": number,
   "localeId": "string"
}
```

## Response Elements
<a name="API_DescribeCustomVocabularyMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-botId"></a>
The identifier of the bot that contains the custom vocabulary.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-botVersion"></a>
The version of the bot that contains the custom vocabulary to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [creationDateTime](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-creationDateTime"></a>
The date and time that the custom vocabulary was created.
Type: Timestamp

 ** [customVocabularyStatus](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-customVocabularyStatus"></a>
The status of the custom vocabulary. If the status is `Ready` the custom vocabulary is ready to use.
Type: String
Valid Values: `Ready | Deleting | Exporting | Importing | Creating`

 ** [lastUpdatedDateTime](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-lastUpdatedDateTime"></a>
The date and time that the custom vocabulary was last updated.
Type: Timestamp

 ** [localeId](#API_DescribeCustomVocabularyMetadata_ResponseSyntax) **   <a name="lexv2-DescribeCustomVocabularyMetadata-response-localeId"></a>
The locale that contains the custom vocabulary to describe.
Type: String

## Errors
<a name="API_DescribeCustomVocabularyMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCustomVocabularyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeCustomVocabularyMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
