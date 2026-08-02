---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/faq.html
---

# FAQ
<a name="faq"></a>

## How can I monitor hardware metrics from bare-metal servers located in on-premises data centers or other cloud providers?
<a name="faq1"></a>

[Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) are AWS services. However, you can install and configure Telegraf on bare-metal servers that are located anywhere, including in on-premises data centers or other cloud providers. You can configure Telegraf to send metrics to Amazon Managed Service for Prometheus over the internet or through a secure virtual private network (VPN) connection.

## How can I correlate hardware metrics with application-level metrics in Grafana dashboards?
<a name="faq2"></a>

In addition to the hardware metrics that the Redfish plugin collects, Telegraf can collect application-level metrics by using various other input plugins, such as Prometheus, StatsD, NGINX, or MySQL plugins. By sending all of these metrics to Amazon Managed Service for Prometheus, you can create dashboards in Amazon Managed Grafana that correlate hardware metrics with application-level metrics. This can provide a comprehensive view of your system's performance.

## Can I use Telegraf to monitor hardware metrics from non-Redfish compliant systems?
<a name="faq3"></a>

Although the Redfish input plugin is designed for Redfish-enabled systems, Telegraf supports various other input plugins that can collect hardware metrics from different sources. For example, the [IPMI Sensor input plugin](https://github.com/influxdata/telegraf/blob/release-1.32/plugins/inputs/ipmi_sensor/README.md) can collect metrics from systems that support Intelligent Platform Management Interface (IPMI), and the [Intel Powerstat input plugin](https://github.com/influxdata/telegraf/blob/release-1.32/plugins/inputs/ipmi_sensor/README.md) can collect metrics from Intel CPUs.

## How can I monitor and alert on hardware firmware updates or configuration changes?
<a name="faq4"></a>

The [Redfish input plugin](https://github.com/influxdata/telegraf/blob/release-1.32/plugins/inputs/redfish/README.md) for Telegraf can collect metadata about the hardware, including firmware versions and configuration details. In Amazon Managed Service for Prometheus, you can set up alerts to notify you if these metadata fields change. These notifications can help you monitor for firmware updates or configuration changes that might affect system performance or stability.

## Can I use Telegraf to collect hardware metrics from virtualized environments or containers?
<a name="faq5"></a>

Although the Redfish input plugin for Telegraf is primarily designed for bare-metal hardware monitoring, Telegraf supports various other plugins for monitoring virtualized environments and containers, such as [Docker](https://www.docker.com/) or [Kubernetes](https://kubernetes.io/) containers. You can combine the Telegraf plugins to create a comprehensive monitoring solution for hybrid environments.

## How can I integrate hardware monitoring with other AWS services, such as Lambda or Step Functions?
<a name="faq6"></a>

Telegraf supports sending metrics to various AWS services, including [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). You can configure the Telegraf output plugins to send hardware metrics to these services. This allows you to create automated actions or workflows based on hardware events or metric thresholds.

## How can I help secure and protect my hardware monitoring data?
<a name="faq7"></a>

Telegraf supports secure communication protocols, such as TLS and SSL. You can also configure Telegraf to encrypt data in transit and at rest. Amazon Managed Service for Prometheus and Amazon Managed Grafana also provide security features, such as encryption, access control, and auditing. Additionally, you can use [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for key management and use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for auditing.
