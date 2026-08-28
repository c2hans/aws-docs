---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OutputColumn.html
---

# OutputColumn
<a name="API_OutputColumn"></a>

Output column.

## Contents
<a name="API_OutputColumn_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="QS-Type-OutputColumn-Description"></a>
A description for a column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** Id **   <a name="QS-Type-OutputColumn-Id"></a>
A unique identifier for the output column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Name **   <a name="QS-Type-OutputColumn-Name"></a>
The display name of the column..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SubType **   <a name="QS-Type-OutputColumn-SubType"></a>
The sub data type of the column.
Type: String
Valid Values: `FLOAT | FIXED`
Required: No

 ** Type **   <a name="QS-Type-OutputColumn-Type"></a>
The data type of the column.
Type: String
Valid Values: `STRING | INTEGER | DECIMAL | DATETIME`
Required: No

## See Also
<a name="API_OutputColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OutputColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OutputColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OutputColumn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
