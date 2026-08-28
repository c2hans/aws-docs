---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredModelAlgorithmAssociationSummary.html
---

# ConfiguredModelAlgorithmAssociationSummary
<a name="API_ConfiguredModelAlgorithmAssociationSummary"></a>

Provides summary information about the configured model algorithm association.

## Contents
<a name="API_ConfiguredModelAlgorithmAssociationSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** configuredModelAlgorithmArn **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm that is being associated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** configuredModelAlgorithmAssociationArn **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-createTime"></a>
The time at which the configured model algorithm association was created.
Type: Timestamp
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-membershipIdentifier"></a>
The membership ID of the member that created the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-name"></a>
The name of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-updateTime"></a>
The most recent time at which the configured model algorithm association was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredModelAlgorithmAssociationSummary-description"></a>
The description of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredModelAlgorithmAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
