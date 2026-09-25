---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/device-management.html
---

# Device management
<a name="device-management"></a>

Remotely onboard, monitor, and control the physical AWS DeepRacer cars and timers used at your events.

With device management, event administrators and race facilitators can remotely onboard, monitor, and control the physical hardware used at AWS DeepRacer events. You manage AWS DeepRacer cars and Raspberry Pi timing strips directly from the AWS DeepRacer on AWS console, without physically handling each device.

Devices are managed through AWS Systems Manager. Each device runs a lightweight agent that connects outbound only, so no inbound ports are required. As a result, device management works behind the network address translation (NAT) and restrictive Wi-Fi that are common at event venues.

Device management is included by default and has near-zero cost when idle.

Device management is intended for administrators and race facilitators who run physical events. Racers do not have device access. For more information about roles, see [Types of users](types-of-users.md).

**Note**
Device management is available in AWS DeepRacer on AWS starting with the v1.3.0 release. Existing deployments gain it by updating the solution, through AWS Launch Wizard or a CloudFormation stack update.
