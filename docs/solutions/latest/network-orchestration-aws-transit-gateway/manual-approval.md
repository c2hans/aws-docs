---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/manual-approval.html
---

# Manual approval
<a name="manual-approval"></a>

You can choose to manually approve network requests from spoke accounts, instead of automated approval. This section provides detail about this workflow.

**Important**
If you don’t deploy the UI, you can’t approve or reject a network change. All the network changes will be auto-approved. You can use the compliance rules to automatically approve and reject network changes.

 **Architecture diagram of AWS resources deployed to support manual approval of network requests.**

![manual approval architecture](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/manual-approval-architecture.png)

1. If you set the **ApprovalRequired** tag key to `Yes` or `Conditional` in the **Transit gateway route table** parameter, the state machine skips changes depending on the rules set under the `Conditional` setting. To set up this flag, refer to [Transit Gateway route table tags](custom-compliance.md#add-tags-to-transit-gateway-route-table).

1. The administrator signs in to the web UI, and the Amazon Cognito [user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) authenticates each user. CloudFront delivers the web UI content from an S3 bucket.

1. The S3 bucket hosts the web UI.

1. The web UI gets a token from Amazon Cognito and sends a request to AWS AppSync. AWS WAF protects the APIs from security events. A configured set of rules called a web ACL allows, blocks, or counts web requests based on configurable, user-defined web security rules and conditions.

1. AWS AppSync provides the API layer for this Guidance using GraphQL.

1. Amazon Cognito authenticates the token in the header of the API requests.

1. An AWS AppSync [resolver](https://docs.aws.amazon.com/appsync/latest/devguide/system-overview-and-architecture.html#resolver) updates the DynamoDB table with the processing status.

1. An AWS AppSync resolver invokes a Lambda function that validates the event.

1. A Lambda function starts a new state machine execution.

1. The state machine workflow attaches a VPC to the transit gateway.

1. The state machine workflow updates the VPC route table associated with the tagged subnet.

1. The state machine workflow updates the transit gateway route table with association and propagation changes.
**Note**
This workflow only updates the transit gateway route table defined in the VPC tags.

1. (Optional) The state machine workflow updates the attachment name with the VPC name and the Organizational Unit (OU) name for the spoke account (retrieved from the Org Management account).
**Note**
This occurs only if you provide your Organizations ARN for the **Account List or AWS Organizations ARN** template parameter. For more information, see [Step 4: Launch the hub stack](step-4-launch-the-hub-stack.md).

1. The state machine updates the DynamoDB with the information extracted from the event and resources created, updated, or deleted in the workflow. The changes in DynamoDB are automatically reflected in the web UI dashboard. Administrators and users can sign in to the web UI to review the history of all changes that occurred in the network.
