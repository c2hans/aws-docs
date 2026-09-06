---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_SystemEventDetails.html
---

# SystemEventDetails
<a name="API_SystemEventDetails"></a>

Contains the details of a system event.

## Contents
<a name="API_SystemEventDetails_Contents"></a>

 ** description **   <a name="ngresiliencehub-Type-SystemEventDetails-description"></a>
The description of the event.
Type: String
Required: Yes

 ** title **   <a name="ngresiliencehub-Type-SystemEventDetails-title"></a>
The title of the event.
Type: String
Required: Yes

 ** eventMetadata **   <a name="ngresiliencehub-Type-SystemEventDetails-eventMetadata"></a>
Type-specific metadata for each system event type.
Type: [SystemEventMetadata](API_SystemEventMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_SystemEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/SystemEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/SystemEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/SystemEventDetails)
