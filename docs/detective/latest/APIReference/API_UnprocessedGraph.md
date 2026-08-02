---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_UnprocessedGraph.html
---

# UnprocessedGraph
<a name="API_UnprocessedGraph"></a>

Behavior graphs that could not be processed in the request.

## Contents
<a name="API_UnprocessedGraph_Contents"></a>

 ** GraphArn **   <a name="detective-Type-UnprocessedGraph-GraphArn"></a>
The ARN of the organization behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: No

 ** Reason **   <a name="detective-Type-UnprocessedGraph-Reason"></a>
The reason data source package information could not be processed for a behavior graph.
Type: String
Required: No

## See Also
<a name="API_UnprocessedGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/UnprocessedGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/UnprocessedGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/UnprocessedGraph)
