---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomActionURLOperation.html
---

# CustomActionURLOperation
<a name="API_CustomActionURLOperation"></a>

The URL operation that opens a link to another webpage.

## Contents
<a name="API_CustomActionURLOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** URLTarget **   <a name="QS-Type-CustomActionURLOperation-URLTarget"></a>
The target of the `CustomActionURLOperation`.
Valid values are defined as follows:
+  `NEW_TAB`: Opens the target URL in a new browser tab.
+  `NEW_WINDOW`: Opens the target URL in a new browser window.
+  `SAME_TAB`: Opens the target URL in the same browser tab.
Type: String
Valid Values: `NEW_TAB | NEW_WINDOW | SAME_TAB`
Required: Yes

 ** URLTemplate **   <a name="QS-Type-CustomActionURLOperation-URLTemplate"></a>
THe URL link of the `CustomActionURLOperation`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_CustomActionURLOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomActionURLOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomActionURLOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomActionURLOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
