---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/lifecycle-hooks.html
---

# Configure container lifecycle hooks
<a name="lifecycle-hooks"></a>

During a graceful container shutdown, your application should respond to a `SIGTERM` signal by starting its shutdown so that clients don't experience any downtime. Your application should run cleanup procedures such as the following:
+ Saving data
+ Closing file descriptors
+ Closing database connections
+ Completing in-flight requests gracefully
+ Exiting in a timely manner to fulfill the pod termination request

Set a grace period that is long enough for cleanup to finish. To learn how to respond to the `SIGTERM` signal, see the documentation for the programming language that you use for your application.

[Container lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) enable containers to be aware of events in their management lifecycle. Containers can run code implemented in a handler when the corresponding lifecycle hook is executed. Container lifecycle hooks provide a workaround for the asynchronous nature of Kubernetes and the cloud. This approach can prevent the loss of connections that are forwarded to the terminating pod before the ingress resource and `iptables` are updated to not send new traffic to the pod.

Container lifecycle, `Endpoint`, and `EndpointSlice` are part of different APIs. It's important to orchestrate these APIs. However, when a pod is being terminated, the Kubernetes API simultaneously notifies both the kubelet (for Container Lifecycle) and the `EndpointSlice` controller. For more information, including a diagram, see [Gracefully handle the client requests](https://docs.aws.amazon.com/eks/latest/best-practices/load-balancing.html#_gracefully_handle_the_client_requests) in the *Amazon EKS Best Practices Guide*.

When `kubelet` sends `SIGTERM` to the pod, the `EndpointSlice` controller is terminating the `EndpointSlice` object. That termination notifies the Kubernetes API servers to notify the `kube-proxy` of each node to update `iptables`. Although these actions occur at the same time, there are no dependencies or sequences between them. There is a high chance that the container receives the `SIGKILL` signal much earlier than the `kube-proxy` on each node updates the local `iptables` rules. In that case, possible scenarios include the following:
+ If your application immediately and bluntly drops the in-flight requests and connections upon receipt of `SIGTERM, `the clients see `500` errors.
+ If your application ensures that all in-flight requests and connections are processed completely upon receipt of `SIGTERM`, during the grace period, new client requests would still be sent to the application container because `iptables` rules might not be updated yet. Until the cleanup procedure closes the server socket on the container, those new requests will result in new connections. When the grace period ends, the new connections that were established after the `SIGTERM` was sent are dropped unconditionally.

To address the previous scenarios, you can implement in-app integration or the PreStop lifecycle hook. For more information, including a diagram, see [Gracefully shutdown applications](https://docs.aws.amazon.com/eks/latest/best-practices/load-balancing.html#_gracefully_shutdown_applications) in the *Amazon EKS Best Practices Guide*.

**Note**
Regardless of whether the application shuts down gracefully, or the result of the `preStop` hook, the application containers are eventually terminated at the end of the grace period through `SIGKILL`.

Use the `preStop` hook with a `sleep` command to delay sending `SIGTERM`. This will help to continue accepting the new connections while the ingress object routes them to the pod. Test the time value of the `sleep` command to ensure that any latency of Kubernetes and other application dependencies are taken into account, as shown in the following example:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      lifecycle:
        # This "sleep" preStop hook delays the Pod shutdown until
        # after the Ingress Controller removes the matching Endpoint or EndpointSlice
        preStop:
          exec:
            command:
              - /bin/sleep
              - "20"
              # This period should be turned to Ingress/Service Mesh update latency
```

For more information, see [Container hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks) in the Kubernetes documentation and [Gracefully shutdown applications](https://docs.aws.amazon.com/eks/latest/best-practices/load-balancing.html#_gracefully_shutdown_applications) in the *Amazon EKS Best Practices Guide.*
