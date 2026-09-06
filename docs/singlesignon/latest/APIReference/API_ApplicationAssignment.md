---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationAssignment.html
---

# ApplicationAssignment
<a name="API_ApplicationAssignment"></a>

A structure that describes an assignment of a principal to an application.

## Contents
<a name="API_ApplicationAssignment_Contents"></a>

 ** ApplicationArn **   <a name="singlesignon-Type-ApplicationAssignment-ApplicationArn"></a>
The ARN of the application that has principals assigned.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** PrincipalId **   <a name="singlesignon-Type-ApplicationAssignment-PrincipalId"></a>
The unique identifier of the principal assigned to the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** PrincipalType **   <a name="singlesignon-Type-ApplicationAssignment-PrincipalType"></a>
The type of the principal assigned to the application.
Type: String
Valid Values: `USER | GROUP`
Required: Yes

## See Also
<a name="API_ApplicationAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ApplicationAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ApplicationAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ApplicationAssignment)
