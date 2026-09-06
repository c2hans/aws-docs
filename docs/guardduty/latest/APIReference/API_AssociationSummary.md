---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AssociationSummary.html
---

# AssociationSummary
<a name="API_AssociationSummary"></a>

Contains summary information about a custom detection rule association.

## Contents
<a name="API_AssociationSummary_Contents"></a>

 ** arn **   <a name="guardduty-Type-AssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:([0-9]*|aws):.+`
Required: Yes

 ** associationId **   <a name="guardduty-Type-AssociationSummary-associationId"></a>
The unique identifier for the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** createdAt **   <a name="guardduty-Type-AssociationSummary-createdAt"></a>
The timestamp when the association was created.
Type: Timestamp
Required: Yes

 ** mode **   <a name="guardduty-Type-AssociationSummary-mode"></a>
The rule execution mode. Valid values: `LIVE` \| `DRY_RUN`.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** ruleId **   <a name="guardduty-Type-AssociationSummary-ruleId"></a>
The unique identifier for the custom detection rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-AssociationSummary-updatedAt"></a>
The timestamp when the association was last updated.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="guardduty-Type-AssociationSummary-expiresAt"></a>
The timestamp when the association expires.
Type: Timestamp
Required: No

## See Also
<a name="API_AssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AssociationSummary)
