---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterfaceTestHistory.html
---

# VirtualInterfaceTestHistory
<a name="API_VirtualInterfaceTestHistory"></a>

Information about the virtual interface failover test.

## Contents
<a name="API_VirtualInterfaceTestHistory_Contents"></a>

 ** bgpPeers **   <a name="DX-Type-VirtualInterfaceTestHistory-bgpPeers"></a>
The BGP peers that were put in the DOWN state as part of the virtual interface failover test.
Type: Array of strings
Required: No

 ** endTime **   <a name="DX-Type-VirtualInterfaceTestHistory-endTime"></a>
The time that the virtual interface moves out of the DOWN state.
Type: Timestamp
Required: No

 ** ownerAccount **   <a name="DX-Type-VirtualInterfaceTestHistory-ownerAccount"></a>
The owner ID of the tested virtual interface.
Type: String
Required: No

 ** startTime **   <a name="DX-Type-VirtualInterfaceTestHistory-startTime"></a>
The time that the virtual interface moves to the DOWN state.
Type: Timestamp
Required: No

 ** status **   <a name="DX-Type-VirtualInterfaceTestHistory-status"></a>
The status of the virtual interface failover test.
Type: String
Required: No

 ** testDurationInMinutes **   <a name="DX-Type-VirtualInterfaceTestHistory-testDurationInMinutes"></a>
The time that the virtual interface failover test ran in minutes.
Type: Integer
Required: No

 ** testId **   <a name="DX-Type-VirtualInterfaceTestHistory-testId"></a>
The ID of the virtual interface failover test.
Type: String
Required: No

 ** virtualInterfaceId **   <a name="DX-Type-VirtualInterfaceTestHistory-virtualInterfaceId"></a>
The ID of the tested virtual interface.
Type: String
Required: No

## See Also
<a name="API_VirtualInterfaceTestHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/VirtualInterfaceTestHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/VirtualInterfaceTestHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/VirtualInterfaceTestHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
