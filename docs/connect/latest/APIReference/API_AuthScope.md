---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AuthScope.html
---

# AuthScope
<a name="API_AuthScope"></a>

Contains the scope configuration for an authorization code. Defines the permissions and access boundaries for the session.

## Contents
<a name="API_AuthScope_Contents"></a>

 ** EntityType **   <a name="connect-Type-AuthScope-EntityType"></a>
The type of entity to scope the session to.
Type: String
Valid Values: `CUSTOMER_PROFILE`
Required: Yes

 ** DomainName **   <a name="connect-Type-AuthScope-DomainName"></a>
The name of the Customer Profiles domain to scope the session to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** EntityId **   <a name="connect-Type-AuthScope-EntityId"></a>
The identifier of the entity to scope the session to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** SecurityProfileIds **   <a name="connect-Type-AuthScope-SecurityProfileIds"></a>
The list of security profile identifiers to scope the session to. Maximum of 10 security profiles.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AuthScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AuthScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AuthScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AuthScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
