---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/forensic-image-and-ssm-document-builder-service.html
---

# Forensic image and SSM Document builder service
<a name="forensic-image-and-ssm-document-builder-service"></a>

The forensic image builder pipeline creates the forensic AMI with necessary forensic tools needed to perform forensic investigation. The diagram below represents the overall implementation.

**Note**
Customers can use your own forensic AMI or leverage the [Amazon EC2 Image Builder samples](https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/master/CDK/Linux/hello-world) to build a forensic Image.

 **Forensic image and SSM document builder service**

![forensic image ssm document builder](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-image-ssm-document-builder.png)

Amazon EC2 Image Builder initiates the EC2 Image Builder pipeline to build the EC2 Image based on the forensic tools configured in the document. . After successful creation of the AMI, it drops the message as an Amazon SNS topic. . The AWS Lambda function listens to the Amazon SNS topic and gets initiated for each message. . The AWS Lambda function stores the AMI ID in Parameter Store and is used to launch the forensic instance.
