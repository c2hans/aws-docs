---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/envoy-configuration.html
---

# Envoy configuration for ELB for Envoy

Envoy is a high-performance, open source edge and service proxy. You define how it listens, routes requests, and connects to upstream targets through Envoy's configuration. With Elastic Load Balancing for Envoy (ELB for Envoy), you provide that configuration and ELB for Envoy runs it on the proxy. For more information, see the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/v1.40.0/).

Envoy takes its configuration in two ways, which the following diagram shows.

![Diagram. An Envoy data plane instance holds static resources from the bootstrap file (node identity, admin port, and the xds_cluster definition) and dynamic resources held in memory: listeners (LDS), routes (RDS), upstream clusters (CDS), live endpoints (EDS), and TLS secrets (SDS). The bootstrap xds_cluster points Envoy at an xDS control plane server, such as Istio or go-control-plane, which streams the dynamic resources to Envoy over a gRPC ADS stream using the xDS API.](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/images/envoy-config.png)

Bootstrap configuration
The bootstrap file is the static configuration Envoy reads at startup: the node identity (ID and zone), the admin interface, and static resources. In ELB for Envoy, the bootstrap file is the configuration file you supply when you create or update a proxy. For the fields ELB for Envoy supports, see [Bootstrap configuration](how-envoy-runs.md#how-envoy-runs-bootstrap).

Dynamic configuration
Envoy can also receive resources at runtime and hold them in memory, updating without a restart, through discovery services: `LDS` (listeners), `RDS` (routes), `CDS` (upstream clusters), `EDS` (endpoints), and `SDS` (TLS secrets).

The xDS control plane
The discovery services are the xDS APIs, served by an xDS control plane (for example, Istio or go-control-plane). Your bootstrap file declares an `xds_cluster` that points Envoy at your control plane, and Envoy opens a gRPC stream (commonly the aggregated discovery service, ADS) that streams resource updates to keep its configuration current. You run your own xDS control plane; ELB for Envoy doesn't provide one.

This chapter describes how the proxy runs your configuration and how to update it.

**Topics**
+ [How the proxy runs Envoy](how-envoy-runs.md)
+ [Update a proxy configuration](update-proxy-configuration.md)
+ [Envoy configuration limits and unsupported features](envoy-limits.md)
+ [Use the Envoy admin interface securely](envoy-admin-interface.md)
+ [Invoke Lambda functions from a proxy](invoke-lambda.md)
