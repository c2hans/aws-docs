---
source_url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_RoleMapping.html
---

# RoleMapping
<a name="API_RoleMapping"></a>

A role mapping.

## Contents
<a name="API_RoleMapping_Contents"></a>

 ** Type **   <a name="CognitoIdentity-Type-RoleMapping-Type"></a>
The role mapping type. Token will use `cognito:roles` and `cognito:preferred_role` claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.
Type: String
Valid Values: `Token | Rules`
Required: Yes

 ** AmbiguousRoleResolution **   <a name="CognitoIdentity-Type-RoleMapping-AmbiguousRoleResolution"></a>
If you specify Token or Rules as the `Type`, `AmbiguousRoleResolution` is required.
Specifies the action to be taken if either no rules match the claim value for the `Rules` type, or there is no `cognito:preferred_role` claim and there are multiple `cognito:roles` matches for the `Token` type.
Type: String
Valid Values: `AuthenticatedRole | Deny`
Required: No

 ** RulesConfiguration **   <a name="CognitoIdentity-Type-RoleMapping-RulesConfiguration"></a>
The rules to be used for mapping users to roles.
If you specify Rules as the role mapping type, `RulesConfiguration` is required.
Type: [RulesConfigurationType](API_RulesConfigurationType.md) object
Required: No

## See Also
<a name="API_RoleMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/RoleMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/RoleMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/RoleMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitoidentity` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
