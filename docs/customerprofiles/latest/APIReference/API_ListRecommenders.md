---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenders.html
---

# ListRecommenders
<a name="API_connect-customer-profiles_ListRecommenders"></a>

Returns a list of recommenders in the specified domain.

## Request Syntax
<a name="API_connect-customer-profiles_ListRecommenders_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/recommenders?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListRecommenders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListRecommenders_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenders-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListRecommenders_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenders-request-uri-MaxResults"></a>
The maximum number of recommenders to return in the response. The default value is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenders_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenders-request-uri-NextToken"></a>
A token received from a previous ListRecommenders call to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListRecommenders_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListRecommenders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Recommenders": [
      {
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
         "RecipeName": "string",
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
         "RecommenderSchemaName": "string",
         "Status": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListRecommenders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenders_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenders-response-NextToken"></a>
A token to retrieve the next page of results. Null if there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Recommenders](#API_connect-customer-profiles_ListRecommenders_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenders-response-Recommenders"></a>
A list of recommenders and their properties in the specified domain.
Type: Array of [RecommenderSummary](API_connect-customer-profiles_RecommenderSummary.md) objects

## Errors
<a name="API_connect-customer-profiles_ListRecommenders_Errors"></a>

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
<a name="API_connect-customer-profiles_ListRecommenders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListRecommenders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListRecommenders)
