---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_MembershipSummary.html
---

# MembershipSummary
<a name="API_MembershipSummary"></a>

Contains summary information about a membership.

## Contents
<a name="API_MembershipSummary_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-MembershipSummary-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** applicationId **   <a name="securityagent-Type-MembershipSummary-applicationId"></a>
The unique identifier of the application.
Type: String
Required: Yes

 ** createdAt **   <a name="securityagent-Type-MembershipSummary-createdAt"></a>
The date and time the membership was created, in UTC format.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="securityagent-Type-MembershipSummary-createdBy"></a>
The identifier of the entity that created the membership.
Type: String
Required: Yes

 ** membershipId **   <a name="securityagent-Type-MembershipSummary-membershipId"></a>
The unique identifier of the membership.
Type: String
Required: Yes

 ** memberType **   <a name="securityagent-Type-MembershipSummary-memberType"></a>
The type of member.
Type: String
Valid Values: `USER`
Required: Yes

 ** updatedAt **   <a name="securityagent-Type-MembershipSummary-updatedAt"></a>
The date and time the membership was last updated, in UTC format.
Type: Timestamp
Required: Yes

 ** updatedBy **   <a name="securityagent-Type-MembershipSummary-updatedBy"></a>
The identifier of the entity that last updated the membership.
Type: String
Required: Yes

 ** config **   <a name="securityagent-Type-MembershipSummary-config"></a>
The configuration for the membership.
Type: [MembershipConfig](API_MembershipConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** metadata **   <a name="securityagent-Type-MembershipSummary-metadata"></a>
The metadata for the member.
Type: [MemberMetadata](API_MemberMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_MembershipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/MembershipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/MembershipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/MembershipSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
