---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

 This section describes the components and AWS services that make up this guidance and the architecture details on how these components work together.

## AWS Network Firewall configuration
<a name="aws-network-firewall-configuration"></a>

 This guidance deploys with a default network firewall policy, which doesn't disrupt your existing network. This allows you to design and deploy custom network firewall policies, as well as stateful and stateless rule groups. This also includes existing [Suricata](https://suricata.io/) stateful rules. For more information about Suricata, refer to the [Working with stateful rule groups in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html) in the *AWS Network Firewall Developer Guide*.

**Note**
 You can also use Firewall Manager to centrally configure and manage firewall rules for this guidance.

## Using this guidance with AWS Transit Gateway
<a name="using-this-guidance-with-aws-transit-gateway"></a>

**Note**
 To create transit gateways and manage VPCs and peering attachments, we recommend using the [Network Orchestration for AWS Transit Gateway](https://aws.amazon.com/solutions/implementations/network-orchestration-aws-transit-gateway/) guidance. You can use both guidance for the same transit gateway resource.

 **With an existing transit gateway**

 This guidance works with your existing transit gateway to create a VPC transit gateway attachment if you provide the transit gateway ID. The guidance also creates association and propagation to the existing transit gateway route tables if you provide the route table ID and transit gateway ID. For details, refer to [Step 2: Launch the stack](step-2-launch-the-stack.md).

 **Without an existing transit gateway**

 You can deploy this guidance without a transit gateway to test it before making any network changes. If you don't provide a transit gateway ID, this guidance won't create the transit gateway to VPC attachment. This ensures that your network engineers can customize the Network Firewall configuration and update the firewall policies before making network changes.

## Amazon CloudWatch
<a name="amazon-cloudwatch"></a>

 If you select `CloudWatchLogs` for the **Select the type of log destination for the Network Firewall** parameter when you [launch the stack](step-2-launch-the-stack.md), this guidance creates a log group for your logs. Your alert and flow logs collect log records and consolidate them into log files. For more information, refer to the [AWS Network Firewall Developer Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).

## Amazon Simple Storage Service
<a name="amazon-simple-storage-service"></a>

 The guidance creates the following [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets:
+  **Source code bucket** – This bucket hosts versions of the source code used by the [AWS CodeBuild](https://aws.amazon.com/codebuild/) stage to validate and deploy Network Firewall resources and update related resources.
+  **CodePipeline artifacts bucket** – This bucket stores input and output artifacts created by the CodePipeline stages. CodePipeline zips and transfers the files for input or output artifacts as appropriate for the action type in the stage.
+  **(Optional) Network Firewall log destination bucket** – This bucket stores the guidance's logs. This S3 bucket is only created if you select `Amazon S3` for the **Select the type of log destination for the Network Firewall** parameter when you [launch the stack](step-2-launch-the-stack.md).
