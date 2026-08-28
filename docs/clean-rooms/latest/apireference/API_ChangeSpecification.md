---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ChangeSpecification.html
---

# ChangeSpecification
<a name="API_ChangeSpecification"></a>

A union that contains the specification details for different types of changes.

## Contents
<a name="API_ChangeSpecification_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** collaboration **   <a name="API-Type-ChangeSpecification-collaboration"></a>
The collaboration configuration changes being requested. Currently, this only supports modifying which change types are auto-approved for the collaboration.
Type: [CollaborationChangeSpecification](API_CollaborationChangeSpecification.md) object
Required: No

 ** member **   <a name="API-Type-ChangeSpecification-member"></a>
The member change specification when the change type is `MEMBER`.
Type: [MemberChangeSpecification](API_MemberChangeSpecification.md) object
Required: No

## See Also
<a name="API_ChangeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ChangeSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ChangeSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ChangeSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
