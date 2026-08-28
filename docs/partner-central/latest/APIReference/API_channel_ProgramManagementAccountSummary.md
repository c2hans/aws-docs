---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ProgramManagementAccountSummary.html
---

# ProgramManagementAccountSummary
<a name="API_channel_ProgramManagementAccountSummary"></a>

Summary information about a program management account.

## Contents
<a name="API_channel_ProgramManagementAccountSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accountId **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-accountId"></a>
The AWS account ID associated with the program management account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

 ** arn **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-arn"></a>
The Amazon Resource Name (ARN) of the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** catalog **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-catalog"></a>
The catalog identifier associated with the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: No

 ** createdAt **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-createdAt"></a>
The timestamp when the account was created.
Type: Timestamp
Required: No

 ** displayName **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-displayName"></a>
The display name of the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-id"></a>
The unique identifier of the program management account.
Type: String
Length Constraints: Fixed length of 17.
Pattern: `pma-[a-z0-9]{13}`
Required: No

 ** program **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-program"></a>
The program type for the management account.
Type: String
Valid Values: `SOLUTION_PROVIDER | DISTRIBUTION | DISTRIBUTION_SELLER`
Required: No

 ** revision **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-revision"></a>
The current revision number of the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

 ** startDate **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-startDate"></a>
The start date of the program management account.
Type: Timestamp
Required: No

 ** status **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-status"></a>
The current status of the program management account.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE`
Required: No

 ** updatedAt **   <a name="AWSPartnerCentral-Type-channel_ProgramManagementAccountSummary-updatedAt"></a>
The timestamp when the account was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_ProgramManagementAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ProgramManagementAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ProgramManagementAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ProgramManagementAccountSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
