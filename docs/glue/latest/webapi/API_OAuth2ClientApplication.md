---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OAuth2ClientApplication.html
---

# OAuth2ClientApplication
<a name="API_OAuth2ClientApplication"></a>

The OAuth2 client app used for the connection.

## Contents
<a name="API_OAuth2ClientApplication_Contents"></a>

 ** AWSManagedClientApplicationReference **   <a name="Glue-Type-OAuth2ClientApplication-AWSManagedClientApplicationReference"></a>
The reference to the SaaS-side client app that is AWS managed.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** UserManagedClientApplicationClientId **   <a name="Glue-Type-OAuth2ClientApplication-UserManagedClientApplicationClientId"></a>
The client application clientID if the ClientAppType is `USER_MANAGED`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## See Also
<a name="API_OAuth2ClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OAuth2ClientApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OAuth2ClientApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OAuth2ClientApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
