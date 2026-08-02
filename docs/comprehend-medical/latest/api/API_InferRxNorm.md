---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferRxNorm.html
---

# InferRxNorm
<a name="API_InferRxNorm"></a>

InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts.

## Request Syntax
<a name="API_InferRxNorm_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_InferRxNorm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_InferRxNorm_RequestSyntax) **   <a name="comprehendmedical-InferRxNorm-request-Text"></a>
The input text used for analysis. The input for InferRxNorm is a string from 1 to 10000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

## Response Syntax
<a name="API_InferRxNorm_ResponseSyntax"></a>

```
{
   "Entities": [
      {
         "Attributes": [
            {
               "BeginOffset": number,
               "EndOffset": number,
               "Id": number,
               "RelationshipScore": number,
               "Score": number,
               "Text": "string",
               "Traits": [
                  {
                     "Name": "string",
                     "Score": number
                  }
               ],
               "Type": "string"
            }
         ],
         "BeginOffset": number,
         "Category": "string",
         "EndOffset": number,
         "Id": number,
         "RxNormConcepts": [
            {
               "Code": "string",
               "Description": "string",
               "Score": number
            }
         ],
         "Score": number,
         "Text": "string",
         "Traits": [
            {
               "Name": "string",
               "Score": number
            }
         ],
         "Type": "string"
      }
   ],
   "ModelVersion": "string",
   "PaginationToken": "string"
}
```

## Response Elements
<a name="API_InferRxNorm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_InferRxNorm_ResponseSyntax) **   <a name="comprehendmedical-InferRxNorm-response-Entities"></a>
The medication entities detected in the text linked to RxNorm concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.
Type: Array of [RxNormEntity](API_RxNormEntity.md) objects

 ** [ModelVersion](#API_InferRxNorm_ResponseSyntax) **   <a name="comprehendmedical-InferRxNorm-response-ModelVersion"></a>
The version of the model used to analyze the documents, in the format *n*.*n*.*n* You can use this information to track the model used for a particular batch of documents.
Type: String
Length Constraints: Minimum length of 1.

 ** [PaginationToken](#API_InferRxNorm_ResponseSyntax) **   <a name="comprehendmedical-InferRxNorm-response-PaginationToken"></a>
If the result of the previous request to `InferRxNorm` was truncated, include the `PaginationToken` to fetch the next page of medication entities.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_InferRxNorm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidEncodingException **
 The input text was not in valid UTF-8 character encoding. Check your text then retry your request.
HTTP Status Code: 400

 ** InvalidRequestException **
 The request that you made is invalid. Check your request to determine why it's invalid and then retry the request.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The Comprehend Medical; service is temporarily unavailable. Please wait and then retry your request.
HTTP Status Code: 400

 ** TextSizeLimitExceededException **
 The size of the text you submitted exceeds the size limit. Reduce the size of the text or use a smaller document and then retry your request.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again. Contact customer support for more information about a service limit increase.
HTTP Status Code: 400

## See Also
<a name="API_InferRxNorm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/InferRxNorm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/InferRxNorm)
