---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUnameErrorResponseItem.html
---

# BatchUnameErrorResponseItem
<a name="API_BatchUnameErrorResponseItem"></a>

Contains error information for a username hash lookup that failed in a batch uname lookup request.

## Contents
<a name="API_BatchUnameErrorResponseItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** uname **   <a name="wickr-Type-BatchUnameErrorResponseItem-uname"></a>
The username hash that failed to be looked up.
Type: String
Required: Yes

 ** field **   <a name="wickr-Type-BatchUnameErrorResponseItem-field"></a>
The field that caused the error.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** reason **   <a name="wickr-Type-BatchUnameErrorResponseItem-reason"></a>
A description of why the username hash lookup failed.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_BatchUnameErrorResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchUnameErrorResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchUnameErrorResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchUnameErrorResponseItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
