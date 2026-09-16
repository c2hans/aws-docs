---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.html
---

# ListUsageForLicenseConfiguration
<a name="API_ListUsageForLicenseConfiguration"></a>

Lists all license usage records for a license configuration, displaying license consumption details by resource at a selected point in time. Use this action to audit the current license consumption for any license inventory and configuration.

## Request Syntax
<a name="API_ListUsageForLicenseConfiguration_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "LicenseConfigurationArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsageForLicenseConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListUsageForLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-request-Filters"></a>
Filters to scope the results. The following filters and logical operators are supported:
+  `resourceArn` - The ARN of the license configuration resource.
+  `resourceType` - The resource type (`EC2_INSTANCE` \| `EC2_HOST` \| `EC2_AMI` \| `SYSTEMS_MANAGER_MANAGED_INSTANCE`).
+  `resourceAccount` - The ID of the account that owns the resource.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [LicenseConfigurationArn](#API_ListUsageForLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-request-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String
Required: Yes

 ** [MaxResults](#API_ListUsageForLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListUsageForLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListUsageForLicenseConfiguration_ResponseSyntax"></a>

```
{
   "LicenseConfigurationUsageList": [
      {
         "AssociationTime": number,
         "ConsumedLicenses": number,
         "ResourceArn": "string",
         "ResourceOwnerId": "string",
         "ResourceStatus": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListUsageForLicenseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseConfigurationUsageList](#API_ListUsageForLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-response-LicenseConfigurationUsageList"></a>
Information about the license configurations.
Type: Array of [LicenseConfigurationUsage](API_LicenseConfigurationUsage.md) objects

 ** [NextToken](#API_ListUsageForLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-ListUsageForLicenseConfiguration-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListUsageForLicenseConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** FilterLimitExceededException **
The request uses too many filters or too many filter values.
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
<a name="API_ListUsageForLicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListUsageForLicenseConfiguration)
