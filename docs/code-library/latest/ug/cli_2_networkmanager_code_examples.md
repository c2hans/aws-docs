---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_networkmanager_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Network Manager examples using AWS CLI
<a name="cli_2_networkmanager_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Network Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `associate-customer-gateway`
<a name="networkmanager_AssociateCustomerGateway_cli_2_topic"></a>

The following code example shows how to use `associate-customer-gateway`.

**AWS CLI**
**To associate a customer gateway**
The following `associate-customer-gateway` example associates customer gateway `cgw-11223344556677889` in the specified global network with device `device-07f6fd08867abc123`.

```
aws networkmanager associate-customer-gateway \
    --customer-gateway-arn {{arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-11223344556677889}} \
    --global-network-id {{global-network-01231231231231231}} \
    --device-id {{device-07f6fd08867abc123}}
```
Output:

```
{
    "CustomerGatewayAssociation": {
        "CustomerGatewayArn": "arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-11223344556677889",
        "GlobalNetworkId": "global-network-01231231231231231",
        "DeviceId": "device-07f6fd08867abc123",
        "State": "PENDING"
    }
}
```
For more information, see [Gateway associations in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gw-association.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [AssociateCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/associate-customer-gateway.html) in *AWS CLI Command Reference*.

### `associate-link`
<a name="networkmanager_AssociateLink_cli_2_topic"></a>

The following code example shows how to use `associate-link`.

**AWS CLI**
**To associate a link**
The following `associate-link` example associates link `link-11112222aaaabbbb1` with device `device-07f6fd08867abc123`. The link and device are in the specified global network.

```
aws networkmanager associate-link \
    --global-network-id {{global-network-01231231231231231}} \
    --device-id {{device-07f6fd08867abc123}} \
    --link-id {{link-11112222aaaabbbb1}}
```
Output:

```
{
    "LinkAssociation": {
        "GlobalNetworkId": "global-network-01231231231231231",
        "DeviceId": "device-07f6fd08867abc123",
        "LinkId": "link-11112222aaaabbbb1",
        "LinkAssociationState": "PENDING"
    }
}
```
For more information, see [Associate or disassociate a device link using AWS Network Manager](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-device-link-associate.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [AssociateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/associate-link.html) in *AWS CLI Command Reference*.

### `create-core-network`
<a name="networkmanager_CreateCoreNetwork_cli_2_topic"></a>

The following code example shows how to use `create-core-network`.

**AWS CLI**
**To create a core network**
The following `create-core-network` example creates a core network using an optional description and tags within an AWS Cloud WAN global network.

```
aws networkmanager create-core-network \
    --global-network-id {{global-network-0d59060f16a73bc41}} \
    --description {{"Main headquarters location"}} \
    --tags Key=Name,Value="New York City office"
```
Output:

```
{
    "CoreNetwork": {
        "GlobalNetworkId": "global-network-0d59060f16a73bc41",
        "CoreNetworkId": "core-network-0fab62fe438d94db6",
        "CoreNetworkArn": "arn:aws:networkmanager::123456789012:core-network/core-network-0fab62fe438d94db6",
        "Description": "Main headquarters location",
        "CreatedAt": "2022-01-10T19:53:59+00:00",
        "State": "AVAILABLE",
        "Tags": [
            {
                "Key": "Name",
                "Value": "New York City office"
            }
        ]
    }
}
```
For more information, see [Global and core networks in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-networks-working-with.html) in the *AWS Cloud WAN User Guide*.
+  For API details, see [CreateCoreNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-core-network.html) in *AWS CLI Command Reference*.

### `create-device`
<a name="networkmanager_CreateDevice_cli_2_topic"></a>

The following code example shows how to use `create-device`.

**AWS CLI**
**To create a device**
The following `create-device` example creates a device in the specified global network. The device details include a description, the type, vendor, model, and serial number.

```
aws networkmanager create-device \
    --global-network-id {{global-network-01231231231231231}} \
    --description {{"New York office device"}} \
    --type {{"office device"}} \
    --vendor {{"anycompany"}} \
    --model {{"abcabc"}} \
    --serial-number {{"1234"}}
```
Output:

```
{
    "Device": {
        "DeviceId": "device-07f6fd08867abc123",
        "DeviceArn": "arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "New York office device",
        "Type": "office device",
        "Vendor": "anycompany",
        "Model": "abcabc",
        "SerialNumber": "1234",
        "CreatedAt": 1575554005.0,
        "State": "PENDING"
    }
}
```
For more information, see [Devices in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [CreateDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-device.html) in *AWS CLI Command Reference*.

### `create-global-network`
<a name="networkmanager_CreateGlobalNetwork_cli_2_topic"></a>

The following code example shows how to use `create-global-network`.

**AWS CLI**
**To create a global network**
The following `create-global-network` examples creates a new global network. The initial state upon creation is `PENDING`.

```
aws networkmanager create-global-network
```
Output:

```
{
    "GlobalNetwork": {
        "GlobalNetworkId": "global-network-00a77fc0f722dae74",
        "GlobalNetworkArn": "arn:aws:networkmanager::123456789012:global-network/global-network-00a77fc0f722dae74",
        "CreatedAt": "2022-03-14T20:31:56+00:00",
        "State": "PENDING"
    }
}
```
For more information, see [Global networks in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [CreateGlobalNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-global-network.html) in *AWS CLI Command Reference*.

### `create-link`
<a name="networkmanager_CreateLink_cli_2_topic"></a>

The following code example shows how to use `create-link`.

**AWS CLI**
**To create a link**
The following `create-link` example creates a link in the specified global network. The link includes a description and details about the link type, bandwidth, and provider. The site ID indicates the site to which the link is associated.

```
aws networkmanager create-link \
    --global-network-id {{global-network-01231231231231231}} \
    --description {{"VPN Link"}} \
    --type {{"broadband"}} \
    --bandwidth {{UploadSpeed=10,DownloadSpeed=20}} \
    --provider {{"AnyCompany"}} \
    --site-id {{site-444555aaabbb11223}}
```
Output:

```
{
    "Link": {
        "LinkId": "link-11112222aaaabbbb1",
        "LinkArn": "arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1",
        "GlobalNetworkId": "global-network-01231231231231231",
        "SiteId": "site-444555aaabbb11223",
        "Description": "VPN Link",
        "Type": "broadband",
        "Bandwidth": {
            "UploadSpeed": 10,
            "DownloadSpeed": 20
        },
        "Provider": "AnyCompany",
        "CreatedAt": 1575555811.0,
        "State": "PENDING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [CreateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-link.html) in *AWS CLI Command Reference*.

### `create-site`
<a name="networkmanager_CreateSite_cli_2_topic"></a>

The following code example shows how to use `create-site`.

**AWS CLI**
**To create a site**
The following `create-site` example creates a site in the specified global network. The site details include a description and the location information.

```
aws networkmanager create-site \
    --global-network-id {{global-network-01231231231231231}} \
    --description {{"New York head office"}} \
    --location {{Latitude=40.7128,Longitude=-74.0060}}
```
Output:

```
{
    "Site": {
        "SiteId": "site-444555aaabbb11223",
        "SiteArn": "arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "New York head office",
        "Location": {
            "Latitude": "40.7128",
            "Longitude": "-74.0060"
        },
        "CreatedAt": 1575554300.0,
        "State": "PENDING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [CreateSite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-site.html) in *AWS CLI Command Reference*.

### `create-vpc-attachment`
<a name="networkmanager_CreateVpcAttachment_cli_2_topic"></a>

The following code example shows how to use `create-vpc-attachment`.

**AWS CLI**
**To create a VPC attachment**
The following `create-vpc-attachment` example creates a VPC attachment with IPv6 support in a core network.

```
aws networkmanager create-vpc-attachment \
    --core-network-id {{core-network-0fab62fe438d94db6}} \
    --vpc-arn {{arn:aws:ec2:us-west-2:123456789012:vpc/vpc-09f37f69e2786eeb8}}  \
    --subnet-arns {{arn:aws:ec2:us-west-2:123456789012:subnet/subnet-04ca4e010857e7bb7}} \
    --Ipv6Support=true
```
Output:

```
{
    "VpcAttachment": {
        "Attachment": {
            "CoreNetworkId": "core-network-0fab62fe438d94db6",
            "AttachmentId": "attachment-05e1da6eba87a06e6",
            "OwnerAccountId": "123456789012",
            "AttachmentType": "VPC",
            "State": "CREATING",
            "EdgeLocation": "us-west-2",
            "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-09f37f69e2786eeb8",
            "Tags": [],
            "CreatedAt": "2022-03-10T20:59:14+00:00",
            "UpdatedAt": "2022-03-10T20:59:14+00:00"
        },
        "SubnetArns": [
            "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-04ca4e010857e7bb7"
        ],
        "Options": {
            "Ipv6Support": true
        }
    }
}
```
For more information, see [Create an attachment](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-create-attachment.html) in the *Cloud WAN User Guide*.
+  For API details, see [CreateVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html) in *AWS CLI Command Reference*.

### `delete-attachment`
<a name="networkmanager_DeleteAttachment_cli_2_topic"></a>

The following code example shows how to use `delete-attachment`.

**AWS CLI**
**To delete an attachment**
The following `delete-attachment` example deletes a Connect attachment.

```
aws networkmanager delete-attachment \
    --attachment-id {{attachment-01feddaeae26ab68c}}
```
Output:

```
{
    "Attachment": {
        "CoreNetworkId": "core-network-0f4b0a9d5ee7761d1",
        "AttachmentId": "attachment-01feddaeae26ab68c",
        "OwnerAccountId": "123456789012",
        "AttachmentType": "CONNECT",
        "State": "DELETING",
        "EdgeLocation": "us-west-2",
        "ResourceArn": "arn:aws:networkmanager::123456789012:attachment/attachment-02c3964448fedf5aa",
        "CreatedAt": "2022-03-15T19:18:41+00:00",
        "UpdatedAt": "2022-03-15T19:28:59+00:00"
    }
}
```
For more information, see [Delete an AWS Cloud WAN core network attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-deleting.html) in the *Cloud WAN User Guide*.
+  For API details, see [DeleteAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-attachment.html) in *AWS CLI Command Reference*.

### `delete-core-network`
<a name="networkmanager_DeleteCoreNetwork_cli_2_topic"></a>

The following code example shows how to use `delete-core-network`.

**AWS CLI**
**To delete a core network**
The following `delete-core-network` example deletes a core network from a Cloud WAN global network.

```
aws networkmanager delete-core-network \
    --core-network-id {{core-network-0fab62fe438d94db6}}
```
Output:

```
{
    "CoreNetwork": {
        "GlobalNetworkId": "global-network-0d59060f16a73bc41",
        "CoreNetworkId": "core-network-0fab62fe438d94db6",
        "Description": "Main headquarters location",
        "CreatedAt": "2021-12-09T18:31:11+00:00",
        "State": "DELETING",
        "Segments": [
            {
                "Name": "dev",
                "EdgeLocations": [
                    "us-west-2"
                ],
                "SharedSegments": []
            }
        ],
        "Edges": [
            {
                "EdgeLocation": "us-west-2",
                "Asn": 64512,
                "InsideCidrBlocks": []
            }
        ]
    }
}
```
For more information, see [Core networks](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-networks-working-with.html) in the *Cloud WAN User Guide*.
+  For API details, see [DeleteCoreNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-core-network.html) in *AWS CLI Command Reference*.

### `delete-device`
<a name="networkmanager_DeleteDevice_cli_2_topic"></a>

The following code example shows how to use `delete-device`.

**AWS CLI**
**To delete a device**
The following `delete-device` example deletes the specified device from the specified global network.

```
aws networkmanager delete-device \
    --global-network-id {{global-network-01231231231231231}} \
    --device-id {{device-07f6fd08867abc123}}
```
Output:

```
{
    "Device": {
        "DeviceId": "device-07f6fd08867abc123",
        "DeviceArn": "arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "New York office device",
        "Type": "office device",
        "Vendor": "anycompany",
        "Model": "abcabc",
        "SerialNumber": "1234",
        "SiteId": "site-444555aaabbb11223",
        "CreatedAt": 1575554005.0,
        "State": "DELETING"
    }
}
```
For more information, see [Devices in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DeleteDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-device.html) in *AWS CLI Command Reference*.

### `delete-global-network`
<a name="networkmanager_DeleteGlobalNetwork_cli_2_topic"></a>

The following code example shows how to use `delete-global-network`.

**AWS CLI**
**To delete a global network**
The following `delete-global-network` example deletes a global network.

```
aws networkmanager delete-global-network \
    --global-network-id {{global-network-052bedddccb193b6b}}
```
Output:

```
{
    "GlobalNetwork": {
        "GlobalNetworkId": "global-network-052bedddccb193b6b",
        "GlobalNetworkArn": "arn:aws:networkmanager::123456789012:global-network/global-network-052bedddccb193b6b",
        "CreatedAt": "2021-12-09T18:19:12+00:00",
        "State": "DELETING"
    }
}
```
For more information, see [Global networks in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [DeleteGlobalNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-global-network.html) in *AWS CLI Command Reference*.

### `delete-link`
<a name="networkmanager_DeleteLink_cli_2_topic"></a>

The following code example shows how to use `delete-link`.

**AWS CLI**
**To delete a link**
The following `delete-link` example deletes the specified link from the specified global network.

```
aws networkmanager delete-link \
    --global-network-id {{global-network-01231231231231231}} \
    --link-id {{link-11112222aaaabbbb1}}
```
Output:

```
{
    "Link": {
        "LinkId": "link-11112222aaaabbbb1",
        "LinkArn": "arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1",
        "GlobalNetworkId": "global-network-01231231231231231",
        "SiteId": "site-444555aaabbb11223",
        "Description": "VPN Link",
        "Type": "broadband",
        "Bandwidth": {
            "UploadSpeed": 20,
            "DownloadSpeed": 20
        },
        "Provider": "AnyCompany",
        "CreatedAt": 1575555811.0,
        "State": "DELETING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DeleteLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-link.html) in *AWS CLI Command Reference*.

### `delete-site`
<a name="networkmanager_DeleteSite_cli_2_topic"></a>

The following code example shows how to use `delete-site`.

**AWS CLI**
**To delete a site**
The following `delete-site` example deletes the specified site (`site-444555aaabbb11223`) in the specified global network.

```
aws networkmanager delete-site \
    --global-network-id {{global-network-01231231231231231}} \
    --site-id {{site-444555aaabbb11223}}
```
Output:

```
{
    "Site": {
        "SiteId": "site-444555aaabbb11223",
        "SiteArn": "arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "New York head office",
        "Location": {
            "Latitude": "40.7128",
            "Longitude": "-74.0060"
        },
        "CreatedAt": 1575554300.0,
        "State": "DELETING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DeleteSite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-site.html) in *AWS CLI Command Reference*.

### `deregister-transit-gateway`
<a name="networkmanager_DeregisterTransitGateway_cli_2_topic"></a>

The following code example shows how to use `deregister-transit-gateway`.

**AWS CLI**
**To deregister a transit gateway from a global network**
The following `deregister-transit-gateway` example deregisters the specified transit gateway from the specified global network.

```
aws networkmanager deregister-transit-gateway \
    --global-network-id {{global-network-01231231231231231}} \
    --transit-gateway-arn {{arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc}}
```
Output:

```
{
    "TransitGatewayRegistration": {
        "GlobalNetworkId": "global-network-01231231231231231",
        "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc",
        "State": {
            "Code": "DELETING"
        }
    }
}
```
For more information, see [Transit Gateway Registrations](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-registrations.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DeregisterTransitGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/deregister-transit-gateway.html) in *AWS CLI Command Reference*.

### `describe-global-networks`
<a name="networkmanager_DescribeGlobalNetworks_cli_2_topic"></a>

The following code example shows how to use `describe-global-networks`.

**AWS CLI**
**To describe your global networks**
The following `describe-global-networks` example describes all of your global networks in your account.

```
aws networkmanager describe-global-networks
```
Output:

```
{
    "GlobalNetworks": [
        {
            "GlobalNetworkId": "global-network-01231231231231231",
            "GlobalNetworkArn": "arn:aws:networkmanager::123456789012:global-network/global-network-01231231231231231",
            "Description": "Company 1 global network",
            "CreatedAt": 1575553525.0,
            "State": "AVAILABLE"
        }
    ]
}
```
For more information, see [Global networks in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [DescribeGlobalNetworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/describe-global-networks.html) in *AWS CLI Command Reference*.

### `disassociate-customer-gateway`
<a name="networkmanager_DisassociateCustomerGateway_cli_2_topic"></a>

The following code example shows how to use `disassociate-customer-gateway`.

**AWS CLI**
**To disassociate a customer gateway**
The following `disassociate-customer-gateway` example disassociates the specified customer gateway (`cgw-11223344556677889`) from the specified global network.

```
aws networkmanager disassociate-customer-gateway \
    --global-network-id {{global-network-01231231231231231}} \
    --customer-gateway-arn {{arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-11223344556677889}}
```
Output:

```
{
    "CustomerGatewayAssociation": {
        "CustomerGatewayArn": "arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-11223344556677889",
        "GlobalNetworkId": "global-network-01231231231231231",
        "DeviceId": "device-07f6fd08867abc123",
        "State": "DELETING"
    }
}
```
For more information, see [Gateway associations in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gw-association.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DisassociateCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/disassociate-customer-gateway.html) in *AWS CLI Command Reference*.

### `disassociate-link`
<a name="networkmanager_DisassociateLink_cli_2_topic"></a>

The following code example shows how to use `disassociate-link`.

**AWS CLI**
**To disassociate a link**
The following `disassociate-link` example disassociates the specified link from device `device-07f6fd08867abc123` in the specified global network.

```
aws networkmanager disassociate-link \
    --global-network-id {{global-network-01231231231231231}} \
    --device-id {{device-07f6fd08867abc123}} \
    --link-id {{link-11112222aaaabbbb1}}
```
Output:

```
{
    "LinkAssociation": {
        "GlobalNetworkId": "global-network-01231231231231231",
        "DeviceId": "device-07f6fd08867abc123",
        "LinkId": "link-11112222aaaabbbb1",
        "LinkAssociationState": "DELETING"
    }
}
```
For more information, see [Associate or disassociate a device link using AWS Network Manager](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-device-link-associate.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [DisassociateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/disassociate-link.html) in *AWS CLI Command Reference*.

### `get-customer-gateway-associations`
<a name="networkmanager_GetCustomerGatewayAssociations_cli_2_topic"></a>

The following code example shows how to use `get-customer-gateway-associations`.

**AWS CLI**
**To get your customer gateway associations**
The following `get-customer-gateway-associations` example gets the customer gateway associations for the specified global network.

```
aws networkmanager get-customer-gateway-associations \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "CustomerGatewayAssociations": [
        {
            "CustomerGatewayArn": "arn:aws:ec2:us-west-2:123456789012:customer-gateway/cgw-11223344556677889",
            "GlobalNetworkId": "global-network-01231231231231231",
            "DeviceId": "device-07f6fd08867abc123",
            "State": "AVAILABLE"
        }
    ]
}
```
For more information, see [Associate a customer gateway using AWS Network Manager](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-associate.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetCustomerGatewayAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-customer-gateway-associations.html) in *AWS CLI Command Reference*.

### `get-devices`
<a name="networkmanager_GetDevices_cli_2_topic"></a>

The following code example shows how to use `get-devices`.

**AWS CLI**
**To get your devices**
The following `get-devices` example gets the devices in the specified global network.

```
aws networkmanager get-devices \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "Devices": [
        {
            "DeviceId": "device-07f6fd08867abc123",
            "DeviceArn": "arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123",
            "GlobalNetworkId": "global-network-01231231231231231",
            "Description": "NY office device",
            "Type": "office device",
            "Vendor": "anycompany",
            "Model": "abcabc",
            "SerialNumber": "1234",
            "CreatedAt": 1575554005.0,
            "State": "AVAILABLE"
        }
    ]
}
```
For more information, see [Devices in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-devices.html) in *AWS CLI Command Reference*.

### `get-link-associations`
<a name="networkmanager_GetLinkAssociations_cli_2_topic"></a>

The following code example shows how to use `get-link-associations`.

**AWS CLI**
**To get your link associations**
The following `get-link-associations` example gets the link associations in the specified global network.

```
aws networkmanager get-link-associations \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "LinkAssociations": [
        {
            "GlobalNetworkId": "global-network-01231231231231231",
            "DeviceId": "device-07f6fd08867abc123",
            "LinkId": "link-11112222aaaabbbb1",
            "LinkAssociationState": "AVAILABLE"
        }
    ]
}
```
For more information, see [Associate or disassociate a device link using AWS Network Manager](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-device-link-associate.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetLinkAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-link-associations.html) in *AWS CLI Command Reference*.

### `get-links`
<a name="networkmanager_GetLinks_cli_2_topic"></a>

The following code example shows how to use `get-links`.

**AWS CLI**
**To get your links**
The following `get-links` example gets the links in the specified global network.

```
aws networkmanager get-links \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "Links": [
        {
            "LinkId": "link-11112222aaaabbbb1",
            "LinkArn": "arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1",
            "GlobalNetworkId": "global-network-01231231231231231",
            "SiteId": "site-444555aaabbb11223",
            "Description": "VPN Link",
            "Type": "broadband",
            "Bandwidth": {
                "UploadSpeed": 10,
                "DownloadSpeed": 20
            },
            "Provider": "AnyCompany",
            "CreatedAt": 1575555811.0,
            "State": "AVAILABLE"
        }
    ]
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetLinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-links.html) in *AWS CLI Command Reference*.

### `get-sites`
<a name="networkmanager_GetSites_cli_2_topic"></a>

The following code example shows how to use `get-sites`.

**AWS CLI**
**To get your sites**
The following `get-sites` example gets the sites in the specified global network.

```
aws networkmanager get-sites \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "Sites": [
        {
            "SiteId": "site-444555aaabbb11223",
            "SiteArn": "arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223",
            "GlobalNetworkId": "global-network-01231231231231231",
            "Description": "NY head office",
            "Location": {
                "Latitude": "40.7128",
                "Longitude": "-74.0060"
            },
            "CreatedAt": 1575554528.0,
            "State": "AVAILABLE"
        }
    ]
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetSites](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-sites.html) in *AWS CLI Command Reference*.

### `get-transit-gateway-registrations`
<a name="networkmanager_GetTransitGatewayRegistrations_cli_2_topic"></a>

The following code example shows how to use `get-transit-gateway-registrations`.

**AWS CLI**
**To get your transit gateway registrations**
The following `get-transit-gateway-registrations` example gets the transit gateways that are registered to the specified global network.

```
aws networkmanager get-transit-gateway-registrations \
    --global-network-id {{global-network-01231231231231231}}
```
Output:

```
{
    "TransitGatewayRegistrations": [
        {
            "GlobalNetworkId": "global-network-01231231231231231",
            "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc",
            "State": {
                "Code": "AVAILABLE"
            }
        }
    ]
}
```
For more information, see [Transit gateway registrations in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/tgw-registrations.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [GetTransitGatewayRegistrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-transit-gateway-registrations.html) in *AWS CLI Command Reference*.

### `get-vpc-attachment`
<a name="networkmanager_GetVpcAttachment_cli_2_topic"></a>

The following code example shows how to use `get-vpc-attachment`.

**AWS CLI**
**To get a VPC attachment**
The following `get-vpc-attachment` example returns information about a VPC attachment.

```
aws networkmanager get-vpc-attachment \
    --attachment-id  {{attachment-03b7ea450134787da}}
```
Output:

```
{
    "VpcAttachment": {
        "Attachment": {
            "CoreNetworkId": "core-network-0522de1b226a5d7b3",
            "AttachmentId": "attachment-03b7ea450134787da",
            "OwnerAccountId": "123456789012",
            "AttachmentType": "VPC",
            "State": "CREATING",
            "EdgeLocation": "us-west-2",
            "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-a7c4bbda",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "DevVPC"
                }
            ],
            "CreatedAt": "2022-03-11T17:48:58+00:00",
            "UpdatedAt": "2022-03-11T17:48:58+00:00"
        },
        "SubnetArns": [
            "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-202cde6c",
            "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-e5022dba",
            "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-2387ae02",
            "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-cda9dffc"
        ],
        "Options": {
            "Ipv6Support": false
        }
    }
}
```
For more information, see [Attachments in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-attachment.html) in the *Cloud WAN User Guide*.
+  For API details, see [GetVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-vpc-attachment.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="networkmanager_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list the tags for a resource**
The following `list-tags-for-resource` example lists the tags for the specified device resource (`device-07f6fd08867abc123`).

```
aws networkmanager list-tags-for-resource \
    --resource-arn {{arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123}}
```
Output:

```
{
    "TagList": [
        {
            "Key": "Network",
            "Value": "Northeast"
        }
    ]
}
```
For more information, see [Resource tags in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `register-transit-gateway`
<a name="networkmanager_RegisterTransitGateway_cli_2_topic"></a>

The following code example shows how to use `register-transit-gateway`.

**AWS CLI**
**To register a transit gateway in a global network**
The following `register-transit-gateway` example registers transit gateway `tgw-123abc05e04123abc` in the specified global network.

```
aws networkmanager register-transit-gateway \
    --global-network-id {{global-network-01231231231231231}} \
    --transit-gateway-arn {{arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc}}
```
Output:

```
{
    "TransitGatewayRegistration": {
        "GlobalNetworkId": "global-network-01231231231231231",
        "TransitGatewayArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-123abc05e04123abc",
        "State": {
            "Code": "PENDING"
        }
    }
}
```
For more information, see [Transit Gateway Registrations](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-registrations.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [RegisterTransitGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/register-transit-gateway.html) in *AWS CLI Command Reference*.

### `reject-attachment`
<a name="networkmanager_RejectAttachment_cli_2_topic"></a>

The following code example shows how to use `reject-attachment`.

**AWS CLI**
**To reject an attachment**
The following `reject-attachment` example rejects a VPC attachment request.

```
aws networkmanager reject-attachment \
    --attachment-id  {{attachment-03b7ea450134787da}}
```
Output:

```
{
    "Attachment": {
        "CoreNetworkId": "core-network-0522de1b226a5d7b3",
        "AttachmentId": "attachment-03b7ea450134787da",
        "OwnerAccountId": "123456789012",
        "AttachmentType": "VPC",
        "State": "AVAILABLE",
        "EdgeLocation": "us-west-2",
        "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-a7c4bbda",
        "CreatedAt": "2022-03-11T17:48:58+00:00",
        "UpdatedAt": "2022-03-11T17:51:25+00:00"
    }
}
```
For more information, see [Accept or reject an AWS Cloud WAN core network attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-acceptance.html) in the *Cloud WAN User Guide*.
+  For API details, see [RejectAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/reject-attachment.html) in *AWS CLI Command Reference*.

### `start-route-analysis`
<a name="networkmanager_StartRouteAnalysis_cli_2_topic"></a>

The following code example shows how to use `start-route-analysis`.

**AWS CLI**
**To start route analysis**
The following `start-route-analysis` example starts the analysis between a source and destination, including the optional `include-return-path`.

```
aws networkmanager start-route-analysis \
    --global-network-id {{global-network-00aa0aaa0b0aaa000}} \
    --source {{TransitGatewayAttachmentArn=arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-0d4a2d491bf68c093,IpAddress=10.0.0.0}} \
    --destination {{TransitGatewayAttachmentArn=arn:aws:ec2:us-west-1:123456789012:transit-gateway-attachment/tgw-attach-002577f30bb181742,IpAddress=11.0.0.0}} \
    --include-return-path
```
Output:

```
{
    "RouteAnalysis": {
        "GlobalNetworkId": "global-network-00aa0aaa0b0aaa000",
        "OwnerAccountId": "1111222233333",
        "RouteAnalysisId": "a1873de1-273c-470c-1a2bc2345678",
        "StartTimestamp": 1695760154.0,
        "Status": "RUNNING",
        "Source": {
            "TransitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1234567890abcdef0",
            "TransitGatewayArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-abcdef01234567890",
            "IpAddress": "10.0.0.0"
        },
        "Destination": {
            "TransitGatewayAttachmentArn": "arn:aws:ec2:us-west-1:123456789111:transit-gateway-attachment/tgw-attach-021345abcdef6789",
            "TransitGatewayArn": "arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-09876543210fedcba0",
            "IpAddress": "11.0.0.0"
        },
        "IncludeReturnPath": true,
        "UseMiddleboxes": false
    }
}
```
For more information, see [Route Analyzer](https://docs.aws.amazon.com/network-manager/latest/tgwnm/route-analyzer.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [StartRouteAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/start-route-analysis.html) in *AWS CLI Command Reference*.

### `tag-resource`
<a name="networkmanager_TagResource_cli_2_topic"></a>

The following code example shows how to use `tag-resource`.

**AWS CLI**
**To apply tags to a resource**
The following `tag-resource` example applies the tag `Network=Northeast` to the device `device-07f6fd08867abc123`.

```
aws networkmanager tag-resource \
    --resource-arn {{arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123}} \
    --tags {{Key=Network,Value=Northeast}}
```
This command produces no output.
For more information, see [Resource tags in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/tag-resource.html) in *AWS CLI Command Reference*.

### `untag-resource`
<a name="networkmanager_UntagResource_cli_2_topic"></a>

The following code example shows how to use `untag-resource`.

**AWS CLI**
**To remove tags from a resource**
The following `untag-resource` example removes the tag with the key `Network` from the device `device-07f6fd08867abc123`.

```
aws networkmanager untag-resource \
    --resource-arn {{arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123}} \
    --tag-keys {{Network}}
```
This command produces no output.
For more information, see [Resource tags in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html) in the *AWS Global Networks for Transit Gateways User Guide*.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/untag-resource.html) in *AWS CLI Command Reference*.

### `update-device`
<a name="networkmanager_UpdateDevice_cli_2_topic"></a>

The following code example shows how to use `update-device`.

**AWS CLI**
**To update a device**
The following `update-device` example updates device `device-07f6fd08867abc123` by specifying a site ID for the device.

```
aws networkmanager update-device \
    --global-network-id {{global-network-01231231231231231}} \
    --device-id {{device-07f6fd08867abc123}} \
    --site-id {{site-444555aaabbb11223}}
```
Output:

```
{
    "Device": {
        "DeviceId": "device-07f6fd08867abc123",
        "DeviceArn": "arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "NY office device",
        "Type": "Office device",
        "Vendor": "anycompany",
        "Model": "abcabc",
        "SerialNumber": "1234",
        "SiteId": "site-444555aaabbb11223",
        "CreatedAt": 1575554005.0,
        "State": "UPDATING"
    }
}
```
For more information, see [Devices in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [UpdateDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html) in *AWS CLI Command Reference*.

### `update-global-network`
<a name="networkmanager_UpdateGlobalNetwork_cli_2_topic"></a>

The following code example shows how to use `update-global-network`.

**AWS CLI**
**To update a global network**
The following `update-global-network` example updates the description for global network `global-network-01231231231231231`.

```
aws networkmanager update-global-network \
    --global-network-id {{global-network-01231231231231231}} \
    --description {{"Head offices"}}
```
Output:

```
{
    "GlobalNetwork": {
        "GlobalNetworkId": "global-network-01231231231231231",
        "GlobalNetworkArn": "arn:aws:networkmanager::123456789012:global-network/global-network-01231231231231231",
        "Description": "Head offices",
        "CreatedAt": 1575553525.0,
        "State": "UPDATING"
    }
}
```
For more information, see [Global Networks](https://docs.aws.amazon.com/vpc/latest/tgw/global-networks.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [UpdateGlobalNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-global-network.html) in *AWS CLI Command Reference*.

### `update-link`
<a name="networkmanager_UpdateLink_cli_2_topic"></a>

The following code example shows how to use `update-link`.

**AWS CLI**
**To update a link**
The following `update-link` example updates the bandwidth information for link `link-11112222aaaabbbb1`.

```
aws networkmanager update-link \
    --global-network-id {{global-network-01231231231231231}} \
    --link-id {{link-11112222aaaabbbb1}} \
    --bandwidth {{UploadSpeed=20,DownloadSpeed=20}}
```
Output:

```
{
    "Link": {
        "LinkId": "link-11112222aaaabbbb1",
        "LinkArn": "arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1",
        "GlobalNetworkId": "global-network-01231231231231231",
        "SiteId": "site-444555aaabbb11223",
        "Description": "VPN Link",
        "Type": "broadband",
        "Bandwidth": {
            "UploadSpeed": 20,
            "DownloadSpeed": 20
        },
        "Provider": "AnyCompany",
        "CreatedAt": 1575555811.0,
        "State": "UPDATING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [UpdateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-link.html) in *AWS CLI Command Reference*.

### `update-site`
<a name="networkmanager_UpdateSite_cli_2_topic"></a>

The following code example shows how to use `update-site`.

**AWS CLI**
**To update a site**
The following `update-site` example updates the description for site `site-444555aaabbb11223` in the specified global network.

```
aws networkmanager update-site \
    --global-network-id {{global-network-01231231231231231}} \
    --site-id {{site-444555aaabbb11223}} \
    --description {{"New York Office site"}}
```
Output:

```
{
    "Site": {
        "SiteId": "site-444555aaabbb11223",
        "SiteArn": "arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "New York Office site",
        "Location": {
            "Latitude": "40.7128",
            "Longitude": "-74.0060"
        },
        "CreatedAt": 1575554528.0,
        "State": "UPDATING"
    }
}
```
For more information, see [Sites and links in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html) in the *Transit Gateway Network Manager Guide*.
+  For API details, see [UpdateSite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-site.html) in *AWS CLI Command Reference*.
