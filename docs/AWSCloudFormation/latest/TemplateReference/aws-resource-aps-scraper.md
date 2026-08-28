---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aps-scraper.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper
<a name="aws-resource-aps-scraper"></a>

A scraper is a fully-managed agentless collector that discovers and pulls metrics automatically. A scraper pulls metrics from Prometheus-compatible sources within an Amazon EKS cluster, and sends them to your Amazon Managed Service for Prometheus workspace. Scrapers are flexible. You can configure the scraper to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your cluster. You must configure this role with a policy that allows it to scrape metrics from your cluster. For more information, see [Configuring your Amazon EKS cluster](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup) in the *Amazon Managed Service for Prometheus User Guide*.

The `scrapeConfiguration` parameter contains the YAML configuration for the scraper.

**Note**
For more information about collectors, including what metrics are collected, and how to configure the scraper, see [Using an AWS managed collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Syntax
<a name="aws-resource-aps-scraper-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aps-scraper-syntax.json"></a>

```
{
  "Type" : "AWS::APS::Scraper",
  "Properties" : {
      "[Alias](#cfn-aps-scraper-alias)" : {{String}},
      "[Destination](#cfn-aps-scraper-destination)" : {{Destination}},
      "[RoleConfiguration](#cfn-aps-scraper-roleconfiguration)" : {{RoleConfiguration}},
      "[ScrapeConfiguration](#cfn-aps-scraper-scrapeconfiguration)" : {{ScrapeConfiguration}},
      "[ScraperLoggingConfiguration](#cfn-aps-scraper-scraperloggingconfiguration)" : {{ScraperLoggingConfiguration}},
      "[Source](#cfn-aps-scraper-source)" : {{Source}},
      "[Tags](#cfn-aps-scraper-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-aps-scraper-syntax.yaml"></a>

```
Type: AWS::APS::Scraper
Properties:
  [Alias](#cfn-aps-scraper-alias): {{String}}
  [Destination](#cfn-aps-scraper-destination): {{
    Destination}}
  [RoleConfiguration](#cfn-aps-scraper-roleconfiguration): {{
    RoleConfiguration}}
  [ScrapeConfiguration](#cfn-aps-scraper-scrapeconfiguration): {{
    ScrapeConfiguration}}
  [ScraperLoggingConfiguration](#cfn-aps-scraper-scraperloggingconfiguration): {{
    ScraperLoggingConfiguration}}
  [Source](#cfn-aps-scraper-source): {{
    Source}}
  [Tags](#cfn-aps-scraper-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-aps-scraper-properties"></a>

`Alias`  <a name="cfn-aps-scraper-alias"></a>
An optional user-assigned scraper alias.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z][-.0-9A-Z_a-z]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-aps-scraper-destination"></a>
The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
*Required*: Yes
*Type*: [Destination](aws-properties-aps-scraper-destination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleConfiguration`  <a name="cfn-aps-scraper-roleconfiguration"></a>
The role configuration in an Amazon Managed Service for Prometheus scraper.
*Required*: No
*Type*: [RoleConfiguration](aws-properties-aps-scraper-roleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScrapeConfiguration`  <a name="cfn-aps-scraper-scrapeconfiguration"></a>
The configuration in use by the scraper.
*Required*: Yes
*Type*: [ScrapeConfiguration](aws-properties-aps-scraper-scrapeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScraperLoggingConfiguration`  <a name="cfn-aps-scraper-scraperloggingconfiguration"></a>
The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
*Required*: No
*Type*: [ScraperLoggingConfiguration](aws-properties-aps-scraper-scraperloggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-aps-scraper-source"></a>
The Amazon EKS cluster from which the scraper collects metrics.
*Required*: Yes
*Type*: [Source](aws-properties-aps-scraper-source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-aps-scraper-tags"></a>
(Optional) The list of tag keys and values associated with the scraper.
*Required*: No
*Type*: Array of [Tag](aws-properties-aps-scraper-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-aps-scraper-return-values"></a>

### Ref
<a name="aws-resource-aps-scraper-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "Id" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-aps-scraper-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-aps-scraper-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the scraper. For example, `arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34`.

`RoleArn`  <a name="RoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.
For example, `arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example`.

`ScraperId`  <a name="ScraperId-fn::getatt"></a>
The ID of the scraper. For example, `s-example1-1234-abcd-5678-ef9012abcd34`.

## Examples
<a name="aws-resource-aps-scraper--examples"></a>

### Amazon Managed Service for Prometheus scraper example
<a name="aws-resource-aps-scraper--examples--Amazon_Managed_Service_for_Prometheus_scraper_example"></a>

The following example creates a scraper, showing how to pass in configuration. You must replace values in braces (`{}`) with values that match your system.

#### YAML
<a name="aws-resource-aps-scraper--examples--Amazon_Managed_Service_for_Prometheus_scraper_example--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09 Resources: Scraper: Type:
                AWS::APS::Scraper UpdateReplacePolicy: Retain DeletionPolicy: Delete Properties:
                Alias: "Scraper-Test" Source: EksConfiguration: ClusterArn:
                "arn:aws:eks:{region}:{account-id}:cluster/{cluster-name}" SecurityGroupIds: -
                "sg-{security-group-id}" SubnetIds: - "subnet-{subnet-id-1}" -
                "subnet-{subnet-id-2}" Destination: AmpConfiguration: WorkspaceArn:
                "arn:aws:aps:{region}:{account-id}:workspace/ws-{workspace-id}" ScrapeConfiguration:
                ConfigurationBlob: "global:\n scrape_interval: 30s\n # external_labels:\n #
                clusterArn: {cluster-arn}\nscrape_configs:\n # pod metrics\n - job_name:
                pod_exporter\n kubernetes_sd_configs:\n - role: pod\n # container metrics\n -
                job_name: cadvisor\n scheme: https\n authorization:\n credentials_file:
                /var/run/secrets/kubernetes.io/serviceaccount/token\n kubernetes_sd_configs:\n -
                role: node\n relabel_configs:\n - action: labelmap\n regex:
                __meta_kubernetes_node_label_(.+)\n - replacement: kubernetes.default.svc:443\n
                target_label: __address__\n - source_labels: [__meta_kubernetes_node_name]\n regex:
                (.+)\n target_label: __metrics_path__\n replacement:
                /api/v1/nodes/$1/proxy/metrics/cadvisor\n # apiserver metrics\n - bearer_token_file:
                /var/run/secrets/kubernetes.io/serviceaccount/token\n job_name:
                kubernetes-apiservers\n kubernetes_sd_configs:\n - role: endpoints\n
                relabel_configs:\n - action: keep\n regex: default;kubernetes;https\n
                source_labels:\n - __meta_kubernetes_namespace\n - __meta_kubernetes_service_name\n
                - __meta_kubernetes_endpoint_port_name\n scheme: https\n # kube proxy metrics\n -
                job_name: kube-proxy\n honor_labels: true\n kubernetes_sd_configs:\n - role: pod\n
                relabel_configs:\n - action: keep\n source_labels:\n - __meta_kubernetes_namespace\n
                - __meta_kubernetes_pod_name\n separator: '/'\n regex: 'kube-system/kube-proxy.+'\n
                - source_labels:\n - __address__\n action: replace\n target_label: __address__\n
                regex: (.+?)(\\:\\d+)?\n replacement: $1:10249" Tags: - Key: "BusinessPurpose"
                Value: "Testing"
```

#### JSON
<a name="aws-resource-aps-scraper--examples--Amazon_Managed_Service_for_Prometheus_scraper_example--json"></a>

```
{ "CreateInputs": { "Alias": "Scraper-Test",
                "ScrapeConfiguration": { "ConfigurationBlob": "global:\n scrape_interval: 30s\n #
                external_labels:\n # clusterArn: {cluster-arn}\nscrape_configs:\n # pod metrics\n -
                job_name: pod_exporter\n kubernetes_sd_configs:\n - role: pod\n # container
                metrics\n - job_name: cadvisor\n scheme: https\n authorization:\n credentials_file:
                /var/run/secrets/kubernetes.io/serviceaccount/token\n kubernetes_sd_configs:\n -
                role: node\n relabel_configs:\n - action: labelmap\n regex:
                __meta_kubernetes_node_label_(.+)\n - replacement: kubernetes.default.svc:443\n
                target_label: __address__\n - source_labels: [__meta_kubernetes_node_name]\n regex:
                (.+)\n target_label: __metrics_path__\n replacement:
                /api/v1/nodes/$1/proxy/metrics/cadvisor\n # apiserver metrics\n - bearer_token_file:
                /var/run/secrets/kubernetes.io/serviceaccount/token\n job_name:
                kubernetes-apiservers\n kubernetes_sd_configs:\n - role: endpoints\n
                relabel_configs:\n - action: keep\n regex: default;kubernetes;https\n
                source_labels:\n - __meta_kubernetes_namespace\n - __meta_kubernetes_service_name\n
                - __meta_kubernetes_endpoint_port_name\n scheme: https\n # kube proxy metrics\n -
                job_name: kube-proxy\n honor_labels: true\n kubernetes_sd_configs:\n - role: pod\n
                relabel_configs:\n - action: keep\n source_labels:\n - __meta_kubernetes_namespace\n
                - __meta_kubernetes_pod_name\n separator: '/'\n regex: 'kube-system/kube-proxy.+'\n
                - source_labels:\n - __address__\n action: replace\n target_label: __address__\n
                regex: (.+?)(\\:\\d+)?\n replacement: $1:10249" }, "Source": { "EksConfiguration": {
                "ClusterArn": "arn:aws:eks:{region}:{account-id}:cluster/{cluster-name}",
                "SecurityGroupIds": [ "sg-{security-group-id}" ], "SubnetIds": [
                "subnet-{subnet-id-1}", "subnet-{subnet-id-2}" ] } }, "Destination": {
                "AmpConfiguration": { "WorkspaceArn":
                "arn:aws:aps:{region}:{account-id}:workspace/ws-{workspace-id}" } }, "Tags": [ {
                "Key": "BusinessPurpose", "Value": "Testing" } ] }, "PatchInputs": [] }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
