---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributeDefinitions.html
---

# ListCalculatedAttributeDefinitions
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions"></a>

Lists calculated attribute definitions for Customer Profiles

## Request Syntax
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/calculated-attributes?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListCalculatedAttributeDefinitions-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListCalculatedAttributeDefinitions-request-uri-MaxResults"></a>
The maximum number of calculated attribute definitions returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListCalculatedAttributeDefinitions-request-uri-NextToken"></a>
The pagination token from the previous call to ListCalculatedAttributeDefinitions.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CalculatedAttributeName": "string",
         "CreatedAt": number,
         "Description": "string",
         "DisplayName": "string",
         "LastUpdatedAt": number,
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "UseHistoricalData": boolean
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListCalculatedAttributeDefinitions_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListCalculatedAttributeDefinitions-response-Items"></a>
The list of calculated attribute definitions.
Type: Array of [ListCalculatedAttributeDefinitionItem](API_connect-customer-profiles_ListCalculatedAttributeDefinitionItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListCalculatedAttributeDefinitions_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListCalculatedAttributeDefinitions-response-NextToken"></a>
The pagination token from the previous call to ListCalculatedAttributeDefinitions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_Errors"></a>

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
<a name="API_connect-customer-profiles_ListCalculatedAttributeDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions)
