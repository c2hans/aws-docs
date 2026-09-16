---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListDomainLayouts.html
---

# ListDomainLayouts
<a name="API_connect-customer-profiles_ListDomainLayouts"></a>

Lists the existing layouts that can be used to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.

## Request Syntax
<a name="API_connect-customer-profiles_ListDomainLayouts_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/layouts?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_ListDomainLayouts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_ListDomainLayouts_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListDomainLayouts-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_ListDomainLayouts_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListDomainLayouts-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_ListDomainLayouts_RequestSyntax) **   <a name="connect-connect-customer-profiles_ListDomainLayouts-request-uri-NextToken"></a>
Identifies the next page of results to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_ListDomainLayouts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_ListDomainLayouts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CreatedAt": number,
         "Description": "string",
         "DisplayName": "string",
         "IsDefault": boolean,
         "LastUpdatedAt": number,
         "LayoutDefinitionName": "string",
         "LayoutType": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_ListDomainLayouts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_ListDomainLayouts_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListDomainLayouts-response-Items"></a>
Contains summary information about an EventStream.
Type: Array of [LayoutItem](API_connect-customer-profiles_LayoutItem.md) objects

 ** [NextToken](#API_connect-customer-profiles_ListDomainLayouts_ResponseSyntax) **   <a name="connect-connect-customer-profiles_ListDomainLayouts-response-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_ListDomainLayouts_Errors"></a>

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
<a name="API_connect-customer-profiles_ListDomainLayouts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/ListDomainLayouts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListDomainLayouts)
