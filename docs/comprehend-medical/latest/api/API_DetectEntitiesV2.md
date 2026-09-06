---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectEntitiesV2.html
---

# DetectEntitiesV2
<a name="API_DetectEntitiesV2"></a>

Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.

The `DetectEntitiesV2` operation replaces the [DetectEntities](API_DetectEntities.md) operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the `DetectEntitiesV2` operation in all new applications.

The `DetectEntitiesV2` operation returns the `Acuity` and `Direction` entities as attributes instead of types.

## Request Syntax
<a name="API_DetectEntitiesV2_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectEntitiesV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_DetectEntitiesV2_RequestSyntax) **   <a name="comprehendmedical-DetectEntitiesV2-request-Text"></a>
A UTF-8 string containing the clinical content being examined for entities. Each string must contain fewer than 20,000 bytes of characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20000.
Required: Yes

## Response Syntax
<a name="API_DetectEntitiesV2_ResponseSyntax"></a>

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
   "PaginationToken": "string",
   "UnmappedAttributes": [
      {
         "Attribute": {
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
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DetectEntitiesV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_DetectEntitiesV2_ResponseSyntax) **   <a name="comprehendmedical-DetectEntitiesV2-response-Entities"></a>
The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence in the detection and analysis. Attributes and traits of the entity are also returned.
Type: Array of [Entity](API_Entity.md) objects

 ** [ModelVersion](#API_DetectEntitiesV2_ResponseSyntax) **   <a name="comprehendmedical-DetectEntitiesV2-response-ModelVersion"></a>
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.
Type: String
Length Constraints: Minimum length of 1.

 ** [PaginationToken](#API_DetectEntitiesV2_ResponseSyntax) **   <a name="comprehendmedical-DetectEntitiesV2-response-PaginationToken"></a>
If the result to the `DetectEntitiesV2` operation was truncated, include the `PaginationToken` to fetch the next page of entities.
Type: String
Length Constraints: Minimum length of 1.

 ** [UnmappedAttributes](#API_DetectEntitiesV2_ResponseSyntax) **   <a name="comprehendmedical-DetectEntitiesV2-response-UnmappedAttributes"></a>
Attributes extracted from the input text that couldn't be related to an entity.
Type: Array of [UnmappedAttribute](API_UnmappedAttribute.md) objects

## Errors
<a name="API_DetectEntitiesV2_Errors"></a>

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
<a name="API_DetectEntitiesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/DetectEntitiesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/DetectEntitiesV2)
