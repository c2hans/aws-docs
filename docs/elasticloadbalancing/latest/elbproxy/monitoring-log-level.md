---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/monitoring-log-level.html
---

# Set the Envoy log level

The Envoy log level controls how much detail a proxy writes to its logs. You set the log level as a proxy attribute. For more information about proxy attributes, see [Proxy attributes](proxy-attributes.md).

The `envoy.log_level` attribute accepts the following levels: `off`, `critical`, `error`, `warning` (alias `warn`), `info`, `debug`, and `trace`. To set per-component levels, use the `envoy.component_log_level` attribute, which accepts comma-separated `component:level` pairs, for example `http:debug,router:debug`.

Set the log level using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To set the Envoy log level for a proxy**

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

1. In the navigation pane, choose **Proxies**.

1. Select the proxy that you want to update, and then choose **Edit attributes**.

1. Under **Envoy log level**, choose a value for **Log level**.

1. (Optional) To set per-component levels, add a **Component log level** entry with a **Component name** and a **Log level**.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To set the Envoy log level, run the **update-proxy-attributes** command and set the `envoy.log_level` attribute.

```
aws elb-proxy update-proxy-attributes \
    --proxy-identifier <proxy-arn> \
    --attributes key=envoy.log_level,value=debug
```

Replace {{proxy-arn}} with the ARN of your proxy. Replace `debug` with the level that you want.

To set per-component levels, set the `envoy.component_log_level` attribute instead.

```
aws elb-proxy update-proxy-attributes \
    --proxy-identifier <proxy-arn> \
    --attributes '[{"key":"envoy.component_log_level","value":"http:debug,router:debug"}]'
```

Replace {{proxy-arn}} with the ARN of your proxy. Replace the `component:level` pairs with the components and levels that you want.

------
#### [ CloudFormation ]

Set the Envoy log level on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

```yaml
Properties:
  Attributes:
    - Key: envoy.log_level
      Value: debug
```

------
