---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html
---

# ListLinkedWhatsAppBusinessAccounts
<a name="API_ListLinkedWhatsAppBusinessAccounts"></a>

List all WhatsApp Business Accounts linked to your AWS account.

## Request Syntax
<a name="API_ListLinkedWhatsAppBusinessAccounts_RequestSyntax"></a>

```
GET /v1/whatsapp/waba/list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLinkedWhatsAppBusinessAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListLinkedWhatsAppBusinessAccounts_RequestSyntax) **   <a name="Social-ListLinkedWhatsAppBusinessAccounts-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListLinkedWhatsAppBusinessAccounts_RequestSyntax) **   <a name="Social-ListLinkedWhatsAppBusinessAccounts-request-uri-nextToken"></a>
The next token for pagination.
Length Constraints: Minimum length of 1. Maximum length of 600.

## Request Body
<a name="API_ListLinkedWhatsAppBusinessAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLinkedWhatsAppBusinessAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "linkedAccounts": [
      {
         "arn": "string",
         "datasetId": "string",
         "eventDestinations": [
            {
               "eventDestinationArn": "string",
               "roleArn": "string"
            }
         ],
         "id": "string",
         "linkDate": number,
         "marketingMessagesOnboardingStatus": "string",
         "registrationStatus": "string",
         "wabaId": "string",
         "wabaName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLinkedWhatsAppBusinessAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [linkedAccounts](#API_ListLinkedWhatsAppBusinessAccounts_ResponseSyntax) **   <a name="Social-ListLinkedWhatsAppBusinessAccounts-response-linkedAccounts"></a>
A list of WhatsApp Business Accounts linked to your AWS account.
Type: Array of [LinkedWhatsAppBusinessAccountSummary](API_LinkedWhatsAppBusinessAccountSummary.md) objects

 ** [nextToken](#API_ListLinkedWhatsAppBusinessAccounts_ResponseSyntax) **   <a name="Social-ListLinkedWhatsAppBusinessAccounts-response-nextToken"></a>
The next token for pagination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.

## Errors
<a name="API_ListLinkedWhatsAppBusinessAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_ListLinkedWhatsAppBusinessAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/ListLinkedWhatsAppBusinessAccounts)
