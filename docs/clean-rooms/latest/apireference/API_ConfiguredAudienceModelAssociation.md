---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredAudienceModelAssociation.html
---

# ConfiguredAudienceModelAssociation
<a name="API_ConfiguredAudienceModelAssociation"></a>

Details about the configured audience model association.

## Contents
<a name="API_ConfiguredAudienceModelAssociation_Contents"></a>

 ** arn **   <a name="API-Type-ConfiguredAudienceModelAssociation-arn"></a>
The Amazon Resource Name (ARN) of the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/configuredaudiencemodelassociation/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-ConfiguredAudienceModelAssociation-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains this configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-ConfiguredAudienceModelAssociation-collaborationId"></a>
A unique identifier of the collaboration that contains this configured audience model association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** configuredAudienceModelArn **   <a name="API-Type-ConfiguredAudienceModelAssociation-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredAudienceModelAssociation-createTime"></a>
The time at which the configured audience model association was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredAudienceModelAssociation-id"></a>
A unique identifier of the configured audience model association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** manageResourcePolicies **   <a name="API-Type-ConfiguredAudienceModelAssociation-manageResourcePolicies"></a>
When `TRUE`, indicates that the resource policy for the configured audience model resource being associated is configured for AWS Clean Rooms to manage permissions related to the given collaboration. When `FALSE`, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.
Type: Boolean
Required: Yes

 ** membershipArn **   <a name="API-Type-ConfiguredAudienceModelAssociation-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership that contains this configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ConfiguredAudienceModelAssociation-membershipId"></a>
A unique identifier for the membership that contains this configured audience model association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredAudienceModelAssociation-name"></a>
The name of the configured audience model association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredAudienceModelAssociation-updateTime"></a>
The most recent time at which the configured audience model association was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredAudienceModelAssociation-description"></a>
The description of the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredAudienceModelAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredAudienceModelAssociation)
