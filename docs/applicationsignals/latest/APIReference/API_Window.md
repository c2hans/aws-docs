---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Window.html
---

# Window
<a name="API_Window"></a>

The object that defines the time length of an exclusion window.

## Contents
<a name="API_Window_Contents"></a>

 ** Duration **   <a name="applicationsignals-Type-Window-Duration"></a>
The number of time units for the exclusion window length.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** DurationUnit **   <a name="applicationsignals-Type-Window-DurationUnit"></a>
The unit of time for the exclusion window duration. Valid values: MINUTE, HOUR, DAY, MONTH.
Type: String
Valid Values: `MINUTE | HOUR | DAY | MONTH`
Required: Yes

## See Also
<a name="API_Window_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Window)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Window)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Window)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
