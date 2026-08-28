---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TransformerSummary.html
---

# TransformerSummary
<a name="API_TransformerSummary"></a>

Contains the details for a transformer object. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

## Contents
<a name="API_TransformerSummary_Contents"></a>

 ** createdAt **   <a name="b2bi-Type-TransformerSummary-createdAt"></a>
Returns a timestamp indicating when the transformer was created. For example, `2023-07-20T19:58:44.624Z`.
Type: Timestamp
Required: Yes

 ** name **   <a name="b2bi-Type-TransformerSummary-name"></a>
Returns the descriptive name for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9_-]{1,512}`
Required: Yes

 ** status **   <a name="b2bi-Type-TransformerSummary-status"></a>
Returns the state of the newly created transformer. The transformer can be either `active` or `inactive`. For the transformer to be used in a capability, its status must `active`.
Type: String
Valid Values: `active | inactive`
Required: Yes

 ** transformerId **   <a name="b2bi-Type-TransformerSummary-transformerId"></a>
Returns the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** ediType **   <a name="b2bi-Type-TransformerSummary-ediType"></a>
 *This member has been deprecated.*
Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** fileFormat **   <a name="b2bi-Type-TransformerSummary-fileFormat"></a>
 *This member has been deprecated.*
Returns that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`
Required: No

 ** inputConversion **   <a name="b2bi-Type-TransformerSummary-inputConversion"></a>
Returns a structure that contains the format options for the transformation.
Type: [InputConversion](API_InputConversion.md) object
Required: No

 ** mapping **   <a name="b2bi-Type-TransformerSummary-mapping"></a>
Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
Type: [Mapping](API_Mapping.md) object
Required: No

 ** mappingTemplate **   <a name="b2bi-Type-TransformerSummary-mappingTemplate"></a>
 *This member has been deprecated.*
Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.
Required: No

 ** modifiedAt **   <a name="b2bi-Type-TransformerSummary-modifiedAt"></a>
Returns a timestamp representing the date and time for the most recent change for the transformer object.
Type: Timestamp
Required: No

 ** outputConversion **   <a name="b2bi-Type-TransformerSummary-outputConversion"></a>
Returns the `OutputConversion` object, which contains the format options for the outbound transformation.
Type: [OutputConversion](API_OutputConversion.md) object
Required: No

 ** sampleDocument **   <a name="b2bi-Type-TransformerSummary-sampleDocument"></a>
 *This member has been deprecated.*
Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** sampleDocuments **   <a name="b2bi-Type-TransformerSummary-sampleDocuments"></a>
Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
Type: [SampleDocuments](API_SampleDocuments.md) object
Required: No

## See Also
<a name="API_TransformerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/TransformerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/TransformerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/TransformerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
