---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/forensic-memory-and-disk-acquisition-service.html
---

# Forensic memory and disk acquisition service
<a name="forensic-memory-and-disk-acquisition-service"></a>

The diagram below represents the logical interaction view of the forensic memory and disk acquisition service. The Forensic triaging step function initiates forensic acquisition flow to perform memory and disk acquisition. Following memory and disk acquisition, the investigation function is initiated.

Isolation of EC2 instance or EKS cluster is done based on the Security Hub action event types - Forensic triage and Forensic isolation.

## Interaction view
<a name="interaction-view-1"></a>

 **"Forensic memory disk acquisition**

![interaction step"](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-memory-disk-acquisition-interaction.png)

## Implementation view
<a name="memory-forensics-acquisition-workflow-implementation"></a>

 **Memory forensics acquisition workflow implementation**

![memory forensics acquisition workflow implementation](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/memory-forensics-acquisition-workflow-implementation.png)

The *Forensic triage* Step Function initiates the *memory acquisition* flow. . The *Memory acquisition* Lambda function in workflow leverages the SSM command to run SSM document in the compromised instance. . The *Memory acquisition* Lambda function assumes a role in the application account and passes the SSM document to be run along with credentials to copy the memory dump into an S3 bucket. . AWS Systems Manager runs a memory acquisition document via the Run Command.

\+ ** The memory dump is stored in an S3 bucket of the forensic account. ** The memory dump has associated meta data tags to indicate the underlying OS and kernel the dump is associated with, assisting the *memory analysis flow* further downstream. . The *Check memory acquisition* Lambda function checks for SSM Run Command to be completed. . If the response from SSM Run Command status is `Pending` or `Delayed` or `In Progress`, it waits for 120 seconds. . If the response from SSM Run Command status is `Success`, it checks if isolation is needed. . If **isolation** is set to `true`, then the Lambda function assumes role into the application account and attaches a security group with no egress and ingress security group, and detaches the existing security group. Isolation is set to `true` during the triaging phase based on security event type. . This initiates investigation flow with forensic type as `MEMORY`. . If any error occurs during the memory acquisition process, the EC2 instance or EKS cluster isolation will be performed based on the `isolation` flag.

**Note**
When the isolation flag is set to `true`, isolation is still performed regardless of the memory acquisition result.

## What happens to instances after isolation?
<a name="instances-after-isolation"></a>

Instances after isolation will have:
+ Termination protection for the compromised EC2 instance or EKS cluster is set to `true`
+ Shutdown behavior set to `STOP`
+ Any EIP assigned to the compromised instance will be disassociated
+ EBS volumes attached to the compromised instance will be preserved
+ Instance profile will be updated to a strict profile
+ All open credentials session based on the compromised instance role will be invalidated.

**Note**
On isolation, instances sharing the same role with the compromised instance would be impacted as the credentials will be invalidated. If your application does not have the correct retry mechanism to renew new credentials, it can result in failure of the application. For more information, refer to the [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk-ec2-instances) topic about creating new credentials. Applications using AWS CLI will not be impacted as the credentials will be refreshed automatically
