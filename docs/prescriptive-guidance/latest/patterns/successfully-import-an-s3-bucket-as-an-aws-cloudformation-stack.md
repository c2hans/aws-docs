---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack.html
---

# Successfully import an S3 bucket as an AWS CloudFormation stack
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-summary"></a>

If you use Amazon Web Services (AWS) resources, such as Amazon Simple Storage Service (Amazon S3) buckets, and want to use an infrastructure as code (IaC) approach, then you can import your resources into AWS CloudFormation and manage them as a stack.

This pattern provides steps to successfully import an S3 bucket as an AWS CloudFormation stack. By using this pattern's approach, you can avoid possible errors that might occur if you import your S3 bucket in a single action.

## Prerequisites and limitations
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing S3 bucket and S3 bucket policy. For more information about this, see [What S3 bucket policy should I use to comply with the AWS Config rule s3-bucket-ssl-requests-only](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/) in the AWS Knowledge Center.
+ An existing AWS Key Management Service (AWS KMS) key and its alias. For more information about this, see [Working with aliases](https://docs.aws.amazon.com/kms/latest/developerguide/programming-aliases.html) in the AWS KMS documentation.
+ The sample `CloudFormation-template-S3-bucket` AWS CloudFormation template (attached), downloaded to your local computer.

## Architecture
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-architecture"></a>

![Workflow to use CloudFormation template to create a CloudFormation stack to import an S3 bucket.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/aea7f6fe-8e67-46c4-8b90-1ab06b879111/images/ee143374-a0a4-42d9-b7ca-16593a597a84.png)

The diagram shows the following workflow:

1. The user creates a JSON or YAML-formatted AWS CloudFormation template.

1. The template creates an AWS CloudFormation stack to import the S3 bucket.

1. The AWS CloudFormation stack manages the S3 bucket that you specified in the template.

**Technology stack**
+ AWS CloudFormation
+ AWS Identity and Access Management (IAM)
+ AWS KMS
+ Amazon S3

**Tools**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you to create and provision AWS infrastructure deployments predictably and repeatedly.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – IAM is a web service for securely controlling access to AWS services.
+ [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) – AWS Key Management Service (AWS KMS) is an encryption and key management service scaled for the cloud.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the Internet.

## Epics
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-epics"></a>

### Import an S3 bucket with AWS KMS key-based encryption as an AWS CloudFormation stack
<a name="import-an-s3-bucket-with-kms-key-long--based-encryption-as-an-aws-cloudformation-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a template to import the S3 bucket and KMS key. | On your local computer, create a template to import your S3 bucket and KMS key by using the following sample template:<pre>AWSTemplateFormatVersion: 2010-09-09<br /><br />Parameters:<br /><br />  bucketName:<br /><br />    Type: String<br /><br />Resources:<br /><br />  S3Bucket:<br /><br />    Type: 'AWS::S3::Bucket'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties:<br /><br />      BucketName: !Ref bucketName<br /><br />      BucketEncryption:<br /><br />        ServerSideEncryptionConfiguration:<br /><br />          - ServerSideEncryptionByDefault:<br /><br />              SSEAlgorithm: 'aws:kms'<br /><br />              KMSMasterKeyID: !GetAtt <br /><br />                - KMSS3Encryption<br /><br />                - Arn<br /><br />  KMSS3Encryption:<br /><br />    Type: 'AWS::KMS::Key'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties:<br /><br />      Enabled: true<br /><br />      KeyPolicy: !Sub |-<br /><br />        {<br /><br />            "Id": "key-consolepolicy-3",<br /><br />            "Version": "2012-10-17",		 	 	 <br /><br />            "Statement": [<br /><br />                {<br /><br />                    "Sid": "Enable IAM User Permissions",<br /><br />                    "Effect": "Allow",<br /><br />                    "Principal": {<br /><br />                        "AWS": ["arn:aws:iam::${AWS::AccountId}:root"]<br /><br />                    },<br /><br />                    "Action": "kms:*",<br /><br />                    "Resource": "*"<br /><br />                }<br /><br />                }<br /><br />            ]<br /><br />        }<br /><br />      EnableKeyRotation: true</pre> | AWS DevOps |
| Create the stack. | 1. Sign in to the AWS Management Console, open the AWS CloudFormation console, choose **View stack**, choose **Create stack**, and then choose **With existing resources (import resources)**.<br />2. Choose **Upload a template file** and then upload the template file that you created earlier.<br />3. Enter a name for your stack and configure the remaining options according to your requirements.<br />4. Choose **Create stack** and wait for the stack’s status to change to `IMPORT_COMPLETE`. | AWS DevOps |
| Create the KMS key alias. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the `Resource` section of your template, and then choose **Create stack** and complete the wizard:<pre>KMSS3EncryptionAlias:<br /><br />    Type: 'AWS::KMS::Alias'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties: <br /><br />    AliasName: alias/S3BucketKey<br /><br />    TargetKeyId: !Ref KMSS3Encryption</pre>For more information about this, see [AWS CloudFormation stack updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html) in the AWS CloudFormation documentation.  | AWS DevOps |
| Update the stack to include the S3 bucket policy. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the `Resource` section of the template, and then choose **Create stack** and complete the wizard:<pre>S3BucketPolicy:<br /><br />  Type: 'AWS::S3::BucketPolicy'<br /><br />  Properties:<br /><br />    Bucket: !Ref S3Bucket<br /><br />    PolicyDocument: !Sub |-<br /><br />      {<br /><br />                  "Version": "2008-10-17",		 	 	 <br /><br />                  "Id": "restricthttp",<br /><br />                  "Statement": [<br /><br />                      {<br /><br />                          "Sid": "denyhttp",<br /><br />                          "Effect": "Deny",<br /><br />                          "Principal": {<br /><br />                              "AWS": "*"<br /><br />                          },<br /><br />                          "Action": "s3:*",<br /><br />                          "Resource": ["arn:aws:s3:::${S3Bucket}","arn:aws:s3:::${S3Bucket}/*"],<br /><br />                          "Condition": {<br /><br />                              "Bool": {<br /><br />                                  "aws:SecureTransport": "false"<br /><br />                              }<br /><br />                          }<br /><br />                      }<br /><br />                  ]<br /><br />              }</pre>This S3 bucket policy has a deny statement that restricts API calls that are not secure.  | AWS DevOps |
| Update the key policy. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Modify the template’s KMS resource to include the key policy that allows administrators to administer the KMS key.<br />3. Choose **Create stack**, choose **Next**, and then complete the wizard according to your requirements.For more information, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the AWS KMS documentation. | AWS administrator |
| Add resource-level tags. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the Amazon S3 resource `Properties` section of the template, and then choose **Create stack** and complete the wizard:<pre>Tags:<br /><br />  - Key: createdBy<br /><br />    Value: Cloudformation</pre> | AWS DevOps |

## Related resources
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-resources"></a>
+ [Bringing existing resources into AWS CloudFormation management ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html)
+ [AWS re:Invent 2017: Deep dive on AWS CloudFormation](https://www.youtube.com/watch?v=01hy48R9Kr8) (video)

## Attachments
<a name="attachments-aea7f6fe-8e67-46c4-8b90-1ab06b879111"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/aea7f6fe-8e67-46c4-8b90-1ab06b879111/attachments/attachment.zip)
