---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ResoldUnifiedOperations.html
---

# ResoldUnifiedOperations
<a name="API_channel_ResoldUnifiedOperations"></a>

Configuration for resold unified operations support plans.

## Contents
<a name="API_channel_ResoldUnifiedOperations_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** coverage **   <a name="AWSPartnerCentral-Type-channel_ResoldUnifiedOperations-coverage"></a>
The coverage level for resold unified operations support.
Type: String
Valid Values: `ENTIRE_ORGANIZATION | MANAGEMENT_ACCOUNT_ONLY`
Required: Yes

 ** tamLocation **   <a name="AWSPartnerCentral-Type-channel_ResoldUnifiedOperations-tamLocation"></a>
The location of the Technical Account Manager (TAM).
Type: String
Required: Yes

 ** chargeAccountId **   <a name="AWSPartnerCentral-Type-channel_ResoldUnifiedOperations-chargeAccountId"></a>
The AWS account ID to charge for the support plan.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: No

## See Also
<a name="API_channel_ResoldUnifiedOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ResoldUnifiedOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ResoldUnifiedOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ResoldUnifiedOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
