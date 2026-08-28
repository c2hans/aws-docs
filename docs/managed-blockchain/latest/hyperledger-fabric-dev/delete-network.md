---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/delete-network.html
---

# Delete a Hyperledger Fabric Network on Amazon Managed Blockchain (AMB)
<a name="delete-network"></a>

A Hyperledger Fabric network on Amazon Managed Blockchain (AMB) remains active as long as there are members. A network is deleted only when the last member deletes itself from the network. No member or AWS account, even the creator's AWS account, can delete the network until they are the last member and delete themselves. When you delete the last member, all resources for that member and the blockchain network are deleted. For more information, see [Delete a Member in Your AWS Account](managed-blockchain-members.md#managed-blockchain-delete-account-member).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
