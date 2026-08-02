---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualCustomActionOperation.html
---

# VisualCustomActionOperation
<a name="API_VisualCustomActionOperation"></a>

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_VisualCustomActionOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FilterOperation **   <a name="QS-Type-VisualCustomActionOperation-FilterOperation"></a>
The filter operation that filters data included in a visual or in an entire sheet.
Type: [CustomActionFilterOperation](API_CustomActionFilterOperation.md) object
Required: No

 ** NavigationOperation **   <a name="QS-Type-VisualCustomActionOperation-NavigationOperation"></a>
The navigation operation that navigates between different sheets in the same analysis.
Type: [CustomActionNavigationOperation](API_CustomActionNavigationOperation.md) object
Required: No

 ** SetParametersOperation **   <a name="QS-Type-VisualCustomActionOperation-SetParametersOperation"></a>
The set parameter operation that sets parameters in custom action.
Type: [CustomActionSetParametersOperation](API_CustomActionSetParametersOperation.md) object
Required: No

 ** URLOperation **   <a name="QS-Type-VisualCustomActionOperation-URLOperation"></a>
The URL operation that opens a link to another webpage.
Type: [CustomActionURLOperation](API_CustomActionURLOperation.md) object
Required: No

## See Also
<a name="API_VisualCustomActionOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VisualCustomActionOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VisualCustomActionOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VisualCustomActionOperation)
