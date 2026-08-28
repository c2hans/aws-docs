---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateXMLClassifierRequest.html
---

# UpdateXMLClassifierRequest
<a name="API_UpdateXMLClassifierRequest"></a>

Specifies an XML classifier to be updated.

## Contents
<a name="API_UpdateXMLClassifierRequest_Contents"></a>

 ** Name **   <a name="Glue-Type-UpdateXMLClassifierRequest-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Classification **   <a name="Glue-Type-UpdateXMLClassifierRequest-Classification"></a>
An identifier of the data format that the classifier matches.
Type: String
Required: No

 ** RowTag **   <a name="Glue-Type-UpdateXMLClassifierRequest-RowTag"></a>
The XML tag designating the element that contains each record in an XML document being parsed. This cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
Type: String
Required: No

## See Also
<a name="API_UpdateXMLClassifierRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateXMLClassifierRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateXMLClassifierRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateXMLClassifierRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
