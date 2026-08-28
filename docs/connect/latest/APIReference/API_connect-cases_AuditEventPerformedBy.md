---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_AuditEventPerformedBy.html
---

# AuditEventPerformedBy
<a name="API_connect-cases_AuditEventPerformedBy"></a>

Information of the user which performed the audit.

## Contents
<a name="API_connect-cases_AuditEventPerformedBy_Contents"></a>

 ** iamPrincipalArn **   <a name="connect-Type-connect-cases_AuditEventPerformedBy-iamPrincipalArn"></a>
Unique identifier of an IAM role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** user **   <a name="connect-Type-connect-cases_AuditEventPerformedBy-user"></a>
Represents the entity that performed the action.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_connect-cases_AuditEventPerformedBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/AuditEventPerformedBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/AuditEventPerformedBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/AuditEventPerformedBy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
