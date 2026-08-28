---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_TraceUser.html
---

# TraceUser
<a name="API_TraceUser"></a>

Information about a user recorded in segment documents.

## Contents
<a name="API_TraceUser_Contents"></a>

 ** ServiceIds **   <a name="xray-Type-TraceUser-ServiceIds"></a>
Services that the user's request hit.
Type: Array of [ServiceId](API_ServiceId.md) objects
Required: No

 ** UserName **   <a name="xray-Type-TraceUser-UserName"></a>
The user's name.
Type: String
Required: No

## See Also
<a name="API_TraceUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/TraceUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/TraceUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/TraceUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
