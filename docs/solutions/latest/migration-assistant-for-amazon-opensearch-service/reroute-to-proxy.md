---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/reroute-to-proxy.html
---

# Reroute client traffic to the capture proxy
<a name="reroute-to-proxy"></a>

This phase applies only to zero-downtime migrations (Scenario 3) and to capture-and-replay migrations (Scenario 2). If you are running a backfill-only migration, skip it. See [Migration scenarios](use-the-solution.md#migration-scenarios).

For a zero-downtime migration, you must start capturing traffic **before** you take the source snapshot. Capture has to be active first so that no writes are lost in the window between the snapshot point-in-time and the moment replay catches the target up. The Capture Proxy forwards each client request to the source cluster and simultaneously records it to a durable [Apache Kafka](https://kafka.apache.org/) stream (managed by Strimzi on Amazon EKS) for the Traffic Replayer to consume later.

## Resources the workflow creates
<a name="reroute-resources"></a>

When your workflow configuration includes a `traffic` section, the workflow provisions the following:
+ a fleet of capture proxy pods,
+ a Kubernetes Service in front of those pods, and
+ the Apache Kafka wiring needed to record captured traffic for replay.

Client traffic is sent to the proxy Service, which forwards requests to the source cluster and records them. On Amazon EKS, the Service can be backed by AWS load-balancer infrastructure — an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) or a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) — and the bootstrap path handles the platform wiring for you. On a generic Kubernetes cluster, you are responsible for routing client traffic to the proxy Service.

## Configure the capture proxy
<a name="reroute-configure"></a>

Add a `traffic` section to your workflow configuration and edit it from the Migration Console pod:

```
workflow configure edit
```

Configure proxy settings under `traffic.proxies.<PROXY_NAME>.proxyConfig`.

