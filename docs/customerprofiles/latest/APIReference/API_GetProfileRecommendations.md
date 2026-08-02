---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileRecommendations.html
---

# GetProfileRecommendations
<a name="API_connect-customer-profiles_GetProfileRecommendations"></a>

Fetches the recommendations for a profile in the input Customer Profiles domain. Fetches all the profile recommendations

## Request Syntax
<a name="API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/{{ProfileId}}/recommendations HTTP/1.1
Content-type: application/json

{
   "CandidateIds": [ "{{string}}" ],
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "MaxResults": {{number}},
   "MetadataConfig": {
      "MetadataColumns": [ "{{string}}" ]
   },
   "RecommenderFilters": [
      {
         "Name": "{{string}}",
         "Values": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "RecommenderName": "{{string}}",
   "RecommenderPromotionalFilters": [
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
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetProfileRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ProfileId](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-uri-ProfileId"></a>
The unique identifier of the profile for which to retrieve recommendations.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetProfileRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CandidateIds](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-CandidateIds"></a>
A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Context](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-Context"></a>
The contextual metadata used to provide dynamic runtime information to tailor recommendations.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [MaxResults](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-MaxResults"></a>
The maximum number of recommendations to return. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [MetadataConfig](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-MetadataConfig"></a>
Configuration for including item metadata in the recommendation response. Use this to specify which metadata columns to return alongside recommended items.
Type: [MetadataConfig](API_connect-customer-profiles_MetadataConfig.md) object
Required: No

 ** [RecommenderFilters](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-RecommenderFilters"></a>
A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.
Type: Array of [RecommenderFilter](API_connect-customer-profiles_RecommenderFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** [RecommenderName](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-RecommenderName"></a>
The unique name of the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderPromotionalFilters](#API_connect-customer-profiles_GetProfileRecommendations_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-request-RecommenderPromotionalFilters"></a>
A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.
Type: Array of [RecommenderPromotionalFilter](API_connect-customer-profiles_RecommenderPromotionalFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_GetProfileRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_connect-customer-profiles_GetProfileRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Recommendations](#API_connect-customer-profiles_GetProfileRecommendations_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileRecommendations-response-Recommendations"></a>
List of recommendations generated by the recommender.
Type: Array of [Recommendation](API_connect-customer-profiles_Recommendation.md) objects

## Errors
<a name="API_connect-customer-profiles_GetProfileRecommendations_Errors"></a>

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
<a name="API_connect-customer-profiles_GetProfileRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetProfileRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetProfileRecommendations)
