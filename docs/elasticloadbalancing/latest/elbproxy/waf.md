---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/waf.html
---

# Protect a proxy with AWS WAF

Elastic Load Balancing for Envoy (ELB for Envoy) can inspect the traffic that passes through a proxy with an AWS WAF web ACL. You bring your own web ACL and associate it with the proxy. ELB for Envoy never creates, owns, or deletes a web ACL for you.

Associating an AWS WAF web ACL with a proxy is optional. A proxy runs without a web ACL until you associate one. You associate or change the web ACL in the console, either in the create wizard at the **Add service integrations** step (see [Associate a web ACL when you create a proxy](#waf-associate-at-create)) or later on the proxy's **Integrations** tab (see [Associate or change the web ACL after creation](#waf-associate)). This chapter covers the association lifecycle, how inspection works, and the attributes that control it.

**Topics**
+ [Run a proxy without a web ACL](#waf-default)
+ [Associate a web ACL when you create a proxy](#waf-associate-at-create)
+ [Associate or change the web ACL after creation](#waf-associate)
+ [View the web ACL for a proxy](#waf-view)
+ [List the proxies that use a web ACL](#waf-list-resources)
+ [Remove the web ACL from a proxy](#waf-remove)
+ [Allow traffic when AWS WAF is unavailable](#waf-fail-open)
+ [How AWS WAF inspection works](#waf-inspection)
+ [AWS WAF inspection limitations](#waf-limitations)
+ [AWS WAF attributes reference](#waf-attributes)

## Run a proxy without a web ACL
<a name="waf-default"></a>

A proxy without a web ACL transitions to `active` after infrastructure provisioning completes. AWS WAF does not gate the status.

To confirm that a proxy has no web ACL, read its attributes and check that `waf.web_acl_arn` is empty.

```
aws elb-proxy get-proxy-attributes --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy. An empty `waf.web_acl_arn` value means that no web ACL is attached.

```
{
    "attributes": [
        {
            "key": "waf.web_acl_arn",
            "value": ""
        },
        {
            "key": "waf.fail_open.enabled",
            "value": "false",
            "defaultValue": "false"
        },
        {
            "key": "deletion_protection.enabled",
            "value": "false",
            "defaultValue": "false"
        },
        ...
    ]
}
```

The response lists every proxy attribute, in no fixed order. The examples on this page show the AWS WAF attributes.

## Associate a web ACL when you create a proxy
<a name="waf-associate-at-create"></a>

To protect a proxy from the start, pass your web ACL ARN with the `waf.web_acl_arn` attribute at create time. ELB for Envoy associates the web ACL synchronously using your credentials.

Before you begin, you must have the `wafv2:AssociateWebACL` permission on the web ACL resource.

Associate a web ACL at create time using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To associate a web ACL in the create wizard**

1. In the create wizard, go to the **Add service integrations** step. For the full create procedure, see [Create a proxy](create-proxy.md).

1. Under **AWS WAF**, select **Apply application layer security protections**.

1. For **Web ACL**, choose a web ACL.

1. Choose **Next**, review your settings, and then choose **Create proxy**.

------
#### [ AWS CLI ]

Add the `--attributes` option to your **create-proxy** command. For the full command, see [Create a proxy](create-proxy.md).

Fragment:

```
  --attributes key=waf.web_acl_arn,value=<web-acl-arn>
```

Replace {{web-acl-arn}} with the ARN of your web ACL. The **create-proxy** command fails immediately if the ARN is invalid, the web ACL does not exist in the Region, or you lack permission.

------
#### [ CloudFormation ]

Set the web ACL at create time through the `waf.web_acl_arn` attribute on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

```yaml
Properties:
  Attributes:
    - Key: waf.web_acl_arn
      Value: arn:aws:wafv2:us-east-1:123456789012:regional/webacl/my-acl/abc-123
```

------

## Associate or change the web ACL after creation
<a name="waf-associate"></a>

Associate a web ACL with the **associate-web-acl** command in AWS WAF, passing your proxy ARN. ELB for Envoy updates `waf.web_acl_arn` to the new ARN. This works whether the proxy currently has no web ACL or an existing one. Any previous association is replaced atomically.

Associate or change the web ACL using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To associate or change the web ACL**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose the name of your proxy to open its details page.

1. Choose the **Integrations** tab.

1. Choose **Associate a WAF resource**.

1. For **Web ACL**, choose a web ACL, and then choose **Confirm**. A proxy can have one web ACL. Associating a new one replaces the current association.

------
#### [ AWS CLI ]

Run the **associate-web-acl** command.

```
aws wafv2 associate-web-acl \
  --web-acl-arn arn:aws:wafv2:us-east-1:<account-id>:regional/webacl/my-new-acl/abc-123 \
  --resource-arn <proxy-arn> \
  --region us-east-1
```

Replace {{account-id}} with your AWS account ID, and {{proxy-arn}} with the ARN of your proxy.

The call returns an empty response on success. Afterward, **get-proxy-attributes** shows the new web ACL.

```
{
    "key": "waf.web_acl_arn",
    "value": "arn:aws:wafv2:us-east-1:<account-id>:regional/webacl/my-new-acl/abc-123"
}
```
+ Associating the web ACL that is already attached succeeds and changes nothing.
+ If the web ACL does not exist, the call fails with `WAFNonexistentItemException` and the current association is kept.

Your web ACL is always yours. ELB for Envoy only records the association and never modifies or deletes it.

------
#### [ CloudFormation ]

The `waf.web_acl_arn` attribute can't be changed by a stack update. To change the web ACL after creation, use the console or the AWS WAF **associate-web-acl** command (see the AWS CLI tab), and then reconcile your template.

------

## View the web ACL for a proxy
<a name="waf-view"></a>

View the web ACL associated with a proxy using the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To view the web ACL for a proxy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose the name of your proxy to open its details page.

1. Choose the **Integrations** tab. The **AWS WAF web ACL** field shows the associated web ACL. The field is empty when no web ACL is associated.

------
#### [ AWS CLI ]

To find the web ACL from the proxy, read the proxy attributes and look for `waf.web_acl_arn`. An empty value means that no web ACL is attached.

```
aws elb-proxy get-proxy-attributes --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy.

You can also query from the AWS WAF side with the **get-web-acl-for-resource** command.

```
aws wafv2 get-web-acl-for-resource \
  --resource-arn <proxy-arn> \
  --region us-east-1
```

Replace {{proxy-arn}} with the ARN of your proxy.

```
{
    "WebACL": {
        "Name": "my-acl",
        "Id": "abc-123",
        "ARN": "arn:aws:wafv2:us-east-1:<account-id>:regional/webacl/my-acl/abc-123",
        "DefaultAction": {
            "Allow": {}
        },
        "Rules": [ ... ],
        ...
    }
}
```

When no web ACL is attached, the response has no `WebACL` field.

------

## List the proxies that use a web ACL
<a name="waf-list-resources"></a>

You can list the proxies associated with a web ACL from the AWS WAF side.

------
#### [ AWS CLI ]

Run the **list-resources-for-web-acl** command.

```
aws wafv2 list-resources-for-web-acl \
  --web-acl-arn <web-acl-arn> \
  --resource-type ELB_PROXY \
  --region us-east-1
```

Replace {{web-acl-arn}} with the ARN of your web ACL.

```
{
    "ResourceArns": [
        "arn:aws:elasticloadbalancing:us-east-1:<account-id>:proxy/my-proxy:03cb30ca67c0385a"
    ]
}
```

The resource type for proxies is `ELB_PROXY`. Without `--resource-type`, AWS WAF lists Application Load Balancers only, so your proxies do not appear.

------

## Remove the web ACL from a proxy
<a name="waf-remove"></a>

The proxy console has no action to remove a web ACL. Remove the association from the AWS WAF console, or with the **disassociate-web-acl** command. ELB for Envoy clears `waf.web_acl_arn`, and your web ACL is untouched. ELB for Envoy never deletes a customer web ACL.

------
#### [ AWS CLI ]

Run the **disassociate-web-acl** command.

```
aws wafv2 disassociate-web-acl \
  --resource-arn <proxy-arn> \
  --region us-east-1
```

Replace {{proxy-arn}} with the ARN of your proxy.

The call returns an empty response on success, and `waf.web_acl_arn` is empty again. Calling **disassociate-web-acl** on a proxy with no web ACL attached also succeeds.

------

Deleting a proxy does not affect your web ACL. ELB for Envoy removes only the association, and your web ACL remains in your account.

The reverse is blocked. While a web ACL is associated with a proxy, AWS WAF refuses to delete the web ACL (`WAFAssociatedItemException`). Disassociate it from the proxy first.

## Allow traffic when AWS WAF is unavailable
<a name="waf-fail-open"></a>

By default, the proxy blocks requests when AWS WAF is unavailable. To let traffic through instead, set the `waf.fail_open.enabled` attribute to `true`.

**Note**
When fail open is enabled, requests pass through uninspected if AWS WAF is unavailable.

Change this behavior using the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To enable fail open**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Select your proxy, and then choose **Edit attributes**.

1. Turn on **WAF fail open**.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

Set the `waf.fail_open.enabled` attribute with the **update-proxy-attributes** command.

```
aws elb-proxy update-proxy-attributes \
  --proxy-identifier <proxy-arn> \
  --attributes key=waf.fail_open.enabled,value=true
```

Replace {{proxy-arn}} with the ARN of your proxy.

------

## How AWS WAF inspection works
<a name="waf-inspection"></a>

When you associate a web ACL, ELB for Envoy performs AWS WAF inspection inside your Envoy data plane. You do not modify your configuration to enable it. ELB for Envoy makes the following changes:
+ Inserts an AWS WAF filter into the `http_filters` chain of every `HttpConnectionManager` in your configuration, immediately before the final router filter. The filter inspects requests after your own HTTP filters run. This applies to connection managers in your bootstrap configuration and to those delivered over xDS.
+ Adds a cluster for the AWS WAF data plane to your static resources.
+ Places a TLS inspector listener filter, with JA3 and JA4 fingerprinting enabled, at the front of every listener's filter chain. If your configuration already declares a TLS inspector, ELB for Envoy replaces it with the fingerprinting-enabled one. ELB for Envoy sends the JA3 and JA4 fingerprints with each inspection request, so your web ACL rules can use them as match and aggregation keys.

For each HTTP request, the filter sends the request headers and up to the first 64 KB of the request body to AWS WAF for evaluation, and enforces the allow or block decision. If AWS WAF is unavailable, the proxy blocks requests by default. To let traffic through instead, see [Allow traffic when AWS WAF is unavailable](#waf-fail-open).

When no web ACL is associated, the filter stays inactive and adds no inspection step to your traffic.

## AWS WAF inspection limitations
<a name="waf-limitations"></a>
+ AWS WAF inspection applies to HTTP and HTTPS traffic handled by an `HttpConnectionManager`. Traffic proxied by other network filters, for example plain `tcp_proxy`, is not inspected.
+ HTTP/3 (QUIC) traffic cannot use JA3 and JA4 fingerprints with AWS WAF. The TLS inspector captures the fingerprints, and it sees only TCP connections.
+ Request body inspection is limited to the first 64 KB.

## AWS WAF attributes reference
<a name="waf-attributes"></a>

The following proxy attributes control AWS WAF protection. For how to view and change proxy attributes, see [Proxy attributes](proxy-attributes.md).

| Attribute | Default | Description |
| --- | --- | --- |
| waf.web\_acl\_arn | "" | ARN of the associated web ACL. An empty value means that no web ACL is associated. Set it at create time, or change it with the AWS WAF associate-web-acl and disassociate-web-acl commands, not with update-proxy-attributes. |
| waf.fail\_open.enabled | false | Allow traffic when AWS WAF is unavailable. Change it with the update-proxy-attributes command. |
