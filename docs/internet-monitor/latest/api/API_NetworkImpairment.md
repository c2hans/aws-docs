---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_NetworkImpairment.html
---

# NetworkImpairment
<a name="API_NetworkImpairment"></a>

Information about the network impairment for a specific network measured by Internet Monitor.

## Contents
<a name="API_NetworkImpairment_Contents"></a>

 ** AsPath **   <a name="internetmonitor-Type-NetworkImpairment-AsPath"></a>
The combination of the Autonomous System Number (ASN) of the network and the name of the network.
Type: Array of [Network](API_Network.md) objects
Required: Yes

 ** NetworkEventType **   <a name="internetmonitor-Type-NetworkImpairment-NetworkEventType"></a>
The type of network impairment.
Type: String
Valid Values: `AWS | Internet`
Required: Yes

 ** Networks **   <a name="internetmonitor-Type-NetworkImpairment-Networks"></a>
The networks that could be impacted by a network impairment event.
Type: Array of [Network](API_Network.md) objects
Required: Yes

## See Also
<a name="API_NetworkImpairment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/NetworkImpairment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/NetworkImpairment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/NetworkImpairment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
