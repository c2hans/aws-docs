---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_StopRecommender.html
---

# StopRecommender
<a name="API_connect-customer-profiles_StopRecommender"></a>

Stops a recommender, suspending its ability to generate recommendations. The recommender can be restarted later using StartRecommender.

## Request Syntax
<a name="API_connect-customer-profiles_StopRecommender_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/recommenders/{{RecommenderName}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_StopRecommender_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_StopRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_StopRecommender-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [RecommenderName](#API_connect-customer-profiles_StopRecommender_RequestSyntax) **   <a name="connect-connect-customer-profiles_StopRecommender-request-uri-RecommenderName"></a>
The name of the recommender to stop.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_StopRecommender_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_StopRecommender_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-customer-profiles_StopRecommender_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-customer-profiles_StopRecommender_Errors"></a>

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
<a name="API_connect-customer-profiles_StopRecommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/StopRecommender)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/StopRecommender)
