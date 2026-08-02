---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PermissionSet.html
---

# PermissionSet
<a name="API_PermissionSet"></a>

An entity that contains IAM policies.

## Contents
<a name="API_PermissionSet_Contents"></a>

 ** CreatedDate **   <a name="singlesignon-Type-PermissionSet-CreatedDate"></a>
The date that the permission set was created.
Type: Timestamp
Required: No

 ** Description **   <a name="singlesignon-Type-PermissionSet-Description"></a>
The description of the [PermissionSet](#API_PermissionSet).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 700.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** Name **   <a name="singlesignon-Type-PermissionSet-Name"></a>
The name of the permission set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\w+=,.@-]+`
Required: No

 ** PermissionSetArn **   <a name="singlesignon-Type-PermissionSet-PermissionSetArn"></a>
The ARN of the permission set. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: No

 ** RelayState **   <a name="singlesignon-Type-PermissionSet-RelayState"></a>
Used to redirect users within the application during the federation authentication process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.
Pattern: `[a-zA-Z0-9&$@#\\\/%?=~\-_'"|!:,.;*+\[\]\ \(\)\{\}]+`
Required: No

 ** SessionDuration **   <a name="singlesignon-Type-PermissionSet-SessionDuration"></a>
The length of time that the application user sessions are valid for in the ISO-8601 standard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(-?)P(?=\d|T\d)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)([DW]))?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?`
Required: No

## See Also
<a name="API_PermissionSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/PermissionSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/PermissionSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/PermissionSet)
