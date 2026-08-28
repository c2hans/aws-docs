---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/vpc-interface-endpoints.html
---

# AWS IoT Greengrass and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and the AWS IoT Greengrass control plane by creating an *interface VPC endpoint*. You can use this endpoint to manage components, deployments, and core devices in the AWS IoT Greengrass service. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to access AWS IoT Greengrass APIs privately without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with AWS IoT Greengrass APIs. Traffic between your VPC and AWS IoT Greengrass does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*.

**Topics**
+ [Considerations for AWS IoT Greengrass VPC endpoints](#vpc-endpoint-considerations)
+ [Create an interface VPC endpoint for AWS IoT Greengrass control plane operations](#create-vpc-endpoint-control-plane)
+ [Creating a VPC endpoint policy for AWS IoT Greengrass](#vpc-endpoint-policy)
+ [Operate an AWS IoT Greengrass core device in VPC](#vpc-operate-device-vpce)

## Considerations for AWS IoT Greengrass VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS IoT Greengrass, review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. Additionally, be aware of the following considerations:
+ AWS IoT Greengrass supports making calls to all of its control plane API actions from your VPC. The control plane includes operations such as [CreateDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html) and [ListEffectiveDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListEffectiveDeployments.html). The control plane does *not* include operations such as [ResolveComponentCandidates](device-auth.md#iot-policies) and [Discover](greengrass-discover-api.md), which are data plane operations.
+ VPC endpoints for AWS IoT Greengrass are currently not supported in AWS China Regions.

## Create an interface VPC endpoint for AWS IoT Greengrass control plane operations
<a name="create-vpc-endpoint-control-plane"></a>

You can create a VPC endpoint for the AWS IoT Greengrass control plane using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for AWS IoT Greengrass using the following service name:
+ com.amazonaws.{{region}}.greengrass

If you enable private DNS for the endpoint, you can make API requests to AWS IoT Greengrass using its default DNS name for the Region, for example, `greengrass.us-east-1.amazonaws.com`. Private DNS is enabled by default.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for AWS IoT Greengrass
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to AWS IoT Greengrass control plane operations. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that the principal can perform.
+ The resources that the principal can perform actions on.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Example: VPC endpoint policy for AWS IoT Greengrass actions**
The following is an example of an endpoint policy for AWS IoT Greengrass. When attached to an endpoint, this policy grants access to the listed AWS IoT Greengrass actions for all principals on all resources.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "greengrass:CreateDeployment",
                "greengrass:ListEffectiveDeployments"
            ],
            "Resource": "*"
        }
    ]
}
```

## Operate an AWS IoT Greengrass core device in VPC
<a name="vpc-operate-device-vpce"></a>

You can operate a Greengrass core device and perform deployments in VPC without public internet access. At a minimum, you must set up the following VPC endpoints with the corresponding DNS aliases. For more information about how to create and use VPC endpoints, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *Amazon VPC User Guide*.

**Note**
The VPC feature for automatically creating a DNS record is disabled for AWS IoT data and AWS IoT Credentials. To connect these endpoints, you must manually create a Private DNS record. For more information, see [Private DNS for interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#vpce-private-dns). For more information about AWS IoT Core VPC limitations, see [Limitations of VPC endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html#VPC-limitations).

### Prerequisites
<a name="vpc-endpoint-prerequisites"></a>
+ You must install the AWS IoT Greengrass Core software using the manual provisioning steps. For more information, see [Install AWS IoT Greengrass Core software with manual resource provisioning](manual-installation.md).

### Limitations
<a name="vpc-endpoint-limitaions"></a>
+ Operating a Greengrass core device in VPC is not supported in China Regions and AWS GovCloud (US) Regions.
+ For more information about limitations of AWS IoT data and AWS IoT credential provider VPC endpoints, see [Limitations](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html#VPC-limitations).

### Set up your Greengrass core device to operate in VPC
<a name="vpc-endpoint-operate-gg-core"></a>

1. Get the AWS IoT endpoints for your AWS account, and save them to use later. Your device uses these endpoints to connect to AWS IoT. Do the following:

   1. Get the AWS IoT data endpoint for your AWS account.

      ```
      aws iot describe-endpoint --endpoint-type iot:Data-ATS
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "endpointAddress": "{{device-data-prefix}}-ats.iot.us-west-2.amazonaws.com"
      }
      ```

   1. Get the AWS IoT credentials endpoint for your AWS account.

      ```
      aws iot describe-endpoint --endpoint-type iot:CredentialProvider
      ```

      The response looks similar to the following example, if the request succeeds.

      ```
      {
        "endpointAddress": "{{device-credentials-prefix}}.credentials.iot.us-west-2.amazonaws.com"
      }
      ```

1. Create an Amazon VPC interface for AWS IoT data and AWS IoT credentials endpoints:

   1. Navigate to the [VPC](https://console.aws.amazon.com/vpc/home#/endpoints) **Endpoints** console, under **Virtual private cloud** on the left menu, choose **Endpoints** then **Create Endpoint**.

   1. In the **Create endpoint** page, specify the following information.
      + Choose **AWS services** for **Service category**.
      + For **Service Name**, search by entering the keyword `iot`. In the list of `iot` services displayed, choose the endpoint.

        If you create a VPC endpoint for AWS IoT Core data plane, choose the AWS IoT Core data plane API endpoint for your Region. The endpoint will be of the format `com.amazonaws.{{region}}.iot.data`.

        If you create a VPC endpoint for AWS IoT Core credential provider, choose the AWS IoT Core credential provider endpoint for your Region. The endpoint will be of the format `com.amazonaws.{{region}}.iot.credentials`.
**Note**
The service name for AWS IoT Core data plane in China Region will be of the format `cn.com.amazonaws.{{region}}.iot.data`. Creating VPC endpoints for AWS IoT Core credential provider is not supported in China Region.
      + For **VPC** and **Subnets**, choose the VPC where you want to create the endpoint, and the Availability Zones (AZs) in which you want to create the endpoint network.
      + For **Enable DNS name**, make sure that **Enable for this endpoint** is not selected. Neither AWS IoT Core data plane nor AWS IoT Core credential provider supports private DNS names yet.
      + For **Security group**, choose the security groups you want to associate with the endpoint network interfaces.
      + Optionally, you can add or remove tags. Tags are name-value pairs that you use to associate with your endpoint.

   1. To create your VPC endpoint, choose **Create endpoint**.

1. After you create the AWS PrivateLink endpoint, in the **Details** tab of your endpoint, you'll see a list of DNS names. You can use one of these DNS names you created in this section to [configure your private hosted zone](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html#connect-iot-core-create-phz-lns).

1. Create an Amazon S3 endpoint. For more information, see [Create a VPC endpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#s3-creating-vpc).

1. If you are using [AWS-provided Greengrass components](https://docs.aws.amazon.com/greengrass/v2/developerguide/public-components.html), additional endpoints and configurations may be required. To view the endpoints requirements, select the component from the list of AWS-provided components and look at the Requirements section. For example, the [log manager component requirements](log-manager-component.md#log-manager-component-requirements) advise that this component must be able to perform outbound requests to the endpoint `logs.{{region}}.amazonaws.com`.

   If you are using your own component, you may need to review the dependencies and perform additional testing to determine if any additional endpoints are required.

1. In Greengrass nucleus configuration, `greengrassDataPlaneEndpoint` must be set to **iotdata**. For more information, see [Greengrass nucleus configuration](greengrass-nucleus-component.md#greengrass-nucleus-component-configuration).

1. If you are in the `us-east-1` region, set the configuration parameter `s3EndpointType` to **REGIONAL** in the Greengrass nucleus configuration. This feature is available for Greengrass nucleus versions 2.11.3 or later.

**Example: Component configuration**

```
{
"aws.greengrass.Nucleus": {
   "configuration": {
      "awsRegion": "us-east-1",
      "iotCredEndpoint": "xxxxxx.credentials.iot.region.amazonaws.com",
      "iotDataEndpoint": "xxxxxx-ats.iot.region.amazonaws.com",
      "greengrassDataPlaneEndpoint": "iotdata",
      "s3EndpointType": "REGIONAL"
      ...
     }
   }
}
```

The following table gives information about the corresponding custom private DNS aliases.

| Service | VPC endpoint service name | VPC endpoint type | Custom private DNS alias | Notes |
| --- | --- | --- | --- | --- |
| AWS IoT data | `com.amazonaws.{{region}}.iot.data` | Interface | `{{prefix}}-ats.iot.{{region}}.amazonaws.com` | The private DNS record should match your account's AWS IoT data endpoint: `aws iot describe–endpoint ––endpoint–type iot:Data-ATS`. |
| AWS IoT Credentials | `com.amazonaws.{{region}}.iot.credentials` | Interface | `{{prefix}}.credentials.iot.{{region}}.amazonaws.com` | The private DNS record should match your account AWS IoT Credentials endpoint: `aws iot describe–endpoint ––endpoint–type iot:CredentialProvider`. |
| Amazon S3 | `com.amazonaws.{{region}}.s3` | Interface |  | The DNS record is automatically created. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
