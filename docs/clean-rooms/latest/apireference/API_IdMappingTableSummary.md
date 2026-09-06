---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IdMappingTableSummary.html
---

# IdMappingTableSummary
<a name="API_IdMappingTableSummary"></a>

Detailed information about the ID mapping table.

## Contents
<a name="API_IdMappingTableSummary_Contents"></a>

 ** arn **   <a name="API-Type-IdMappingTableSummary-arn"></a>
The Amazon Resource Name (ARN) of this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/idmappingtable/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-IdMappingTableSummary-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-IdMappingTableSummary-collaborationId"></a>
The unique identifier of the collaboration that contains this ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-IdMappingTableSummary-createTime"></a>
The time at which this ID mapping table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-IdMappingTableSummary-id"></a>
The unique identifier of this ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** inputReferenceConfig **   <a name="API-Type-IdMappingTableSummary-inputReferenceConfig"></a>
The input reference configuration for the ID mapping table.
Type: [IdMappingTableInputReferenceConfig](API_IdMappingTableInputReferenceConfig.md) object
Required: Yes

 ** membershipArn **   <a name="API-Type-IdMappingTableSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership resource for this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-IdMappingTableSummary-membershipId"></a>
The unique identifier of the membership resource for this ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IdMappingTableSummary-name"></a>
The name of this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** updateTime **   <a name="API-Type-IdMappingTableSummary-updateTime"></a>
The most recent time at which this ID mapping table was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-IdMappingTableSummary-description"></a>
The description of this ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_IdMappingTableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IdMappingTableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IdMappingTableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IdMappingTableSummary)
