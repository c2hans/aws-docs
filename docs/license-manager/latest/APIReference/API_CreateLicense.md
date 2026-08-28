---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicense.html
---

# CreateLicense
<a name="API_CreateLicense"></a>

Creates a license.

## Request Syntax
<a name="API_CreateLicense_RequestSyntax"></a>

```
{
   "Beneficiary": "{{string}}",
   "ClientToken": "{{string}}",
   "ConsumptionConfiguration": {
      "BorrowConfiguration": {
         "AllowEarlyCheckIn": {{boolean}},
         "MaxTimeToLiveInMinutes": {{number}}
      },
      "ProvisionalConfiguration": {
         "MaxTimeToLiveInMinutes": {{number}}
      },
      "RenewType": "{{string}}"
   },
   "Entitlements": [
      {
         "AllowCheckIn": {{boolean}},
         "MaxCount": {{number}},
         "Name": "{{string}}",
         "Overage": {{boolean}},
         "Unit": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "HomeRegion": "{{string}}",
   "Issuer": {
      "Name": "{{string}}",
      "SignKey": "{{string}}"
   },
   "LicenseMetadata": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "LicenseName": "{{string}}",
   "ProductName": "{{string}}",
   "ProductSKU": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Validity": {
      "Begin": "{{string}}",
      "End": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLicense_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Beneficiary](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-Beneficiary"></a>
License beneficiary.
Type: String
Required: Yes

 ** [ClientToken](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [ConsumptionConfiguration](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-ConsumptionConfiguration"></a>
Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.
Type: [ConsumptionConfiguration](API_ConsumptionConfiguration.md) object
Required: Yes

 ** [Entitlements](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-Entitlements"></a>
License entitlements.
Type: Array of [Entitlement](API_Entitlement.md) objects
Required: Yes

 ** [HomeRegion](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-HomeRegion"></a>
Home Region for the license.
Type: String
Required: Yes

 ** [Issuer](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-Issuer"></a>
License issuer.
Type: [Issuer](API_Issuer.md) object
Required: Yes

 ** [LicenseMetadata](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-LicenseMetadata"></a>
Information about the license.
Type: Array of [Metadata](API_Metadata.md) objects
Required: No

 ** [LicenseName](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-LicenseName"></a>
License name.
Type: String
Required: Yes

 ** [ProductName](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-ProductName"></a>
Product name.
Type: String
Required: Yes

 ** [ProductSKU](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-ProductSKU"></a>
Product SKU.
Type: String
Required: Yes

 ** [Tags](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-Tags"></a>
Tags to add to the license. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Validity](#API_CreateLicense_RequestSyntax) **   <a name="licensemanager-CreateLicense-request-Validity"></a>
Date and time range during which the license is valid, in ISO8601-UTC format.
Type: [DatetimeRange](API_DatetimeRange.md) object
Required: Yes

## Response Syntax
<a name="API_CreateLicense_ResponseSyntax"></a>

```
{
   "LicenseArn": "string",
   "Status": "string",
   "Version": "string"
}
```

## Response Elements
<a name="API_CreateLicense_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseArn](#API_CreateLicense_ResponseSyntax) **   <a name="licensemanager-CreateLicense-response-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Status](#API_CreateLicense_ResponseSyntax) **   <a name="licensemanager-CreateLicense-response-Status"></a>
License status.
Type: String
Valid Values: `AVAILABLE | PENDING_AVAILABLE | DEACTIVATED | SUSPENDED | EXPIRED | PENDING_DELETE | DELETED`

 ** [Version](#API_CreateLicense_ResponseSyntax) **   <a name="licensemanager-CreateLicense-response-Version"></a>
License version.
Type: String

## Errors
<a name="API_CreateLicense_Errors"></a>

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

 ** RedirectException **
This is not the correct Region for the resource. Try again.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateLicense_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicense)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicense)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
