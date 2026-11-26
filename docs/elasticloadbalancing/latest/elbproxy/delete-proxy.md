---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/delete-proxy.html
---

# Delete a proxy

When you no longer need a proxy, delete it to release its resources. In ELB for Envoy, you delete a proxy with the `DeleteProxy` operation. The proxy enters the `delete-in-progress` state while its resources are cleaned up, and then it no longer appears in the output of `ListProxies`.

**Important**
Deleting a proxy is permanent and stops traffic to the proxy's DNS endpoint. You can't recover a deleted proxy. Make sure that clients no longer depend on the proxy before you delete it.

If deletion protection is turned on for the proxy, you must turn it off before you can delete the proxy. For more information, see [Proxy attributes](proxy-attributes.md).

**Note**
Deleting a proxy doesn't delete an associated web ACL. ELB for Envoy never owns your web ACL, so deleting the proxy only removes the association. The web ACL remains in your account. For more information about using a web ACL with a proxy, see [Protect a proxy with AWS WAF](waf.md).

Before you delete a proxy, make sure you have the ARN of the proxy you want to delete.

Delete the proxy using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To delete a proxy**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. In the **Proxies** list, select the proxy that you want to delete.

1. Choose **Delete proxy**.

1. In the confirmation dialog, enter **confirm**.

1. Choose **Delete**.

------
#### [ AWS CLI ]

To delete a proxy, run the **delete-proxy** command.

```
aws elb-proxy delete-proxy --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy. The response shows the proxy's `status` as `delete-in-progress`.

------
#### [ CloudFormation ]

To delete the proxy, delete the stack, or remove the `AWS::ElasticLoadBalancingProxy::Proxy` resource from your template and update the stack.

------

## Verify the deletion
<a name="delete-proxy-verify"></a>

While the proxy is being deleted, **get-proxy** shows the `delete-in-progress` state. After deletion completes, the proxy no longer appears in **list-proxies**.

```
aws elb-proxy list-proxies
```

The deleted proxy no longer appears in the output.
