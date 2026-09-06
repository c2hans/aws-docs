---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UserJourney.html
---

# UserJourney
<a name="API_UserJourney"></a>

Represents a user journey that defines a critical path through a system.

## Contents
<a name="API_UserJourney_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-UserJourney-name"></a>
Entity label (not part of ARN — spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}`
Required: Yes

 ** userJourneyId **   <a name="ngresiliencehub-Type-UserJourney-userJourneyId"></a>
The unique identifier of the user journey.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-UserJourney-createdAt"></a>
The timestamp when the user journey was created.
Type: Timestamp
Required: No

 ** description **   <a name="ngresiliencehub-Type-UserJourney-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** policyArn **   <a name="ngresiliencehub-Type-UserJourney-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-UserJourney-updatedAt"></a>
The timestamp when the user journey was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_UserJourney_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/UserJourney)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/UserJourney)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/UserJourney)
