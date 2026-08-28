---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-memcached.html
---

# Set up memcached with a metric exporter on Amazon EKS and Kubernetes
<a name="ContainerInsights-Prometheus-Sample-Workloads-memcached"></a>

memcached is an open-source memory object caching system. For more information, see [What is Memcached?](https://www.memcached.org).

If you are running memcached on a cluster with the Fargate launch type, you need to set up a Fargate profile before doing the steps in this procedure. To set up the profile, enter the following command. Replace {{MyCluster}} with the name of your cluster.

```
eksctl create fargateprofile --cluster {{MyCluster}} \
--namespace memcached-sample --name memcached-sample
```

**To install memcached with a metric exporter to test Container Insights Prometheus support**

1. Enter the following command to add the repo:

   ```
   helm repo add bitnami https://charts.bitnami.com/bitnami
   ```

1. Enter the following command to create a new namespace:

   ```
   kubectl create namespace memcached-sample
   ```

1. Enter the following command to install Memcached

   ```
   helm install my-memcached bitnami/memcached --namespace memcached-sample \
   --set metrics.enabled=true \
   --set-string serviceAnnotations.prometheus\\.io/port="9150" \
   --set-string serviceAnnotations.prometheus\\.io/scrape="true"
   ```

1. Enter the following command to confirm the annotation of the running service:

   ```
   kubectl describe service my-memcached-metrics -n memcached-sample
   ```

   You should see the following two annotations:

   ```
   Annotations:   prometheus.io/port: 9150
                  prometheus.io/scrape: true
   ```

**To uninstall memcached**
+ Enter the following commands:

  ```
  helm uninstall my-memcached --namespace memcached-sample
  kubectl delete namespace memcached-sample
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
