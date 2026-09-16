---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseManagerReportGenerator.html
---

# UpdateLicenseManagerReportGenerator
<a name="API_UpdateLicenseManagerReportGenerator"></a>

Updates a report generator.

After you make changes to a report generator, it starts generating new reports within 60 minutes of being updated.

## Request Syntax
<a name="API_UpdateLicenseManagerReportGenerator_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "LicenseManagerReportGeneratorArn": "{{string}}",
   "ReportContext": {
      "licenseAssetGroupArns": [ "{{string}}" ],
      "licenseConfigurationArns": [ "{{string}}" ],
      "reportEndDate": {{number}},
      "reportStartDate": {{number}}
   },
   "ReportFrequency": {
      "period": "{{string}}",
      "value": {{number}}
   },
   "ReportGeneratorName": "{{string}}",
   "Type": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateLicenseManagerReportGenerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [Description](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-Description"></a>
Description of the report generator.
Type: String
Required: No

 ** [LicenseManagerReportGeneratorArn](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-LicenseManagerReportGeneratorArn"></a>
Amazon Resource Name (ARN) of the report generator to update.
Type: String
Required: Yes

 ** [ReportContext](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-ReportContext"></a>
The report context.
Type: [ReportContext](API_ReportContext.md) object
Required: Yes

 ** [ReportFrequency](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-ReportFrequency"></a>
Frequency by which reports are generated.
Type: [ReportFrequency](API_ReportFrequency.md) object
Required: Yes

 ** [ReportGeneratorName](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-ReportGeneratorName"></a>
Name of the report generator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Type](#API_UpdateLicenseManagerReportGenerator_RequestSyntax) **   <a name="licensemanager-UpdateLicenseManagerReportGenerator-request-Type"></a>
Type of reports to generate. The following report types are supported:
+ License configuration report - Reports the number and details of consumed licenses for a license configuration.
+ Resource report - Reports the tracked licenses and resource consumption for a license configuration.
Type: Array of strings
Valid Values: `LicenseConfigurationSummaryReport | LicenseConfigurationUsageReport | LicenseAssetGroupUsageReport`
Required: Yes

## Response Elements
<a name="API_UpdateLicenseManagerReportGenerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLicenseManagerReportGenerator_Errors"></a>

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

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
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
<a name="API_UpdateLicenseManagerReportGenerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UpdateLicenseManagerReportGenerator)
