---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_ListLanguages.html
---

# ListLanguages
<a name="API_ListLanguages"></a>

Provides a list of languages (RFC-5646 codes and names) that Amazon Translate supports.

## Request Syntax
<a name="API_ListLanguages_RequestSyntax"></a>

```
{
   "DisplayLanguageCode": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLanguages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DisplayLanguageCode](#API_ListLanguages_RequestSyntax) **   <a name="translate-ListLanguages-request-DisplayLanguageCode"></a>
The language code for the language to use to display the language names in the response. The language code is `en` by default.
Type: String
Valid Values: `de | en | es | fr | it | ja | ko | pt | zh | zh-TW`
Required: No

 ** [MaxResults](#API_ListLanguages_RequestSyntax) **   <a name="translate-ListLanguages-request-MaxResults"></a>
The maximum number of results to return in each response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListLanguages_RequestSyntax) **   <a name="translate-ListLanguages-request-NextToken"></a>
Include the NextToken value to fetch the next group of supported languages.
Type: String
Length Constraints: Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`
Required: No

## Response Syntax
<a name="API_ListLanguages_ResponseSyntax"></a>

```
{
   "DisplayLanguageCode": "string",
   "Languages": [
      {
         "LanguageCode": "string",
         "LanguageName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLanguages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DisplayLanguageCode](#API_ListLanguages_ResponseSyntax) **   <a name="translate-ListLanguages-response-DisplayLanguageCode"></a>
The language code passed in with the request.
Type: String
Valid Values: `de | en | es | fr | it | ja | ko | pt | zh | zh-TW`

 ** [Languages](#API_ListLanguages_ResponseSyntax) **   <a name="translate-ListLanguages-response-Languages"></a>
The list of supported languages.
Type: Array of [Language](API_Language.md) objects

 ** [NextToken](#API_ListLanguages_ResponseSyntax) **   <a name="translate-ListLanguages-response-NextToken"></a>
 If the response does not include all remaining results, use the NextToken in the next request to fetch the next group of supported languages.
Type: String
Length Constraints: Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Errors
<a name="API_ListLanguages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value of the parameter is not valid. Review the value of the parameter you are using to correct it, and then retry your operation.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again.
HTTP Status Code: 400

 ** UnsupportedDisplayLanguageCodeException **
Requested display language code is not supported.
 ** DisplayLanguageCode **
Language code passed in with the request.
HTTP Status Code: 400

## See Also
<a name="API_ListLanguages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/ListLanguages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/ListLanguages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/ListLanguages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/ListLanguages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/ListLanguages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/ListLanguages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/ListLanguages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/ListLanguages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/ListLanguages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/ListLanguages)
