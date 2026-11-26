---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/kubernetes-overview.html
---

# Overview

Envoy Gateway normally runs Envoy as pods that you own. You handle their sizing, scaling, upgrades, and CVE patching. With Elastic Load Balancing for Envoy (ELB for Envoy), ELB for Envoy runs those Envoy proxies for you. You keep the Kubernetes Gateway API and Envoy Gateway for routing and policy.

## How it works
<a name="kubernetes-overview-how-it-works"></a>

An open source controller, `elb-envoy-remote-infra-provider`, implements Envoy Gateway's remote infrastructure provider API. The controller runs as a sidecar in the Envoy Gateway pod and communicates with Envoy Gateway over a Unix domain socket.

For each Gateway, the controller provisions one ELB for Envoy proxy through the ELB for Envoy API. In Envoy Gateway's merged-gateways mode, it provisions one proxy for each GatewayClass instead. The controller generates the proxy's bootstrap configuration so that the proxy connects back to Envoy Gateway's xDS server. Envoy Gateway then keeps pushing routing configuration to the proxy over xDS.

The controller also handles the AWS networking around the proxy. It discovers or uses your subnets, creates and maintains security groups, and opens the node security group rules that your backends need. It publishes the proxy's address on the Gateway status. When you delete the Gateway, the controller deletes the proxy and the security groups that it created.

![Diagram of Envoy Gateway running on ELB for Envoy. In Amazon EKS, you apply Gateway API resources, such as Gateway and HTTPRoute, with kubectl. The Envoy Gateway pod runs Envoy Gateway as the xDS server, alongside the remote infrastructure provider. The remote infrastructure provider calls the ELB for Envoy API operation CreateProxy, which creates a proxy across three Availability Zones in the ELB for Envoy service account. The proxy receives its routing configuration from Envoy Gateway over xDS. Clients send traffic to the proxy, which forwards it to your pods in the cluster.](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/images/eks_white_v2.png)

## The ELBProxyConfiguration resource
<a name="kubernetes-overview-elbproxyconfiguration"></a>

You opt a Gateway in with one custom resource, `ELBProxyConfiguration`. It's a Gateway API policy that attaches to a Gateway or a GatewayClass through `targetRefs`. The resource carries the AWS settings for the proxy: the proxy's IAM role (`roleArn`), IPv4 and IPv6 addressing, subnets, security groups, tags, and proxy attributes. The controller doesn't touch Gateways that have no `ELBProxyConfiguration`.

## Requirements at a glance
<a name="kubernetes-overview-requirements"></a>

To use ELB for Envoy with Envoy Gateway, you need the following:
+ Amazon EKS, with a Kubernetes version that your Envoy Gateway release supports.
+ Envoy Gateway, configured as a remote infrastructure provider, with its own leader election disabled.
+ Pod IPs that are routable in the VPC, for example with the Amazon VPC CNI.

**Note**
This integration is in early development. The API version is `v1alpha1`.

## Key differences
<a name="kubernetes-overview-differences"></a>

Because the proxy runs on ELB for Envoy instead of in your cluster, a few things differ from in-cluster Envoy. ELB for Envoy runs and scales the proxy, so Kubernetes replica and autoscaling settings don't apply. Access logs must use a network sink, either OpenTelemetry or ALS, rather than a file sink. Global rate limiting isn't supported, so use local rate limiting instead.

## Operating it
<a name="kubernetes-overview-operating"></a>

The `ELBProxyConfiguration` reports whether it is attached to its targets. Problems appear as Warning events on the Gateway, such as a configuration that the API rejects, or an IP addressing change that requires recreating the proxy.

The CRD validates settings up front and rejects what the ELB for Envoy API would reject. For example, it rejects an invalid IPv4 and IPv6 combination, a single subnet, or a change to the proxy role after creation. You find out at `kubectl apply` rather than minutes later.

You can attach an `ELBProxyConfiguration` to one Gateway or to a whole GatewayClass. In merged-gateways mode, all Gateways in a class share one proxy.
