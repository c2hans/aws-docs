---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/eks-observability-addon-configure.html
---

# Configuring the add-on and the Helm chart

This page applies to both Enhanced Container Insights (Classic) and OTel Container Insights. The add-on and the Helm chart use the same configuration values. The examples on this page turn on OTel Container Insights and change the gRPC port of the OTLP endpoint.

Settings that only one mode reads are on the pages for that mode. For Enhanced Container Insights (Classic), including its Fluent Bit log pipeline, see [(Optional) Configuring Enhanced Container Insights (Classic) and Fluent Bit](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration). For OTel Container Insights, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).

## Configuring the Amazon EKS add-on
<a name="eks-observability-addon-configure-addon"></a>

Pass the configuration values as JSON in the `--configuration-values` option of the `aws eks update-addon` command.

**Important**
`--configuration-values` replaces the whole add-on configuration. Any value that you leave out returns to its default. To keep your current settings, merge your change into the current configuration, as in the following procedure. The `--resolve-conflicts` option doesn't change this. It only decides what happens to fields of add-on resources that someone changed on the cluster outside of Amazon EKS.

**To change the add-on configuration**

1. Save the current configuration values to a file. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```bash
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query addon.configurationValues \
     --output text > config.json
   ```

   If the add-on has no configuration values, the file contains `None`. Replace it with `{}`.

1. Merge your change into `config.json`. The examples in this guide are fragments to merge, not complete configurations. For example, merge the following fragment to turn on OTel Container Insights and change the gRPC port of the OTLP endpoint.

   ```json
   {
     "otelContainerInsights": { "enabled": true },
     "otlp": { "grpc": { "port": 14317 } }
   }
   ```

1. Update the add-on with the merged configuration.

   ```bash
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values file://config.json \
     --resolve-conflicts OVERWRITE
   ```

   If the update fails because a configuration value isn't valid, compare your configuration with the schema that your add-on version accepts. For the command, see the end of this section.

1. Check that the add-on status is `ACTIVE` and that it has your configuration values. The update might take a few minutes.

   ```bash
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.{Status:status,ConfigValues:configurationValues}" \
     --output table
   ```

1. Check that the CloudWatch agent pods restarted and are in `Running` status.

   ```bash
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

To see the configuration values that an add-on version accepts, run the following command. Replace {{version}} with the add-on version.

```bash
aws eks describe-addon-configuration \
  --addon-name amazon-cloudwatch-observability \
  --addon-version {{version}}
```

## Configuring the Helm chart
<a name="eks-observability-addon-configure-helm"></a>

Pass the configuration values in a values file or with `--set`. The `--reuse-values` option keeps the values that you set before.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.enabled=true \
  --set otlp.grpc.port=14317
```

## Setting agent CPU and memory
<a name="eks-observability-addon-configure-agent-resources"></a>

Large clusters generate more telemetry, so the CloudWatch agent might need more CPU and memory than the defaults. By default, each agent requests 250m CPU and 128Mi memory, and its limits are 500m CPU and 512Mi memory. The `agent.resources` value applies to every CloudWatch agent that the add-on runs. These are the agent on each node, the cluster scraper that OTel Container Insights adds, and the Windows agents. To change the values, merge the following fragment into your configuration. Replace {{cpu-request}}, {{memory-request}}, {{cpu-limit}}, and {{memory-limit}} with the values that you want.

```json
{
  "agent": {
    "resources": {
      "requests": {
        "cpu": "{{cpu-request}}",
        "memory": "{{memory-request}}"
      },
      "limits": {
        "cpu": "{{cpu-limit}}",
        "memory": "{{memory-limit}}"
      }
    }
  }
}
```

To give one Linux agent different values, set `resources` on its entry in the `agents` list. Your list replaces the default list, so include both default entries. The following fragment raises the memory limit of the cluster scraper only.

```json
{
  "agents": [
    { "name": "cloudwatch-agent" },
    {
      "name": "cloudwatch-agent-cluster-scraper",
      "mode": "deployment",
      "config": "default",
      "resources": { "limits": { "memory": "{{memory-limit}}" } }
    }
  ]
}
```

