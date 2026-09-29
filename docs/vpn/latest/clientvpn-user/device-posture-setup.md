---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/device-posture-setup.html
---

# Setting up a device trust provider
<a name="device-posture-setup"></a>

If your administrator has enabled device posture on a Client VPN endpoint, your device must have a supported device trust provider configured. The device trust provider makes a device posture token available on your device, which the AWS provided client reads when you connect.

This page describes the prerequisites for device posture and how to set up each supported provider on your device.

## Prerequisites
<a name="device-posture-setup-prerequisites"></a>

Before you set up a device trust provider, make sure you have the following.
+ The AWS provided client, version 6.2.0 or later.
+ An administrator who has enabled device posture on the Client VPN endpoint that you connect to.
+ A client configuration (`.ovpn`) file that contains the device posture directive. Your administrator provides this file.

## CrowdStrike
<a name="device-posture-setup-crowdstrike"></a>

Supported platforms
macOS, Windows

Install the CrowdStrike Falcon sensor on your device. Your organization's IT administrator typically deploys this.

For more information, see [CrowdStrike Zero Trust Assessment](https://developer.crowdstrike.com/falcon-mcp/modules/zero-trust-assessment/) on the provider's website.

## Jamf
<a name="device-posture-setup-jamf"></a>

Supported platforms
macOS

Minimum agent version
Jamf Trust 2.26.0

Enroll your macOS device in Jamf Pro. Your organization's IT administrator typically handles enrollment.

For more information, see [Jamf Trusted Access](https://trusted.jamf.com/docs/enabling-access-for-trusted-devices) on the provider's website.

## JumpCloud
<a name="device-posture-setup-jumpcloud"></a>

Supported platforms
macOS, Windows, Ubuntu

Minimum agent version
JumpCloud Agent 2.144.3

Install the JumpCloud agent on your device. Your organization's IT administrator typically deploys this.

For more information, see [JumpCloud Device Trust](https://www.jumpcloud.com/support/understand-device-trust-readiness) on the provider's website.

## What to expect when connecting
<a name="device-posture-setup-connecting"></a>

When you connect to a Client VPN endpoint that has device posture enabled, the AWS provided client reads the device posture token from your device trust provider and sends it to Client VPN for evaluation. If your device meets the requirements in your administrator's authorization policy, the connection proceeds normally.

If your device does not meet the requirements, Client VPN rejects the connection and the AWS provided client displays the message `Authorization policy evaluation failed`. If you see this message, contact your administrator.
