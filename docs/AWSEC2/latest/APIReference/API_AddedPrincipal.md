---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AddedPrincipal.html
---

# AddedPrincipal
<a name="API_AddedPrincipal"></a>

Describes a principal.

## Contents
<a name="API_AddedPrincipal_Contents"></a>

 ** principal **
The Amazon Resource Name (ARN) of the principal.
Type: String
Required: No

 ** principalType **
The type of principal.
Type: String
Valid Values: `All | Service | OrganizationUnit | Account | User | Role`
Required: No

 ** serviceId **
The ID of the service.
Type: String
Required: No

 ** servicePermissionId **
The ID of the service permission.
Type: String
Required: No

## See Also
<a name="API_AddedPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AddedPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AddedPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AddedPrincipal)
