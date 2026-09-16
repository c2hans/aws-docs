---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileAttributeValues.html
---

# ListProfileAttributeValues
<a name="API_connect-customer-profiles_ListProfileAttributeValues"></a>

Fetch the possible attribute values given the attribute name.

## Request Syntax
<a name="API_connect-customer-profiles_ListProfileAttributeValues_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/profile-attributes/{{AttributeName}}/values HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListProfileAttributeValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeName](#API_connect-customer-profiles_ListProfileAttributeValues_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-request-uri-AttributeName"></a>
The attribute name.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [DomainName](#API_connect-customer-profiles_ListProfileAttributeValues_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-request-uri-DomainName"></a>
The unique identifier of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_ListProfileAttributeValues_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListProfileAttributeValues_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
Content-type: application/json

{
   "AttributeName": "string",
   "DomainName": "string",
   "Items": [
      {
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListProfileAttributeValues_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_connect-customer-profiles_ListProfileAttributeValues_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-response-StatusCode"></a>
The status code for the response.

The following data is returned in JSON format by the service.

 ** [AttributeName](#API_connect-customer-profiles_ListProfileAttributeValues_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-response-AttributeName"></a>
The attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [DomainName](#API_connect-customer-profiles_ListProfileAttributeValues_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-response-DomainName"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Items](#API_connect-customer-profiles_ListProfileAttributeValues_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListProfileAttributeValues-response-Items"></a>
The items returned as part of the response.
Type: Array of [AttributeValueItem](API_connect-customer-profiles_AttributeValueItem.md) objects

## Errors
<a name="API_connect-customer-profiles_ListProfileAttributeValues_Errors"></a>

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
<a name="API_connect-customer-profiles_ListProfileAttributeValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListProfileAttributeValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListProfileAttributeValues)
