---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/probes-checks.html
---

# Configure probes and load balancer health checks
<a name="probes-checks"></a>

Kubernetes provides several ways to perform application health checks in addition to load balancer health checks. You can run the following Kubernetes built-in probes together with the load balancer health check as a command in the pod's context or as an HTTP/TCP probe to kubelet or the host IP address.

Liveness probes and readiness probes should be different and independent (or at least with different timeout values). If an application has a temporary issue, the readiness probe will mark the pod as unready until the issue is resolved. If the liveness probe settings aren't correct, the liveness probe might terminate the pod.

## Startup probe
<a name="startup-probe"></a>

Use startup probes to protect applications that have long initialization cycles. Until the startup probe succeeds, the other probes are disabled.

You can define a maximum time that Kubernetes should wait for application startup. If, after the maximum configured time, the pod still fails the startup probes, the application is terminated, and a new pod is created.

Use startup probes when the startup time of an application is unpredictable. If you know that your application needs 10 seconds to start, use a liveness probe or a readiness probe with `initialDelaySeconds` instead.

## Liveness probe
<a name="liveness-probe"></a>

Use liveness probes to detect application issues or whether the process is running without issues. A liveness probe can detect deadlock conditions where the process continues to run but the application becomes unresponsive. When using a liveness probe, do the following:
+ Use `initialDelaySeconds` to delay the first probe.
+ Don't set the same specification for liveness and readiness probes.
+ Don't configure a liveness probe to depend on a factor that is external to your pod (for example, a database).
+ Set the liveness probe for a specific `terminationGracePeriodSeconds`. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

## Readiness probe
<a name="readiness-probe"></a>

Use a readiness probe to detect the following:
+ Whether the application is ready to accept traffic
+ Partial availability, where the application might be temporarily unavailable but is expected to be healthy again after a certain operation completes

Readiness probes help to ensure that the application configuration and dependencies are running without issues or errors, so that the application can serve traffic. However, a poorly configured readiness probe can cause an outage instead of preventing it. Readiness probes that depend on external factors, such as connectivity to a database, can cause all pods to fail the probe. Such failures can result in an outage, and they can lead to a cascading failure from a backend service to other services that used the failed pods.

## Ingress resource and load balancer health checks
<a name="health-checks"></a>

Application Load Balancer and Kubernetes `ingress` provide health-check features. For the Application Load Balancer health checks, specify the target ports and path.

**Note**
** **For the Kubernetes `ingress`, there will be a deregistration latency. The default for Application Load Balancer is 300 seconds. Consider setting up your ingress resource or load balancer health check by using the same values that you used for your readiness probe.

NGINX also provides a health check. For more information, see the [NGINX documentation](https://nginx.org/en/docs/http/load_balancing.html#nginx_load_balancing_health_checks).

Istio ingress and egress gateways don't have a health check mechanism that's comparable to the HTTP health check from NGINX. However, you can achieve similar functionality by using the [Istio circuit breaker](https://istio.io/latest/docs/tasks/traffic-management/circuit-breaking/) or `DestinationRule `outlier detection.

For more information, see [Availability and Pod Lifecycle](https://docs.aws.amazon.com/eks/latest/best-practices/load-balancing.html#_availability_and_pod_lifecycle) in the *Amazon EKS Best Practices Guide*.
