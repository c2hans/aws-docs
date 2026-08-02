---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_AssociatedSystem.html
---

# AssociatedSystem
<a name="API_AssociatedSystem"></a>

Represents a system associated with a service.

## Contents
<a name="API_AssociatedSystem_Contents"></a>

 ** systemArn **   <a name="ngresiliencehub-Type-AssociatedSystem-systemArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** systemName **   <a name="ngresiliencehub-Type-AssociatedSystem-systemName"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** userJourneyIds **   <a name="ngresiliencehub-Type-AssociatedSystem-userJourneyIds"></a>
The list of user journey identifiers that associate this system with the service.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: No

## See Also
<a name="API_AssociatedSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/AssociatedSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/AssociatedSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/AssociatedSystem)
