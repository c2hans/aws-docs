---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionTarget.html
---

# ConversionTarget
<a name="API_ConversionTarget"></a>

Provide a sample of what the output of the transformation should look like.

## Contents
<a name="API_ConversionTarget_Contents"></a>

 ** fileFormat **   <a name="b2bi-Type-ConversionTarget-fileFormat"></a>
Currently, only X12 format is supported.
Type: String
Valid Values: `X12`
Required: Yes

 ** advancedOptions **   <a name="b2bi-Type-ConversionTarget-advancedOptions"></a>
A structure that contains advanced options for EDI processing. Currently, only X12 advanced options are supported.
Type: [AdvancedOptions](API_AdvancedOptions.md) object
Required: No

 ** formatDetails **   <a name="b2bi-Type-ConversionTarget-formatDetails"></a>
A structure that contains the formatting details for the conversion target.
Type: [ConversionTargetFormatDetails](API_ConversionTargetFormatDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** outputSampleFile **   <a name="b2bi-Type-ConversionTarget-outputSampleFile"></a>
Container for the location of a sample file used for outbound transformations.
Type: [OutputSampleFileSource](API_OutputSampleFileSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ConversionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ConversionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ConversionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ConversionTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
