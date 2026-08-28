---
source_url: https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-audit-checks.html
---

# Audit checks
<a name="device-defender-audit-checks"></a>

**Note**
When you enable a check, data collection starts immediately. If there is a large amount of data in your account to collect, results of the check might not be available for some time after you enabled it.

The following audit checks are supported:
+ [Intermediate CA revoked for active device certificates check](audit-chk-active-intermediary-device-revoked-CA.md)
+ [Revoked CA certificate still active](audit-chk-revoked-ca-cert.md)
+ [Device certificate shared](audit-chk-device-cert-shared.md)
+ [Device certificate key quality](audit-chk-device-cert-key-quality.md)
+ [CA certificate key quality](audit-chk-ca-cert-key-quality.md)
+ [Unauthenticated Cognito role overly permissive](audit-chk-unauth-cognito-role-permissive.md)
+ [Authenticated Cognito role overly permissive](audit-chk-auth-cognito-role-permissive.md)
+ [AWS IoT policies overly permissive](audit-chk-iot-policy-permissive.md)
+ [AWS IoT policy potentially misconfigured](audit-chk-iot-misconfigured-policies.md)
+ [Role alias overly permissive](audit-chk-iot-role-alias-permissive.md)
+ [Role alias allows access to unused services](audit-chk-role-alias-unused-svcs.md)
+ [CA certificate expiring](audit-chk-ca-cert-approaching-expiration.md)
+ [Conflicting MQTT client IDs](audit-chk-conflicting-client-ids.md)
+ [Device certificate expiring](audit-chk-device-cert-approaching-expiration.md)
+ [Device certificate age check](device-certificate-age-check.md)
+ [Revoked device certificate still active](audit-chk-revoked-device-cert.md)
+ [Logging disabled](audit-chk-logging-disabled.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Device Defender. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-device-defender` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
