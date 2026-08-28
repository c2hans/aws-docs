---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_PrincipalPermissions.html
---

# PrincipalPermissions
<a name="API_PrincipalPermissions"></a>

Permissions granted to a principal.

## Contents
<a name="API_PrincipalPermissions_Contents"></a>

 ** Permissions **   <a name="lakeformation-Type-PrincipalPermissions-Permissions"></a>
The permissions that are granted to the principal.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** Principal **   <a name="lakeformation-Type-PrincipalPermissions-Principal"></a>
The principal who is granted permissions.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

## See Also
<a name="API_PrincipalPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/PrincipalPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/PrincipalPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/PrincipalPermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
