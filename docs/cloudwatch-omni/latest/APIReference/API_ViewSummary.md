---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ViewSummary.html
---

# ViewSummary
<a name="API_ViewSummary"></a>

Summary information about a view. Does not include the view definition.

## Contents
<a name="API_ViewSummary_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-ViewSummary-createdAt"></a>
The timestamp when the view was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-ViewSummary-name"></a>
The name of the view.
Type: String
Required: Yes

 ** type **   <a name="cloudwatchomni-Type-ViewSummary-type"></a>
The ownership category of the view.
Type: String
Valid Values: `USER | MANAGED`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-ViewSummary-updatedAt"></a>
The timestamp when the view was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="cloudwatchomni-Type-ViewSummary-description"></a>
The description of the view.
Type: String
Required: No

## See Also
<a name="API_ViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ViewSummary)
