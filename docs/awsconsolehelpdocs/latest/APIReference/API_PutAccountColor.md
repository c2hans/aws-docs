---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_PutAccountColor.html
---

# PutAccountColor (Deprecated)
<a name="API_PutAccountColor"></a>

**Important**
This action has been deprecated. Use [UpdateAccountCustomizations](API_UpdateAccountCustomizations.md) instead.

Sets the color associated with an account.

## Request Syntax
<a name="API_PutAccountColor_RequestSyntax"></a>

```
PUT /v1/account-color HTTP/1.1
Content-type: application/json

{
   "color": "string"
}
```

## URI Request Parameters
<a name="API_PutAccountColor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountColor_RequestBody"></a>

The request accepts the following data in JSON format.

**color**
The color to associate with the account.
Type: String
Valid Values: `none` \| `pink` \| `purple` \| `darkBlue` \| `lightBlue` \| `teal` \| `green` \| `yellow` \| `orange` \| `red`
Required: Yes

## Response Syntax
<a name="API_PutAccountColor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "color": "string"
}
```

## Response Elements
<a name="API_PutAccountColor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**color**
The color associated with the account.
Type: String
Valid Values: `none` \| `pink` \| `purple` \| `darkBlue` \| `lightBlue` \| `teal` \| `green` \| `yellow` \| `orange` \| `red`

## Errors
<a name="API_PutAccountColor_Errors"></a>

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
