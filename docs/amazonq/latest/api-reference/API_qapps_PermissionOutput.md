---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PermissionOutput.html
---

# PermissionOutput
<a name="API_qapps_PermissionOutput"></a>

The permission granted to the Amazon Q App.

## Contents
<a name="API_qapps_PermissionOutput_Contents"></a>

 ** action **   <a name="qbusiness-Type-qapps_PermissionOutput-action"></a>
The action associated with the permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `read | write`
Required: Yes

 ** principal **   <a name="qbusiness-Type-qapps_PermissionOutput-principal"></a>
The principal user to which the permission applies.
Type: [PrincipalOutput](API_qapps_PrincipalOutput.md) object
Required: Yes

## See Also
<a name="API_qapps_PermissionOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/PermissionOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/PermissionOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/PermissionOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
