---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadClientCredentialsGrantDetails.html
---

# ReadClientCredentialsGrantDetails
<a name="API_ReadClientCredentialsGrantDetails"></a>

Read-only configuration details for OAuth2 client credentials grant flow, including client ID and token endpoint.

## Contents
<a name="API_ReadClientCredentialsGrantDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-ReadClientCredentialsGrantDetails-ClientId"></a>
The client identifier for the OAuth2 client credentials grant flow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** TokenEndpoint **   <a name="QS-Type-ReadClientCredentialsGrantDetails-TokenEndpoint"></a>
The authorization server endpoint used to obtain access tokens via the client credentials grant flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `https://.*`
Required: Yes

## See Also
<a name="API_ReadClientCredentialsGrantDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadClientCredentialsGrantDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadClientCredentialsGrantDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadClientCredentialsGrantDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
