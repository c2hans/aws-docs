---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionTargetFormatDetails.html
---

# ConversionTargetFormatDetails
<a name="API_ConversionTargetFormatDetails"></a>

Contains a structure describing the X12 details for the conversion target.

## Contents
<a name="API_ConversionTargetFormatDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** x12 **   <a name="b2bi-Type-ConversionTargetFormatDetails-x12"></a>
A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.
If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.
Type: [X12Details](API_X12Details.md) object
Required: No

## See Also
<a name="API_ConversionTargetFormatDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ConversionTargetFormatDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ConversionTargetFormatDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ConversionTargetFormatDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
