---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/monitoring-view-metrics.html
---

# View proxy metrics

View the metrics for a proxy using the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

The **Monitoring** tab on the proxy details page shows graphs of the proxy metrics. You can also view the same metrics in the CloudWatch console.

**To view metrics for a proxy**

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

1. In the navigation pane, choose **Proxies**.

1. Choose the name of the proxy to open its details page.

1. Choose the **Monitoring** tab to view the metric graphs.

------
#### [ AWS CLI ]

To retrieve metric data for a proxy, run the **get-metric-statistics** command for CloudWatch. Filter the data with the `LoadBalancer` dimension, using the ARN of your proxy as the value.

Fragment:

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/ProxyELB \
    --metric-name RequestCount \
    --dimensions Name=LoadBalancer,Value=<proxy-arn> \
    --start-time <start-time> \
    --end-time <end-time> \
    --period 60 \
    --statistics Sum
```

Replace {{proxy-arn}} with the ARN of your proxy. Replace {{start-time}} and {{end-time}} with the start and end of the time range that you want.

------
