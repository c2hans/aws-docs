---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Member.html
---

# Member
<a name="API_Member"></a>

Details on a member account in your organization.

## Contents
<a name="API_Member_Contents"></a>

 ** accountId **   <a name="inspector2-Type-Member-accountId"></a>
The AWS account ID of the member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** delegatedAdminAccountId **   <a name="inspector2-Type-Member-delegatedAdminAccountId"></a>
The AWS account ID of the Amazon Inspector delegated administrator for this member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** relationshipStatus **   <a name="inspector2-Type-Member-relationshipStatus"></a>
The status of the member account.
Type: String
Valid Values: `CREATED | INVITED | DISABLED | ENABLED | REMOVED | RESIGNED | DELETED | EMAIL_VERIFICATION_IN_PROGRESS | EMAIL_VERIFICATION_FAILED | REGION_DISABLED | ACCOUNT_SUSPENDED | CANNOT_CREATE_DETECTOR_IN_ORG_MASTER`
Required: No

 ** updatedAt **   <a name="inspector2-Type-Member-updatedAt"></a>
A timestamp showing when the status of this member was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Member)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
