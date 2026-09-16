---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListObjectTypeAttributes.html
---

# ListObjectTypeAttributes
<a name="API_connect-customer-profiles_ListObjectTypeAttributes"></a>

Fetch the possible attribute values given the attribute name.

## Request Syntax
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/object-types/{{ObjectTypeName}}/attributes?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListObjectTypeAttributes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-request-uri-DomainName"></a>
The unique identifier of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListObjectTypeAttributes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListObjectTypeAttributes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-request-uri-NextToken"></a>
The pagination token from the previous call.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ObjectTypeName](#API_connect-customer-profiles_ListObjectTypeAttributes_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-request-uri-ObjectTypeName"></a>
The name of the profile object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AttributeName": "string",
         "LastUpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListObjectTypeAttributes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-response-Items"></a>
The items returned as part of the response.
Type: Array of [ListObjectTypeAttributeItem](API_connect-customer-profiles_ListObjectTypeAttributeItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListObjectTypeAttributes_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListObjectTypeAttributes-response-NextToken"></a>
The pagination token from the previous call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_Errors"></a>

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
<a name="API_connect-customer-profiles_ListObjectTypeAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListObjectTypeAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListObjectTypeAttributes)
