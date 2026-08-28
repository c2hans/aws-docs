---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_Credential.html
---

# Credential
<a name="API_Credential"></a>

Contains credential information for an application.

## Contents
<a name="API_Credential_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** apiKeyCredential **   <a name="appfabric-Type-Credential-apiKeyCredential"></a>
Contains API key credential information.
Type: [ApiKeyCredential](API_ApiKeyCredential.md) object
Required: No

 ** oauth2Credential **   <a name="appfabric-Type-Credential-oauth2Credential"></a>
Contains OAuth2 client credential information.
Type: [Oauth2Credential](API_Oauth2Credential.md) object
Required: No

## See Also
<a name="API_Credential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/Credential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/Credential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/Credential)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
