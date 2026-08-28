---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_TransferParticipant.html
---

# TransferParticipant
<a name="API_TransferParticipant"></a>

Contains details for a participant in a transfer. A *transfer* is the arrangement between two management accounts where one account designates the other with specified responsibilities for their organization.

## Contents
<a name="API_TransferParticipant_Contents"></a>

 ** ManagementAccountEmail **   <a name="organizations-Type-TransferParticipant-ManagementAccountEmail"></a>
Email address for the management account.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: No

 ** ManagementAccountId **   <a name="organizations-Type-TransferParticipant-ManagementAccountId"></a>
ID for the management account.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_TransferParticipant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/TransferParticipant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/TransferParticipant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/TransferParticipant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
