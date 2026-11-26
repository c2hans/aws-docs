---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/tag-proxy.html
---

# Tag a proxy

Tags are key-value pairs that you attach to a proxy to categorize it, for example by purpose, owner, or environment. In ELB for Envoy, you can add tags to a proxy, remove tags, and view the tags on a proxy. You add or remove tags with the `TagResource` and `UntagResource` operations, and view them with the `ListTagsForResource` operation.

The following tag constraints apply:
+ A tag key can be 1 to 128 characters.
+ A tag value can be 0 to 256 characters.
+ A tag key can't start with `aws:`.
+ Allowed characters are letters, numbers, spaces, and the following: `_ . : / = + - @`.
+ A proxy can have a maximum of 50 tags.

Before you tag a proxy, make sure you have the ARN of an existing proxy.

## Add tags
<a name="tag-proxy-add"></a>

Add tags using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To add tags to a proxy**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy that you want to tag to open its details page, and then choose the **Tags** tab. Alternatively, select the proxy in the **Proxies** list.

1. Choose **Manage user tags** to open the **Manage user tags** page.

1. Add a tag by entering a key and an optional value.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To add tags to a proxy, run the **tag-resource** command.

```
aws elb-proxy tag-resource \
    --cli-input-json '{
        "resourceArn": "<proxy-arn>",
        "tags": {
            "environment": "production",
            "team": "platform"
        }
    }'
```

Replace {{proxy-arn}} with the ARN of your proxy. Replace the keys and values in `tags` with the tags you want to add.

------
#### [ CloudFormation ]

Set tags on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

The `Tags` property is a map of keys to values.

```yaml
Properties:
  Tags:
    team: networking
    environment: production
```

------

## Remove tags
<a name="tag-proxy-remove"></a>

Remove tags using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To remove tags from a proxy**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy that you want to update to open its details page, and then choose the **Tags** tab. Alternatively, select the proxy in the **Proxies** list.

1. Choose **Manage user tags** to open the **Manage user tags** page.

1. Remove the tag that you no longer need.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To remove tags from a proxy, run the **untag-resource** command. Specify the tag keys you want to remove.

```
aws elb-proxy untag-resource \
    --cli-input-json '{
        "resourceArn": "<proxy-arn>",
        "tagKeys": ["environment", "team"]
    }'
```

Replace {{proxy-arn}} with the ARN of your proxy. Replace the values in `tagKeys` with the keys of the tags you want to remove.

------
#### [ CloudFormation ]

To remove a tag, delete its key from the `Tags` map on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

------

## View tags
<a name="tag-proxy-view"></a>

View tags using the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To view the tags on a proxy**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy whose tags you want to view to open its details page.

1. Choose the **Tags** tab.

------
#### [ AWS CLI ]

To view the tags on a proxy, run the **list-tags-for-resource** command.

```
aws elb-proxy list-tags-for-resource --resource-arn <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy. The response lists the proxy's tags as key-value pairs.

------
