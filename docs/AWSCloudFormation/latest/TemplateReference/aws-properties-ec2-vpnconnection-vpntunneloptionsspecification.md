---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection VpnTunnelOptionsSpecification
<a name="aws-properties-ec2-vpnconnection-vpntunneloptionsspecification"></a>

The tunnel options for a single VPN tunnel.

## Syntax
<a name="aws-properties-ec2-vpnconnection-vpntunneloptionsspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-vpntunneloptionsspecification-syntax.json"></a>

```
{
  "[DPDTimeoutAction](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutaction)" : {{String}},
  "[DPDTimeoutSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutseconds)" : {{Integer}},
  "[EnableTunnelLifecycleControl](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-enabletunnellifecyclecontrol)" : {{Boolean}},
  "[IKEVersions](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-ikeversions)" : {{[ IKEVersionsRequestListValue, ... ]}},
  "[LogOptions](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-logoptions)" : {{VpnTunnelLogOptionsSpecification}},
  "[Phase1DHGroupNumbers](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1dhgroupnumbers)" : {{[ Phase1DHGroupNumbersRequestListValue, ... ]}},
  "[Phase1EncryptionAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1encryptionalgorithms)" : {{[ Phase1EncryptionAlgorithmsRequestListValue, ... ]}},
  "[Phase1IntegrityAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1integrityalgorithms)" : {{[ Phase1IntegrityAlgorithmsRequestListValue, ... ]}},
  "[Phase1LifetimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1lifetimeseconds)" : {{Integer}},
  "[Phase2DHGroupNumbers](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2dhgroupnumbers)" : {{[ Phase2DHGroupNumbersRequestListValue, ... ]}},
  "[Phase2EncryptionAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2encryptionalgorithms)" : {{[ Phase2EncryptionAlgorithmsRequestListValue, ... ]}},
  "[Phase2IntegrityAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2integrityalgorithms)" : {{[ Phase2IntegrityAlgorithmsRequestListValue, ... ]}},
  "[Phase2LifetimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2lifetimeseconds)" : {{Integer}},
  "[PreSharedKey](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-presharedkey)" : {{String}},
  "[RekeyFuzzPercentage](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeyfuzzpercentage)" : {{Integer}},
  "[RekeyMarginTimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeymargintimeseconds)" : {{Integer}},
  "[ReplayWindowSize](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-replaywindowsize)" : {{Integer}},
  "[StartupAction](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-startupaction)" : {{String}},
  "[TunnelInsideCidr](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsidecidr)" : {{String}},
  "[TunnelInsideIpv6Cidr](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsideipv6cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-vpntunneloptionsspecification-syntax.yaml"></a>

```
  [DPDTimeoutAction](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutaction): {{String}}
  [DPDTimeoutSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutseconds): {{Integer}}
  [EnableTunnelLifecycleControl](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-enabletunnellifecyclecontrol): {{Boolean}}
  [IKEVersions](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-ikeversions): {{
    - IKEVersionsRequestListValue}}
  [LogOptions](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-logoptions): {{
    VpnTunnelLogOptionsSpecification}}
  [Phase1DHGroupNumbers](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1dhgroupnumbers): {{
    - Phase1DHGroupNumbersRequestListValue}}
  [Phase1EncryptionAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1encryptionalgorithms): {{
    - Phase1EncryptionAlgorithmsRequestListValue}}
  [Phase1IntegrityAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1integrityalgorithms): {{
    - Phase1IntegrityAlgorithmsRequestListValue}}
  [Phase1LifetimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1lifetimeseconds): {{Integer}}
  [Phase2DHGroupNumbers](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2dhgroupnumbers): {{
    - Phase2DHGroupNumbersRequestListValue}}
  [Phase2EncryptionAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2encryptionalgorithms): {{
    - Phase2EncryptionAlgorithmsRequestListValue}}
  [Phase2IntegrityAlgorithms](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2integrityalgorithms): {{
    - Phase2IntegrityAlgorithmsRequestListValue}}
  [Phase2LifetimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2lifetimeseconds): {{Integer}}
  [PreSharedKey](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-presharedkey): {{String}}
  [RekeyFuzzPercentage](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeyfuzzpercentage): {{Integer}}
  [RekeyMarginTimeSeconds](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeymargintimeseconds): {{Integer}}
  [ReplayWindowSize](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-replaywindowsize): {{Integer}}
  [StartupAction](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-startupaction): {{String}}
  [TunnelInsideCidr](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsidecidr): {{String}}
  [TunnelInsideIpv6Cidr](#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsideipv6cidr): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-vpntunneloptionsspecification-properties"></a>

`DPDTimeoutAction`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutaction"></a>
The action to take after DPD timeout occurs. Specify `restart` to restart the IKE initiation. Specify `clear` to end the IKE session.
Valid Values: `clear` \| `none` \| `restart`
Default: `clear`
*Required*: No
*Type*: String
*Allowed values*: `clear | none | restart`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DPDTimeoutSeconds`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-dpdtimeoutseconds"></a>
The number of seconds after which a DPD timeout occurs.
Constraints: A value greater than or equal to 30.
Default: `30`
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableTunnelLifecycleControl`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-enabletunnellifecyclecontrol"></a>
Turn on or off tunnel endpoint lifecycle control feature.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IKEVersions`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-ikeversions"></a>
The IKE versions that are permitted for the VPN tunnel.
Valid values: `ikev1` \| `ikev2`
*Required*: No
*Type*: Array of [IKEVersionsRequestListValue](aws-properties-ec2-vpnconnection-ikeversionsrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogOptions`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-logoptions"></a>
Options for logging VPN tunnel activity.
*Required*: No
*Type*: [VpnTunnelLogOptionsSpecification](aws-properties-ec2-vpnconnection-vpntunnellogoptionsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase1DHGroupNumbers`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1dhgroupnumbers"></a>
One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `2` \| `14` \| `15` \| `16` \| `17` \| `18` \| `19` \| `20` \| `21` \| `22` \| `23` \| `24`
*Required*: No
*Type*: Array of [Phase1DHGroupNumbersRequestListValue](aws-properties-ec2-vpnconnection-phase1dhgroupnumbersrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase1EncryptionAlgorithms`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1encryptionalgorithms"></a>
One or more encryption algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `AES128` \| `AES256` \| `AES128-GCM-16` \| `AES256-GCM-16`
*Required*: No
*Type*: Array of [Phase1EncryptionAlgorithmsRequestListValue](aws-properties-ec2-vpnconnection-phase1encryptionalgorithmsrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase1IntegrityAlgorithms`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1integrityalgorithms"></a>
One or more integrity algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.
Valid values: `SHA1` \| `SHA2-256` \| `SHA2-384` \| `SHA2-512`
*Required*: No
*Type*: Array of [Phase1IntegrityAlgorithmsRequestListValue](aws-properties-ec2-vpnconnection-phase1integrityalgorithmsrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase1LifetimeSeconds`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase1lifetimeseconds"></a>
The lifetime for phase 1 of the IKE negotiation, in seconds.
Constraints: A value between 900 and 28,800.
Default: `28800`
*Required*: No
*Type*: Integer
*Minimum*: `900`
*Maximum*: `28800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase2DHGroupNumbers`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2dhgroupnumbers"></a>
One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `2` \| `5` \| `14` \| `15` \| `16` \| `17` \| `18` \| `19` \| `20` \| `21` \| `22` \| `23` \| `24`
*Required*: No
*Type*: Array of [Phase2DHGroupNumbersRequestListValue](aws-properties-ec2-vpnconnection-phase2dhgroupnumbersrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase2EncryptionAlgorithms`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2encryptionalgorithms"></a>
One or more encryption algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `AES128` \| `AES256` \| `AES128-GCM-16` \| `AES256-GCM-16`
*Required*: No
*Type*: Array of [Phase2EncryptionAlgorithmsRequestListValue](aws-properties-ec2-vpnconnection-phase2encryptionalgorithmsrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase2IntegrityAlgorithms`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2integrityalgorithms"></a>
One or more integrity algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.
Valid values: `SHA1` \| `SHA2-256` \| `SHA2-384` \| `SHA2-512`
*Required*: No
*Type*: Array of [Phase2IntegrityAlgorithmsRequestListValue](aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phase2LifetimeSeconds`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-phase2lifetimeseconds"></a>
The lifetime for phase 2 of the IKE negotiation, in seconds.
Constraints: A value between 900 and 3,600. The value must be less than the value for `Phase1LifetimeSeconds`.
Default: `3600`
*Required*: No
*Type*: Integer
*Minimum*: `900`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreSharedKey`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-presharedkey"></a>
The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.
Constraints: Allowed characters are alphanumeric characters, periods (.), and underscores (\_). Must be between 8 and 64 characters in length and cannot start with zero (0).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RekeyFuzzPercentage`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeyfuzzpercentage"></a>
The percentage of the rekey window (determined by `RekeyMarginTimeSeconds`) during which the rekey time is randomly selected.
Constraints: A value between 0 and 100.
Default: `100`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RekeyMarginTimeSeconds`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-rekeymargintimeseconds"></a>
The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for `RekeyFuzzPercentage`.
Constraints: A value between 60 and half of `Phase2LifetimeSeconds`.
Default: `270`
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplayWindowSize`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-replaywindowsize"></a>
The number of packets in an IKE replay window.
Constraints: A value between 64 and 2048.
Default: `1024`
*Required*: No
*Type*: Integer
*Minimum*: `64`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartupAction`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-startupaction"></a>
The action to take when the establishing the tunnel for the VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify `start` for AWS to initiate the IKE negotiation.
Valid Values: `add` \| `start`
Default: `add`
*Required*: No
*Type*: String
*Allowed values*: `add | start`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TunnelInsideCidr`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsidecidr"></a>
The range of inside IP addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway.
Constraints: A size /30 CIDR block from the `169.254.0.0/16` range. The following CIDR blocks are reserved and cannot be used:
+  `169.254.0.0/30`
+  `169.254.1.0/30`
+  `169.254.2.0/30`
+  `169.254.3.0/30`
+  `169.254.4.0/30`
+  `169.254.5.0/30`
+  `169.254.169.252/30`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TunnelInsideIpv6Cidr`  <a name="cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsideipv6cidr"></a>
The range of inside IPv6 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same transit gateway.
Constraints: A size /126 CIDR block from the local `fd00::/8` range.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
