---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListFailuresForLicenseConfigurationOperations.html
---

# ListFailuresForLicenseConfigurationOperations
<a name="API_ListFailuresForLicenseConfigurationOperations"></a>

Lists the license configuration operations that failed.

## Request Syntax
<a name="API_ListFailuresForLicenseConfigurationOperations_RequestSyntax"></a>

```
{
   "LicenseConfigurationArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFailuresForLicenseConfigurationOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LicenseConfigurationArn](#API_ListFailuresForLicenseConfigurationOperations_RequestSyntax) **   <a name="licensemanager-ListFailuresForLicenseConfigurationOperations-request-LicenseConfigurationArn"></a>
Amazon Resource Name of the license configuration.
Type: String
Required: Yes

 ** [MaxResults](#API_ListFailuresForLicenseConfigurationOperations_RequestSyntax) **   <a name="licensemanager-ListFailuresForLicenseConfigurationOperations-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListFailuresForLicenseConfigurationOperations_RequestSyntax) **   <a name="licensemanager-ListFailuresForLicenseConfigurationOperations-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListFailuresForLicenseConfigurationOperations_ResponseSyntax"></a>

```
{
   "LicenseOperationFailureList": [
      {
         "ErrorMessage": "string",
         "FailureTime": number,
         "MetadataList": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "OperationName": "string",
         "OperationRequestedBy": "string",
         "ResourceArn": "string",
         "ResourceOwnerId": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFailuresForLicenseConfigurationOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseOperationFailureList](#API_ListFailuresForLicenseConfigurationOperations_ResponseSyntax) **   <a name="licensemanager-ListFailuresForLicenseConfigurationOperations-response-LicenseOperationFailureList"></a>
License configuration operations that failed.
Type: Array of [LicenseOperationFailure](API_LicenseOperationFailure.md) objects

 ** [NextToken](#API_ListFailuresForLicenseConfigurationOperations_ResponseSyntax) **   <a name="licensemanager-ListFailuresForLicenseConfigurationOperations-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListFailuresForLicenseConfigurationOperations_Errors"></a>

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
<a name="API_ListFailuresForLicenseConfigurationOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
