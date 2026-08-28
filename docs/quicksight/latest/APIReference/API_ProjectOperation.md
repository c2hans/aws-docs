---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ProjectOperation.html
---

# ProjectOperation
<a name="API_ProjectOperation"></a>

A transform operation that projects columns. Operations that come after a projection can only refer to projected columns.

## Contents
<a name="API_ProjectOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProjectedColumns **   <a name="QS-Type-ProjectOperation-ProjectedColumns"></a>
Projected columns.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** Alias **   <a name="QS-Type-ProjectOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Source **   <a name="QS-Type-ProjectOperation-Source"></a>
The source transform operation that provides input data for column projection.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: No

## See Also
<a name="API_ProjectOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ProjectOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ProjectOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ProjectOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
