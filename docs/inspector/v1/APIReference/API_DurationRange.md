---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_DurationRange.html
---

# DurationRange
<a name="API_DurationRange"></a>

This data type is used in the [AssessmentTemplateFilter](API_AssessmentTemplateFilter.md) data type.

## Contents
<a name="API_DurationRange_Contents"></a>

 ** maxSeconds **   <a name="Inspector-Type-DurationRange-maxSeconds"></a>
The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 86400.
Required: No

 ** minSeconds **   <a name="Inspector-Type-DurationRange-minSeconds"></a>
The minimum value of the duration range. Must be greater than zero.
Type: Integer
Valid Range: Minimum value of 180. Maximum value of 86400.
Required: No

## See Also
<a name="API_DurationRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/DurationRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/DurationRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/DurationRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
