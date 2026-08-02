---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseOperationFailure.html
---

# LicenseOperationFailure
<a name="API_LicenseOperationFailure"></a>

Describes the failure of a license operation.

## Contents
<a name="API_LicenseOperationFailure_Contents"></a>

 ** ErrorMessage **   <a name="licensemanager-Type-LicenseOperationFailure-ErrorMessage"></a>
Error message.
Type: String
Required: No

 ** FailureTime **   <a name="licensemanager-Type-LicenseOperationFailure-FailureTime"></a>
Failure time.
Type: Timestamp
Required: No

 ** MetadataList **   <a name="licensemanager-Type-LicenseOperationFailure-MetadataList"></a>
Reserved.
Type: Array of [Metadata](API_Metadata.md) objects
Required: No

 ** OperationName **   <a name="licensemanager-Type-LicenseOperationFailure-OperationName"></a>
Name of the operation.
Type: String
Required: No

 ** OperationRequestedBy **   <a name="licensemanager-Type-LicenseOperationFailure-OperationRequestedBy"></a>
The requester is "License Manager Automated Discovery".
Type: String
Required: No

 ** ResourceArn **   <a name="licensemanager-Type-LicenseOperationFailure-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** ResourceOwnerId **   <a name="licensemanager-Type-LicenseOperationFailure-ResourceOwnerId"></a>
ID of the AWS account that owns the resource.
Type: String
Required: No

 ** ResourceType **   <a name="licensemanager-Type-LicenseOperationFailure-ResourceType"></a>
Resource type.
Type: String
Valid Values: `EC2_INSTANCE | EC2_HOST | EC2_AMI | RDS | SYSTEMS_MANAGER_MANAGED_INSTANCE`
Required: No

## See Also
<a name="API_LicenseOperationFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseOperationFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseOperationFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseOperationFailure)
