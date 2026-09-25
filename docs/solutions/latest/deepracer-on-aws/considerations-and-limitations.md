---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/considerations-and-limitations.html
---

# Considerations and limitations
<a name="considerations-and-limitations"></a>

Consider the following when you use device management.
+ Remote commands, including emergency stop, are not sub-second. Devices are reachable only through an outbound AWS Systems Manager connection, so allow a few seconds for a command to take effect.
+ Activation codes expire 24 hours after they are generated.
+ Each device needs outbound internet access. We recommend wired ethernet for critical devices at venues.
+ The online or offline status of an idle device can lag by up to about 5 minutes. Remote-command results are reported promptly.
+ Supported timer hardware is Raspberry Pi 3B\+ and 4B.
+ A deployment supports up to about 100 registered devices, which covers typical event scale.
+ If a device’s agent has stopped or the device is powered off, the device is unreachable remotely and requires physical intervention.
+ Device management uses serverless resources and the underlying AWS Systems Manager features at effectively no idle cost, well under USD $1.00 per month per deployment when active. It is included by default with no extra deployment steps.
