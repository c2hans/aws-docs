---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ExtendLicenseConsumption.html
---

# ExtendLicenseConsumption
<a name="API_ExtendLicenseConsumption"></a>

Extends the expiration date for license consumption.

## Request Syntax
<a name="API_ExtendLicenseConsumption_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "LicenseConsumptionToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ExtendLicenseConsumption_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DryRun](#API_ExtendLicenseConsumption_RequestSyntax) **   <a name="licensemanager-ExtendLicenseConsumption-request-DryRun"></a>
Checks whether you have the required permissions for the action, without actually making the request. Provides an error response if you do not have the required permissions.
Type: Boolean
Required: No

 ** [LicenseConsumptionToken](#API_ExtendLicenseConsumption_RequestSyntax) **   <a name="licensemanager-ExtendLicenseConsumption-request-LicenseConsumptionToken"></a>
License consumption token.
Type: String
Required: Yes

## Response Syntax
<a name="API_ExtendLicenseConsumption_ResponseSyntax"></a>

```
{
   "Expiration": "string",
   "LicenseConsumptionToken": "string"
}
```

## Response Elements
<a name="API_ExtendLicenseConsumption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Expiration](#API_ExtendLicenseConsumption_ResponseSyntax) **   <a name="licensemanager-ExtendLicenseConsumption-response-Expiration"></a>
Date and time at which the license consumption expires.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`

 ** [LicenseConsumptionToken](#API_ExtendLicenseConsumption_ResponseSyntax) **   <a name="licensemanager-ExtendLicenseConsumption-response-LicenseConsumptionToken"></a>
License consumption token.
Type: String

## Errors
<a name="API_ExtendLicenseConsumption_Errors"></a>

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

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource cannot be found.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ExtendLicenseConsumption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ExtendLicenseConsumption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ExtendLicenseConsumption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
