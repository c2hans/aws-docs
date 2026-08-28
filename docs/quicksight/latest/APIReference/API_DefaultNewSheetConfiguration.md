---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DefaultNewSheetConfiguration.html
---

# DefaultNewSheetConfiguration
<a name="API_DefaultNewSheetConfiguration"></a>

The configuration for default new sheet settings.

## Contents
<a name="API_DefaultNewSheetConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InteractiveLayoutConfiguration **   <a name="QS-Type-DefaultNewSheetConfiguration-InteractiveLayoutConfiguration"></a>
The options that determine the default settings for interactive layout configuration.
Type: [DefaultInteractiveLayoutConfiguration](API_DefaultInteractiveLayoutConfiguration.md) object
Required: No

 ** PaginatedLayoutConfiguration **   <a name="QS-Type-DefaultNewSheetConfiguration-PaginatedLayoutConfiguration"></a>
The options that determine the default settings for a paginated layout configuration.
Type: [DefaultPaginatedLayoutConfiguration](API_DefaultPaginatedLayoutConfiguration.md) object
Required: No

 ** SheetContentType **   <a name="QS-Type-DefaultNewSheetConfiguration-SheetContentType"></a>
The option that determines the sheet content type.
Type: String
Valid Values: `PAGINATED | INTERACTIVE`
Required: No

## See Also
<a name="API_DefaultNewSheetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DefaultNewSheetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DefaultNewSheetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DefaultNewSheetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
