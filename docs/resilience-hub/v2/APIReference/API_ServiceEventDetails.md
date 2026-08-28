---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceEventDetails.html
---

# ServiceEventDetails
<a name="API_ServiceEventDetails"></a>

Contains the details of a service event.

## Contents
<a name="API_ServiceEventDetails_Contents"></a>

 ** description **   <a name="ngresiliencehub-Type-ServiceEventDetails-description"></a>
The description of the event.
Type: String
Required: Yes

 ** title **   <a name="ngresiliencehub-Type-ServiceEventDetails-title"></a>
The title of the event.
Type: String
Required: Yes

 ** eventMetadata **   <a name="ngresiliencehub-Type-ServiceEventDetails-eventMetadata"></a>
Type-specific metadata for each service event type.
Type: [ServiceEventMetadata](API_ServiceEventMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ServiceEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
