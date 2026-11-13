---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CheckSubdomainAvailability.html
---

# CheckSubdomainAvailability
<a name="API_CheckSubdomainAvailability"></a>

Checks whether a Lightsail subdomain is available to create. Optionally, reserves the subdomain for your account for 15 minutes.

If you don't reserve the subdomain, another account can create it before you do.

## Request Syntax
<a name="API_CheckSubdomainAvailability_RequestSyntax"></a>

```
{
   "reserve": {{boolean}},
   "subdomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_CheckSubdomainAvailability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [reserve](#API_CheckSubdomainAvailability_RequestSyntax) **   <a name="Lightsail-CheckSubdomainAvailability-request-reserve"></a>
Specifies whether to reserve the subdomain for your account if it's available. A reservation holds the subdomain for 15 minutes so that other accounts can't create it. Checking the subdomain again doesn't extend the reservation.
For a nested subdomain, such as `blog.mysite`, the top-level subdomain (`mysite`) is reserved.
You can have up to 5 active reservations at a time.
Type: Boolean
Required: No

 ** [subdomainName](#API_CheckSubdomainAvailability_RequestSyntax) **   <a name="Lightsail-CheckSubdomainAvailability-request-subdomainName"></a>
The subdomain to check (for example, `mysite` or `blog.mysite`).
A subdomain can contain one or two labels separated by a period (`.`). Each label must start and end with a lowercase letter or a number, and can contain only lowercase letters, numbers, and hyphens (`-`). The name can be up to 39 characters long, including periods. Labels that start with `xn--` aren't supported, and some names are reserved.
Specify only the subdomain. A web address, such as `mysite.amazonlightsail.com`, isn't accepted.
Type: String
Required: Yes

## Response Syntax
<a name="API_CheckSubdomainAvailability_ResponseSyntax"></a>

```
{
   "available": boolean,
   "reservationExpiresAt": number,
   "subdomainName": "string"
}
```

## Response Elements
<a name="API_CheckSubdomainAvailability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [available](#API_CheckSubdomainAvailability_ResponseSyntax) **   <a name="Lightsail-CheckSubdomainAvailability-response-available"></a>
A Boolean value that indicates whether the subdomain is available to create.
Type: Boolean

 ** [reservationExpiresAt](#API_CheckSubdomainAvailability_ResponseSyntax) **   <a name="Lightsail-CheckSubdomainAvailability-response-reservationExpiresAt"></a>
The timestamp when the reservation of the subdomain expires.
The expiry is returned only when your account holds an active reservation for the subdomain.
Type: Timestamp

 ** [subdomainName](#API_CheckSubdomainAvailability_ResponseSyntax) **   <a name="Lightsail-CheckSubdomainAvailability-response-subdomainName"></a>
The subdomain that was checked.
Type: String

## Errors
<a name="API_CheckSubdomainAvailability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_CheckSubdomainAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CheckSubdomainAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CheckSubdomainAvailability)
