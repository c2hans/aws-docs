---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryScanningConfiguration.html
---

# PutRegistryScanningConfiguration
<a name="API_PutRegistryScanningConfiguration"></a>

Creates or updates the scanning configuration for your private registry.

## Request Syntax
<a name="API_PutRegistryScanningConfiguration_RequestSyntax"></a>

```
{
   "rules": [
      {
         "repositoryFilters": [
            {
               "filter": "{{string}}",
               "filterType": "{{string}}"
            }
         ],
         "scanFrequency": "{{string}}"
      }
   ],
   "scanType": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRegistryScanningConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [rules](#API_PutRegistryScanningConfiguration_RequestSyntax) **   <a name="ECR-PutRegistryScanningConfiguration-request-rules"></a>
The scanning rules to use for the registry. A scanning rule is used to determine which repository filters are used and at what frequency scanning will occur.
Type: Array of [RegistryScanningRule](API_RegistryScanningRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** [scanType](#API_PutRegistryScanningConfiguration_RequestSyntax) **   <a name="ECR-PutRegistryScanningConfiguration-request-scanType"></a>
The scanning type to set for the registry.
When a registry scanning configuration is not defined, by default the `BASIC` scan type is used. When basic scanning is used, you may specify filters to determine which individual repositories, or all repositories, are scanned when new images are pushed to those repositories. Alternatively, you can do manual scans of images with basic scanning.
When the `ENHANCED` scan type is set, Amazon Inspector provides automated vulnerability scanning. You may choose between continuous scanning or scan on push and you may specify filters to determine which individual repositories, or all repositories, are scanned.
Type: String
Valid Values: `BASIC | ENHANCED`
Required: No

## Response Syntax
<a name="API_PutRegistryScanningConfiguration_ResponseSyntax"></a>

```
{
   "registryScanningConfiguration": {
      "rules": [
         {
            "repositoryFilters": [
               {
                  "filter": "string",
                  "filterType": "string"
               }
            ],
            "scanFrequency": "string"
         }
      ],
      "scanType": "string"
   }
}
```

## Response Elements
<a name="API_PutRegistryScanningConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryScanningConfiguration](#API_PutRegistryScanningConfiguration_ResponseSyntax) **   <a name="ECR-PutRegistryScanningConfiguration-response-registryScanningConfiguration"></a>
The scanning configuration for your registry.
Type: [RegistryScanningConfiguration](API_RegistryScanningConfiguration.md) object

## Errors
<a name="API_PutRegistryScanningConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlockedByOrganizationPolicyException **
The operation did not succeed because the account is managed by a organization policy.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_PutRegistryScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutRegistryScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PutRegistryScanningConfiguration)
