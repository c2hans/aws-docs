---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateRecommenderSchema.html
---

# CreateRecommenderSchema
<a name="API_connect-customer-profiles_CreateRecommenderSchema"></a>

Creates a recommender schema. A recommender schema defines the set of data columns available for training recommenders and filters under a domain.

## Request Syntax
<a name="API_connect-customer-profiles_CreateRecommenderSchema_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/recommender-schemas/{{RecommenderSchemaName}} HTTP/1.1
Content-type: application/json

{
   "Fields": {
      "{{string}}" : [
         {
            "ContentType": "{{string}}",
            "FeatureType": "{{string}}",
            "TargetFieldName": "{{string}}"
         }
      ]
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateRecommenderSchema_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderSchemaName](#API_connect-customer-profiles_CreateRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-request-uri-RecommenderSchemaName"></a>
The name of the recommender schema. The name must be unique within the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateRecommenderSchema_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Fields](#API_connect-customer-profiles_CreateRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-request-Fields"></a>
A map of dataset type to column definitions that specifies which data columns to include in the schema. The `_webAnalytics` and `_catalogItem` keys are supported.
Type: String to array of [RecommenderSchemaField](API_connect-customer-profiles_RecommenderSchemaField.md) objects map
Map Entries: Maximum number of 2 items.
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Required: Yes

 ** [Tags](#API_connect-customer-profiles_CreateRecommenderSchema_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax"></a>

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
   "RecommenderSchemaArn": "string",
   "RecommenderSchemaName": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateRecommenderSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-CreatedAt"></a>
The timestamp of when the recommender schema was created.
Type: Timestamp

 ** [Fields](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-Fields"></a>
A map of dataset type to column definitions included in the schema.
Type: String to array of [RecommenderSchemaField](API_connect-customer-profiles_RecommenderSchemaField.md) objects map
Map Entries: Maximum number of 2 items.
Array Members: Minimum number of 1 item. Maximum number of 9 items.

 ** [RecommenderSchemaArn](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-RecommenderSchemaArn"></a>
The Amazon Resource Name (ARN) of the recommender schema.
Type: String
Pattern: `arn:([a-z\d-]+):profile:.*:.*:.+`

 ** [RecommenderSchemaName](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-RecommenderSchemaName"></a>
The name of the recommender schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Status](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-Status"></a>
The status of the recommender schema.
Type: String
Valid Values: `ACTIVE | DELETING`

 ** [Tags](#API_connect-customer-profiles_CreateRecommenderSchema_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateRecommenderSchema-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_CreateRecommenderSchema_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateRecommenderSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateRecommenderSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateRecommenderSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
