---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicense.html
---

# GetLicense
<a name="API_GetLicense"></a>

Gets detailed information about the specified license.

## Request Syntax
<a name="API_GetLicense_RequestSyntax"></a>

```
{
   "LicenseArn": "{{string}}",
   "Version": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLicense_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LicenseArn](#API_GetLicense_RequestSyntax) **   <a name="licensemanager-GetLicense-request-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [Version](#API_GetLicense_RequestSyntax) **   <a name="licensemanager-GetLicense-request-Version"></a>
License version.
Type: String
Required: No

## Response Syntax
<a name="API_GetLicense_ResponseSyntax"></a>

```
{
   "License": {
      "Beneficiary": "string",
      "ConsumptionConfiguration": {
         "BorrowConfiguration": {
            "AllowEarlyCheckIn": boolean,
            "MaxTimeToLiveInMinutes": number
         },
         "ProvisionalConfiguration": {
            "MaxTimeToLiveInMinutes": number
         },
         "RenewType": "string"
      },
      "CreateTime": "string",
      "Entitlements": [
         {
            "AllowCheckIn": boolean,
            "MaxCount": number,
            "Name": "string",
            "Overage": boolean,
            "Unit": "string",
            "Value": "string"
         }
      ],
      "HomeRegion": "string",
      "Issuer": {
         "KeyFingerprint": "string",
         "Name": "string",
         "SignKey": "string"
      },
      "LicenseArn": "string",
      "LicenseMetadata": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "LicenseName": "string",
      "ProductName": "string",
      "ProductSKU": "string",
      "Status": "string",
      "Validity": {
         "Begin": "string",
         "End": "string"
      },
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_GetLicense_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [License](#API_GetLicense_ResponseSyntax) **   <a name="licensemanager-GetLicense-response-License"></a>
License details.
Type: [License](API_License.md) object

## Errors
<a name="API_GetLicense_Errors"></a>

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

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_GetLicense_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/GetLicense)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/GetLicense)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
