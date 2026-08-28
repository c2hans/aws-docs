---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseConversionTask.html
---

# GetLicenseConversionTask
<a name="API_GetLicenseConversionTask"></a>

Gets information about the specified license type conversion task.

## Request Syntax
<a name="API_GetLicenseConversionTask_RequestSyntax"></a>

```
{
   "LicenseConversionTaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLicenseConversionTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LicenseConversionTaskId](#API_GetLicenseConversionTask_RequestSyntax) **   <a name="licensemanager-GetLicenseConversionTask-request-LicenseConversionTaskId"></a>
ID of the license type conversion task to retrieve information on.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^lct-[a-zA-Z0-9]*`
Required: Yes

## Response Syntax
<a name="API_GetLicenseConversionTask_ResponseSyntax"></a>

```
{
   "DestinationLicenseContext": {
      "ProductCodes": [
         {
            "ProductCodeId": "string",
            "ProductCodeType": "string"
         }
      ],
      "UsageOperation": "string"
   },
   "EndTime": number,
   "LicenseConversionTaskId": "string",
   "LicenseConversionTime": number,
   "ResourceArn": "string",
   "SourceLicenseContext": {
      "ProductCodes": [
         {
            "ProductCodeId": "string",
            "ProductCodeType": "string"
         }
      ],
      "UsageOperation": "string"
   },
   "StartTime": number,
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_GetLicenseConversionTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationLicenseContext](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-DestinationLicenseContext"></a>
Information about the license type converted to.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object

 ** [EndTime](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-EndTime"></a>
Time at which the license type conversion task was completed.
Type: Timestamp

 ** [LicenseConversionTaskId](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-LicenseConversionTaskId"></a>
ID of the license type conversion task.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^lct-[a-zA-Z0-9]*`

 ** [LicenseConversionTime](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-LicenseConversionTime"></a>
Amount of time to complete the license type conversion.
Type: Timestamp

 ** [ResourceArn](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-ResourceArn"></a>
Amazon Resource Names (ARN) of the resources the license conversion task is associated with.
Type: String

 ** [SourceLicenseContext](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-SourceLicenseContext"></a>
Information about the license type converted from.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object

 ** [StartTime](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-StartTime"></a>
Time at which the license type conversion task was started .
Type: Timestamp

 ** [Status](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-Status"></a>
Status of the license type conversion task.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

 ** [StatusMessage](#API_GetLicenseConversionTask_ResponseSyntax) **   <a name="licensemanager-GetLicenseConversionTask-response-StatusMessage"></a>
The status message for the conversion task.
Type: String

## Errors
<a name="API_GetLicenseConversionTask_Errors"></a>

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

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_GetLicenseConversionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/GetLicenseConversionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/GetLicenseConversionTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
