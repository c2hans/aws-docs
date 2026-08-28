---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_TraceLocation.html
---

# TraceLocation
<a name="API_TraceLocation"></a>

Information about where trace data is stored for debugging and monitoring.

## Contents
<a name="API_TraceLocation_Contents"></a>

 ** location **   <a name="novaact-Type-TraceLocation-location"></a>
The specific location where the trace data is stored.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** locationType **   <a name="novaact-Type-TraceLocation-locationType"></a>
The type of storage location for the trace data.
Type: String
Valid Values: `S3`
Required: Yes

## See Also
<a name="API_TraceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/TraceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/TraceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/TraceLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
