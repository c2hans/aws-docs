---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-cloudwatch.html
---

# Amazon CloudWatch metrics for AWS Client VPN
<a name="monitoring-cloudwatch"></a>

AWS Client VPN publishes the following metrics to Amazon CloudWatch for your Client VPN endpoints. Metrics are published to Amazon CloudWatch every five minutes.

| Metric | Description |
| --- | --- |
| ActiveConnectionsCount | The number of active connections to the Client VPN endpoint.<br />Units: Count |
| AuthenticationFailures | The number of authentication failures for the Client VPN endpoint.<br />Units: Count |
| CrlDaysToExpiry | The number of days until the Certificate Revocation List (CRL) which is configured on the Client VPN endpoint expires.<br />Units: Days |
| EgressBytes | The number of bytes sent from the Client VPN endpoint.<br />Units: Bytes |
| EgressPackets | The number of packets sent from the Client VPN endpoint.<br />Units: Count |
| IdpCertDaysToExpiry | The number of days until the identity provider (IdP) certificate which is configured on the Client VPN endpoint expires. This metric is only reported for endpoints configured with SAML-based federated authentication.<br />Units: Days |
| IngressBytes | The number of bytes received by the Client VPN endpoint.<br />Units: Bytes |
| IngressPackets | The number of packets received by the Client VPN endpoint.<br />Units: Count |
| SelfServicePortalClientConfigurationDownloads | The number of downloads of the Client VPN endpoint configuration file from the self-service portal.<br />Unit: Count |

AWS Client VPN publishes the following authorization metrics for your Client VPN endpoints. These cover two separate authorization mechanisms. The [custom connection authorization](connection-authorization.md#connection-authorization-posture-assessment) metrics (prefixed `ClientConnectHandler`) apply to the Lambda-based client connect handler. The authorization policy metrics (prefixed `AuthorizationPolicy`) apply to Cedar-based authorization policies. The two sets of metrics are reported independently.

| Metric | Description |
| --- | --- |
| ClientConnectHandlerTimeouts | The number of timeouts on invoking the client connect handler for connections to the Client VPN endpoint.Units: Count |
| ClientConnectHandlerInvalidResponses | The number of invalid responses returned by the client connect handler for connections to the Client VPN endpoint.<br />Units: Count |
| ClientConnectHandlerOtherExecutionErrors | The number of unexpected errors while running the client connect handler for connections to the Client VPN endpoint.<br />Units: Count |
| ClientConnectHandlerThrottlingErrors | The number of throttling errors on invoking the client connect handler for connections to the Client VPN endpoint.<br />Units: Count |
| ClientConnectHandlerDeniedConnections | The number of connections denied by the client connect handler for connections to the Client VPN endpoint.<br />Units: Count |
| ClientConnectHandlerFailedServiceErrors | The number of service side errors while running the client connect handler for connections to the Client VPN endpoint.<br />Units: Count |
| AuthorizationPolicyDeniedConnections | The number of connections denied by the authorization policy for the Client VPN endpoint.<br />Units: Count |
| AuthorizationPolicyEvaluationCount | The number of authorization policy evaluations performed for the Client VPN endpoint.<br />Units: Count |
| AuthorizationPolicyTerminatedConnections | The number of sessions terminated by a periodic re-evaluation of the authorization policy for the Client VPN endpoint.<br />Units: Count |

You can filter the metrics for your Client VPN endpoint by endpoint.

CloudWatch enables you to retrieve statistics about those data points as an ordered set of time series data, known as metrics. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. Each data point has an associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [View CloudWatch metrics](viewing-metrics.md)
