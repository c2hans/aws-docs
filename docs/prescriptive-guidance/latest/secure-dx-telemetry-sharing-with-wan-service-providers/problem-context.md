---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/problem-context.html
---

# Problem Context

A typical Direct Connect deployment involves three parties: the customer (account owner), the WSP (transport and colocation), and AWS (Direct Connect service). Each party has visibility into a different segment of the connection. None has a complete end-to-end view. When an issue occurs, troubleshooting requires manual information exchange across all three parties.

This coordination introduces measurable delays. When a connection experiences degraded optical light levels at 2:00 AM, the customer's on-call engineer must log in, review CloudWatch metrics, identify the affected connection, determine which WSP manages it, locate the correct contact, and share connection details via email or phone. Only then can the WSP begin transport-side diagnosis. This process typically consumes 30 to 60 minutes before the WSP can act.

With this framework, the WSP's monitoring system detects the degradation independently, queries connection configuration and metrics via the assumed role, retrieves the customer NOC contact from resource tags, and begins diagnosis within minutes — without waiting for the customer to initiate contact.
