---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadAPIKeyConnectionMetadata.html
---

# ReadAPIKeyConnectionMetadata
<a name="API_ReadAPIKeyConnectionMetadata"></a>

Read-only authentication metadata for API key-based connections, containing non-sensitive configuration details.

## Contents
<a name="API_ReadAPIKeyConnectionMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BaseEndpoint **   <a name="QS-Type-ReadAPIKeyConnectionMetadata-BaseEndpoint"></a>
The base endpoint URL for API key authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

 ** Email **   <a name="QS-Type-ReadAPIKeyConnectionMetadata-Email"></a>
The email address associated with the API key authentication.
Type: String
Pattern: `[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`
Required: No

## See Also
<a name="API_ReadAPIKeyConnectionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadAPIKeyConnectionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadAPIKeyConnectionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadAPIKeyConnectionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
