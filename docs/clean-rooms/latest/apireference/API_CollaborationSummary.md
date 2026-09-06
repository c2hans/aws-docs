---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationSummary.html
---

# CollaborationSummary
<a name="API_CollaborationSummary"></a>

The metadata of the collaboration.

## Contents
<a name="API_CollaborationSummary_Contents"></a>

 ** arn **   <a name="API-Type-CollaborationSummary-arn"></a>
The ARN of the collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationSummary-createTime"></a>
The time when the collaboration was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationSummary-creatorAccountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** creatorDisplayName **   <a name="API-Type-CollaborationSummary-creatorDisplayName"></a>
The display name of the collaboration creator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** id **   <a name="API-Type-CollaborationSummary-id"></a>
The identifier for the collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** memberStatus **   <a name="API-Type-CollaborationSummary-memberStatus"></a>
The status of a member in a collaboration.
Type: String
Valid Values: `INVITED | ACTIVE | LEFT | REMOVED`
Required: Yes

 ** name **   <a name="API-Type-CollaborationSummary-name"></a>
A human-readable identifier provided by the collaboration owner. Display names are not unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationSummary-updateTime"></a>
The time the collaboration metadata was last updated.
Type: Timestamp
Required: Yes

 ** analyticsEngine **   <a name="API-Type-CollaborationSummary-analyticsEngine"></a>
 The analytics engine.
After July 16, 2025, the `CLEAN_ROOMS_SQL` parameter will no longer be available.
Type: String
Valid Values: `SPARK | CLEAN_ROOMS_SQL`
Required: No

 ** membershipArn **   <a name="API-Type-CollaborationSummary-membershipArn"></a>
The ARN of a member in a collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: No

 ** membershipId **   <a name="API-Type-CollaborationSummary-membershipId"></a>
The identifier of a member in a collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_CollaborationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationSummary)
