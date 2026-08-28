---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ProjectMembershipAssignment.html
---

# ProjectMembershipAssignment
<a name="API_ProjectMembershipAssignment"></a>

A map of user or group profiles to designations that need to be assigned in the project.

## Contents
<a name="API_ProjectMembershipAssignment_Contents"></a>

 ** designation **   <a name="datazone-Type-ProjectMembershipAssignment-designation"></a>
The designation of the project membership.
Type: String
Valid Values: `PROJECT_OWNER | PROJECT_CONTRIBUTOR | PROJECT_CATALOG_VIEWER | PROJECT_CATALOG_CONSUMER | PROJECT_CATALOG_STEWARD`
Required: Yes

 ** member **   <a name="datazone-Type-ProjectMembershipAssignment-member"></a>
The details about a project member.
Type: [Member](API_Member.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ProjectMembershipAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ProjectMembershipAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ProjectMembershipAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ProjectMembershipAssignment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
