---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Session.html
---

# Session
<a name="API_Session"></a>

Describes a web-based, remote graphical user interface (GUI), Amazon DCV session. The session is used to access a virtual computer’s operating system or application.

## Contents
<a name="API_Session_Contents"></a>

 ** isPrimary **   <a name="Lightsail-Type-Session-isPrimary"></a>
When true, this Boolean value indicates the primary session for the specified resource.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-Session-name"></a>
The session name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** url **   <a name="Lightsail-Type-Session-url"></a>
The session URL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Session)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
