---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_CreateRecommender.html
---

# CreateRecommender
<a name="API_connect-customer-profiles_CreateRecommender"></a>

Creates a recommender

## Request Syntax
<a name="API_connect-customer-profiles_CreateRecommender_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/recommenders/{{RecommenderName}} HTTP/1.1
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
   "RecommenderRecipeName": "{{string}}",
   "RecommenderSchemaName": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateRecommender_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderName](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-uri-RecommenderName"></a>
The name of the recommender.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateRecommender_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-Description"></a>
The description of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [RecommenderConfig](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-RecommenderConfig"></a>
The recommender configuration.
Type: [RecommenderConfig](API_connect-customer-profiles_RecommenderConfig.md) object
Required: No

 ** [RecommenderRecipeName](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-RecommenderRecipeName"></a>
The name of the recommeder recipe.
Type: String
Valid Values: `recommended-for-you | similar-items | frequently-paired-items | popular-items | trending-now | personalized-ranking`
Required: Yes

 ** [RecommenderSchemaName](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-RecommenderSchemaName"></a>
The name of the recommender schema to use for this recommender. If not specified, the default schema is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** [Tags](#API_connect-customer-profiles_CreateRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateRecommender_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RecommenderArn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateRecommender_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecommenderArn](#API_connect-customer-profiles_CreateRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-response-RecommenderArn"></a>
The ARN of the recommender
Type: String
Pattern: `arn:([a-z\d-]+):profile:.*:.*:.+`

 ** [Tags](#API_connect-customer-profiles_CreateRecommender_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommender-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_CreateRecommender_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateRecommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateRecommender)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateRecommender)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
