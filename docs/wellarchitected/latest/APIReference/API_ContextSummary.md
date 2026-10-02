---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ContextSummary.html
---

# ContextSummary
<a name="API_ContextSummary"></a>

Summary of a context associated with a profile, representing application or environment information used during recommendation generation.

## Contents
<a name="API_ContextSummary_Contents"></a>

 ** content **   <a name="wellarchitected-Type-ContextSummary-content"></a>
The typed content of the context, containing application-specific fields such as account IDs, Regions, services, and resource types.
Type: [ContextContent](API_ContextContent.md) object
Required: Yes

 ** contextType **   <a name="wellarchitected-Type-ContextSummary-contextType"></a>
The type of the context.
Type: String
Valid Values: `APPLICATION`
Required: Yes

 ** createdAt **   <a name="wellarchitected-Type-ContextSummary-createdAt"></a>
The timestamp when the context was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="wellarchitected-Type-ContextSummary-createdBy"></a>
The identifier of the user or system that created this context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** id **   <a name="wellarchitected-Type-ContextSummary-id"></a>
The unique identifier of the context.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** profileArn **   <a name="wellarchitected-Type-ContextSummary-profileArn"></a>
The Amazon Resource Name (ARN) of the associated profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

 ** title **   <a name="wellarchitected-Type-ContextSummary-title"></a>
The title of the context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: Yes

 ** applicationType **   <a name="wellarchitected-Type-ContextSummary-applicationType"></a>
The type of application described by this context.
Type: String
Valid Values: `SAS | DESKTOP_APPLICATION | OTHER`
Required: No

 ** criticality **   <a name="wellarchitected-Type-ContextSummary-criticality"></a>
The business criticality of the application described by this context.
Type: String
Valid Values: `MISSION_CRITICAL | BUSINESS_CRITICAL | NON_CRITICAL | TEST_DEVELOPMENT`
Required: No

 ** lastModifiedAt **   <a name="wellarchitected-Type-ContextSummary-lastModifiedAt"></a>
The timestamp when the context was last modified.
Type: Timestamp
Required: No

 ** lastModifiedBy **   <a name="wellarchitected-Type-ContextSummary-lastModifiedBy"></a>
The identifier of the user or system that last modified this context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ContextSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ContextSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ContextSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ContextSummary)
