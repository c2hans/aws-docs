---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/vpc-interface-endpoints.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Access Amazon WorkSpaces Thin Client by using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and Amazon WorkSpaces Thin Client. You can access WorkSpaces Thin Client as a VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't require public IP addresses to access WorkSpaces Thin Client.

You establish this private connection by creating an *interface endpoint* that's powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for WorkSpaces Thin Client.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Considerations for WorkSpaces Thin Client
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for WorkSpaces Thin Client, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

WorkSpaces Thin Client supports making calls to all of its API actions through the interface endpoint.

## Create an interface endpoint for WorkSpaces Thin Client
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for WorkSpaces Thin Client by using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for WorkSpaces Thin Client by using the following service name:

```
com.amazonaws.{{region}}.thinclient.api
```

If you enable private DNS for the interface endpoint, you can make API requests to WorkSpaces Thin Client by using its default Regional DNS name. For example, `api.thinclient.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy gives you full access to WorkSpaces Thin Client through the interface endpoint. To control the access granted to WorkSpaces Thin Client from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for WorkSpaces Thin Client actions**
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed WorkSpaces Thin Client actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "thinclient:ListEnvironments",
            "thinclient:ListDevices",
            "thinclient:ListSoftwareSets"
         ],
         "Resource":"*"
      }
   ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
