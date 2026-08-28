---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IdMappingTable.html
---

# IdMappingTable
<a name="API_IdMappingTable"></a>

Describes information about the ID mapping table.

## Contents
<a name="API_IdMappingTable_Contents"></a>

 ** arn **   <a name="API-Type-IdMappingTable-arn"></a>
The Amazon Resource Name (ARN) of the ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/idmappingtable/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-IdMappingTable-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-IdMappingTable-collaborationId"></a>
The unique identifier of the collaboration that contains this ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-IdMappingTable-createTime"></a>
The time at which the ID mapping table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-IdMappingTable-id"></a>
The unique identifier of the ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** inputReferenceConfig **   <a name="API-Type-IdMappingTable-inputReferenceConfig"></a>
The input reference configuration for the ID mapping table.
Type: [IdMappingTableInputReferenceConfig](API_IdMappingTableInputReferenceConfig.md) object
Required: Yes

 ** inputReferenceProperties **   <a name="API-Type-IdMappingTable-inputReferenceProperties"></a>
The input reference properties for the ID mapping table.
Type: [IdMappingTableInputReferenceProperties](API_IdMappingTableInputReferenceProperties.md) object
Required: Yes

 ** membershipArn **   <a name="API-Type-IdMappingTable-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-IdMappingTable-membershipId"></a>
The unique identifier of the membership resource for the ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IdMappingTable-name"></a>
The name of the ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** updateTime **   <a name="API-Type-IdMappingTable-updateTime"></a>
The most recent time at which the ID mapping table was updated.
Type: Timestamp
Required: Yes

 ** childResources **   <a name="API-Type-IdMappingTable-childResources"></a>
The child resources that depend on this ID mapping table.
Type: Array of [ChildResource](API_ChildResource.md) objects
Required: No

 ** description **   <a name="API-Type-IdMappingTable-description"></a>
The description of the ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** kmsKeyArn **   <a name="API-Type-IdMappingTable-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_IdMappingTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IdMappingTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IdMappingTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IdMappingTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
