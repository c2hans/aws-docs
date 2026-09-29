---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/connection-logging.html
---

# Connection logging for an AWS Client VPN endpoint
<a name="connection-logging"></a>

Connection logging is a feature of AWS Client VPN that enables you to capture *connection logs* for your Client VPN endpoint.

A connection log contains *connection log entries* that capture information about connection events, such as when a client (end user) connects, attempts to connect, or disconnects from your Client VPN endpoint. You can use this information to run forensics, analyze how your Client VPN endpoint is being used, or debug connection issues.

Connection logging is available in all Regions where AWS Client VPN is available. Connection logs are published to a CloudWatch Logs log group in your account.

**Note**
Failed mutual authentication attempts are not logged.

## Connection log entries
<a name="connection-log-entries"></a>

A connection log entry is a JSON-formatted blob of key-value pairs. The following is an example connection log entry.

```
{
    "connection-log-type": "connection-attempt",
    "connection-attempt-status": "successful",
    "connection-reset-status": "NA",
    "connection-attempt-failure-reason": "NA",
    "connection-id": "cvpn-connection-abc123abc123abc12",
    "client-vpn-endpoint-id": "cvpn-endpoint-aaa111bbb222ccc33",
    "transport-protocol": "udp",
    "connection-start-time": "2020-03-26 20:37:15",
    "connection-last-update-time": "2020-03-26 20:37:15",
    "client-ip": "10.0.1.2",
    "common-name": "client1",
    "device-type": "mac",
    "device-ip": "98.247.202.82",
    "port": "50096",
    "ingress-bytes": "0",
    "egress-bytes": "0",
    "ingress-packets": "0",
    "egress-packets": "0",
    "connection-end-time": "NA",
    "username": "joe"
    }
```

