---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack.html
---

# Successfully import an S3 bucket as an AWS CloudFormation stack

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-summary"></a>

This pattern helps you bring an existing [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket under infrastructure as code (IaC) management without changing its current configuration. Importing a bucket together with its related resources in a single action can fail, because an import operation can't also create or update resources. Instead, you build the AWS CloudFormation stack in layers. You first import the bucket and its [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) key. Each stack update after that adds one more part of the bucket's configuration to the template, such as the key alias, bucket policy, key policy, and tags.

Settings that you haven't added to the template keep their current values and remain managed outside CloudFormation.

## Prerequisites and limitations
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing S3 bucket (not managed by CloudFormation) and S3 bucket properties like S3 policy, encryption settings etc. For more information about this, see [What S3 bucket policy should I use to comply with the AWS Config rule s3-bucket-ssl-requests-only](https://repost.aws/knowledge-center/s3-bucket-policy-for-config-rule) in the AWS Knowledge Center.
+ An existing AWS Key Management Service (AWS KMS) key and its alias. For more information about this, see [Working with aliases](https://docs.aws.amazon.com/kms/latest/developerguide/programming-aliases.html) in the AWS KMS documentation.

## Architecture
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-architecture"></a>

![Workflow to use CloudFormation template to create a CloudFormation stack to import an S3 bucket.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/aea7f6fe-8e67-46c4-8b90-1ab06b879111/images/ee143374-a0a4-42d9-b7ca-16593a597a84.png)

The diagram shows the following workflow:

1. You create a JSON- or YAML-formatted AWS CloudFormation template.

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
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is an object storage service that helps you store, protect, and retrieve any amount of data.

## Epics
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-epics"></a>

### Import an S3 bucket with AWS KMS key-based encryption as an AWS CloudFormation stack
<a name="import-an-s3-bucket-with-kms-key-long--based-encryption-as-an-aws-cloudformation-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a template to import the S3 bucket and KMS key. | On your local computer, create a template to import your S3 bucket and KMS key by using the following sample template:<pre>AWSTemplateFormatVersion: 2010-09-09<br /><br />Parameters:<br /><br />  bucketName:<br /><br />    Type: String<br /><br />Resources:<br /><br />  S3Bucket:<br /><br />    Type: 'AWS::S3::Bucket'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties:<br /><br />      BucketName: !Ref bucketName<br /><br />      BucketEncryption:<br /><br />        ServerSideEncryptionConfiguration:<br /><br />          - ServerSideEncryptionByDefault:<br /><br />              SSEAlgorithm: 'aws:kms'<br /><br />              KMSMasterKeyID: !GetAtt <br /><br />                - KMSS3Encryption<br /><br />                - Arn<br /><br />  KMSS3Encryption:<br /><br />    Type: 'AWS::KMS::Key'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties:<br /><br />      Enabled: true<br /><br />      KeyPolicy: !Sub |-<br /><br />        {<br /><br />            "Id": "key-consolepolicy-3",<br /><br />            "Version": "2012-10-17",		 	 	 <br /><br />            "Statement": [<br /><br />                {<br /><br />                    "Sid": "Enable IAM User Permissions",<br /><br />                    "Effect": "Allow",<br /><br />                    "Principal": {<br /><br />                        "AWS": ["arn:aws:iam::${AWS::AccountId}:root"]<br /><br />                    },<br /><br />                    "Action": "kms:*",<br /><br />                    "Resource": "*"<br /><br />                }<br /><br />            ]<br /><br />        }<br /><br />      EnableKeyRotation: true</pre><br />**The **`kms:*`** statement for the account root.** This statement matches the AWS default key policy, and it enables IAM policies to grant permission to use the key. If you remove or restrict this access, make sure that your current user still has access to the key. Removing the key policy entirely can lock you out of the key. | AWS DevOps |
| Create the stack. | 1. Sign in to the AWS Management Console, open the AWS CloudFormation console, choose **View stack**, choose **Create stack**, and then choose **With existing resources (import resources)**.<br />2. Choose **Upload a template file** and then upload the template file that you created earlier.<br />3. Enter a name for your stack and configure the remaining options according to your requirements.<br />4. Choose **Create stack** and wait for the stack’s status to change to `IMPORT_COMPLETE`. | AWS DevOps |
| Create the KMS key alias. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the `Resource` section of your template, and then choose **Create stack** and complete the wizard:<pre>KMSS3EncryptionAlias:<br /><br />    Type: 'AWS::KMS::Alias'<br /><br />    DeletionPolicy: Retain<br /><br />    Properties: <br /><br />    AliasName: alias/S3BucketKey<br /><br />    TargetKeyId: !Ref KMSS3Encryption</pre>For more information about this, see [AWS CloudFormation stack updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html) in the AWS CloudFormation documentation.  | AWS DevOps |
| Update the stack to include the S3 bucket policy. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the `Resource` section of the template, and then choose **Create stack** and complete the wizard:<pre>S3BucketPolicy:<br /><br />  Type: 'AWS::S3::BucketPolicy'<br /><br />  Properties:<br /><br />    Bucket: !Ref S3Bucket<br /><br />    PolicyDocument: !Sub |-<br /><br />      {<br /><br />                  "Version": "2008-10-17",		 	 	 <br /><br />                  "Id": "restricthttp",<br /><br />                  "Statement": [<br /><br />                      {<br /><br />                          "Sid": "denyhttp",<br /><br />                          "Effect": "Deny",<br /><br />                          "Principal": {<br /><br />                              "AWS": "*"<br /><br />                          },<br /><br />                          "Action": "s3:*",<br /><br />                          "Resource": ["arn:aws:s3:::${S3Bucket}","arn:aws:s3:::${S3Bucket}/*"],<br /><br />                          "Condition": {<br /><br />                              "Bool": {<br /><br />                                  "aws:SecureTransport": "false"<br /><br />                              }<br /><br />                          }<br /><br />                      }<br /><br />                  ]<br /><br />              }</pre>This S3 bucket policy has a deny statement that blocks requests that don't use HTTPS (Secure Transport). | AWS DevOps |
| Additional bucket properties. | Modify the template to add the properties that the bucket already has, such as block public access settings, versioning, and logging. | AWS administrator |
| Update the key policy. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Modify the template’s KMS resource to include the key policy that allows administrators to administer the KMS key.<br />3. Choose **Create stack**, choose **Next**, and then complete the wizard according to your requirements.For more information, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the AWS KMS documentation. | AWS administrator |
| Add resource-level tags. | 1. On the AWS CloudFormation console, choose **Stacks**, choose the name of the stack that you created earlier, choose the **Template** pane, and then choose **View in Designer**.<br />2. Add the following snippet to the Amazon S3 resource `Properties` section of the template, and then choose **Create stack** and complete the wizard:<pre>Tags:<br /><br />  - Key: createdBy<br /><br />    Value: Cloudformation</pre> | AWS DevOps |

## Best practices
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-best-practices"></a>
+ **Record the current configuration before you import.** Run commands such as `aws s3api get-bucket-encryption`, `get-public-access-block`, `get-bucket-versioning`, `get-bucket-logging`, and `get-bucket-policy`, and save the output. Then make each layer of the template match the existing values exactly. An import operation fails if it would create, update, or delete a resource.
+ **Retain imported resources.** Set `DeletionPolicy: Retain` and `UpdateReplacePolicy: Retain` on the bucket and the AWS KMS key. Then deleting the stack, or an update that requires replacement, can't remove the bucket, its data, or the key.
+ **Add one layer for each stack update.** Review the change set before you run it. Confirm that it changes only the resource or property you're adding.
+ **Run drift detection after the import and after each layer.** Drift detection reports only on properties the template declares. A result of `IN_SYNC` confirms that the template matches the bucket's current configuration.
+ **Bring security settings under AWS CloudFormation management early.** Add the bucket's existing S3 Block Public Access, versioning, server access logging, and encryption settings as layers. After that, drift detection reports any change made outside of CloudFormation.
+ **Preserve existing bucket policy statements.** CloudFormation replaces the entire bucket policy, so copy every existing statement into the template before you add the `AWS::S3::BucketPolicy` resource.
+ **Match the key policy exactly and keep the account root statement.** Keys created in the console often have additional statements. If you remove the statement that grants the account root access, the key can become unmanageable.
+ **Write policies as structured objects.** Write `PolicyDocument` and `KeyPolicy` as YAML or JSON objects instead of JSON strings. This lets tools such as AWS CloudFormation Guard and cfn-lint check them before deployment.
+ **Protect the stack after import.** Turn on termination protection, and consider a stack policy that prevents updates to the bucket resource.
+ **Test in a non-production account first.** Run the full import and every layer against a test bucket before you apply them to production.

## Related resources
<a name="successfully-import-an-s3-bucket-as-an-aws-cloudformation-stack-resources"></a>
+ [Bringing existing resources into AWS CloudFormation management ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html)
+ [AWS re:Invent 2017: Deep dive on AWS CloudFormation](https://www.youtube.com/watch?v=01hy48R9Kr8) (video)
