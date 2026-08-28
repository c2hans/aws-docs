---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_AlgorithmImage.html
---

# AlgorithmImage
<a name="API_AlgorithmImage"></a>

Describes an algorithm image.

## Contents
<a name="API_AlgorithmImage_Contents"></a>

 ** dockerURI **   <a name="personalize-Type-AlgorithmImage-dockerURI"></a>
The URI of the Docker container for the algorithm image.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** name **   <a name="personalize-Type-AlgorithmImage-name"></a>
The name of the algorithm image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
Required: No

## See Also
<a name="API_AlgorithmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/AlgorithmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/AlgorithmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/AlgorithmImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
