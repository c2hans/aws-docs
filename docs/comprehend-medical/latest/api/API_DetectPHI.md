---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectPHI.html
---

# DetectPHI
<a name="API_DetectPHI"></a>

 Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.

## Request Syntax
<a name="API_DetectPHI_RequestSyntax"></a>

```
{
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_DetectPHI_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Text](#API_DetectPHI_RequestSyntax) **   <a name="comprehendmedical-DetectPHI-request-Text"></a>
 A UTF-8 text string containing the clinical content being examined for PHI entities. Each string must contain fewer than 20,000 bytes of characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20000.
Required: Yes

## Response Syntax
<a name="API_DetectPHI_ResponseSyntax"></a>

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
   "PaginationToken": "string"
}
```

## Response Elements
<a name="API_DetectPHI_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_DetectPHI_ResponseSyntax) **   <a name="comprehendmedical-DetectPHI-response-Entities"></a>
 The collection of PHI entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Comprehend Medical; has in its detection.
Type: Array of [Entity](API_Entity.md) objects

 ** [ModelVersion](#API_DetectPHI_ResponseSyntax) **   <a name="comprehendmedical-DetectPHI-response-ModelVersion"></a>
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.
Type: String
Length Constraints: Minimum length of 1.

 ** [PaginationToken](#API_DetectPHI_ResponseSyntax) **   <a name="comprehendmedical-DetectPHI-response-PaginationToken"></a>
 If the result of the previous request to `DetectPHI` was truncated, include the `PaginationToken` to fetch the next page of PHI entities.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DetectPHI_Errors"></a>

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
<a name="API_DetectPHI_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/DetectPHI)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/DetectPHI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
