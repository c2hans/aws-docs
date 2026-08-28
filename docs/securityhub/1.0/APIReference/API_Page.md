---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Page.html
---

# Page
<a name="API_Page"></a>

An occurrence of sensitive data in an Adobe Portable Document Format (PDF) file.

## Contents
<a name="API_Page_Contents"></a>

 ** LineRange **   <a name="securityhub-Type-Page-LineRange"></a>
An occurrence of sensitive data detected in a non-binary text file or a Microsoft Word file. Non-binary text files include files such as HTML, XML, JSON, and TXT files.
Type: [Range](API_Range.md) object
Required: No

 ** OffsetRange **   <a name="securityhub-Type-Page-OffsetRange"></a>
An occurrence of sensitive data detected in a binary text file.
Type: [Range](API_Range.md) object
Required: No

 ** PageNumber **   <a name="securityhub-Type-Page-PageNumber"></a>
The page number of the page that contains the sensitive data.
Type: Long
Required: No

## See Also
<a name="API_Page_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Page)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Page)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Page)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
