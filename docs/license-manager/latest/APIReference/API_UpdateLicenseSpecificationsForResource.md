---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseSpecificationsForResource.html
---

# UpdateLicenseSpecificationsForResource
<a name="API_UpdateLicenseSpecificationsForResource"></a>

Adds or removes the specified license configurations for the specified AWS resource.

You can update the license specifications of AMIs, instances, and hosts. You cannot update the license specifications for launch templates and CloudFormation templates, as they send license configurations to the operation that creates the resource.

## Request Syntax
<a name="API_UpdateLicenseSpecificationsForResource_RequestSyntax"></a>

```
{
   "AddLicenseSpecifications": [
      {
         "AmiAssociationScope": "{{string}}",
         "LicenseConfigurationArn": "{{string}}"
      }
   ],
   "RemoveLicenseSpecifications": [
      {
         "AmiAssociationScope": "{{string}}",
         "LicenseConfigurationArn": "{{string}}"
      }
   ],
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLicenseSpecificationsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddLicenseSpecifications](#API_UpdateLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-UpdateLicenseSpecificationsForResource-request-AddLicenseSpecifications"></a>
ARNs of the license configurations to add.
Type: Array of [LicenseSpecification](API_LicenseSpecification.md) objects
Required: No

 ** [RemoveLicenseSpecifications](#API_UpdateLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-UpdateLicenseSpecificationsForResource-request-RemoveLicenseSpecifications"></a>
ARNs of the license configurations to remove.
Type: Array of [LicenseSpecification](API_LicenseSpecification.md) objects
Required: No

 ** [ResourceArn](#API_UpdateLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-UpdateLicenseSpecificationsForResource-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the AWS resource.
Type: String
Required: Yes

## Response Elements
<a name="API_UpdateLicenseSpecificationsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLicenseSpecificationsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** ConflictException **
There was a conflict processing the request. Try your request again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** InvalidResourceStateException **
License Manager cannot allocate a license to a resource because of its state.
For example, you cannot allocate a license to an instance in the process of shutting down.
HTTP Status Code: 400

 ** LicenseUsageException **
You do not have enough licenses available to support a new resource launch.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_UpdateLicenseSpecificationsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource)
