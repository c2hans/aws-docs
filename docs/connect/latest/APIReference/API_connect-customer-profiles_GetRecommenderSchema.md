---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetRecommenderSchema.html
---

# GetRecommenderSchema
<a name="API_connect-customer-profiles_GetRecommenderSchema"></a>

Retrieves information about a specific recommender schema in a domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetRecommenderSchema_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/recommender-schemas/{{RecommenderSchemaName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetRecommenderSchema_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderSchemaName](#API_connect-customer-profiles_GetRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-request-uri-RecommenderSchemaName"></a>
The name of the recommender schema to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetRecommenderSchema_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetRecommenderSchema_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_connect-customer-profiles_GetRecommenderSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-response-CreatedAt"></a>
The timestamp of when the recommender schema was created.
Type: Timestamp

 ** [Fields](#API_connect-customer-profiles_GetRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-response-Fields"></a>
A map of dataset type to column definitions included in the schema.
Type: String to array of [RecommenderSchemaField](API_connect-customer-profiles_RecommenderSchemaField.md) objects map
Map Entries: Maximum number of 2 items.
Array Members: Minimum number of 1 item. Maximum number of 9 items.

 ** [RecommenderSchemaName](#API_connect-customer-profiles_GetRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-response-RecommenderSchemaName"></a>
The name of the recommender schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Status](#API_connect-customer-profiles_GetRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetRecommenderSchema-response-Status"></a>
The status of the recommender schema.
Type: String
Valid Values: `ACTIVE | DELETING`

## Errors
<a name="API_connect-customer-profiles_GetRecommenderSchema_Errors"></a>

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
<a name="API_connect-customer-profiles_GetRecommenderSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetRecommenderSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetRecommenderSchema)
