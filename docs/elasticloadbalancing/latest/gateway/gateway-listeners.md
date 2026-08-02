---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html
---

# Listeners for your Gateway Load Balancers
<a name="gateway-listeners"></a>

When you create your Gateway Load Balancer, you add a *listener*. A listener is a process that checks for connection requests.

Listeners for Gateway Load Balancers listen for all IP packets across all ports. You cannot specify a protocol or port when you create a listener for a Gateway Load Balancer.

When you create a listener, you specify a rule for routing requests. This rule forwards requests to the specified target group. You can update the listener rule to forward requests to a different target group.

## Listener attributes
<a name="listener-attributes"></a>

The following are the listener attributes for Gateway Load Balancers:

`tcp.idle_timeout.seconds`
The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.

For more information, see [Update idle timeout](update-idle-timeout.md).
