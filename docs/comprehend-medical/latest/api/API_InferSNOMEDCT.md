---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferSNOMEDCT.html
---

# InferSNOMEDCT
<a name="API_InferSNOMEDCT"></a>

 InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology.

## Request Syntax
<a name="API_InferSNOMEDCT_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_InferSNOMEDCT_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_InferSNOMEDCT_RequestSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-request-Text"></a>
 The input text to be analyzed using InferSNOMEDCT. The text must be a string with 1 to 10000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

## Response Syntax
<a name="API_InferSNOMEDCT_ResponseSyntax"></a>

```
{
   "Characters": {
      "OriginalTextCharacters": number
   },
   "Entities": [
      {
         "Attributes": [
            {
               "BeginOffset": number,
               "Category": "string",
               "EndOffset": number,
               "Id": number,
               "RelationshipScore": number,
               "RelationshipType": "string",
               "Score": number,
               "SNOMEDCTConcepts": [
                  {
                     "Code": "string",
                     "Description": "string",
                     "Score": number
                  }
               ],
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
         "Score": number,
         "SNOMEDCTConcepts": [
            {
               "Code": "string",
               "Description": "string",
               "Score": number
            }
         ],
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
   "PaginationToken": "string",
   "SNOMEDCTDetails": {
      "Edition": "string",
      "Language": "string",
      "VersionDate": "string"
   }
}
```

## Response Elements
<a name="API_InferSNOMEDCT_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Characters](#API_InferSNOMEDCT_ResponseSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-response-Characters"></a>
 The number of characters in the input request documentation.
Type: [Characters](API_Characters.md) object

 ** [Entities](#API_InferSNOMEDCT_ResponseSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-response-Entities"></a>
 The collection of medical concept entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.
Type: Array of [SNOMEDCTEntity](API_SNOMEDCTEntity.md) objects

 ** [ModelVersion](#API_InferSNOMEDCT_ResponseSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-response-ModelVersion"></a>
 The version of the model used to analyze the documents; must be in the format of `n.n.n`. You can use this information to track the model used for a particular batch of documents.
Type: String
Length Constraints: Minimum length of 1.

 ** [PaginationToken](#API_InferSNOMEDCT_ResponseSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-response-PaginationToken"></a>
 If the result of the request is truncated, the pagination token can be used to fetch the next page of entities.
Type: String
Length Constraints: Minimum length of 1.

 ** [SNOMEDCTDetails](#API_InferSNOMEDCT_ResponseSyntax) **   <a name="comprehendmedical-InferSNOMEDCT-response-SNOMEDCTDetails"></a>
 The details of the SNOMED-CT revision, including the edition, language, and version date.
Type: [SNOMEDCTDetails](API_SNOMEDCTDetails.md) object

## Errors
<a name="API_InferSNOMEDCT_Errors"></a>

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
<a name="API_InferSNOMEDCT_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/InferSNOMEDCT)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/InferSNOMEDCT)
