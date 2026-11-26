---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/proxy-attributes.html
---

# Proxy attributes

Proxy attributes are key-value settings that control secondary proxy behavior. Core behavior, such as networking and the Envoy configuration, is set as resource properties. Attributes cover optional features and tuning parameters.

Each attribute has a default value that applies unless you override it. You can set attributes at creation time with the `--attributes` flag on **aws elb-proxy create-proxy**. You can view attributes and their current values with **aws elb-proxy get-proxy-attributes**, and change them with **aws elb-proxy update-proxy-attributes**.

## Attribute reference
<a name="proxy-attributes-reference"></a>

The following table lists the proxy attributes, their default values, whether you can change them after you create a proxy, and their accepted values.

| Attribute key | Description | Default | Can change after creation | Accepted values |
| --- | --- | --- | --- | --- |
| waf.web\_acl\_arn | ARN of the AWS WAF web ACL associated with the proxy. An empty value means no web ACL is attached. | "" (empty) | Yes, but only through AWS WAF (aws wafv2 associate-web-acl and aws wafv2 disassociate-web-acl), not through update-proxy-attributes. | A regional AWS WAF web ACL ARN, or empty for no web ACL. |
| waf.fail\_open.enabled | Whether to allow traffic through when AWS WAF is unavailable. When false, requests are blocked if AWS WAF is unavailable. | false | Yes, through update-proxy-attributes. | true or false. |
| envoy.log\_level | The log level for the Envoy process. | warn | Yes, through update-proxy-attributes. | off, critical, error, warning (alias warn), info, debug, trace. |
| envoy.component\_log\_level | Per-component log level overrides for Envoy, as a comma-separated list of component:level pairs (for example, http:debug,router:debug). |  | Yes, through update-proxy-attributes. | Comma-separated component:level pairs. Levels use the same values as envoy.log\_level. |
| ddos\_protection.syn\_cookie.mode | Controls how the proxy applies SYN cookie mitigations for SYN flood protection. The console label is SYN cookie mode. | reactive | Yes. | reactive (turns mitigation on only when a SYN flood is detected), continuous (always on), off. |
| deletion\_protection.enabled | Prevents the proxy from being deleted accidentally. If you turn on deletion protection, you must turn it off before you can delete the proxy. The console label is Deletion protection. | false | Yes. | true, false. |

## View and change attributes
<a name="proxy-attributes-manage"></a>

To view an attribute, read it from the attribute list. To change a mutable attribute, set a new value. Changes to `waf.web_acl_arn` are made through AWS WAF, not through **update-proxy-attributes** (see [Protect a proxy with AWS WAF](waf.md)).

View and change attributes using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To view and change proxy attributes**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Select the proxy whose attributes you want to view or change.

1. Choose **Edit attributes**.

1. Change the attribute values that you want to update.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To view all attributes for a proxy, run the following command.

```
aws elb-proxy get-proxy-attributes \
  --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy, in the form `arn:aws:elasticloadbalancing:{{region}}:{{account-id}}:proxy/...`.

The response lists each attribute with its current value and its default value.

```
{
    "attributes": [
        {
            "value": "",
            "key": "waf.web_acl_arn"
        },
        {
            "defaultValue": "false",
            "value": "false",
            "key": "waf.fail_open.enabled"
        },
        {
            "defaultValue": "false",
            "value": "false",
            "key": "deletion_protection.enabled"
        }
    ]
}
```

To change one or more attributes, run the following command. Attributes that you do not specify are unchanged.

```
aws elb-proxy update-proxy-attributes \
  --proxy-identifier <proxy-arn> \
  --attributes key=envoy.log_level,value=debug
```

Replace {{proxy-arn}} with the ARN of your proxy. The response returns the attributes after the update.

------
#### [ CloudFormation ]

Set attributes on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

The `Attributes` property is a list of `Key`/`Value` pairs. The same keys shown in this page's attribute table apply.

```yaml
Properties:
  Attributes:
    - Key: deletion_protection.enabled
      Value: "true"
```

The two `waf.*` attributes are set at create time and can't be changed by a stack update. For more information about the web ACL attribute, see [Associate a web ACL when you create a proxy](waf.md#waf-associate-at-create).

------
