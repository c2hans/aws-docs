---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12SplitOptions.html
---

# X12SplitOptions
<a name="API_X12SplitOptions"></a>

Contains options for splitting X12 EDI files into smaller units. This is useful for processing large EDI files more efficiently.

## Contents
<a name="API_X12SplitOptions_Contents"></a>

 ** splitBy **   <a name="b2bi-Type-X12SplitOptions-splitBy"></a>
Specifies the method used to split X12 EDI files. Valid values include `TRANSACTION` (split by individual transaction sets), or `NONE` (no splitting).
Type: String
Valid Values: `NONE | TRANSACTION`
Required: Yes

## See Also
<a name="API_X12SplitOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12SplitOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12SplitOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12SplitOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
