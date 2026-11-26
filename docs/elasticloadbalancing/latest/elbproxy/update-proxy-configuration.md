---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/update-proxy-configuration.html
---

# Update a proxy configuration

You update the Envoy configuration file, the configuration archive, or both for an existing proxy. Fields that you don't provide are carried forward from the current configuration unchanged. You must change at least one of the configuration file or the configuration archive.

To set or rotate the customer managed key that encrypts the proxy's configuration during an update, see [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md).

Before you begin, make sure you have the following:
+ The ARN of an existing proxy.
+ An updated Envoy configuration file, an updated configuration archive, or both.

Update a proxy configuration using the console, the AWS CLI, or AWS CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To update a proxy configuration**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose the name of the proxy that you want to update.

1. Choose **Edit configuration**.

1. Under **Proxy configuration**, for **Source**, choose how to provide the configuration file: **Select S3 bucket**, **Enter manually**, **Upload local file**, or **Reuse from existing proxy**.

1. (Optional) To update the configuration archive, expand **Advanced configurations** and provide the archive.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To update only the configuration file, run the **update-proxy-configuration** command and specify `--configuration-file`. The archive is carried forward unchanged.

```
aws elb-proxy update-proxy-configuration \
--proxy-identifier <proxy-arn> \
--configuration-file configurationBytes@=file:///tmp/envoy-updated.yaml
```

Replace {{proxy-arn}} with the ARN of your proxy, and the file path with the path to your updated configuration file.

To update only the configuration archive, specify `--configuration-archive`. The configuration file is carried forward unchanged.

```
aws elb-proxy update-proxy-configuration \
--proxy-identifier <proxy-arn> \
--configuration-archive configurationBytes@=fileb:///tmp/archive-updated.zip
```

To update both, specify both `--configuration-file` and `--configuration-archive`.

```
aws elb-proxy update-proxy-configuration \
--proxy-identifier <proxy-arn> \
--configuration-file configurationBytes@=file:///tmp/envoy-updated.yaml \
--configuration-archive configurationBytes@=fileb:///tmp/archive-updated.zip
```

To remove the configuration archive and carry the configuration file forward, specify `--reset-configuration-archive`.

```
aws elb-proxy update-proxy-configuration \
--proxy-identifier <proxy-arn> \
--reset-configuration-archive
```

**Note**
When you use AWS CLI version 2, you might need to add `--cli-binary-format raw-in-base64-out`.

The response includes `configurationMetadata` with a hash and a timestamp for each piece. Carried-forward pieces keep their original hash and timestamp.

```
{
    "configurationMetadata": {
        "configFileHash": "2d950007d4f5f50c...",
        "configArchiveHash": "fa56cf18e7b624a9...",
        "configFileLastUpdatedAt": "2026-04-27T21:42:14.074000+00:00",
        "configArchiveLastUpdatedAt": "2026-04-27T21:40:55.917000+00:00"
    }
}
```

------
#### [ CloudFormation ]

To update a proxy configuration with CloudFormation, change the `ConfigurationFile` property (and `ConfigurationArchive`, if your proxy uses one) on your `AWS::ElasticLoadBalancingProxy::Proxy` resource, and then update the stack. To remove the configuration archive, omit the `ConfigurationArchive` property.

------

## How updates are applied
<a name="update-proxy-configuration-apply"></a>

The service validates your configuration before it applies the update. A configuration that fails validation isn't applied, and the previous configuration keeps serving traffic. For more information about validation, see [Configuration validation](how-envoy-runs.md#how-envoy-runs-validation).

When you update the configuration file, the proxy restarts Envoy. The new process takes over the listeners, and the old process drains existing connections before it exits. For more information about draining, see [Configuration updates and connection draining](how-envoy-runs.md#how-envoy-runs-draining).

When you update only the configuration archive, the proxy moves the new files into place without restarting Envoy.

## Verify the update
<a name="update-proxy-configuration-verify"></a>

Verify the update using the console or the AWS CLI. Choose the tab for the method that you want to use.

------
#### [ Console ]

On the proxy details page, choose the **Configuration** tab to view the stored configuration.

------
#### [ AWS CLI ]

Run the **get-proxy-configuration-contents** command to retrieve the currently stored configuration.

```
aws elb-proxy get-proxy-configuration-contents \
--proxy-identifier <proxy-arn> \
--include-config-file
```

Replace {{proxy-arn}} with the ARN of your proxy.

------
