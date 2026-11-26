---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-nccl-metrics.html
---

# Monitoring NCCL communication in training jobs on SageMaker HyperPod clusters

Distributed training jobs synchronize GPUs through NVIDIA Collective Communications Library (NCCL) operations such as AllReduce, AllGather, and ReduceScatter. A collective operation completes only when every rank arrives, so one slow GPU, link, or host slows down the whole job, often without raising an error. NCCL metrics help you find the rank, GPU, or node that holds up a training job.

The Amazon SageMaker HyperPod NCCL profiler is an NCCL profiler plugin that the NCCL library in your training container loads at startup. For more information about NCCL profiler plugins, see [NCCL profiler plugin](https://github.com/NVIDIA/nccl/blob/master/plugins/profiler/README.md) on the GitHub website. The profiler times each collective and send or receive operation on the GPU. It exports per-rank bandwidth, execution time, and wait time metrics through the SageMaker HyperPod observability add-on to Amazon CloudWatch. The metrics carry the same GPU UUID as the GPU metrics that the add-on collects, so you can view NCCL performance next to GPU utilization, clocks, temperature, and errors.

The profiler has the following characteristics:
+ You turn it on for each training job. Jobs that you don't configure aren't profiled.
+ It requires no changes to your training code.
+ If the profiler can't send metrics, training continues unaffected.
+ It sends only the performance metrics that this page describes to the metric store of your observability add-on. It doesn't collect tensor data or model contents.

## Prerequisites
<a name="hyperpod-observability-nccl-metrics-prerequisites"></a>

Before you turn on NCCL metrics, make sure that you have the following:
+ A SageMaker HyperPod cluster orchestrated by Amazon EKS with NVIDIA GPU instances
+ The SageMaker HyperPod observability add-on
+ NCCL version 2.27.5 or later in your training container

## Turn on NCCL metrics for a training job
<a name="hyperpod-observability-nccl-metrics-enable"></a>

The profiler is available as a container image in each supported AWS Region. The image contains the plugin, `libnccl_profiler.so`, and a default configuration file, `profiler.toml`. The default configuration sends metrics to the observability add-on collector every 10 seconds. Use the image in the Region of your cluster:

```
{{account-id}}.dkr.ecr.{{region}}.amazonaws.com/hyperpod-nccl-profiler:latest
```

The following table lists the account ID for each Region.

| Region | Account ID |
| --- | --- |
| ap-northeast-1 | 533267052152 |
| ap-northeast-2 | 982035845025 |
| ap-south-1 | 011528288864 |
| ap-south-2 | 427553886971 |
| ap-southeast-1 | 905418428165 |
| ap-southeast-2 | 851725636348 |
| ap-southeast-3 | 971422672635 |
| ap-southeast-4 | 084375568333 |
| ca-central-1 | 843976229209 |
| eu-central-1 | 211125453373 |
| eu-north-1 | 654654141839 |
| eu-south-2 | 626887787726 |
| eu-west-1 | 533267293120 |
| eu-west-2 | 011528288831 |
| sa-east-1 | 025066253954 |
| us-east-1 | 767398015722 |
| us-east-2 | 851725546812 |
| us-west-1 | 011528288828 |
| us-west-2 | 905418368575 |

The `latest` tag changes with each release. To keep the configuration that you tested, reference the image by its digest instead.

**To turn on NCCL metrics for a training job**

1. In the pod template of your training job, for example a `PyTorchJob` or `HyperPodPyTorchJob`, add an `emptyDir` volume to hold the plugin.

1. Add an init container that uses the profiler image and copies `libnccl_profiler.so` and `profiler.toml` into the volume.

1. Mount the volume read-only in the training container.

1. Set the following environment variables in the training container.

<table>
<thead>
  <tr><th>Variable</th><th>Required</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td><code>NCCL_PROFILER_PLUGIN</code></td><td>Yes</td><td><code>/opt/amazon/hyperpod-nccl-profiler/libnccl_profiler.so</code></td></tr>
  <tr><td><code>HYPERPOD_NCCL_PROFILER_CONFIG</code></td><td>Yes</td><td><code>/opt/amazon/hyperpod-nccl-profiler/profiler.toml</code></td></tr>
  <tr><td><code>HYPERPOD_JOB_NAME</code>, <code>HYPERPOD_JOB_ID</code></td><td>For the dashboard</td><td>Values for the <code>job_name</code> and <code>job_id</code> dimensions. The <b>NCCL Profiler</b> dashboard lists only jobs that set <code>HYPERPOD_JOB_ID</code>.</td></tr>
  <tr><td><code>NODE_NAME</code></td><td>Recommended</td><td><code>spec.nodeName</code>, for the <code>hostname</code> dimension</td></tr>
  <tr><td><code>NCCL_DEBUG</code></td><td>Recommended</td><td><code>WARN</code> (or <code>INFO</code>), so that the profiler's warnings, such as failed exports, appear in the training container's log</td></tr>
</tbody>
</table>

The following example shows a two-node PyTorch job with eight GPUs on each node. Replace {{account-id}} and {{region}} with the values for your Region, and {{training-image}} with your training container image.

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: fsdp2
spec:
  pytorchReplicaSpecs:
    Worker:
      replicas: 2
      restartPolicy: OnFailure
      template:
        spec:
          volumes:
            - name: hyperpod-nccl-profiler
              emptyDir: {}
          initContainers:
            - name: install-nccl-profiler
              image: {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/hyperpod-nccl-profiler:latest
              command:
                - sh
                - -c
                - cp -v /hyperpod-nccl-profiler/libnccl_profiler.so /hyperpod-nccl-profiler/profiler.toml /opt/amazon/hyperpod-nccl-profiler/
              volumeMounts:
                - name: hyperpod-nccl-profiler
                  mountPath: /opt/amazon/hyperpod-nccl-profiler
          containers:
            - name: pytorch
              image: {{training-image}}
              command:
                - torchrun
                - --nproc_per_node=8
                - --nnodes=2
                - --rdzv_backend=c10d
                - --rdzv_endpoint=fsdp2-worker-0
                - train.py
              resources:
                limits:
                  nvidia.com/gpu: 8
              volumeMounts:
                - name: hyperpod-nccl-profiler
                  mountPath: /opt/amazon/hyperpod-nccl-profiler
                  readOnly: true
              env:
                - name: NCCL_DEBUG
                  value: WARN
                - name: NCCL_PROFILER_PLUGIN
                  value: /opt/amazon/hyperpod-nccl-profiler/libnccl_profiler.so
                - name: HYPERPOD_NCCL_PROFILER_CONFIG
                  value: /opt/amazon/hyperpod-nccl-profiler/profiler.toml
                - name: HYPERPOD_JOB_NAME
                  value: fsdp2
                - name: HYPERPOD_JOB_ID
                  value: run-1
                - name: NODE_NAME
                  valueFrom:
                    fieldRef:
                      fieldPath: spec.nodeName
```

If you build your own training image, you can copy the profiler files into the image instead of using an init container and a volume. In that case, you only set the environment variables.

```dockerfile
COPY --from={{account-id}}.dkr.ecr.{{region}}.amazonaws.com/hyperpod-nccl-profiler:latest \
     /hyperpod-nccl-profiler/ /opt/amazon/hyperpod-nccl-profiler/
```

**Note**
The profiler sends metrics to the add-on collector through the cluster DNS name `hyperpod-otel-collector.hyperpod-observability`. If your training pods use `hostNetwork: true`, also set `dnsPolicy: ClusterFirstWithHostNet`. Otherwise, the name doesn't resolve, and no metrics arrive.

## Verify NCCL metrics
<a name="hyperpod-observability-nccl-metrics-verify"></a>

**To verify that NCCL metrics arrive in CloudWatch**

1. Check that the training pods are running. Run `kubectl get pods`, and confirm that the status is `Running`. If the status is `Init:ErrImagePull` or `Init:ImagePullBackOff`, check that the image is the one for the Region of your cluster.

1. Set `NCCL_DEBUG` to `INFO`, and check the training container log for the line `PROFILER/Plugin: Loaded HYPERPOD_NCCL_PROFILER_V{{n}}`. This line shows that NCCL loaded the profiler.

1. A few minutes after training starts, run a PromQL query for `nccl_bus_bandwidth_gbs` in Query Studio in the CloudWatch console. For an example query, see [NCCL metrics reference](#hyperpod-observability-nccl-metrics-reference).

If no metrics appear, check the following:
+ The NCCL version in the training container log (`NCCL INFO NCCL version`) is 2.27.5 or later.
+ A `hyperpod-observability-node-collector` pod is running on the same node as the training pod. The profiler sends metrics only to the collector on its own node.
+ The collector pod logs don't show export or permission errors. An access denied error for `cloudwatch:PutMetricData` means that the collector role is missing the permission.

**Note**
NCCL metrics don't appear in the output of `aws cloudwatch list-metrics`. Use PromQL to query them.

## NCCL metrics reference
<a name="hyperpod-observability-nccl-metrics-reference"></a>

The bus bandwidth values are comparable with `nccl-tests` results. Every 10 seconds, the profiler reports one data point for each series: the most recently completed operation in that interval. A rank that completes no operations in an interval reports no data point, so an idle or stalled rank appears as a gap. Operations smaller than 8 KiB aren't measured, because latency dominates their timing.

The following table describes the NCCL metrics.

| Metric | Unit | Description |
| --- | --- | --- |
| nccl\_collective\_exec\_time\_microseconds | Microseconds | The time that the GPU kernels of a collective operation spent running. |
| nccl\_collective\_wait\_time\_microseconds | Microseconds | The time from when the framework issues a collective operation to when its first GPU kernel starts. Includes launch latency and time queued behind earlier work. |
| nccl\_collective\_algobw\_gbs, nccl\_algorithm\_bandwidth\_gbs | GB/s | Algorithm bandwidth: the data moved for each rank, divided by the execution time. Both metrics have the same value. |
| nccl\_bus\_bandwidth\_gbs | GB/s | Bus bandwidth: the algorithm bandwidth, adjusted for the number of ranks in the communicator. Use it to compare bandwidth across communicator sizes. |
| nccl\_p2p\_exec\_time\_microseconds | Microseconds | The GPU execution time of a send or receive operation. |
| nccl\_p2p\_wait\_time\_microseconds | Microseconds | The time from when a send or receive operation is issued to when its first GPU kernel starts. |
| nccl\_p2p\_bus\_bandwidth\_gbs, nccl\_p2p\_algobw\_gbs | GB/s | The bandwidth of a send or receive operation. Both metrics have the same value. |

Each data point has the following dimensions.

| Dimension | Description |
| --- | --- |
| job\_name, job\_id | The training job, from HYPERPOD\_JOB\_NAME and HYPERPOD\_JOB\_ID. The value is unknown if the variable isn't set. |
| hostname, node | The Kubernetes node name from NODE\_NAME, or the host name if the variable isn't set. |
| rank, nranks | The rank and the size of the communicator that ran the operation. |
| comm\_id, comm\_name | The NCCL communicator. Use it to separate, for example, tensor parallel groups from data parallel groups. |
| gpu\_uuid | The GPU UUID, in the same GPU- format as nvidia-smi and the GPU metrics of the add-on. |
| gpu\_id, gpu, gpu\_device\_id | The CUDA device ordinal. |
| nnodes, n\_nodes | The number of nodes in the communicator. |
| op, collective, p2p\_operation | The operation type, such as AllReduce, AllGather, ReduceScatter, Send, or Recv. |
| algo, proto, algo\_proto | The NCCL algorithm and protocol, such as RING and SIMPLE. |
| peer | The peer rank of a send or receive operation. |
| message\_size | The message size range, such as 4-5MB. |

The following PromQL query returns the AllGather bus bandwidth of each GPU in a job. Replace {{my-job}} with the value of `HYPERPOD_JOB_NAME`. For more information about querying metrics in CloudWatch, see [Viewing SageMaker HyperPod cluster metrics in Amazon CloudWatch](hyperpod-observability-addon-cloudwatch-metrics.md).

```
avg by (gpu_uuid, hostname) (nccl_bus_bandwidth_gbs{op="AllGather", job_name="{{my-job}}"})
```

In a healthy job, every rank of a communicator shows similar execution time and bandwidth for the same operation and message size. A collective operation completes only when every rank arrives, and ranks that arrive early wait inside it, so their execution time includes that wait. Look for the following patterns:
+ **One rank with lower execution time (higher bandwidth) than the rest of its communicator** – The other ranks are waiting for it. Check the clocks, throttling, temperature, and error counters of that GPU, and its host for CPU contention or data loading.
+ **Execution time that rises, and bandwidth that drops, on every rank at the same time** – The cause is shared, such as a slow or congested network path, a change of NCCL algorithm, or a change in the workload.
+ **Wait time** – Wait time follows the step time on every rank, so on its own it doesn't identify the slow rank.
+ **A series that stops reporting while the job stops making progress** – The rank stopped completing collective operations. Check for a hang.

## View NCCL metrics in Amazon Managed Grafana
<a name="hyperpod-observability-nccl-metrics-dashboard"></a>

When you set up the observability add-on in the SageMaker HyperPod console with an Amazon Managed Grafana workspace, the console installs the **NCCL Profiler** dashboard in the workspace. It shows NCCL metrics next to GPU metrics, from the job level down to a single GPU. Choose a **Job ID** at the top of the dashboard to get started.

| Row | What it answers | Panels |
| --- | --- | --- |
| Job summary | What is the job's layout? | GPUs and nodes reporting, communicators, group sizes, send/receive communicators |
| Groups of N GPUs, one row per communicator size | Which node or GPU are the others waiting for? | Nodes below 0.95x, slowest node, slowest GPU; slowest node and GPU over time; bus bandwidth by collective (median and slowest communicator); nodes vs their group; slowest GPUs; communicators, slowest first |
| Send/receive: groups of N GPUs (only when the job sends and receives) | The same, for pipeline and all-to-all traffic | Bandwidth (median and slowest communicator), execution time |
| AllGather, ReduceScatter, AllReduce, Send/receive: inside vs across nodes | Did communicators inside one node or across nodes slow down, and at which message size? | Bus bandwidth and execution time, one line per message size, group size, and NCCL algorithm and protocol (algo\_proto), for communicators inside one node and across nodes |
| Per-GPU detail – AllGather, ReduceScatter, AllReduce | What is one GPU's NCCL doing? | Bus bandwidth, algorithm bandwidth, execution time, and wait time per GPU |
| Per-GPU hardware (DCGM) – compute, memory | Why is that GPU slow? | Tensor Core utilization, temperature, SM clock, power draw, share of time power- and thermal-throttled, XID errors, GPU utilization; memory temperature, memory clock, memory copy utilization, ECC error counts, memory used |

Filter **Host** or **Comm ID** before you expand a **Per-GPU detail** row on a large job: those panels draw one line per GPU, and CloudWatch returns at most 500 series per query.

## Turn off NCCL metrics
<a name="hyperpod-observability-nccl-metrics-disable"></a>

To turn off NCCL metrics for a job, remove the `NCCL_PROFILER_PLUGIN` environment variable from the training container. Without it, NCCL doesn't load the profiler. You can also remove the init container, the volume, and the volume mount.

## Considerations
<a name="hyperpod-observability-nccl-metrics-considerations"></a>
+ **Overhead** – In testing with models of up to 13B parameters on two `ml.g7.48xlarge` nodes, the profiler used about 1.5 host CPU cores and 150–190 MiB of host memory for each rank, and no GPU memory. Training step time was unchanged when network performance was steady. If your workload is CPU-bound on the host, for example because of heavy data loading, leave headroom for the profiler.
+ **Deep GPU queues** – If more than 5 seconds of GPU work is queued ahead of a collective operation, the operation produces no data point, so metrics can stop while the job keeps running. The training job itself isn't affected. For `nccl-tests` runs with large messages, use the `-z 1` option.
