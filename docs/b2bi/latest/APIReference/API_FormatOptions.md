---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_FormatOptions.html
---

# FormatOptions
<a name="API_FormatOptions"></a>

A structure that contains the X12 transaction set and version.

## Contents
<a name="API_FormatOptions_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** x12 **   <a name="b2bi-Type-FormatOptions-x12"></a>
A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.
If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.
Type: [X12Details](API_X12Details.md) object
Required: No

## See Also
<a name="API_FormatOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/FormatOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/FormatOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/FormatOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
