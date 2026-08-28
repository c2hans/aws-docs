---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_BasicAuthCredentials.html
---

# BasicAuthCredentials
<a name="API_BasicAuthCredentials"></a>

 The basic auth credentials required for basic authentication.

## Contents
<a name="API_BasicAuthCredentials_Contents"></a>

 ** password **   <a name="appflow-Type-BasicAuthCredentials-password"></a>
 The password to use to connect to a resource.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** username **   <a name="appflow-Type-BasicAuthCredentials-username"></a>
 The username to use to connect to a resource.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

## See Also
<a name="API_BasicAuthCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/BasicAuthCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/BasicAuthCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/BasicAuthCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
