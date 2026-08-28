---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredAudienceModelAssociationSummary.html
---

# ConfiguredAudienceModelAssociationSummary
<a name="API_ConfiguredAudienceModelAssociationSummary"></a>

A summary of the configured audience model association.

## Contents
<a name="API_ConfiguredAudienceModelAssociationSummary_Contents"></a>

 ** arn **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/configuredaudiencemodelassociation/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-collaborationId"></a>
A unique identifier of the collaboration that configured audience model is associated with.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** configuredAudienceModelArn **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-createTime"></a>
The time at which the configured audience model association was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-id"></a>
A unique identifier of the configured audience model association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership that contains the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-membershipId"></a>
A unique identifier of the membership that contains the configured audience model association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-name"></a>
The name of the configured audience model association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-updateTime"></a>
The most recent time at which the configured audience model association was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredAudienceModelAssociationSummary-description"></a>
The description of the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredAudienceModelAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
