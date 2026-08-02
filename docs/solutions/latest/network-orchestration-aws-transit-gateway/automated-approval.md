---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/automated-approval.html
---

# Automated approval
<a name="automated-approval"></a>

By default, the solution approves network requests from spoke accounts automatically. This section provides detail about this workflow.

 **Architecture diagram of AWS resources deployed to approve network requests automatically.**

![automated approval architecture](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/automated-approval-architecture.png)

1. Depending on the event, the state machine can perform the following actions:
   + Create, update, or delete transit gateway attachments to the VPC
   + Create or update transit gateway route table associations
   + Enable or disable transit gateway route table propagations

1. The state machine creates routes in the VPC route tables associated with the subnets that you tagged, with the following exceptions (see [Step 5. Add tags](step-5-add-tags.md) for more information):
   + If there is no explicit route table associated with the subnet, the solution updates the main route table instead.
   + If you tag a second subnet in the same Availability Zone, you must use the `route-to-tgw` tag key to only add the route and skip adding the subnet in the attachment.

1. The state machine then adds a new status tag to the VPC or the subnet with the status of the request.

1. The state machine updates the DynamoDB table to activate the network administrator to audit the network change history. The changes in DynamoDB are automatically reflected in the web UI dashboard. Administrators and users can sign in to the web UI to review the history of all changes that occurred in the network.
