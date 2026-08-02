---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_Permission.html
---

# Permission
<a name="API_Permission"></a>

Permissions designate which private CA actions can be performed by an AWS service or entity. In order for ACM to automatically renew private certificates, you must give the ACM service principal all available permissions (`IssueCertificate`, `GetCertificate`, and `ListPermissions`). Permissions can be assigned with the [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html) action, removed with the [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html) action, and listed with the [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html) action.

## Contents
<a name="API_Permission_Contents"></a>

 ** Actions **   <a name="privateca-Type-Permission-Actions"></a>
The private CA actions that can be performed by the designated AWS service.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `IssueCertificate | GetCertificate | ListPermissions`
Required: No

 ** CertificateAuthorityArn **   <a name="privateca-Type-Permission-CertificateAuthorityArn"></a>
The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: No

 ** CreatedAt **   <a name="privateca-Type-Permission-CreatedAt"></a>
The time at which the permission was created.
Type: Timestamp
Required: No

 ** Policy **   <a name="privateca-Type-Permission-Policy"></a>
The name of the policy that is associated with the permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 81920.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** Principal **   <a name="privateca-Type-Permission-Principal"></a>
The AWS service or entity that holds the permission. At this time, the only valid principal is `acm.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^*]+`
Required: No

 ** SourceAccount **   <a name="privateca-Type-Permission-SourceAccount"></a>
The ID of the account that assigned the permission.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_Permission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/Permission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/Permission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/Permission)
