---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_EdiConfiguration.html
---

# EdiConfiguration
<a name="API_EdiConfiguration"></a>

Specifies the details for the EDI (electronic data interchange) transformation.

## Contents
<a name="API_EdiConfiguration_Contents"></a>

 ** inputLocation **   <a name="b2bi-Type-EdiConfiguration-inputLocation"></a>
Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an `S3Location` object.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** outputLocation **   <a name="b2bi-Type-EdiConfiguration-outputLocation"></a>
Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an `S3Location` object.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** transformerId **   <a name="b2bi-Type-EdiConfiguration-transformerId"></a>
Returns the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** type **   <a name="b2bi-Type-EdiConfiguration-type"></a>
Returns the type of the capability. Currently, only `edi` is supported.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capabilityDirection **   <a name="b2bi-Type-EdiConfiguration-capabilityDirection"></a>
Specifies whether this is capability is for inbound or outbound transformations.
Type: String
Valid Values: `INBOUND | OUTBOUND`
Required: No

## See Also
<a name="API_EdiConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/EdiConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/EdiConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/EdiConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
