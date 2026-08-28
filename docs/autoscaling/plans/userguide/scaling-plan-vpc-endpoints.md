---
source_url: https://docs.aws.amazon.com/autoscaling/plans/userguide/scaling-plan-vpc-endpoints.html
---

# Access scaling plans using interface VPC endpoints
<a name="scaling-plan-vpc-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and AWS Auto Scaling. You can access AWS Auto Scaling as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access AWS Auto Scaling.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for AWS Auto Scaling.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [Create an interface VPC endpoint for scaling plans](#create-vpce-scaling-plans)
+ [Create a VPC endpoint policy for scaling plans](#create-vpce-policy-scaling-plans)
+ [Endpoint migration](#upgrading-cli-sdk-aws-as-api)

## Create an interface VPC endpoint for scaling plans
<a name="create-vpce-scaling-plans"></a>

Create an endpoint for AWS Auto Scaling scaling plans using the following service name:

```
com.amazonaws.{{region}}.autoscaling-plans
```

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

You do not need to change any other settings. AWS Auto Scaling API calls other AWS services using either service endpoints or private interface VPC endpoints, whichever are in use.

## Create a VPC endpoint policy for scaling plans
<a name="create-vpce-policy-scaling-plans"></a>

You can attach a policy to your VPC endpoint to control access to the AWS Auto Scaling API. The policy specifies:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resource on which the actions can be performed.

The following example shows a VPC endpoint policy that denies everyone permission to delete a scaling plan through the endpoint. The example policy also grants everyone permission to perform all other actions.

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
            "Action": "{{autoscaling-plans:DeleteScalingPlan}}",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

For more information, see [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

## Endpoint migration
<a name="upgrading-cli-sdk-aws-as-api"></a>

On November 22, 2019, we introduced `autoscaling-plans.{{region}}.amazonaws.com` as the new default DNS hostname and endpoint for calls to the AWS Auto Scaling API. The new endpoint is compatible with the latest release of the AWS CLI and SDKs. If you have not done so already, install the latest AWS CLI and SDKs to use the new endpoint. To update the AWS CLI, see [Installing or updating the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. For information about the AWS SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/developer/tools/).

**Important**
For backward compatibility, the existing `autoscaling.{{region}}.amazonaws.com` endpoint will continue to be supported for calls to the AWS Auto Scaling API. To set up the `autoscaling.{{region}}.amazonaws.com` endpoint as a private interface VPC endpoint, see [Amazon EC2 Auto Scaling and interface VPC endpoints](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-endpoints.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Endpoint to Call When Using the CLI or the AWS Auto Scaling API**
For the current release of AWS Auto Scaling, your calls to the AWS Auto Scaling API automatically go to the `autoscaling-plans.{{region}}.amazonaws.com` endpoint instead of `autoscaling.{{region}}.amazonaws.com`.

You can call the new endpoint in the CLI by using the following parameter with each command to specify the endpoint: `--endpoint-url https://autoscaling-plans.{{region}}.amazonaws.com`.

Although it is not recommended, you can also call the old endpoint in the CLI by using the following parameter with each command to specify the endpoint: `--endpoint-url https://autoscaling.{{region}}.amazonaws.com`.

For the various SDKs used to call the APIs, see the documentation for the SDK of interest to learn how to direct the requests to a specific endpoint. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/developer/tools/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
