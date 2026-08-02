---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAssociatedEnclaveCertificateIamRoles.html
---

# GetAssociatedEnclaveCertificateIamRoles
<a name="API_GetAssociatedEnclaveCertificateIamRoles"></a>

Returns the IAM roles that are associated with the specified ACM (ACM) certificate. It also returns the name of the Amazon S3 bucket and the Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored, and the ARN of the KMS key that's used to encrypt the private key.

## Request Parameters
<a name="API_GetAssociatedEnclaveCertificateIamRoles_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CertificateArn**
The ARN of the ACM certificate for which to view the associated IAM roles, encryption keys, and Amazon S3 object information.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetAssociatedEnclaveCertificateIamRoles_ResponseElements"></a>

The following elements are returned by the service.

 **associatedRoleSet**
Information about the associated IAM roles.
Type: Array of [AssociatedRole](API_AssociatedRole.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetAssociatedEnclaveCertificateIamRoles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetAssociatedEnclaveCertificateIamRoles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetAssociatedEnclaveCertificateIamRoles)
