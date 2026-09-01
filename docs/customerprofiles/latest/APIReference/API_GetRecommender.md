---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommender.html
---

# GetRecommender
<a name="API_connect-customer-profiles_GetRecommender"></a>

Retrieves a recommender.

## Request Syntax
<a name="API_connect-customer-profiles_GetRecommender_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/recommenders/{{RecommenderName}}?training-metrics-count={{TrainingMetricsCount}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetRecommender_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderName](#API_connect-customer-profiles_GetRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-request-uri-RecommenderName"></a>
The name of the recommender.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [TrainingMetricsCount](#API_connect-customer-profiles_GetRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-request-uri-TrainingMetricsCount"></a>
The number of training metrics to retrieve for the recommender.
Valid Range: Minimum value of 0. Maximum value of 5.

## Request Body
<a name="API_connect-customer-profiles_GetRecommender_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetRecommender_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActiveRecommenderVersionName": "string",
   "CreatedAt": number,
   "Description": "string",
   "FailureReason": "string",
   "LastUpdatedAt": number,
   "LatestRecommenderUpdate": {
      "CreatedAt": number,
      "FailureReason": "string",
      "LastUpdatedAt": number,
      "RecommenderConfig": {
         "DiversityConfig": {
            "DiversityColumns": [
               {
                  "CapType": "string",
                  "Name": "string",
                  "Target": "string"
               }
            ]
         },
         "EventsConfig": {
            "EventParametersList": [
               {
                  "EventType": "string",
                  "EventValueThreshold": number,
                  "EventWeight": number
               }
            ]
         },
         "ExcludedColumns": {
            "string" : [ "string" ]
         },
         "IncludedColumns": {
            "string" : [ "string" ]
         },
         "InferenceConfig": {
            "MinProvisionedTPS": number
         },
         "TrainingFrequency": number
      },
      "RecommenderVersionName": "string",
      "Status": "string"
   },
   "RecommenderConfig": {
      "DiversityConfig": {
         "DiversityColumns": [
            {
               "CapType": "string",
               "Name": "string",
               "Target": "string"
            }
         ]
      },
      "EventsConfig": {
         "EventParametersList": [
            {
               "EventType": "string",
               "EventValueThreshold": number,
               "EventWeight": number
            }
         ]
      },
      "ExcludedColumns": {
         "string" : [ "string" ]
      },
      "IncludedColumns": {
         "string" : [ "string" ]
      },
      "InferenceConfig": {
         "MinProvisionedTPS": number
      },
      "TrainingFrequency": number
   },
   "RecommenderName": "string",
   "RecommenderRecipeName": "string",
   "RecommenderSchemaName": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "TrainingMetrics": [
      {
         "Metrics": {
            "string" : number
         },
         "RecommenderVersionName": "string",
         "Time": number
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetRecommender_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActiveRecommenderVersionName](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-ActiveRecommenderVersionName"></a>
The name of the recommender version currently serving recommendations. Omitted when no active recommender version is set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+/\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z`

 ** [CreatedAt](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-CreatedAt"></a>
The timestamp of when the recommender was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-Description"></a>
A detailed description of the recommender providing information about its purpose and functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [FailureReason](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-FailureReason"></a>
If the recommender fails, provides the reason for the failure.
Type: String

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-LastUpdatedAt"></a>
The timestamp of when the recommender was edited.
Type: Timestamp

 ** [LatestRecommenderUpdate](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-LatestRecommenderUpdate"></a>
Information about the most recent update performed on the recommender, including status and timestamp.
Type: [RecommenderUpdate](API_connect-customer-profiles_RecommenderUpdate.md) object

 ** [RecommenderConfig](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-RecommenderConfig"></a>
The configuration settings for the recommender, including parameters and settings that define its behavior.
Type: [RecommenderConfig](API_connect-customer-profiles_RecommenderConfig.md) object

 ** [RecommenderName](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-RecommenderName"></a>
The name of the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [RecommenderRecipeName](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-RecommenderRecipeName"></a>
The name of the recipe used by the recommender to generate recommendations.
Type: String
Valid Values: `recommended-for-you | similar-items | frequently-paired-items | popular-items | trending-now | personalized-ranking`

 ** [RecommenderSchemaName](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-RecommenderSchemaName"></a>
The name of the recommender schema associated with this recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Status](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-Status"></a>
The current status of the recommender, indicating whether it is active, creating, updating, or in another state.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | FAILED | STOPPING | INACTIVE | STARTING | DELETING`

 ** [Tags](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [TrainingMetrics](#API_connect-customer-profiles_GetRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommender-response-TrainingMetrics"></a>
A set of metrics that provide information about the recommender's training performance and accuracy.
Type: Array of [TrainingMetrics](API_connect-customer-profiles_TrainingMetrics.md) objects

## Errors
<a name="API_connect-customer-profiles_GetRecommender_Errors"></a>

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
<a name="API_connect-customer-profiles_GetRecommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetRecommender)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetRecommender)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
