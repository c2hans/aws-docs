---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConversionTasks.html
---

# ListLicenseConversionTasks
<a name="API_ListLicenseConversionTasks"></a>

Lists the license type conversion tasks for your account.

## Request Syntax
<a name="API_ListLicenseConversionTasks_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLicenseConversionTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLicenseConversionTasks_RequestSyntax) **   <a name="licensemanager-ListLicenseConversionTasks-request-Filters"></a>
 Filters to scope the results. Valid filters are `ResourceArns` and `Status`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListLicenseConversionTasks_RequestSyntax) **   <a name="licensemanager-ListLicenseConversionTasks-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListLicenseConversionTasks_RequestSyntax) **   <a name="licensemanager-ListLicenseConversionTasks-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListLicenseConversionTasks_ResponseSyntax"></a>

```
{
   "LicenseConversionTasks": [
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLicenseConversionTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseConversionTasks](#API_ListLicenseConversionTasks_ResponseSyntax) **   <a name="licensemanager-ListLicenseConversionTasks-response-LicenseConversionTasks"></a>
Information about the license configuration tasks for your account.
Type: Array of [LicenseConversionTask](API_LicenseConversionTask.md) objects

 ** [NextToken](#API_ListLicenseConversionTasks_ResponseSyntax) **   <a name="licensemanager-ListLicenseConversionTasks-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListLicenseConversionTasks_Errors"></a>

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
<a name="API_ListLicenseConversionTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListLicenseConversionTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListLicenseConversionTasks)
