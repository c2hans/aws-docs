---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_NameServersUpdateState.html
---

# NameServersUpdateState
<a name="API_NameServersUpdateState"></a>

Describes the state of the name server records update made by Amazon Lightsail to an Amazon Route 53 registered domain.

For more information, see [DNS in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-dns-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_NameServersUpdateState_Contents"></a>

 ** code **   <a name="Lightsail-Type-NameServersUpdateState-code"></a>
The status code for the name servers update.
Following are the possible values:
+  `SUCCEEDED` - The name server records were successfully updated.
+  `PENDING` - The name server record update is in progress.
+  `FAILED` - The name server record update failed.
+  `STARTED` - The automatic name server record update started.
Type: String
Valid Values: `SUCCEEDED | PENDING | FAILED | STARTED`
Required: No

 ** message **   <a name="Lightsail-Type-NameServersUpdateState-message"></a>
The message that describes the reason for the status code.
Type: String
Required: No

## See Also
<a name="API_NameServersUpdateState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/NameServersUpdateState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/NameServersUpdateState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/NameServersUpdateState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
