---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-eks-otel-accelerated-compute.html
---

# Accelerated compute

With the Amazon CloudWatch Observability EKS add-on, you get out-of-the-box support for [Accelerated Compute Insights](Accelerated-Compute-Insights.md) on Amazon EKS. With OTel Container Insights, the add-on collects the metrics of NVIDIA GPUs, AWS Trainium and AWS Inferentia devices, and AWS Elastic Fabric Adapter (EFA) devices on each node. Each device metric carries the attributes of the pod that uses the device, so you can see which workload uses each device. You don't need to configure anything per accelerator.

## Prerequisites
<a name="container-insights-eks-otel-accelerated-compute-prereqs"></a>
+ Version 8.0.0 or later of the `amazon-cloudwatch-observability` add-on or Helm chart
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))

## NVIDIA GPUs
<a name="container-insights-eks-otel-accelerated-compute-gpu"></a>

The add-on runs the NVIDIA Data Center GPU Manager (DCGM) exporter on each node, and the CloudWatch agent collects the GPU metrics that it exposes, such as utilization, memory, temperature, and power.

## AWS Trainium and Inferentia
<a name="container-insights-eks-otel-accelerated-compute-neuron"></a>

The add-on runs Neuron Monitor, the monitoring tool of the AWS Neuron SDK, on each node, and the CloudWatch agent collects the metrics of the Trainium and Inferentia devices and their NeuronCores that Neuron Monitor exposes.

## AWS Elastic Fabric Adapter
<a name="container-insights-eks-otel-accelerated-compute-efa"></a>

The CloudWatch agent collects the metrics of each EFA device on the node.

## Device pod correlation
<a name="container-insights-eks-otel-accelerated-compute-correlation"></a>

The add-on detects which pod and container use each device, and adds the attributes of that pod and container to the metrics of the device. These attributes include the namespace, pod, container, and workload, and the Kubernetes labels of the pod. For the list of attributes, see [Telemetry enrichment](eks-standard-telemetry-attributes.md).

For devices that a Kubernetes device plugin allocates, such as the NVIDIA, Neuron, and EFA device plugins, the add-on reads the kubelet pod resources API. This API reports which devices the kubelet allocated to each container. The DCGM exporter reads it for GPUs, and the CloudWatch agent reads it for Trainium, Inferentia, and EFA devices.

### Using Dynamic Resource Allocation
<a name="container-insights-eks-otel-accelerated-compute-dra"></a>

With Kubernetes Dynamic Resource Allocation (DRA), a pod claims devices through `ResourceClaim` objects instead of resource requests, and a DRA driver allocates the devices for each claim. The add-on correlates EFA devices that the `dra.net` driver allocates and Trainium and Inferentia devices that the `neuron.aws.com` driver allocates. For NVIDIA GPUs, it uses the DRA support of the DCGM exporter. DRA correlation needs an Amazon EKS cluster that runs Kubernetes 1.34 or later.

The add-on supports device plugins and DRA at the same time, and correlates each device from whichever one a workload uses.

### Querying device metrics by pod label
<a name="container-insights-eks-otel-accelerated-compute-example"></a>

Every Kubernetes label that your pods already carry is available on the metrics of the devices that those pods use, as a `k8s.pod.label.{{label-key}}` attribute. You can query the GPU, Trainium, Inferentia, and EFA metrics by any of these labels without adding new labels to your workloads.

For example, the Kubeflow Training Operator and the MPI Operator add the `training.kubeflow.org/job-name` label, with the name of the training job as its value, to every pod of a training job. The following query returns the average GPU utilization of each training job in a cluster. Replace `{{cluster-name}}` with the name of your Amazon EKS cluster:

```promql
avg by ("@resource.k8s.pod.label.training.kubeflow.org/job-name") (
  DCGM_FI_DEV_GPU_UTIL{"@resource.k8s.cluster.name"="{{cluster-name}}"}
)
```

{{cluster-name}}
The name of your Amazon EKS cluster.

`@resource.k8s.pod.label.training.kubeflow.org/job-name`
The `training.kubeflow.org/job-name` label of the pod that uses the GPU. The agent adds pod labels as resource attributes, so the query uses the `@resource.` prefix.

## Monitoring AI and ML workloads
<a name="container-insights-eks-otel-accelerated-compute-solutions"></a>

The following solutions collect metrics from the software that serves and trains models on your accelerated compute:
+ [vLLM metrics](container-insights-eks-otel-vllm.md) – Request load, token throughput, KV cache use, and inference latency of the models that vLLM serves.
+ [SGLang metrics](container-insights-eks-otel-sglang.md) – Request load, token throughput, cache use, and latency of the models that SGLang serves.
+ [Ray metrics](container-insights-eks-otel-ray.md) – Ray core, Ray Serve, and Ray Serve LLM metrics from your KubeRay clusters.
+ [KServe metrics](container-insights-eks-otel-kserve.md) – Metrics of the KServe controller as it reconciles your InferenceServices.
