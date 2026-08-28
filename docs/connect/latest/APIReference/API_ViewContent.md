---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ViewContent.html
---

# ViewContent
<a name="API_ViewContent"></a>

View content containing all content necessary to render a view except for runtime input data.

## Contents
<a name="API_ViewContent_Contents"></a>

 ** Actions **   <a name="connect-Type-ViewContent-Actions"></a>
A list of possible actions from the view.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: No

 ** InputSchema **   <a name="connect-Type-ViewContent-InputSchema"></a>
The data schema matching data that the view template must be provided to render.
Type: String
Required: No

 ** Template **   <a name="connect-Type-ViewContent-Template"></a>
The view template representing the structure of the view.
Type: String
Required: No

## See Also
<a name="API_ViewContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ViewContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ViewContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ViewContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