Replace {{memory-limit}} with the memory limit that you want for the cluster scraper.

The agent pods restart with the new values, which might take a few minutes. To check the values after the update, run the following command. It lists the resources of each agent.

```bash
kubectl get amazoncloudwatchagents -n amazon-cloudwatch \
  -o custom-columns='NAME:.metadata.name,RESOURCES:.spec.resources'
```

## Managing tolerations and node selectors
<a name="CloudWatch-Observability-EKS-addon-Tolerations"></a>

Starting with version 1.7.0 of the Amazon CloudWatch Observability EKS add-on, the add-on and the Helm chart by default set Kubernetes *tolerations* to tolerate all taints on the pod workloads that they install. This means that daemonsets such as the CloudWatch agent and Fluent Bit can schedule pods on all nodes in your cluster by default. For more information about tolerations and taints, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation.

The default tolerations set by the add-on or the Helm chart are as follows:

```yaml
tolerations:
- operator: Exists
```

You can override the default tolerations by setting the `tolerations` field at the root level of the configuration values. An example would look like the following:

```yaml
tolerations:
- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"
```

To omit tolerations completely, you can use a config that looks like the following:

```yaml
tolerations: []
```

Changes to the root `tolerations` apply to all pod workloads that the add-on or the Helm chart installs. To set tolerations for one component only, set `tolerations` under that component, for example `agent.tolerations`. A component value replaces the root value.

To choose the nodes that run the CloudWatch agent, set `agent.nodeSelector`. Its default is `kubernetes.io/os: linux`, and the labels that you add are combined with it.

## Managing admission webhook TLS certificates
<a name="CloudWatch-Observability-EKS-addon-Webhook"></a>

The Amazon CloudWatch Observability EKS add-on and the Helm chart use Kubernetes [ admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) to validate and mutate `AmazonCloudWatchAgent` and `Instrumentation` custom resource (CR) requests, and optionally Kubernetes pod requests on the cluster if CloudWatch Application Signals is enabled. In Kubernetes, webhooks require a TLS certificate that the API server is configured to trust to make sure secure communication.

By default, the Amazon CloudWatch Observability EKS add-on and the Helm chart auto-generate a self-signed CA and a TLS certificate signed by this CA for securing the communication between the API server and the webhook server. This certificate is valid for 3,650 days (10 years), and the add-on doesn't renew it automatically. The add-on and the Helm chart generate the CA bundle and the certificate again every time that you upgrade or reinstall them, which resets the validity period.

For a more secure and feature-rich certificate authority solution, the add-on has opt-in support for [ cert-manager](https://cert-manager.io/docs/), a widely-adopted solution for TLS certificate management in Kubernetes that simplifies the process of obtaining, renewing, managing and using those certificates. It ensures that certificates are valid and up to date, and attempts to renew certificates at a configured time before expiry. cert-manager also simplifies issuing certificates from a variety of supported sources, including [AWS Certificate Manager Private Certificate Authority](https://aws.amazon.com/private-ca/).

We recommend that you review best practices for management of TLS certificates on your clusters and advise you to opt in to cert-manager for production environments. Note that if you opt-in to enabling cert-manager for managing the admission webhook TLS certificates, you are required to pre-install cert-manager on your Amazon EKS cluster before you install the Amazon CloudWatch Observability EKS add-on or the Helm chart. For more information about available installation options, see [ cert-manager documentation](https://cert-manager.io/docs/installation/). After you install it, you can opt in to using cert-manager for managing the admission webhook TLS certificates using the following additional configuration.
+ If you are using the Amazon CloudWatch Observability EKS add-on

  ```
  --configuration-values '{ "admissionWebhooks": { "certManager": { "enabled": true } } }'
  ```
+ If you are using the Helm chart

  ```
  --set admissionWebhooks.certManager.enabled=true
  ```

The advanced configuration discussed in this section will by default use a [ SelfSigned](https://cert-manager.io/docs/configuration/selfsigned/) issuer.
