---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseManagerReportGenerators.html
---

# ListLicenseManagerReportGenerators
<a name="API_ListLicenseManagerReportGenerators"></a>

Lists the report generators for your account.

## Request Syntax
<a name="API_ListLicenseManagerReportGenerators_RequestSyntax"></a>

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
<a name="API_ListLicenseManagerReportGenerators_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLicenseManagerReportGenerators_RequestSyntax) **   <a name="licensemanager-ListLicenseManagerReportGenerators-request-Filters"></a>
Filters to scope the results. The following filters are supported:
+  `LicenseConfigurationArn`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListLicenseManagerReportGenerators_RequestSyntax) **   <a name="licensemanager-ListLicenseManagerReportGenerators-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListLicenseManagerReportGenerators_RequestSyntax) **   <a name="licensemanager-ListLicenseManagerReportGenerators-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListLicenseManagerReportGenerators_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ReportGenerators": [
      {
         "CreateTime": "string",
         "Description": "string",
         "LastReportGenerationTime": "string",
         "LastRunFailureReason": "string",
         "LastRunStatus": "string",
         "LicenseManagerReportGeneratorArn": "string",
         "ReportContext": {
            "licenseAssetGroupArns": [ "string" ],
            "licenseConfigurationArns": [ "string" ],
            "reportEndDate": number,
            "reportStartDate": number
         },
         "ReportCreatorAccount": "string",
         "ReportFrequency": {
            "period": "string",
            "value": number
         },
         "ReportGeneratorName": "string",
         "ReportType": [ "string" ],
         "S3Location": {
            "bucket": "string",
            "keyPrefix": "string"
         },
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListLicenseManagerReportGenerators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListLicenseManagerReportGenerators_ResponseSyntax) **   <a name="licensemanager-ListLicenseManagerReportGenerators-response-NextToken"></a>
Token for the next set of results.
Type: String

 ** [ReportGenerators](#API_ListLicenseManagerReportGenerators_ResponseSyntax) **   <a name="licensemanager-ListLicenseManagerReportGenerators-response-ReportGenerators"></a>
A report generator that creates periodic reports about your license configurations.
Type: Array of [ReportGenerator](API_ReportGenerator.md) objects

## Errors
<a name="API_ListLicenseManagerReportGenerators_Errors"></a>

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
<a name="API_ListLicenseManagerReportGenerators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListLicenseManagerReportGenerators)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListLicenseManagerReportGenerators)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
