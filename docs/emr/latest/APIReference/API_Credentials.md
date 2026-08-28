---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_Credentials.html
---

# Credentials
<a name="API_Credentials"></a>

The credentials that you can use to connect to cluster endpoints. Credentials consist of a username and a password.

## Contents
<a name="API_Credentials_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** UsernamePassword **   <a name="EMR-Type-Credentials-UsernamePassword"></a>
The username and password that you use to connect to cluster endpoints.
Type: [UsernamePassword](API_UsernamePassword.md) object
Required: No

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
