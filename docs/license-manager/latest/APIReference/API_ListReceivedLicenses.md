---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListReceivedLicenses.html
---

# ListReceivedLicenses
<a name="API_ListReceivedLicenses"></a>

Lists received licenses.

## Request Syntax
<a name="API_ListReceivedLicenses_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "LicenseArns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReceivedLicenses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListReceivedLicenses_RequestSyntax) **   <a name="licensemanager-ListReceivedLicenses-request-Filters"></a>
Filters to scope the results. The following filters are supported:
+  `ProductSKU`
+  `Status`
+  `Fingerprint`
+  `IssuerName`
+  `Beneficiary`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [LicenseArns](#API_ListReceivedLicenses_RequestSyntax) **   <a name="licensemanager-ListReceivedLicenses-request-LicenseArns"></a>
Amazon Resource Names (ARNs) of the licenses.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** [MaxResults](#API_ListReceivedLicenses_RequestSyntax) **   <a name="licensemanager-ListReceivedLicenses-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListReceivedLicenses_RequestSyntax) **   <a name="licensemanager-ListReceivedLicenses-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListReceivedLicenses_ResponseSyntax"></a>

```
{
   "Licenses": [
      {
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
         "ReceivedMetadata": {
            "AllowedOperations": [ "string" ],
            "ReceivedStatus": "string",
            "ReceivedStatusReason": "string"
         },
         "Status": "string",
         "Validity": {
            "Begin": "string",
            "End": "string"
         },
         "Version": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListReceivedLicenses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Licenses](#API_ListReceivedLicenses_ResponseSyntax) **   <a name="licensemanager-ListReceivedLicenses-response-Licenses"></a>
Received license details.
Type: Array of [GrantedLicense](API_GrantedLicense.md) objects

 ** [NextToken](#API_ListReceivedLicenses_ResponseSyntax) **   <a name="licensemanager-ListReceivedLicenses-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListReceivedLicenses_Errors"></a>

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

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListReceivedLicenses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListReceivedLicenses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListReceivedLicenses)
