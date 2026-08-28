---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateGrokClassifierRequest.html
---

# CreateGrokClassifierRequest
<a name="API_CreateGrokClassifierRequest"></a>

Specifies a `grok` classifier for `CreateClassifier` to create.

## Contents
<a name="API_CreateGrokClassifierRequest_Contents"></a>

 ** Classification **   <a name="Glue-Type-CreateGrokClassifierRequest-Classification"></a>
An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
Type: String
Required: Yes

 ** GrokPattern **   <a name="Glue-Type-CreateGrokClassifierRequest-GrokPattern"></a>
The grok pattern used by this classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\t]*`
Required: Yes

 ** Name **   <a name="Glue-Type-CreateGrokClassifierRequest-Name"></a>
The name of the new classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CustomPatterns **   <a name="Glue-Type-CreateGrokClassifierRequest-CustomPatterns"></a>
Optional custom grok patterns used by this classifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_CreateGrokClassifierRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateGrokClassifierRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateGrokClassifierRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateGrokClassifierRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
