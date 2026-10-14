---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PolicyEventDetails.html
---

# PolicyEventDetails
<a name="API_PolicyEventDetails"></a>

Contains the title, description, and event-specific metadata for a single event on the timeline of a resilience policy.

## Contents
<a name="API_PolicyEventDetails_Contents"></a>

 ** description **   <a name="ngresiliencehub-Type-PolicyEventDetails-description"></a>
A description of the event.
Type: String
Required: Yes

 ** title **   <a name="ngresiliencehub-Type-PolicyEventDetails-title"></a>
A short summary of the event.
Type: String
Required: Yes

 ** eventMetadata **   <a name="ngresiliencehub-Type-PolicyEventDetails-eventMetadata"></a>
The event-specific metadata, with one member populated according to the event type.
Type: [PolicyEventMetadata](API_PolicyEventMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PolicyEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/PolicyEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/PolicyEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/PolicyEventDetails)
