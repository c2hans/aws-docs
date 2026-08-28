---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ExtractedParameter.html
---

# ExtractedParameter
<a name="API_ExtractedParameter"></a>

Parameter extraction configuration that defines how to extract and map values from API responses to request parameters.

## Contents
<a name="API_ExtractedParameter_Contents"></a>

 ** DefaultValue **   <a name="Glue-Type-ExtractedParameter-DefaultValue"></a>
The default value to use if the parameter cannot be extracted from the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*[^<>&'"].*`
Required: No

 ** Key **   <a name="Glue-Type-ExtractedParameter-Key"></a>
The parameter key name that will be used in subsequent requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** PropertyLocation **   <a name="Glue-Type-ExtractedParameter-PropertyLocation"></a>
Specifies where this extracted parameter should be placed in subsequent requests, such as in headers, query parameters, or request body.
Type: String
Valid Values: `HEADER | BODY | QUERY_PARAM | PATH`
Required: No

 ** Value **   <a name="Glue-Type-ExtractedParameter-Value"></a>
The JSON path or extraction mapping that defines how to extract the parameter value from API responses.
Type: [ResponseExtractionMapping](API_ResponseExtractionMapping.md) object
Required: No

## See Also
<a name="API_ExtractedParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ExtractedParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ExtractedParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ExtractedParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
