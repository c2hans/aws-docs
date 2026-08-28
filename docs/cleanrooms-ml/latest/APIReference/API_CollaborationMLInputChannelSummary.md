---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CollaborationMLInputChannelSummary.html
---

# CollaborationMLInputChannelSummary
<a name="API_CollaborationMLInputChannelSummary"></a>

Provides summary information about an ML input channel in a collaboration.

## Contents
<a name="API_CollaborationMLInputChannelSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-CollaborationMLInputChannelSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the ML input channel.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** configuredModelAlgorithmAssociations **   <a name="API-Type-CollaborationMLInputChannelSummary-configuredModelAlgorithmAssociations"></a>
The associated configured model algorithms used to create the ML input channel.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationMLInputChannelSummary-createTime"></a>
The time at which the ML input channel was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationMLInputChannelSummary-creatorAccountId"></a>
The account ID of the member who created the ML input channel.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-CollaborationMLInputChannelSummary-membershipIdentifier"></a>
The membership ID of the membership that contains the ML input channel.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** mlInputChannelArn **   <a name="API-Type-CollaborationMLInputChannelSummary-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** name **   <a name="API-Type-CollaborationMLInputChannelSummary-name"></a>
The name of the ML input channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-CollaborationMLInputChannelSummary-status"></a>
The status of the ML input channel.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED | INACTIVE`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationMLInputChannelSummary-updateTime"></a>
The most recent time at which the ML input channel was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-CollaborationMLInputChannelSummary-description"></a>
The description of the ML input channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** payerConfiguration **   <a name="API-Type-CollaborationMLInputChannelSummary-payerConfiguration"></a>
The payer configuration for the ML input channel.
Type: [PayerConfiguration](API_PayerConfiguration.md) object
Required: No

## See Also
<a name="API_CollaborationMLInputChannelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CollaborationMLInputChannelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CollaborationMLInputChannelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CollaborationMLInputChannelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
