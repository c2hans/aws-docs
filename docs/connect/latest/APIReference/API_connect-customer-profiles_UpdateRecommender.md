---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_UpdateRecommender.html
---

# UpdateRecommender
<a name="API_connect-customer-profiles_UpdateRecommender"></a>

Updates the properties of an existing recommender, allowing you to modify its configuration and description.

## Request Syntax
<a name="API_connect-customer-profiles_UpdateRecommender_RequestSyntax"></a>

```
PATCH /domains/{{DomainName}}/recommenders/{{RecommenderName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "RecommenderConfig": {
      "DiversityConfig": {
         "DiversityColumns": [
            {
               "CapType": "{{string}}",
               "Name": "{{string}}",
               "Target": "{{string}}"
            }
         ]
      },
      "EventsConfig": {
         "EventParametersList": [
            {
               "EventType": "{{string}}",
               "EventValueThreshold": {{number}},
               "EventWeight": {{number}}
            }
         ]
      },
      "ExcludedColumns": {
         "{{string}}" : [ "{{string}}" ]
      },
      "IncludedColumns": {
         "{{string}}" : [ "{{string}}" ]
      },
      "InferenceConfig": {
         "MinProvisionedTPS": {{number}}
      },
      "TrainingFrequency": {{number}}
   },
   "RecommenderVersionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_UpdateRecommender_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_UpdateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderName](#API_connect-customer-profiles_UpdateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-request-uri-RecommenderName"></a>
The name of the recommender to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_UpdateRecommender_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-customer-profiles_UpdateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-request-Description"></a>
The new description to assign to the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [RecommenderConfig](#API_connect-customer-profiles_UpdateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-request-RecommenderConfig"></a>
The new configuration settings to apply to the recommender, including updated parameters and settings that define its behavior.
Type: [RecommenderConfig](API_connect-customer-profiles_RecommenderConfig.md) object
Required: No

 ** [RecommenderVersionName](#API_connect-customer-profiles_UpdateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-request-RecommenderVersionName"></a>
The name of a specific recommender version to activate as part of this update (for example, to roll back to a previously trained version).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+/\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z`
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_UpdateRecommender_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RecommenderName": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_UpdateRecommender_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecommenderName](#API_connect-customer-profiles_UpdateRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_UpdateRecommender-response-RecommenderName"></a>
The name of the recommender that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_connect-customer-profiles_UpdateRecommender_Errors"></a>

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
<a name="API_connect-customer-profiles_UpdateRecommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/UpdateRecommender)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/UpdateRecommender)
