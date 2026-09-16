---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferICD10CM.html
---

# InferICD10CM
<a name="API_InferICD10CM"></a>

InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts.

## Request Syntax
<a name="API_InferICD10CM_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_InferICD10CM_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_InferICD10CM_RequestSyntax) **   <a name="comprehendmedical-InferICD10CM-request-Text"></a>
The input text used for analysis. The input for InferICD10CM is a string from 1 to 10000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

## Response Syntax
<a name="API_InferICD10CM_ResponseSyntax"></a>

```
{
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
         "ICD10CMConcepts": [
            {
               "Code": "string",
               "Description": "string",
               "Score": number
            }
         ],
         "Id": number,
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
<a name="API_InferICD10CM_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_InferICD10CM_ResponseSyntax) **   <a name="comprehendmedical-InferICD10CM-response-Entities"></a>
The medical conditions detected in the text linked to ICD-10-CM concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.
Type: Array of [ICD10CMEntity](API_ICD10CMEntity.md) objects

 ** [ModelVersion](#API_InferICD10CM_ResponseSyntax) **   <a name="comprehendmedical-InferICD10CM-response-ModelVersion"></a>
The version of the model used to analyze the documents, in the format *n*.*n*.*n* You can use this information to track the model used for a particular batch of documents.
Type: String
Length Constraints: Minimum length of 1.

 ** [PaginationToken](#API_InferICD10CM_ResponseSyntax) **   <a name="comprehendmedical-InferICD10CM-response-PaginationToken"></a>
If the result of the previous request to `InferICD10CM` was truncated, include the `PaginationToken` to fetch the next page of medical condition entities.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_InferICD10CM_Errors"></a>

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
<a name="API_InferICD10CM_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/InferICD10CM)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/InferICD10CM)
