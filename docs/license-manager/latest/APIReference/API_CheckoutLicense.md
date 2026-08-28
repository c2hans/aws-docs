---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CheckoutLicense.html
---

# CheckoutLicense
<a name="API_CheckoutLicense"></a>

Checks out the specified license.

**Note**
If the account that created the license is the same that is performing the check out, you must specify the account as the beneficiary.

## Request Syntax
<a name="API_CheckoutLicense_RequestSyntax"></a>

```
{
   "Beneficiary": "{{string}}",
   "CheckoutType": "{{string}}",
   "ClientToken": "{{string}}",
   "Entitlements": [
      {
         "Name": "{{string}}",
         "Unit": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "KeyFingerprint": "{{string}}",
   "NodeId": "{{string}}",
   "ProductSKU": "{{string}}"
}
```

## Request Parameters
<a name="API_CheckoutLicense_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Beneficiary](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-Beneficiary"></a>
License beneficiary.
Type: String
Required: No

 ** [CheckoutType](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-CheckoutType"></a>
Checkout type.
Type: String
Valid Values: `PROVISIONAL | PERPETUAL`
Required: Yes

 ** [ClientToken](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [Entitlements](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-Entitlements"></a>
License entitlements.
Type: Array of [EntitlementData](API_EntitlementData.md) objects
Required: Yes

 ** [KeyFingerprint](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-KeyFingerprint"></a>
Key fingerprint identifying the license.
Type: String
Required: Yes

 ** [NodeId](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-NodeId"></a>
Node ID.
Type: String
Required: No

 ** [ProductSKU](#API_CheckoutLicense_RequestSyntax) **   <a name="licensemanager-CheckoutLicense-request-ProductSKU"></a>
Product SKU.
Type: String
Required: Yes

## Response Syntax
<a name="API_CheckoutLicense_ResponseSyntax"></a>

```
{
   "CheckoutType": "string",
   "EntitlementsAllowed": [
      {
         "Name": "string",
         "Unit": "string",
         "Value": "string"
      }
   ],
   "Expiration": "string",
   "IssuedAt": "string",
   "LicenseArn": "string",
   "LicenseConsumptionToken": "string",
   "NodeId": "string",
   "SignedToken": "string"
}
```

## Response Elements
<a name="API_CheckoutLicense_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CheckoutType](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-CheckoutType"></a>
Checkout type.
Type: String
Valid Values: `PROVISIONAL | PERPETUAL`

 ** [EntitlementsAllowed](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-EntitlementsAllowed"></a>
Allowed license entitlements.
Type: Array of [EntitlementData](API_EntitlementData.md) objects

 ** [Expiration](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-Expiration"></a>
Date and time at which the license checkout expires.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`

 ** [IssuedAt](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-IssuedAt"></a>
Date and time at which the license checkout is issued.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`

 ** [LicenseArn](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-LicenseArn"></a>
Amazon Resource Name (ARN) of the checkout license.
Type: String

 ** [LicenseConsumptionToken](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-LicenseConsumptionToken"></a>
License consumption token.
Type: String

 ** [NodeId](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-NodeId"></a>
Node ID.
Type: String

 ** [SignedToken](#API_CheckoutLicense_ResponseSyntax) **   <a name="licensemanager-CheckoutLicense-response-SignedToken"></a>
Signed token.
Type: String
Length Constraints: Minimum length of 4096.

## Errors
<a name="API_CheckoutLicense_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** NoEntitlementsAllowedException **
There are no entitlements found for this license, or the entitlement maximum count is reached.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** RedirectException **
This is not the correct Region for the resource. Try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource cannot be found.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** UnsupportedDigitalSignatureMethodException **
The digital signature method is unsupported. Try your request again.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CheckoutLicense_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CheckoutLicense)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CheckoutLicense)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