Useful capture proxy fields include the following:
+  `listenPort` - the port the proxy listens on (for example, `9200`). This value is required and is used to construct the proxy Service endpoint.
+  `podReplicas` - the number of capture proxy pods. Increase this for higher throughput or availability.
+  `serviceType` - Kubernetes Service type. The default is `LoadBalancer`; use `ClusterIP` when traffic reaches the proxy only from inside the cluster.
+  `internetFacing` - on Amazon EKS, whether a `LoadBalancer` proxy Service is exposed through an internet-facing load balancer.
+  `resources` - Kubernetes resource requests and limits for capture proxy pods.
+  `tls` - the TLS mode for the proxy (see [TLS behavior](#reroute-tls)).
+  `setHeader` - flattened alternating list of header names and values to inject, for host-based routing to the source, such as `["Host", "source.example.com", "X-Migration", "pilot"]`. The list must contain an even number of entries. The proxy removes any existing header with that name before setting the configured value; if the same header appears more than once in the configured list, the last configured value wins.
+  `destinationConnectionPoolSize` - number of warm persistent connections to keep for the source cluster per Netty worker thread. The default `0` disables warm connection pooling, so the proxy opens destination connections on demand. When this is greater than `0`, the total possible warm connections is approximately `destinationConnectionPoolSize * numThreads`.
+  `destinationConnectionPoolTimeout` - ISO-8601 duration for recycling idle source-cluster connections when warm connection pooling is enabled. The default is `PT30S`.
+  `maxTrafficBufferSize` - maximum bytes buffered for a single HTTP request or response payload before writing to Kafka. The default and maximum are `1048576` bytes.
+  `numThreads` - Netty worker threads for the proxy. The workflow default is `1`.
+  `kafkaClientId` - Kafka producer client ID, useful for identifying this proxy in Kafka broker logs and metrics.
+  `enableMSKAuth` - legacy process flag for direct MSK IAM Kafka producer wiring. The workflow Kafka cluster profile path resolves `auth.type` as `none` or `scram-sha-512`; use this flag only for low-level process configurations that are wired consistently with the replayer.
+  `otelMetricsCollectorEndpoint` and `otelTraceCollectorEndpoint` - OpenTelemetry collector endpoints for capture proxy pods. Metrics default to `http://otel-collector:4317`; set the metrics endpoint to an empty string to disable metrics export. Trace export is disabled unless you configure a trace endpoint.
+  `loggingConfigurationOverrideConfigMap` - ConfigMap name for a custom proxy logging configuration.

The proxy also supports capture suppression fields:
+  `noCapture` - forwards traffic to the source without recording it to Kafka. Use this only when you intentionally want proxy routing or TLS termination without replayable traffic.
+  `suppressCaptureForHeaderMatch` - flattened alternating list of header names and regexes, such as `["user-agent", ".healthcheck."]`. The list must contain an even number of entries. Matching requests are forwarded but not recorded. Header names are matched case-insensitively; if the same header appears more than once in the configured list, the last configured regex wins.
+  `suppressCaptureForMethod` - regex matched against the HTTP method. Matching requests are forwarded but not recorded.
+  `suppressCaptureForUriPath` - regex matched against the URI path. Matching requests are forwarded but not recorded.
+  `suppressMethodAndPath` - regex matched against `METHOD /path`, such as `(.* /ephemeral/.|GET /_cat/.)`.

Suppression regexes use full-string matching. Use patterns such as `.healthcheck. ` for contains-style matching, not `healthcheck`.

The capture proxy also suppresses HTTP/2 traffic from capture. Those requests can be forwarded to the source, but they are not written to Kafka for replay. Use HTTP/1.1 for traffic that must be replayed on the target.

Do not suppress writes, deletes, or other state-changing requests that must be replayed on the target. Suppression is best reserved for health checks, diagnostics, and other traffic that you intentionally do not want in Kafka.

## Kafka cluster configuration
<a name="reroute-kafka-configuration"></a>

By default, if your workflow includes `traffic.proxies` or `traffic.s3Sources` and you do not define `kafkaClusterConfiguration`, the workflow creates a Strimzi-managed Kafka cluster named `default`. Capture proxies and S3 traffic loaders use that cluster unless you set their `kafka` field to a different cluster name. For `traffic.s3Sources`, define the Kafka profile explicitly with `autoCreate.auth.type: none` or `existing.auth.type: none`; the implicit workflow-managed Kafka default resolves to SCRAM, and the S3 loader does not mount SCRAM passwords or Kafka CA certificates. See [Replay a captured-traffic archive from Amazon S3](using-traffic-replayer.md#replay-s3-captured-traffic).

Define `kafkaClusterConfiguration` when you need to tune the workflow-managed Kafka cluster, use more than one Kafka cluster, or point Migration Assistant at an existing Kafka or Amazon MSK cluster. The `kafka` and `kafkaTopic` fields live next to `proxyConfig`, not inside it. The `traffic.replayers` map is required by the workflow schema; use an empty object while you are configuring capture only, then add replayer entries when you are ready to replay.

```
{
  "kafkaClusterConfiguration": {
    "default": {
      "autoCreate": {}
    }
  },
  "traffic": {
    "proxies": {
      "capture-proxy": {
        "source": "source",
        "kafka": "default",
        "kafkaTopic": "capture-traffic",
        "proxyConfig": {
          "listenPort": 9200
        }
      }
    },
    "replayers": {}
  }
}
```

For an auto-created Strimzi cluster, configure overrides under `kafkaClusterConfiguration.<cluster>.autoCreate`:
+  `auth` - workflow-owned listener authentication. Supported values are `none` and `scram-sha-512`. If omitted, the workflow-managed default is SCRAM.
+  `clusterSpecOverrides` - partial Strimzi `Kafka.spec` overrides.
+  `nodePoolSpecOverrides` - partial Strimzi `KafkaNodePool.spec` overrides, such as broker count or storage size.
+  `topicSpecOverrides` - partial Strimzi `KafkaTopic.spec` overrides, such as partitions, replicas, and retention settings for capture topics.

The workflow-managed baseline is a three-broker combined controller/broker Kafka cluster, with 2 GiB persistent storage per broker for smoke-test-sized deployments, SCRAM authentication, topic `partitions: 1`, topic `replicas: 3`, `retention.ms: 604800000` (seven days), `segment.bytes: 1073741824` (1 GiB), and broker quorum settings that use replication factor 3 with `min.insync.replicas: 2`. Override storage size and topic retention for production traffic volumes; override replicas only if you accept the durability tradeoff for captured traffic.

For an existing Kafka or Amazon MSK cluster, use `kafkaClusterConfiguration.<cluster>.existing` with `kafkaConnection`, optional default `kafkaTopic`, and an explicit auth configuration. The workflow profile supports `auth.type: none` for unauthenticated Kafka and `auth.type: scram-sha-512` for SCRAM; `msk-iam` is not a valid workflow `auth.type` value. For SCRAM, `secretName` must name a Kubernetes Secret in the `ma` namespace with a `password` key, `caSecretName` must name a Secret with the cluster CA certificate at `ca.crt`, and `kafkaUserName` should be the Kafka principal for that password.

```
{
  "kafkaClusterConfiguration": {
    "external-kafka": {
      "existing": {
        "kafkaConnection": "broker-a.example.com:9092,broker-b.example.com:9092",
        "kafkaTopic": "migration-traffic",
        "auth": {
          "type": "none"
        }
      }
    }
  },
  "traffic": {
    "proxies": {
      "capture-proxy": {
        "source": "source",
        "kafka": "external-kafka",
        "proxyConfig": {
          "listenPort": 9200
        }
      }
    },
    "replayers": {}
  }
}
```

For an existing SCRAM-protected Kafka cluster, configure the client identity and trust material explicitly:

```
{
  "kafkaClusterConfiguration": {
    "external-kafka": {
      "existing": {
        "kafkaConnection": "broker-a.example.com:9093,broker-b.example.com:9093",
        "kafkaTopic": "migration-traffic",
        "auth": {
          "type": "scram-sha-512",
          "secretName": "existing-kafka-user",
          "caSecretName": "existing-kafka-ca",
          "kafkaUserName": "migration-app"
        }
      }
    }
  }
}
```

If you define any `kafkaClusterConfiguration` entries, every proxy or S3 traffic source must resolve to one of those entries. If you omit `kafka`, the workflow uses the name `default`, so include a `default` Kafka entry or set `kafka` explicitly.

Each capture proxy and S3 traffic loader writes to one captured-traffic topic. Within a single Kafka cluster, every `traffic.proxies` and `traffic.s3Sources` producer must resolve to a unique topic. The effective topic is the explicit `kafkaTopic`, or the traffic source key when `kafkaTopic` is omitted. Using the same topic name on different Kafka clusters is valid; using the same topic name twice on the same cluster is rejected because replay would interleave records from different sources.

## TLS behavior
<a name="reroute-tls"></a>

The capture proxy is secure by default. If you do not configure TLS explicitly, the workflow provisions a cert-manager certificate for the proxy through the `migrations-ca` issuer, with DNS names for the proxy Service (`<proxy-name>`, `<proxy-name>.ma`, and `<proxy-name>.ma.svc.cluster.local`). When the deployment is configured with an AWS Region for proxy certificate defaults, the generated certificate also includes the regional Elastic Load Balancing wildcard name. You can also configure cert-manager-issued certificates, an existing AWS Private Certificate Authority (AWS Private CA), or a new AWS Private CA through the bootstrap script’s TLS flags. See [Deploy the solution](deploy-the-solution.md).

The `tls` configuration supports these modes:
+  `certManager` - provisions a certificate through cert-manager. Provide `issuerRef` and `dnsNames`; `duration`, `renewBefore`, and `commonName` are optional.
+  `existingSecret` - uses an existing Kubernetes TLS secret with `tls.crt` and `tls.key`.
+  `plaintext` - explicitly disables TLS. Use this only when you intentionally want plaintext HTTP.

To require mutual TLS client authentication, add `clientAuth` under the `certManager` or `existingSecret` TLS configuration. Provide exactly one trust source: `trustedClientCaFile` or `trustedClientCaPem`. The `required` field defaults to `true`, so clients must present a certificate signed by that trusted CA. Setting `required` to `false` disables the enforcement requirement; it doesn’t create a separate optional client-certificate verification mode.

The following example serves the proxy with an existing Kubernetes TLS secret and requires client certificates signed by the CA stored in a ConfigMap:

```
{
  "traffic": {
    "proxies": {
      "capture-proxy": {
        "source": "source",
        "proxyConfig": {
          "listenPort": 9200,
          "tls": {
            "mode": "existingSecret",
            "secretName": "proxy-tls",
            "clientAuth": {
              "trustedClientCaFile": {
                "configMap": "trusted-client-roots",
                "path": "ca.crt"
              },
              "required": true
            }
          }
        }
      }
    },
    "replayers": {}
  }
}
```

 `trustedClientCaFile` uses the same file-reference shape as transform file sources: use `configMap` plus a ConfigMap key, or use `image` plus a path relative to the mounted image root. The workflow mounts the file and passes the resolved path to the proxy. If you use `trustedClientCaPem` instead, the PEM value is passed through an environment variable.

## Host and header overrides
<a name="reroute-headers"></a>

If your source cluster routes on the `Host` header or you need to inject a static header on captured requests, use `setHeader` in the proxy configuration. For example:

```
{
  "setHeader": ["Host", "source.example.com"]
}
```

## Find the proxy endpoint
<a name="reroute-find-endpoint"></a>

After the workflow creates the proxy, find the Service endpoint that clients should target:

```
kubectl get svc -n ma
```

On Amazon EKS, the external address of the load-balancer-backed Service is the endpoint you point clients at.

## Verify capture before proceeding
<a name="reroute-verify"></a>

Confirm that traffic is flowing through the proxy and being recorded before you start the snapshot and backfill phase. Use the Workflow CLI to watch the run:

```
workflow status
workflow manage
```

Only after capture is confirmed active should you proceed to snapshot creation and [metadata migration](migrate-metadata.md).
