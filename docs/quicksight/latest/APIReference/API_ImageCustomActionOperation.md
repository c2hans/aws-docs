---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ImageCustomActionOperation.html
---

# ImageCustomActionOperation
<a name="API_ImageCustomActionOperation"></a>

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_ImageCustomActionOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NavigationOperation **   <a name="QS-Type-ImageCustomActionOperation-NavigationOperation"></a>
The navigation operation that navigates between different sheets in the same analysis.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [CustomActionNavigationOperation](API_CustomActionNavigationOperation.md) object
Required: No

 ** SetParametersOperation **   <a name="QS-Type-ImageCustomActionOperation-SetParametersOperation"></a>
The set parameter operation that sets parameters in custom action.
Type: [CustomActionSetParametersOperation](API_CustomActionSetParametersOperation.md) object
Required: No

 ** URLOperation **   <a name="QS-Type-ImageCustomActionOperation-URLOperation"></a>
The URL operation that opens a link to another webpage.
Type: [CustomActionURLOperation](API_CustomActionURLOperation.md) object
Required: No

## See Also
<a name="API_ImageCustomActionOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ImageCustomActionOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ImageCustomActionOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ImageCustomActionOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
