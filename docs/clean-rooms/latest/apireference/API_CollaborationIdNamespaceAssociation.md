---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationIdNamespaceAssociation.html
---

# CollaborationIdNamespaceAssociation
<a name="API_CollaborationIdNamespaceAssociation"></a>

Defines details for the collaboration ID namespace association.

## Contents
<a name="API_CollaborationIdNamespaceAssociation_Contents"></a>

 ** arn **   <a name="API-Type-CollaborationIdNamespaceAssociation-arn"></a>
The Amazon Resource Name (ARN) of the collaboration ID namespace association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/idnamespaceassociation/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-CollaborationIdNamespaceAssociation-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains the collaboration ID namespace association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationIdNamespaceAssociation-collaborationId"></a>
The unique identifier of the collaboration that contains the collaboration ID namespace association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationIdNamespaceAssociation-createTime"></a>
The time at which the collaboration ID namespace association was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationIdNamespaceAssociation-creatorAccountId"></a>
The unique identifier of the AWS account that created the collaboration ID namespace association.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** id **   <a name="API-Type-CollaborationIdNamespaceAssociation-id"></a>
The unique identifier of the collaboration ID namespace association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** inputReferenceConfig **   <a name="API-Type-CollaborationIdNamespaceAssociation-inputReferenceConfig"></a>
The input reference configuration that's necessary to create the collaboration ID namespace association.
Type: [IdNamespaceAssociationInputReferenceConfig](API_IdNamespaceAssociationInputReferenceConfig.md) object
Required: Yes

 ** inputReferenceProperties **   <a name="API-Type-CollaborationIdNamespaceAssociation-inputReferenceProperties"></a>
The input reference properties that are needed to create the collaboration ID namespace association.
Type: [IdNamespaceAssociationInputReferenceProperties](API_IdNamespaceAssociationInputReferenceProperties.md) object
Required: Yes

 ** name **   <a name="API-Type-CollaborationIdNamespaceAssociation-name"></a>
The name of the collaboration ID namespace association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationIdNamespaceAssociation-updateTime"></a>
The most recent time at which the collaboration ID namespace was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-CollaborationIdNamespaceAssociation-description"></a>
The description of the collaboration ID namespace association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** idMappingConfig **   <a name="API-Type-CollaborationIdNamespaceAssociation-idMappingConfig"></a>
The configuration settings for the ID mapping table.
Type: [IdMappingConfig](API_IdMappingConfig.md) object
Required: No

## See Also
<a name="API_CollaborationIdNamespaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationIdNamespaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationIdNamespaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationIdNamespaceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
