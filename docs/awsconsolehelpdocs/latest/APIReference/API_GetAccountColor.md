---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_GetAccountColor.html
---

# GetAccountColor (Deprecated)
<a name="API_GetAccountColor"></a>

**Important**
This action has been deprecated. Use [GetAccountCustomizations](API_GetAccountCustomizations.md) instead.

Gets the color associated with the account.

## Request Syntax
<a name="API_GetAccountColor_RequestSyntax"></a>

```
GET /v1/account-color HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountColor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountColor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountColor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "color": "string"
}
```

## Response Elements
<a name="API_GetAccountColor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**color**
The color associated with the account.
Type: String
Valid Values: `none` \| `pink` \| `purple` \| `darkBlue` \| `lightBlue` \| `teal` \| `green` \| `yellow` \| `orange` \| `red`

## Errors
<a name="API_GetAccountColor_Errors"></a>

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
