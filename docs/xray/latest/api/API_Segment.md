---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Segment.html
---

# Segment
<a name="API_Segment"></a>

A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html), or an `inferred` segment for a downstream service, generated from a subsegment sent by the service that called it.

For the full segment document schema, see [AWS X-Ray segment documents](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-api.html#xray-api-segmentdocuments) in the * AWS X-Ray Developer Guide*.

## Contents
<a name="API_Segment_Contents"></a>

 ** Document **   <a name="xray-Type-Segment-Document"></a>
The segment document.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Id **   <a name="xray-Type-Segment-Id"></a>
The segment's ID.
Type: String
Required: No

## See Also
<a name="API_Segment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Segment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Segment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Segment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