A connection log entry contains the following keys:
+ `connection-log-type` — The type of connection log entry (`connection-attempt` or `connection-reset`).
+ `connection-attempt-status` — The status of the connection request (`successful`, `failed`, `waiting-for-assertion`, or `NA`).
+ `connection-reset-status` — The status of a connection reset event (`NA` or `assertion-received`).
+ `connection-attempt-failure-reason` — The reason for the connection failure, if applicable. When the authorization policy denies a connection, the value is `authorization-policy-deny`.
+ `connection-id` — The ID of the connection.
+ `client-vpn-endpoint-id` — The ID of the Client VPN endpoint to which the connection was made.
+ `transport-protocol` — The transport protocol that was used for the connection.
+ `connection-start-time` — The start time of the connection.
+ `connection-last-update-time` — The last update time of the connection. This value is periodically updated in the logs.
+ `client-ip` — The IP address of the client, which is allocated from the client IPv4 CIDR range for the Client VPN endpoint.
+ `common-name` — The common name of the certificate that's used for certificate-based authentication.
+ `device-type` — The type of device used for the connection by the end user.
+ `device-ip` — The public IP address of the device.
+ `port` — The port number for the connection.
+ `ingress-bytes` — The number of ingress (inbound) bytes for the connection. This value is periodically updated in the logs.
+ `egress-bytes` — The number of egress (outbound) bytes for the connection. This value is periodically updated in the logs.
+ `ingress-packets` — The number of ingress (inbound) packets for the connection. This value is periodically updated in the logs.
+ `egress-packets` — The number of egress (outbound) packets for the connection. This value is periodically updated in the logs.
+ `connection-end-time` — The end time of the connection. The value is `NA` if the connection is still in progress or if the connection attempt failed.
+ `posture-compliance-statuses` — The compliance statuses returned by the [client connect handler](connection-authorization.md) for [custom connection authorization](connection-authorization.md#connection-authorization-posture-assessment), if applicable.
+ `authorization-policy-evaluation` — The result of evaluating the authorization policy, if an authorization policy is configured. This value contains the following subfields:
  + `result` — The authorization decision (`permit`, `deny`, or `error`). An `error` result can occur when a Cedar policy references an attribute that is absent from the connection context, among other reasons. For example, the client doesn't provide a device token and the policy references that provider's context. An error can also occur when the policy references a SAML or AD attribute that isn't present for the user. When shadow mode is `disabled`, Client VPN denies the connection.
  + `evaluation-type` — The type of evaluation (`connection-attempt` or `periodic`). A `connection-attempt` evaluation occurs when the client connects. A `periodic` evaluation occurs during a re-evaluation of an active session.
  + `shadow-mode` — A string that indicates the shadow mode setting (`enabled` or `disabled`). When `enabled`, Client VPN evaluates the policy without enforcing the decision. When `disabled`, Client VPN enforces `deny` and `error` decisions.
  + `reason` — The reason for the authorization decision. This field is present only for `deny` and `error` results. The current emitted value is `policy-deny`.
  + `device-token-status` — An object that contains the device token status for each device trust provider. Each provider entry contains a `status` subfield (`validated` or `failed`). If the status is `failed`, the entry also includes a `reason` subfield that describes the failure.
  + `context` — The full authorization policy evaluation context. This subfield is included only when `IncludeAuthorizationPolicyContext` is enabled.
+ `username` — The username is recorded when user-based authentication (AD or SAML) is used for the endpoint.
+ `connection-duration-seconds` — The duration of a connection in seconds. Equal to the difference between "connection-start-time" and "connection-end-time".

For more information about enabling connection logging, see [AWS Client VPN connection logs](cvpn-working-with-connection-logs.md).

When you enable connection logging for a new or existing endpoint, you can set `IncludeAuthorizationPolicyContext` to include the full authorization policy evaluation context in your connection log entries. For more information, see [Connection logging options](#connection-log-options).

## Device token status failure reasons
<a name="device-token-status-failure-reasons"></a>

When the `status` of a `device-token-status` provider entry is `failed`, the entry includes a `reason` subfield. The `reason` subfield can have one of the following values.
+ `token-expired`
+ `signature-invalid`
+ `token-malformed`
+ `tenant-mismatch`
+ `key-resolution-failed`
+ `network-error`
+ `internal-error`

## Connection logging options
<a name="connection-log-options"></a>

You can configure the following option to control the content of your connection logs:
+ `IncludeAuthorizationPolicyContext` — When `true`, connection log entries include the full authorization policy evaluation context. The default is `false`.

## Authorization policy connection log examples
<a name="connection-log-examples-device-posture"></a>

When an authorization policy is configured, connection log entries record the authorization decision. The following example shows a successful connection that was permitted by the authorization policy.

```
{
  "connection-log-type": "connection-attempt",
  "connection-attempt-status": "successful",
  "connection-attempt-failure-reason": "NA",
  "connection-id": "cvpn-connection-01f248f0e3084e4f2",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "2026-09-24 22:22:25",
  "connection-last-update-time": "2026-09-24 22:22:25",
  "client-ip": "172.1.0.162",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "5567",
  "ingress-bytes": "0",
  "egress-bytes": "0",
  "ingress-packets": "0",
  "egress-packets": "0",
  "authorization-policy-evaluation": {
    "result": "permit",
    "evaluation-type": "connection-attempt",
    "shadow-mode": "disabled",
    "device-token-status": {
      "crowdstrike": {
        "status": "validated"
      }
    }
  },
  "connection-end-time": "NA",
  "connection-duration-seconds": "0"
}
```

The following example shows a connection that was denied by the authorization policy.

```
{
  "connection-log-type": "connection-attempt",
  "connection-attempt-status": "failed",
  "connection-attempt-failure-reason": "authorization-policy-deny",
  "connection-id": "cvpn-connection-0a39f1b3b7082abbb",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "NA",
  "connection-last-update-time": "2026-09-25 17:14:11",
  "client-ip": "NA",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "28081",
  "ingress-bytes": "0",
  "egress-bytes": "0",
  "ingress-packets": "0",
  "egress-packets": "0",
  "authorization-policy-evaluation": {
    "result": "error",
    "evaluation-type": "connection-attempt",
    "shadow-mode": "disabled",
    "reason": "policy-deny",
    "device-token-status": {
      "crowdstrike": {
        "status": "failed",
        "reason": "token-malformed"
      }
    }
  },
  "connection-end-time": "NA",
  "connection-duration-seconds": "NA"
}
```

The following example shows a session that was terminated when a periodic re-evaluation of the authorization policy no longer met the requirements.

```
{
  "connection-log-type": "connection-reset",
  "connection-attempt-status": "NA",
  "connection-attempt-failure-reason": "NA",
  "connection-id": "cvpn-connection-01f248f0e3084e4f2",
  "client-vpn-endpoint-id": "cvpn-endpoint-0f2d58d4869ece501",
  "transport-protocol": "udp",
  "connection-start-time": "2026-09-24 22:22:25",
  "connection-last-update-time": "2026-09-24 22:27:43",
  "client-ip": "172.1.0.162",
  "client-ip-v6": "NA",
  "common-name": "client1.domain.tld",
  "device-type": "linux",
  "device-ip": "72.21.198.66",
  "port": "5567",
  "ingress-bytes": "21017",
  "egress-bytes": "16438",
  "ingress-packets": "330",
  "egress-packets": "325",
  "authorization-policy-evaluation": {
    "result": "deny",
    "evaluation-type": "periodic",
    "shadow-mode": "disabled",
    "reason": "policy-deny",
    "device-token-status": {
      "crowdstrike": {
        "status": "validated"
      }
    }
  },
  "connection-end-time": "2026-09-24 22:27:43",
  "connection-reset-status": "NA",
  "connection-duration-seconds": "318"
}
```
