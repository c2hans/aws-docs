---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetRecommenderFilter.html
---

# GetRecommenderFilter
<a name="API_connect-customer-profiles_GetRecommenderFilter"></a>

Retrieves information about a specific recommender filter in a domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetRecommenderFilter_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/recommender-filters/{{RecommenderFilterName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetRecommenderFilter_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetRecommenderFilter_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderFilterName](#API_connect-customer-profiles_GetRecommenderFilter_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-request-uri-RecommenderFilterName"></a>
The name of the recommender filter to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetRecommenderFilter_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "FailureReason": "string",
   "RecommenderFilterExpression": "string",
   "RecommenderFilterName": "string",
   "RecommenderSchemaName": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetRecommenderFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-CreatedAt"></a>
The timestamp of when the recommender filter was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-Description"></a>
The description of the recommender filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [FailureReason](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-FailureReason"></a>
If the recommender filter failed, provides the reason for the failure.
Type: String

 ** [RecommenderFilterExpression](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-RecommenderFilterExpression"></a>
The filter expression that defines which items to include or exclude from recommendations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [RecommenderFilterName](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-RecommenderFilterName"></a>
The name of the recommender filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9_-]+`

 ** [RecommenderSchemaName](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-RecommenderSchemaName"></a>
The name of the recommender schema associated with this recommender filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Status](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-Status"></a>
The status of the recommender filter.
Type: String
Valid Values: `ACTIVE | PENDING | IN_PROGRESS | FAILED | DELETING`

 ** [Tags](#API_connect-customer-profiles_GetRecommenderFilter_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderFilter-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_GetRecommenderFilter_Errors"></a>

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
<a name="API_connect-customer-profiles_GetRecommenderFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetRecommenderFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetRecommenderFilter)
