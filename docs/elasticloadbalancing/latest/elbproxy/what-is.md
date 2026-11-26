---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/what-is.html
---

# What is Elastic Load Balancing for Envoy?

Elastic Load Balancing for Envoy (ELB for Envoy) runs the open source [Envoy](https://www.envoyproxy.io/docs) for you. You provide your Envoy configuration, and ELB for Envoy provisions the proxy, scales it with traffic, patches the operating system, and maintains high availability across Availability Zones. The proxy runs in your virtual private cloud (VPC), so you keep control of your network, security groups, and AWS Identity and Access Management (IAM) permissions. You can optionally associate an AWS WAF web ACL to inspect proxy traffic.

ELB for Envoy is part of the Elastic Load Balancing family, alongside Application Load Balancers and Network Load Balancers. Application Load Balancer and Network Load Balancer are the right choice for most standard load balancing needs. ELB for Envoy is for customers who need Envoy's full feature set and programmable data plane delivered as a managed service.

**Topics**
+ [How ELB for Envoy works](#what-is-how-it-works)
+ [Your responsibilities and the service's responsibilities](#what-is-responsibilities)
+ [Features of ELB for Envoy](#what-is-features)
+ [Related services](#what-is-related-services)
+ [Accessing ELB for Envoy](#what-is-accessing)
+ [First-time users](#what-is-first-time-users)

## How ELB for Envoy works
<a name="what-is-how-it-works"></a>

A proxy is the resource you create. It's a single point of contact for your clients, and it runs Envoy with the configuration you provide.

When you create a proxy, you provide the following:
+ A configuration file, which is your Envoy bootstrap YAML.
+ (Optional) A configuration archive, which is a ZIP file of supporting files that your configuration references.
+ A proxy version, which is the Envoy version the proxy runs.
+ A proxy role, which is an IAM role that the proxy uses to publish logs and call other AWS services.
+ At least two subnets in different Availability Zones of the same VPC.
+ At least one security group.
+ An IP addressing configuration for IPv4 and IPv6.

ELB for Envoy runs your configuration on ELB for Envoy nodes that it manages. It gives your proxy a unique DNS name that points to IP addresses in your VPC. Your security groups control the traffic that reaches the proxy. ELB for Envoy maintains high availability across the Availability Zones you select and scales the proxy as traffic changes.

For details about proxy states, IP address types, and DNS names, see [How proxies work](how-proxies-work.md).

## Your responsibilities and the service's responsibilities
<a name="what-is-responsibilities"></a>

You're responsible for the following:
+ Making sure that your Envoy configuration is correct.
+ Setting up the debugging and visibility tools that you need.
+ Tuning your configuration for performance.

ELB for Envoy is responsible for the following:
+ Measuring the load on your proxy and scaling it to handle more traffic.
+ Operating your proxy with high availability.
+ Applying regular operating system patches.
+ Qualifying new open source Envoy releases.

## Features of ELB for Envoy
<a name="what-is-features"></a>

Your Envoy configuration
Bring an Envoy bootstrap configuration file and an optional configuration archive. Your proxy can also receive configuration from your own control plane over xDS. For details, see [How the proxy runs Envoy](how-envoy-runs.md).

Programmable extensions
Use Lua scripts and WebAssembly (Wasm) filters in your configuration. Lua runs with a restricted set of standard libraries, and Wasm runs on the V8 runtime only. For details, see [Envoy configuration limits and unsupported features](envoy-limits.md).

Automatic scaling and high availability
ELB for Envoy scales your proxy as traffic changes and runs it across at least two Availability Zones.

Network control
Your proxy runs in your VPC with your security groups. You choose internet-facing or internal addressing for IPv4 and IPv6 independently, including dual-stack.

TLS with AWS Certificate Manager
Associate AWS Certificate Manager (ACM) certificates with your proxy and reference them in your listeners. For details, see [Terminate TLS with an ACM certificate](tls-acm-certificate.md).

AWS WAF protection
Associate your own AWS WAF web ACL with a proxy to inspect its traffic. For details, see [Protect a proxy with AWS WAF](waf.md).

Configuration encryption
ELB for Envoy encrypts your configuration with an AWS owned key by default. You can use your own AWS Key Management Service (AWS KMS) customer managed key instead. For details, see [Security in ELB for Envoy](security.md).

Kubernetes integration
Use ELB for Envoy proxies with Envoy Gateway in your Kubernetes cluster. For details, see [Use ELB for Envoy with Kubernetes](kubernetes.md).

Monitoring
The proxy publishes metrics to Amazon CloudWatch and Envoy logs to Amazon CloudWatch Logs. For details, see [Monitor a proxy](monitoring.md).

## Related services
<a name="what-is-related-services"></a>

Elastic Load Balancing
ELB for Envoy is part of Elastic Load Balancing. For standard load balancing, see the [User Guide for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) and the [User Guide for Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/).

Amazon EC2 and Amazon VPC
Your proxy runs in your VPC. Security groups control the traffic that reaches it.

AWS Certificate Manager
Provides the certificates that your proxy uses to terminate TLS.

AWS WAF
Inspects the traffic that passes through your proxy when you associate a web ACL.

AWS Key Management Service
Encrypts your proxy configuration with a customer managed key that you choose.

Amazon CloudWatch
Collects your proxy metrics and Envoy logs.

AWS CloudTrail
Records ELB for Envoy API calls in your account. For details, see [Security in ELB for Envoy](security.md).

AWS Identity and Access Management
Controls who can manage your proxies, and provides the proxy role that your proxy uses.

## Accessing ELB for Envoy
<a name="what-is-accessing"></a>

AWS Management Console
In the Amazon EC2 console, choose **Proxies** in the navigation pane.

AWS Command Line Interface (AWS CLI)
Use the **aws elb-proxy** commands. For setup steps, see [Set up ELB for Envoy](setting-up.md).

AWS SDKs and the ELB for Envoy API
Call the ELB for Envoy API directly or through an AWS SDK. For details, see the [*Elastic Load Balancing for Envoy API Reference*](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/).

Kubernetes
Manage proxies from your cluster with Envoy Gateway. For details, see [Use ELB for Envoy with Kubernetes](kubernetes.md).

## First-time users
<a name="what-is-first-time-users"></a>

If you're new to ELB for Envoy, start with the following sections:

1. [Set up ELB for Envoy](setting-up.md)

1. [Get started: create your first proxy](getting-started.md)

1. [How proxies work](how-proxies-work.md)

1. [How the proxy runs Envoy](how-envoy-runs.md)
