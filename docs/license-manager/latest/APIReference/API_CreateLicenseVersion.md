---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseVersion.html
---

# CreateLicenseVersion
<a name="API_CreateLicenseVersion"></a>

Creates a new version of the specified license.

## Request Syntax
<a name="API_CreateLicenseVersion_RequestSyntax"></a>

```
{
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
   "LicenseArn": "{{string}}",
   "LicenseMetadata": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "LicenseName": "{{string}}",
   "ProductName": "{{string}}",
   "SourceVersion": "{{string}}",
   "Status": "{{string}}",
   "Validity": {
      "Begin": "{{string}}",
      "End": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLicenseVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [ConsumptionConfiguration](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-ConsumptionConfiguration"></a>
Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.
Type: [ConsumptionConfiguration](API_ConsumptionConfiguration.md) object
Required: Yes

 ** [Entitlements](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-Entitlements"></a>
License entitlements.
Type: Array of [Entitlement](API_Entitlement.md) objects
Required: Yes

 ** [HomeRegion](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-HomeRegion"></a>
Home Region of the license.
Type: String
Required: Yes

 ** [Issuer](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-Issuer"></a>
License issuer.
Type: [Issuer](API_Issuer.md) object
Required: Yes

 ** [LicenseArn](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [LicenseMetadata](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-LicenseMetadata"></a>
Information about the license.
Type: Array of [Metadata](API_Metadata.md) objects
Required: No

 ** [LicenseName](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-LicenseName"></a>
License name.
Type: String
Required: Yes

 ** [ProductName](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-ProductName"></a>
Product name.
Type: String
Required: Yes

 ** [SourceVersion](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-SourceVersion"></a>
Current version of the license.
Type: String
Required: No

 ** [Status](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-Status"></a>
License status.
Type: String
Valid Values: `AVAILABLE | PENDING_AVAILABLE | DEACTIVATED | SUSPENDED | EXPIRED | PENDING_DELETE | DELETED`
Required: Yes

 ** [Validity](#API_CreateLicenseVersion_RequestSyntax) **   <a name="licensemanager-CreateLicenseVersion-request-Validity"></a>
Date and time range during which the license is valid, in ISO8601-UTC format.
Type: [DatetimeRange](API_DatetimeRange.md) object
Required: Yes

## Response Syntax
<a name="API_CreateLicenseVersion_ResponseSyntax"></a>

```
{
   "LicenseArn": "string",
   "Status": "string",
   "Version": "string"
}
```

## Response Elements
<a name="API_CreateLicenseVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseArn](#API_CreateLicenseVersion_ResponseSyntax) **   <a name="licensemanager-CreateLicenseVersion-response-LicenseArn"></a>
License ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Status](#API_CreateLicenseVersion_ResponseSyntax) **   <a name="licensemanager-CreateLicenseVersion-response-Status"></a>
License status.
Type: String
Valid Values: `AVAILABLE | PENDING_AVAILABLE | DEACTIVATED | SUSPENDED | EXPIRED | PENDING_DELETE | DELETED`

 ** [Version](#API_CreateLicenseVersion_ResponseSyntax) **   <a name="licensemanager-CreateLicenseVersion-response-Version"></a>
New version of the license.
Type: String

## Errors
<a name="API_CreateLicenseVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** ConflictException **
There was a conflict processing the request. Try your request again.
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

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateLicenseVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicenseVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicenseVersion)
