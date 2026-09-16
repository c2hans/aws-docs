---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConfigurationsForOrganization.html
---

# ListLicenseConfigurationsForOrganization
<a name="API_ListLicenseConfigurationsForOrganization"></a>

Lists license configurations for an organization.

## Request Syntax
<a name="API_ListLicenseConfigurationsForOrganization_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "LicenseConfigurationArns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLicenseConfigurationsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListLicenseConfigurationsForOrganization_RequestSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-request-Filters"></a>
Filters to scope the results.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [LicenseConfigurationArns](#API_ListLicenseConfigurationsForOrganization_RequestSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-request-LicenseConfigurationArns"></a>
License configuration ARNs.
Type: Array of strings
Required: No

 ** [MaxResults](#API_ListLicenseConfigurationsForOrganization_RequestSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListLicenseConfigurationsForOrganization_RequestSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListLicenseConfigurationsForOrganization_ResponseSyntax"></a>

```
{
   "LicenseConfigurations": [
      {
         "AutomatedDiscoveryInformation": {
            "LastRunTime": number
         },
         "ConsumedLicenses": number,
         "ConsumedLicenseSummaryList": [
            {
               "ConsumedLicenses": number,
               "ResourceType": "string"
            }
         ],
         "Description": "string",
         "DisassociateWhenNotFound": boolean,
         "LicenseConfigurationArn": "string",
         "LicenseConfigurationId": "string",
         "LicenseCount": number,
         "LicenseCountHardLimit": boolean,
         "LicenseCountingType": "string",
         "LicenseExpiry": number,
         "LicenseRules": [ "string" ],
         "ManagedResourceSummaryList": [
            {
               "AssociationCount": number,
               "ResourceType": "string"
            }
         ],
         "Name": "string",
         "OwnerAccountId": "string",
         "ProductInformationList": [
            {
               "ProductInformationFilterList": [
                  {
                     "ProductInformationFilterComparator": "string",
                     "ProductInformationFilterName": "string",
                     "ProductInformationFilterValue": [ "string" ]
                  }
               ],
               "ResourceType": "string"
            }
         ],
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLicenseConfigurationsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseConfigurations](#API_ListLicenseConfigurationsForOrganization_ResponseSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-response-LicenseConfigurations"></a>
License configurations.
Type: Array of [LicenseConfiguration](API_LicenseConfiguration.md) objects

 ** [NextToken](#API_ListLicenseConfigurationsForOrganization_ResponseSyntax) **   <a name="licensemanager-ListLicenseConfigurationsForOrganization-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListLicenseConfigurationsForOrganization_Errors"></a>

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
<a name="API_ListLicenseConfigurationsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListLicenseConfigurationsForOrganization)
