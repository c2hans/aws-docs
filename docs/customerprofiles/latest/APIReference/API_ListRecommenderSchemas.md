---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderSchemas.html
---

# ListRecommenderSchemas
<a name="API_connect-customer-profiles_ListRecommenderSchemas"></a>

Returns a list of recommender schemas in the specified domain.

## Request Syntax
<a name="API_connect-customer-profiles_ListRecommenderSchemas_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/recommender-schemas?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListRecommenderSchemas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListRecommenderSchemas_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderSchemas-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListRecommenderSchemas_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderSchemas-request-uri-MaxResults"></a>
The maximum number of recommender schemas to return in the response. The default value is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenderSchemas_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderSchemas-request-uri-NextToken"></a>
A token received from a previous ListRecommenderSchemas call to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListRecommenderSchemas_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListRecommenderSchemas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecommenderSchemas": [
      {
         "CreatedAt": number,
         "Fields": {
            "string" : [
               {
                  "ContentType": "string",
                  "FeatureType": "string",
                  "TargetFieldName": "string"
               }
            ]
         },
         "RecommenderSchemaName": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListRecommenderSchemas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_connect-customer-profiles_ListRecommenderSchemas_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderSchemas-response-NextToken"></a>
A token to retrieve the next page of results. Null if there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [RecommenderSchemas](#API_connect-customer-profiles_ListRecommenderSchemas_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListRecommenderSchemas-response-RecommenderSchemas"></a>
A list of recommender schemas and their properties in the specified domain.
Type: Array of [RecommenderSchemaSummary](API_connect-customer-profiles_RecommenderSchemaSummary.md) objects

## Errors
<a name="API_connect-customer-profiles_ListRecommenderSchemas_Errors"></a>

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
<a name="API_connect-customer-profiles_ListRecommenderSchemas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListRecommenderSchemas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListRecommenderSchemas)
