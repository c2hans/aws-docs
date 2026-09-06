---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_Graph.html
---

# Graph
<a name="API_Graph"></a>

A behavior graph in Detective.

## Contents
<a name="API_Graph_Contents"></a>

 ** Arn **   <a name="detective-Type-Graph-Arn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: No

 ** CreatedTime **   <a name="detective-Type-Graph-CreatedTime"></a>
The date and time that the behavior graph was created. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

## See Also
<a name="API_Graph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/Graph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/Graph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/Graph)
