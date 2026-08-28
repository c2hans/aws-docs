---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Range.html
---

# Range
<a name="API_Range"></a>

Identifies where the sensitive data begins and ends.

## Contents
<a name="API_Range_Contents"></a>

 ** End **   <a name="securityhub-Type-Range-End"></a>
The number of lines (for a line range) or characters (for an offset range) from the beginning of the file to the end of the sensitive data.
Type: Long
Required: No

 ** Start **   <a name="securityhub-Type-Range-Start"></a>
The number of lines (for a line range) or characters (for an offset range) from the beginning of the file to the end of the sensitive data.
Type: Long
Required: No

 ** StartColumn **   <a name="securityhub-Type-Range-StartColumn"></a>
In the line where the sensitive data starts, the column within the line where the sensitive data starts.
Type: Long
Required: No

## See Also
<a name="API_Range_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Range)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Range)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Range)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
