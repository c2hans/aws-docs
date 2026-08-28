---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PropagateTags.html
---

# PropagateTags
<a name="API_PropagateTags"></a>

Configuration for tag propagation to managed resources launched by the capacity provider.

## Contents
<a name="API_PropagateTags_Contents"></a>

 ** ExplicitTags **   <a name="lambda-Type-PropagateTags-ExplicitTags"></a>
A list of tags to apply to managed resources when `Mode` is set to `Explicit`. You can specify up to 40 tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** Mode **   <a name="lambda-Type-PropagateTags-Mode"></a>
The tag propagation mode. Set to `Explicit` to propagate the tags specified in `ExplicitTags` to managed resources. Set to `None` to disable tag propagation.
Type: String
Valid Values: `None | Explicit`
Required: No

## See Also
<a name="API_PropagateTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PropagateTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PropagateTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PropagateTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
