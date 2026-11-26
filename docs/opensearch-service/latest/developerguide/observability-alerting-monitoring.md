---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-alerting-monitoring.html
---

# Alerting and monitoring

Proactively monitor your data in Amazon OpenSearch Service with alerting and anomaly detection. With alerting, you create monitors that watch your data on a schedule and notify you when conditions are met. Anomaly detection uses machine learning to automatically detect any outliers in your streaming data. You can pair anomaly detection with alerting to ensure you're notified as soon as an anomaly is detected. You work with these features in the Observability workspace in OpenSearch UI.

This section covers the following features:
+ **Notifications** – Configure notification channels and actions to deliver your alerts.
+ **Anomaly detection** – Automatically detect anomalies in your OpenSearch data in near-real time, and pair anomaly detection with alerting to be notified as soon as an anomaly is detected.
+ **Classic alerting with monitors** – Create monitors that query your data on a schedule, evaluate triggers, and send notifications through channels.
+ **Configuring alerting permissions** – Set up the IAM roles, data source access, and domain or collection permissions that alerting requires.
+ **Alerting** – Configure alerts on an Amazon OpenSearch Service domain to get notified when data from one or more indexes meets certain conditions.

**Topics**
+ [Notifications](observability-alerting-notifications.md)
+ [Anomaly detection in Amazon OpenSearch Service](ad.md)
+ [Classic alerting with monitors](observability-alerting-monitors.md)
+ [Configuring alerting permissions](observability-alerting-permissions.md)
+ [Configuring alerts in Amazon OpenSearch Service](alerting.md)
