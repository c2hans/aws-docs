---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseConfiguration.html
---

# CreateLicenseConfiguration
<a name="API_CreateLicenseConfiguration"></a>

Creates a license configuration.

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), license affinity to host (how long a license must be associated with a host), and the number of licenses purchased and used.

## Request Syntax
<a name="API_CreateLicenseConfiguration_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DisassociateWhenNotFound": {{boolean}},
   "LicenseCount": {{number}},
   "LicenseCountHardLimit": {{boolean}},
   "LicenseCountingType": "{{string}}",
   "LicenseExpiry": {{number}},
   "LicenseRules": [ "{{string}}" ],
   "Name": "{{string}}",
   "ProductInformationList": [
      {
         "ProductInformationFilterList": [
            {
               "ProductInformationFilterComparator": "{{string}}",
               "ProductInformationFilterName": "{{string}}",
               "ProductInformationFilterValue": [ "{{string}}" ]
            }
         ],
         "ResourceType": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLicenseConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-Description"></a>
Description of the license configuration.
Type: String
Required: No

 ** [DisassociateWhenNotFound](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-DisassociateWhenNotFound"></a>
When true, disassociates a resource when software is uninstalled.
Type: Boolean
Required: No

 ** [LicenseCount](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-LicenseCount"></a>
Number of licenses managed by the license configuration.
Type: Long
Required: No

 ** [LicenseCountHardLimit](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-LicenseCountHardLimit"></a>
Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks the launch of new instances.
Type: Boolean
Required: No

 ** [LicenseCountingType](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-LicenseCountingType"></a>
Dimension used to track the license inventory.
Type: String
Valid Values: `vCPU | Instance | Core | Socket`
Required: Yes

 ** [LicenseExpiry](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-LicenseExpiry"></a>
License configuration expiry.
Type: Long
Required: No

 ** [LicenseRules](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-LicenseRules"></a>
License rules. The syntax is \#name=value (for example, \#allowedTenancy=EC2-DedicatedHost). The available rules vary by dimension, as follows.
+  `Cores` dimension: `allowedTenancy` \| `licenseAffinityToHost` \| `maximumCores` \| `minimumCores`
+  `Instances` dimension: `allowedTenancy` \| `maximumVcpus` \| `minimumVcpus`
+  `Sockets` dimension: `allowedTenancy` \| `licenseAffinityToHost` \| `maximumSockets` \| `minimumSockets`
+  `vCPUs` dimension: `allowedTenancy` \| `honorVcpuOptimization` \| `maximumVcpus` \| `minimumVcpus`
The unit for `licenseAffinityToHost` is days and the range is 1 to 180. The possible values for `allowedTenancy` are `EC2-Default`, `EC2-DedicatedHost`, and `EC2-DedicatedInstance`. The possible values for `honorVcpuOptimization` are `True` and `False`.
Type: Array of strings
Required: No

 ** [Name](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-Name"></a>
Name of the license configuration.
Type: String
Required: Yes

 ** [ProductInformationList](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-ProductInformationList"></a>
Product information.
Type: Array of [ProductInformation](API_ProductInformation.md) objects
Required: No

 ** [Tags](#API_CreateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-request-Tags"></a>
Tags to add to the license configuration.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateLicenseConfiguration_ResponseSyntax"></a>

```
{
   "LicenseConfigurationArn": "string"
}
```

## Response Elements
<a name="API_CreateLicenseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseConfigurationArn](#API_CreateLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-CreateLicenseConfiguration-response-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String

## Errors
<a name="API_CreateLicenseConfiguration_Errors"></a>

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

## See Also
<a name="API_CreateLicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicenseConfiguration)
