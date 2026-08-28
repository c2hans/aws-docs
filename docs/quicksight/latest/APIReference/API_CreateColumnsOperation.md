---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateColumnsOperation.html
---

# CreateColumnsOperation
<a name="API_CreateColumnsOperation"></a>

A transform operation that creates calculated columns. Columns created in one such operation form a lexical closure.

## Contents
<a name="API_CreateColumnsOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Columns **   <a name="QS-Type-CreateColumnsOperation-Columns"></a>
Calculated columns to create.
Type: Array of [CalculatedColumn](API_CalculatedColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: Yes

 ** Alias **   <a name="QS-Type-CreateColumnsOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Source **   <a name="QS-Type-CreateColumnsOperation-Source"></a>
The source transform operation that provides input data for creating new calculated columns.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: No

## See Also
<a name="API_CreateColumnsOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateColumnsOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateColumnsOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateColumnsOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
