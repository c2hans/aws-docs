---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/framework-client.html
---

# Work with Hyperledger Fabric Components and Chaincode
<a name="framework-client"></a>

You access services and applications in AMB Access Hyperledger Fabric from a framework client machine. The client runs tools and applications that you install for the version of Hyperledger Fabric on the network.

The client accesses AMB Access endpoints for components such as the CA, the orderer, and peer nodes through an interface VPC endpoint that you set up in your AWS account. The client machine must have access to the interface VPC endpoint to access resource endpoints. For more information, see [Create an Interface VPC Endpoint for Amazon Managed Blockchain (AMB) Hyperledger Fabric](managed-blockchain-endpoints.md).

You can get the endpoints that networks, members, and peer nodes make available using the AWS Management Console, or using `get` commands and actions with the AMB Access AWS CLI or SDK.

An AWS CloudFormation template to create a Hyperledger Fabric client is available in the [amazon-managed-blockchain-client-templates repository](https://github.com/awslabs/amazon-managed-blockchain-client-templates) on Github. For more information, see the [readme.md](https://github.com/awslabs/amazon-managed-blockchain-client-templates/blob/master/README.md) in that repository. For more information about using CloudFormation, see [Getting Started](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.Walkthrough.html) in the *AWS CloudFormation User Guide*.

**Topics**
+ [Register and Enroll a Hyperledger Fabric Admin](managed-blockchain-hyperledger-create-admin.md)
+ [Work with Channels](hyperledger-work-with-channels.md)
+ [Add an Anchor Peer to a Channel](hyperledger-anchor-peers.md)
+ [Develop Hyperledger Fabric Chaincode](managed-blockchain-hyperledger-develop-chaincode.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
