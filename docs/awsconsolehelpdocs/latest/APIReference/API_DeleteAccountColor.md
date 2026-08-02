---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_DeleteAccountColor.html
---

# DeleteAccountColor (Deprecated)
<a name="API_DeleteAccountColor"></a>

**Important**
This action has been deprecated. Use [UpdateAccountCustomizations](API_UpdateAccountCustomizations.md) with `accountColor` set to `"none"` instead.

Deletes the account color setting.

## Request Syntax
<a name="API_DeleteAccountColor_RequestSyntax"></a>

```
DELETE /v1/account-color HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountColor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteAccountColor_RequestBody"></a>

The request does not have a request body.

## Response Elements
<a name="API_DeleteAccountColor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccountColor_Errors"></a>

**AccessDeniedException**
You do not have sufficient access to perform this action.
HTTP Status Code: 403

**InternalServerException**
The service encountered an internal error. Try your request again later.
HTTP Status Code: 500

**ThrottlingException**
The request was denied because of request throttling. Reduce the frequency of your requests.
HTTP Status Code: 429

**ValidationException**
The input does not satisfy the constraints that are specified by the service.
HTTP Status Code: 400
