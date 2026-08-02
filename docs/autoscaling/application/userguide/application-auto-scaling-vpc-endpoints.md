---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-vpc-endpoints.html
---

# Access Application Auto Scaling using interface VPC endpoints
<a name="application-auto-scaling-vpc-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and Application Auto Scaling. You can access Application Auto Scaling as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access Application Auto Scaling.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Application Auto Scaling.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [Create an interface VPC endpoint](#create-vpce-app-as)
+ [Create a VPC endpoint policy](#create-vpce-policy-app-as)

## Create an interface VPC endpoint
<a name="create-vpce-app-as"></a>

Create an endpoint for Application Auto Scaling using the following service name:

```
com.amazonaws.{{region}}.application-autoscaling
```

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

You do not need to change any other settings. Application Auto Scaling calls other AWS services using either service endpoints or private interface VPC endpoints, whichever are in use.

## Create a VPC endpoint policy
<a name="create-vpce-policy-app-as"></a>

You can attach a policy to your VPC endpoint to control access to the Application Auto Scaling API. The policy specifies:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resource on which the actions can be performed.

The following example shows a VPC endpoint policy that denies everyone permission to delete a scaling policy through the endpoint. The example policy also grants everyone permission to perform all other actions.

```
{
   "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "{{application-autoscaling:DeleteScalingPolicy}}",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

For more information, see [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies) in the *AWS PrivateLink Guide*.
