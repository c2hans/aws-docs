---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/vpc-interface-endpoints.html
---

# Amazon Connect Customer Profiles and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and Amazon Connect Customer Profiles by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access Amazon Connect Customer Profiles APIs without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Amazon Connect Customer Profiles APIs. Traffic between your VPC and Amazon Connect Customer Profiles does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *AWS PrivateLink Guide*.

## Considerations for Amazon Connect Customer Profiles VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon Connect Customer Profiles, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *AWS PrivateLink Guide*.

Amazon Connect Customer Profiles supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for Amazon Connect Customer Profiles
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Amazon Connect Customer Profiles service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for Amazon Connect Customer Profiles using the following service name:
+ com.amazonaws.{{region}}.profile

If you enable private DNS for the endpoint, you can make API requests to Amazon Connect Customer Profiles using its default DNS name for the Region, for example, `profile.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#access-service-though-endpoint) in the *AWS PrivateLink Guide*.

## Creating a VPC endpoint policy for Amazon Connect Customer Profiles
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon Connect Customer Profiles. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for Amazon Connect Customer Profiles actions**
The following VPC endpoint policy grants access to the listed Amazon Connect Customer Profiles actions for all principals on all resources.

```
{
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                "profile:CreateDomain",
                "profile:CreateProfile",
                "profile:UpdateProfile"
            ],
            "Resource":"*",
            "Principal":"*"
        }
    ]
}
```
