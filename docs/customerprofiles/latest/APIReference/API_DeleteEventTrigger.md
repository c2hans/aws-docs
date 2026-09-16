---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteEventTrigger.html
---

# DeleteEventTrigger
<a name="API_connect-customer-profiles_DeleteEventTrigger"></a>

Disable and deletes the Event Trigger.

**Note**
You cannot delete an Event Trigger with an active Integration associated.

## Request Syntax
<a name="API_connect-customer-profiles_DeleteEventTrigger_RequestSyntax"></a>

```
DELETE /domains/{{DomainName}}/event-triggers/{{EventTriggerName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_DeleteEventTrigger_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_DeleteEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_DeleteEventTrigger-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EventTriggerName](#API_connect-customer-profiles_DeleteEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_DeleteEventTrigger-request-uri-EventTriggerName"></a>
The unique name of the event trigger.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_DeleteEventTrigger_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_DeleteEventTrigger_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_DeleteEventTrigger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_connect-customer-profiles_DeleteEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_DeleteEventTrigger-response-Message"></a>
A message that indicates the delete request is done.
Type: String

## Errors
<a name="API_connect-customer-profiles_DeleteEventTrigger_Errors"></a>

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
<a name="API_connect-customer-profiles_DeleteEventTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/DeleteEventTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DeleteEventTrigger)
