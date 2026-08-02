---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UserJourneySummary.html
---

# UserJourneySummary
<a name="API_UserJourneySummary"></a>

Contains summary information about a user journey.

## Contents
<a name="API_UserJourneySummary_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-UserJourneySummary-name"></a>
Entity label (not part of ARN — spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}`
Required: Yes

 ** userJourneyId **   <a name="ngresiliencehub-Type-UserJourneySummary-userJourneyId"></a>
The unique identifier of the user journey.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-UserJourneySummary-createdAt"></a>
The timestamp when the user journey was created.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-UserJourneySummary-updatedAt"></a>
The timestamp when the user journey was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_UserJourneySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/UserJourneySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/UserJourneySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/UserJourneySummary)
