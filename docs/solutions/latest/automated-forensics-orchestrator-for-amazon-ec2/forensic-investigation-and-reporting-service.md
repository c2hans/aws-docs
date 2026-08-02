---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/forensic-investigation-and-reporting-service.html
---

# Forensic investigation and reporting service
<a name="forensic-investigation-and-reporting-service"></a>

The diagram below represents the logical interaction view of forensic memory and disk investigation service. Once forensic acquisition is completed, forensic investigation flow is initiated, isolation of EC2 instance or EKS cluster is done based on the AWS Security Hub event type.

## Interaction view
<a name="interaction-view-2"></a>

 **Forensic investigation and reporting service - interaction view**

![forensic investigation and reporting interaction](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-investigation-and-reporting-interaction.png)

## Implementation view
<a name="forensic-investigation-and-reporting-service-implementation"></a>

 **Forensic investigation and reporting service**

![forensic investigation and reporting service](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-investigation-and-reporting-service.png)

## Forensic investigation and reporting workflow
<a name="forensics-investigation-and-reporting-workflow"></a>

1. After the acquisition flow, the investigation flow (Step Functions) is initiated.

1. The *Create Instance* Lambda function retrieves the AMI information from AWS Systems Manager Parameter Store and starts an instance in the forensic account.

1. The *Check Instance Lambda* function validates the instance has the necessary tools required for forensic investigation, such as determining the instance is in the running state, AWS Systems Manager is installed and forensic tools are up and running.

1. If the response from SSM Command is `Pending` or `In Progress` it waits for 120 seconds and checks again.

1. Disk forensics investigation flow is initiated for **forensictype** variable set to `DISK`.

1. Disk forensics investigation lambda function creates a volume from the snapshot shared with the forensic account and attaches the volume to the instance started in step 2.

1. The Disk forensics investigation Lambda function leverages the SSM document to perform disk forensics.

1. The Memory forensics investigation flow is initiated for **forensictype** variable set to `MEMORY`.

1. The Lambda function leverages the SSM document to load memory dump from S3 to the EBS volume for memory analysis.
   + The SSM document containing details of the forensic investigation is initiated to *perform disk or memory forensics*.
   + The *Memory forensics flow* retrieves the appropriate meta data tag associated with the memory dump and loads the matching kernel Volatility symbol table from a configurable S3 location.

1. The Lambda function checks if AWS Systems Manager Run Command is complete.

1. The Lambda function waits for 120 seconds before checking again if AWS Systems Manager Run Command is complete.

1. Once complete, the *Terminate Forensic Instance* Lambda function is initiated.

1. The forensic instance is terminated.

1. Details about forensic ID, compromised Amazon EC2 instance or EKS cluster, Amazon S3 bucket location of the results, and Amazon DynamoDB table details about disk and memory analysis are sent as SNS.
