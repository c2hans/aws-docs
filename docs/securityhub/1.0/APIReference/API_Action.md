---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

Provides details about one of the following actions that affects or that was taken on a resource:
+ A remote IP address issued an AWS API call
+ A DNS request was received
+ A remote IP address attempted to connect to an EC2 instance
+ A remote IP address attempted a port probe on an EC2 instance

## Contents
<a name="API_Action_Contents"></a>

 ** ActionType **   <a name="securityhub-Type-Action-ActionType"></a>
The type of action that was detected. The possible action types are:
+  `NETWORK_CONNECTION`
+  `AWS_API_CALL`
+  `DNS_REQUEST`
+  `PORT_PROBE`
Type: String
Pattern: `.*\S.*`
Required: No

 ** AwsApiCallAction **   <a name="securityhub-Type-Action-AwsApiCallAction"></a>
Included if `ActionType` is `AWS_API_CALL`. Provides details about the API call that was detected.
Type: [AwsApiCallAction](API_AwsApiCallAction.md) object
Required: No

 ** DnsRequestAction **   <a name="securityhub-Type-Action-DnsRequestAction"></a>
Included if `ActionType` is `DNS_REQUEST`. Provides details about the DNS request that was detected.
Type: [DnsRequestAction](API_DnsRequestAction.md) object
Required: No

 ** NetworkConnectionAction **   <a name="securityhub-Type-Action-NetworkConnectionAction"></a>
Included if `ActionType` is `NETWORK_CONNECTION`. Provides details about the network connection that was detected.
Type: [NetworkConnectionAction](API_NetworkConnectionAction.md) object
Required: No

 ** PortProbeAction **   <a name="securityhub-Type-Action-PortProbeAction"></a>
Included if `ActionType` is `PORT_PROBE`. Provides details about the port probe that was detected.
Type: [PortProbeAction](API_PortProbeAction.md) object
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Action)
