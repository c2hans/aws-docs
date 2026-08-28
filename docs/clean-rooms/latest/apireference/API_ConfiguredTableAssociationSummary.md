---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConfiguredTableAssociationSummary.html
---

# ConfiguredTableAssociationSummary
<a name="API_ConfiguredTableAssociationSummary"></a>

The configured table association summary for the objects listed by the request.

## Contents
<a name="API_ConfiguredTableAssociationSummary_Contents"></a>

 ** arn **   <a name="API-Type-ConfiguredTableAssociationSummary-arn"></a>
The unique ARN for the configured table association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:configuredtableassociation/[\d\w-]+/[\d\w-]+`
Required: Yes

 ** configuredTableId **   <a name="API-Type-ConfiguredTableAssociationSummary-configuredTableId"></a>
The unique configured table ID that this configured table association refers to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredTableAssociationSummary-createTime"></a>
The time the configured table association was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ConfiguredTableAssociationSummary-id"></a>
The unique ID for the configured table association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ConfiguredTableAssociationSummary-membershipArn"></a>
The unique ARN for the membership that the configured table association belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ConfiguredTableAssociationSummary-membershipId"></a>
The unique ID for the membership that the configured table association belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-ConfiguredTableAssociationSummary-name"></a>
The name of the configured table association. The table is identified by this name when running Protected Queries against the underlying data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredTableAssociationSummary-updateTime"></a>
The time the configured table association was last updated.
Type: Timestamp
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-ConfiguredTableAssociationSummary-analysisRuleTypes"></a>
The analysis rule types that are associated with the configured table associations in this summary.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: No

## See Also
<a name="API_ConfiguredTableAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConfiguredTableAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConfiguredTableAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConfiguredTableAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
