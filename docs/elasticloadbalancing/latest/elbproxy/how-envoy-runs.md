---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-envoy-runs.html
---

# How the proxy runs Envoy

A proxy runs Envoy with the configuration that you provide. You supply an Envoy bootstrap configuration file and an optional archive of supporting files. ELB for Envoy runs the Envoy processes, keeps them patched, and scales them with traffic. This section describes which Envoy functionality is available in the bootstrap configuration and over xDS, and what ELB for Envoy adds to your configuration.

**Topics**
+ [Envoy versions](#how-envoy-runs-versions)
+ [Bootstrap configuration](#how-envoy-runs-bootstrap)
+ [Configuration validation](#how-envoy-runs-validation)
+ [How ELB for Envoy runs your Envoy process](#how-envoy-runs-process)
+ [Configuration archive](#how-envoy-runs-archive)
+ [Configuration updates and connection draining](#how-envoy-runs-draining)
+ [Dynamic configuration (xDS)](#how-envoy-runs-xds)
+ [What ELB for Envoy adds to your configuration](#how-envoy-runs-injected)

## Envoy versions
<a name="how-envoy-runs-versions"></a>

You choose the Envoy version when you create a proxy, through the `proxyVersion` field. The value is a major and minor version. At launch, ELB for Envoy supports Envoy `1.40` only, and the `CreateProxy` operation rejects any other version. Within a version, ELB for Envoy applies patch releases and operating system updates for you.

## Bootstrap configuration
<a name="how-envoy-runs-bootstrap"></a>

The configuration file that you pass as `configurationFile` is an Envoy bootstrap YAML document. ELB for Envoy accepts only the following bootstrap fields and rejects a configuration file that sets any other field. For how ELB for Envoy validates your configuration, see [Configuration validation](#how-envoy-runs-validation). To understand how Envoy structures configuration, including bootstrap and dynamic (xDS) resources, see [Envoy configuration for ELB for Envoy](envoy-configuration.md).

**Accepted bootstrap fields**

| Field | Purpose |
| --- | --- |
| `static_resources` | Statically defined listeners, clusters, and secrets. |
| `dynamic_resources` | LDS, CDS, and ADS configuration for xDS control planes. For details, see [Dynamic configuration (xDS)](#how-envoy-runs-xds). |
| `hds_config` | Health discovery service configuration for cluster endpoint health. |
| `stats_sinks` | Push Envoy statistics to your own collectors, for example the OpenTelemetry stats sink. |
| `stats_config` | Control how Envoy statistics are tagged and processed. |
| `admin` | Envoy's admin interface. For details, see [Use the Envoy admin interface securely](envoy-admin-interface.md). |
| `application_log_config` | The format of Envoy's application logs, for example structured JSON logging. |
| `cluster_manager` | Settings that apply to all upstream clusters, such as `local_cluster_name` and `upstream_bind_config`. |
| `node.cluster` | The cluster name in the node identity presented to your xDS control plane. When you omit it, ELB for Envoy uses your proxy name. The other `node` fields aren't accepted. |

ELB for Envoy delivers Envoy application logs to Amazon CloudWatch Logs (CloudWatch Logs), and you can push Envoy statistics with `stats_sinks`. For details, see [Monitor a proxy](monitoring.md).

## Configuration validation
<a name="how-envoy-runs-validation"></a>

The `CreateProxy` and `UpdateProxyConfiguration` operations validate your configuration file synchronously against the Envoy bootstrap schema of your chosen `proxyVersion`. Validation checks the following:
+ The document is well-formed YAML.
+ Unknown fields are rejected, and every `typed_config` extension type resolves against that Envoy version's API.
+ Field-level constraints declared by Envoy's protos are met.

A schema violation fails the call with a `ValidationException` that names the offending field.

Passing validation does not guarantee that the process starts. Envoy performs further checks at startup, for example that referenced files exist. Before ELB for Envoy starts or restarts Envoy, it runs `envoy --mode validate` against your full configuration. A configuration that fails this second stage is not applied. On an update, the previously running configuration keeps serving traffic.

## How ELB for Envoy runs your Envoy process
<a name="how-envoy-runs-process"></a>

Envoy runs as an unprivileged, sandboxed process:
+ The process sees a private filesystem root that contains your configuration file and extracted archive.
+ It can bind privileged ports (below 1024) directly.
+ It binds listeners on the network interface in your VPC. Your security groups control reachability.

ELB for Envoy owns the Envoy command line. It sets the node identity flags (`--service-node` to the instance ID, `--service-cluster` to your proxy name unless your bootstrap sets `node.cluster`, and `--service-zone` to the Availability Zone), the drain timers, and the log level derived from your proxy attributes. You cannot set Envoy CLI flags yourself.

## Configuration archive
<a name="how-envoy-runs-archive"></a>

If your bootstrap configuration references files on disk, such as certificates, response bodies, or xDS seed files, package them in a ZIP file and pass it as `configurationArchive`:
+ ELB for Envoy extracts the archive into the directory that Envoy sees as its filesystem root. An entry `etc/envoy/response.html` is readable at `/etc/envoy/response.html`.
+ A file named `envoy.yaml` at the archive root is ignored. The authoritative bootstrap is always the `configurationFile` that you supply.
+ When you update only the archive, ELB for Envoy moves the new files into place without restarting Envoy. Filters that read local files through a data source with a [`watched_directory`](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/base.proto#envoy-v3-api-msg-config-core-v3-datasource) pick up the new contents at runtime. This is how you rotate certificates or update file-based xDS resources without a restart.

## Configuration updates and connection draining
<a name="how-envoy-runs-draining"></a>

Updating the configuration file through the `UpdateProxyConfiguration` operation restarts Envoy using its [hot restart](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operations/hot_restart) mechanism. A new process takes over the listeners, and the old process drains existing connections before it exits. During the drain, HTTP/1.1 connections receive a `Connection: close` header and HTTP/2 connections receive `GOAWAY` frames. The drain period is fixed at 60 seconds.

ELB for Envoy does not actively close TCP and WebSocket connections during a drain. Draining relies on your clients periodically recycling connections.

Updating only the archive does not restart Envoy. You can retrieve the currently stored configuration with the `GetProxyConfigurationContents` operation. For the update procedure, see [Update a proxy configuration](update-proxy-configuration.md).

## Dynamic configuration (xDS)
<a name="how-envoy-runs-xds"></a>

ELB for Envoy supports Envoy's dynamic configuration model. Define your xDS control plane clusters in `static_resources` and point `dynamic_resources` (LDS, CDS, or ADS) at them, as you would when running Envoy yourself. ELB for Envoy does not restrict the types of dynamic updates that Envoy receives. Envoy's own semantics apply, including that statically defined resources cannot be overwritten dynamically.

To update your control plane endpoints or rotate its TLS certificates without a restart, load them from files in your configuration archive using `watched_directory` data sources, or serve them from your control plane itself.

## What ELB for Envoy adds to your configuration
<a name="how-envoy-runs-injected"></a>

ELB for Envoy injects a small set of managed elements into the configuration that Envoy loads. They apply to both statically defined resources and resources delivered over xDS. You do not need to, and cannot, configure them yourself.

Health and management extensions
ELB for Envoy adds bootstrap extensions that serve internal health and management endpoints. They run in a separate network namespace, so they do not conflict with your listeners or loopback ports.

TLS Inspector with JA3 and JA4 fingerprinting
ELB for Envoy places a [TLS Inspector](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/listener_filters/tls_inspector) listener filter, with JA3 and JA4 fingerprinting enabled, at the front of every listener's filter chain. If your configuration already declares a TLS Inspector, ELB for Envoy replaces it with the fingerprinting-enabled one. The fingerprints are used for AWS WAF inspection. For details, see [Protect a proxy with AWS WAF](waf.md).

AWS WAF filter and cluster
When a web ACL is associated with your proxy, ELB for Envoy inserts an AWS WAF filter into the HTTP filter chain of every `HttpConnectionManager` and adds a managed cluster for the AWS WAF data plane. For details, see [Protect a proxy with AWS WAF](waf.md).
