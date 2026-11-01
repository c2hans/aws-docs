---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_storage-gateway_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Storage Gateway examples using AWS CLI
<a name="cli_2_storage-gateway_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Storage Gateway.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `describe-gateway-information`
<a name="storage-gateway_DescribeGatewayInformation_cli_2_topic"></a>

The following code example shows how to use `describe-gateway-information`.

**AWS CLI**
**To describe a gateway**
The following `describe-gateway-information` example returns metadata about the specified gateway. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in the command.
This example specifies a gateway with the id `sgw-12A3456B` in account `123456789012`.

```
aws storagegateway describe-gateway-information \
    --gateway-arn {{"arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B"}}
```
This command outputs a JSON block that contains metadata about about the gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not).
Output:

```
{
    "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B",
    "GatewayId": "sgw-12A3456B",
    "GatewayName": "my-gateway",
    "GatewayTimezone": "GMT-8:00",
    "GatewayState": "RUNNING",
    "GatewayNetworkInterfaces": [
        {
            "Ipv4Address": "10.0.0.25"
        }
    ],
    "GatewayType": "STORED",
    "Tags": [],
    "HostEnvironment": "VMWARE",
    "EndpointType": "STANDARD"
}
```
For more information, see [Managing Your Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/managing-gateway-common.html) in the *AWS Storage Gateway Volume Gateway User Guide*.
+  For API details, see [DescribeGatewayInformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-gateway-information.html) in *AWS CLI Command Reference*.

### `list-file-shares`
<a name="storage-gateway_ListFileShares_cli_2_topic"></a>

The following code example shows how to use `list-file-shares`.

**AWS CLI**
**To list file shares**
The following `list-file-shares` example lists the file shares for the specified gateway.

```
aws storagegateway list-file-shares \
    --gateway-arn {{arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-FB02E292}}
```
Output:

```
{
    "FileShareInfoList": [
        {
            "FileShareType": "NFS",
            "FileShareARN": "arn:aws:storagegateway:us-west-2:123456789012:share/share-2FA12345",
            "FileShareId": "share-2FA12345",
            "FileShareStatus": "AVAILABLE",
            "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-FB0AAAAA"
        }
    ],
    "Marker": null
}
```
For more information, see [Managing your Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/managing-gateway-file.html) in the *Amazon S3 File Gateway User Guide*.
+  For API details, see [ListFileShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-file-shares.html) in *AWS CLI Command Reference*.

### `list-gateways`
<a name="storage-gateway_ListGateways_cli_2_topic"></a>

The following code example shows how to use `list-gateways`.

**AWS CLI**
**To list gateways for an account**
The following `list-gateways` example lists all the gateways defined for an account.

```
aws storagegateway list-gateways
```
This command outputs a JSON block that contains a list of gateway Amazon Resource Names (ARNs).
Output:

```
{
    "Gateways": [
        {
            "GatewayId": "sgw-12A3456B",
            "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B",
            "GatewayType": "STORED",
            "GatewayOperationalState": "ACTIVE",
            "GatewayName": "my-gateway",
            "HostEnvironment": "VMWARE"
        },
        {
            "GatewayId": "sgw-23B4567C",
            "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-23B4567C",
            "GatewayType": "CACHED",
            "GatewayOperationalState": "ACTIVE",
            "GatewayName": "my-cached-gateway",
            "HostEnvironment": "VMWARE"
        }
    ]
}
```
For more information, see [Understanding Storage Gateway Resources and Resource IDs](https://docs.aws.amazon.com/storagegateway/latest/vgw/storage-gateway-resource-id.html) in the *AWS Storage Gateway Volume Gateway User Guide*.
+  For API details, see [ListGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-gateways.html) in *AWS CLI Command Reference*.

### `list-volumes`
<a name="storage-gateway_ListVolumes_cli_2_topic"></a>

The following code example shows how to use `list-volumes`.

**AWS CLI**
**To list the volumes configured for a gateway**
The following `list-volumes` example returns a list of volumes configured for the specified gateway. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in the command.
This example specifies a gateway with the id `sgw-12A3456B` in account `123456789012`.

```
aws storagegateway list-volumes \
    --gateway-arn {{"arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B"}}
```
This command outputs a JSON block that a list of volumes that includes the type and ARN for each volume.
Output:

```
{
    "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B",
    "VolumeInfos": [
        {
            "VolumeARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B/volume/vol-1122AABB",
            "VolumeId": "vol-1122AABB",
            "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B",
            "GatewayId": "sgw-12A3456B",
            "VolumeType": "STORED",
            "VolumeSizeInBytes": 10737418240,
            "VolumeAttachmentStatus": "ATTACHED"
        },
        {
            "VolumeARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B/volume/vol-3344CCDD",
            "VolumeId": "vol-3344CCDD",
            "GatewayARN": "arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B",
            "GatewayId": "sgw-12A3456B",
            "VolumeType": "STORED",
            "VolumeSizeInBytes": 10737418240,
            "VolumeAttachmentStatus": "ATTACHED"
        }
    ]
}
```
For more information, see [Managing Your Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/managing-gateway-common.html) in the *AWS Storage Gateway Volume Gateway User Guide*.
+  For API details, see [ListVolumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volumes.html) in *AWS CLI Command Reference*.

### `refresh-cache`
<a name="storage-gateway_RefreshCache_cli_2_topic"></a>

The following code example shows how to use `refresh-cache`.

**AWS CLI**
**To refresh the file share cache**
The following `refresh-cache` example refreshes the cache for the specified file share.

```
aws storagegateway refresh-cache \
    --file-share-arn {{arn:aws:storagegateway:us-west-2:123456789012:share/share-2FA12345}}
```
Output:

```
{
    "FileShareARN": "arn:aws:storagegateway:us-west-2:123456789012:share/share-2FA12345",
    "NotificationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Refreshing Amazon S3 bucket object cache](https://docs.aws.amazon.com/filegateway/latest/files3/refresh-cache.html) in the *Amazon S3 File Gateway User Guide*.
+  For API details, see [RefreshCache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html) in *AWS CLI Command Reference*.
