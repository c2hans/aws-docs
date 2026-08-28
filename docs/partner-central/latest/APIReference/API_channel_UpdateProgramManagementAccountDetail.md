---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_UpdateProgramManagementAccountDetail.html
---

# UpdateProgramManagementAccountDetail
<a name="API_channel_UpdateProgramManagementAccountDetail"></a>

Contains details about an updated program management account.

## Contents
<a name="API_channel_UpdateProgramManagementAccountDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="AWSPartnerCentral-Type-channel_UpdateProgramManagementAccountDetail-arn"></a>
The Amazon Resource Name (ARN) of the updated program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: No

 ** displayName **   <a name="AWSPartnerCentral-Type-channel_UpdateProgramManagementAccountDetail-displayName"></a>
The updated display name of the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** id **   <a name="AWSPartnerCentral-Type-channel_UpdateProgramManagementAccountDetail-id"></a>
The unique identifier of the updated program management account.
Type: String
Length Constraints: Fixed length of 17.
Pattern: `pma-[a-z0-9]{13}`
Required: No

 ** revision **   <a name="AWSPartnerCentral-Type-channel_UpdateProgramManagementAccountDetail-revision"></a>
The new revision number of the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

## See Also
<a name="API_channel_UpdateProgramManagementAccountDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/UpdateProgramManagementAccountDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/UpdateProgramManagementAccountDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/UpdateProgramManagementAccountDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
