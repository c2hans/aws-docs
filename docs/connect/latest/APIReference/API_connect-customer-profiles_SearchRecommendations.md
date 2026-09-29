---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_SearchRecommendations.html
---

# SearchRecommendations
<a name="API_connect-customer-profiles_SearchRecommendations"></a>

Retrieves recommendations for a profile in a specific domain. The profile is identified using a search key, which consists of a `KeyName` and a `KeyValues` list. The `KeyName` can be a predefined key (for example, `_profileId`, `_phone`, `_email`) or a custom-defined key.

The search key must match exactly one profile. If no profile matches the search key, the operation returns a `ResourceNotFoundException`. If more than one profile matches the search key, the operation returns a `BadRequestException`. You can use the SearchProfiles API to review the matching profiles.

## Request Syntax
<a name="API_connect-customer-profiles_SearchRecommendations_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/recommendations HTTP/1.1
Content-type: application/json

{
   "CandidateIds": [ "{{string}}" ],
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "Diversity": {
      "Enabled": {{boolean}},
      "Values": {
         "{{string}}" : {{number}}
      }
   },
   "KeyName": "{{string}}",
   "KeyValues": [ "{{string}}" ],
   "MaxRecommendations": {{number}},
   "Metadata": {
      "Columns": [ "{{string}}" ]
   },
   "Recommender": {
      "Filters": [
         {
            "Name": "{{string}}",
            "Values": {
               "{{string}}" : "{{string}}"
            }
         }
      ],
      "Name": "{{string}}",
      "PromotionalFilters": [
         {
            "Name": "{{string}}",
            "PercentPromotedItems": {{number}},
            "PromotionName": "{{string}}",
            "Values": {
               "{{string}}" : "{{string}}"
            }
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_SearchRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_SearchRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CandidateIds](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-CandidateIds"></a>
A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Context](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-Context"></a>
The contextual metadata used to provide dynamic runtime information to tailor recommendations.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Diversity](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-Diversity"></a>
Runtime diversity configuration for this request. Enables diversity-aware recommendations and optionally supplies values for placeholder-based diversity caps configured on the recommender.
Type: [RecommendationDiversityConfig](API_connect-customer-profiles_RecommendationDiversityConfig.md) object
Required: No

 ** [KeyName](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-KeyName"></a>
A searchable identifier of a customer profile. You can use a predefined key, such as `_profileId`, `_phone`, or `_email`, or a custom-defined key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [KeyValues](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-KeyValues"></a>
A list of key values. Provide one value for each field of the search key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [MaxRecommendations](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-MaxRecommendations"></a>
The maximum number of recommendations to return. The default value is 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [Metadata](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-Metadata"></a>
Configuration for metadata to include in recommendation responses.
Type: [RecommendationMetadata](API_connect-customer-profiles_RecommendationMetadata.md) object
Required: No

 ** [Recommender](#API_connect-customer-profiles_SearchRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-request-Recommender"></a>
The recommender used to generate the recommendations.
Type: [Recommender](API_connect-customer-profiles_Recommender.md) object
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_SearchRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileId": "string",
   "Recommendations": [
      {
         "CatalogItem": {
            "AdditionalInformation": "string",
            "Attributes": {
               "string" : "string"
            },
            "Category": "string",
            "Code": "string",
            "CreatedAt": number,
            "Description": "string",
            "Id": "string",
            "ImageLink": "string",
            "Link": "string",
            "Name": "string",
            "Price": "string",
            "Type": "string",
            "UpdatedAt": number
         },
         "Score": number
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_SearchRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileId](#API_connect-customer-profiles_SearchRecommendations_ResponseSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-response-ProfileId"></a>
The unique identifier of the profile for which to retrieve recommendations.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [Recommendations](#API_connect-customer-profiles_SearchRecommendations_ResponseSyntax) **   <a name="connect-connect-customer-profiles_SearchRecommendations-response-Recommendations"></a>
List of recommendations generated by the recommender.
Type: Array of [Recommendation](API_connect-customer-profiles_Recommendation.md) objects

## Errors
<a name="API_connect-customer-profiles_SearchRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_SearchRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/SearchRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SearchRecommendations)
