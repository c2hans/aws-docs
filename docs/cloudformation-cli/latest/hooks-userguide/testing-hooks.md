---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/testing-hooks.html
---

# Testing a custom Hook in your AWS account
<a name="testing-hooks"></a>

Now that you've coded your handler functions that correspond to an invocation point, it's time to test your custom Hook on a CloudFormation stack.

The Hook failure mode is set to `FAIL` if the CloudFormation template didn't provision an S3 bucket with the following:
+ The Amazon S3 bucket encryption is set.
+ The Amazon S3 bucket key is enabled for the bucket.
+ The encryption algorithm set for the Amazon S3 bucket is the correct algorithm required.
+ The AWS Key Management Service key ID is set.

In the following example, create a template called `my-failed-bucket-stack.yml` with a stack name of `my-hook-stack` that fails the stack configuration and stops before the resource provisions.

## Testing Hooks by provisioning a stack
<a name="testing-hooks-provision-stack"></a>

### Example 1: To provision a stack
<a name="provision-a-stack-example-1"></a>

**Provision a non-compliant stack**

1. Author a template that specifies an S3 bucket. For example, `my-failed-bucket-stack.yml`.

   ```
   AWSTemplateFormatVersion: 2010-09-09
   Resources:
     S3Bucket:
       Type: AWS::S3::Bucket
       Properties: {}
   ```

1. Create a stack, and specify your template in the AWS Command Line Interface (AWS CLI). In the following example, specify the stack name as `my-hook-stack` and the template name as `my-failed-bucket-stack.yml`.

   ```
   $ aws cloudformation create-stack \
     --stack-name {{my-hook-stack}} \
     --template-body {{file://my-failed-bucket-stack.yml}}
   ```

1. (Optional) View your stack progress by specifying your stack name. In the following example, specify the stack name `my-hook-stack`.

   ```
   $ aws cloudformation describe-stack-events \
     --stack-name {{my-hook-stack}}
   ```

   Use the `describe-stack-events` operation to see the Hook failure while creating the bucket. The following is an example output of the command.

   ```
   {
       "StackEvents": [
       ...
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-hook-stack/2c693970-f57e-11eb-a0fb-061a2a83f0b9",
               "EventId": "S3Bucket-CREATE_FAILED-2021-08-04T23:47:03.305Z",
               "StackName": "my-hook-stack",
               "LogicalResourceId": "S3Bucket",
               "PhysicalResourceId": "",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:47:03.305000+00:00",
               "ResourceStatus": "CREATE_FAILED",
               "ResourceStatusReason": "The following hook(s) failed: [MyCompany::Testing::MyTestHook]",
               "ResourceProperties": "{}",
               "ClientRequestToken": "Console-CreateStack-abe71ac2-ade4-a762-0499-8d34d91d6a92"
           },
       ...
       ]
   }
   ```

   *Results*: The Hook invocation failed the stack configuration and stopped the resource from provisioning.

**Use a CloudFormation template to pass Hook validation**

1. To create a stack and pass the Hook validation, update the template so that your resource uses an encrypted S3 bucket. This example uses the template `my-encrypted-bucket-stack.yml`.

   ```
   AWSTemplateFormatVersion: 2010-09-09
   Description: |
     This CloudFormation template provisions an encrypted S3 Bucket
   Resources:
     EncryptedS3Bucket:
       Type: AWS::S3::Bucket
       Properties:
         BucketName: !Sub encryptedbucket-${AWS::Region}-${AWS::AccountId}
         BucketEncryption:
           ServerSideEncryptionConfiguration:
             - ServerSideEncryptionByDefault:
                 SSEAlgorithm: 'aws:kms'
                 KMSMasterKeyID: !Ref EncryptionKey
               BucketKeyEnabled: true
     EncryptionKey:
       Type: AWS::KMS::Key
       DeletionPolicy: Retain
       Properties:
         Description: KMS key used to encrypt the resource type artifacts
         EnableKeyRotation: true
         KeyPolicy:
           Version: 2012-10-17
           Statement:
             - Sid: Enable full access for owning account
               Effect: Allow
               Principal:
                 AWS: !Ref AWS::AccountId
               Action: 'kms:*'
               Resource: '*'
   Outputs:
     EncryptedBucketName:
       Value: !Ref EncryptedS3Bucket
   ```
**Note**
Hooks won't be invoked for skipped resources.

1. Create a stack and specify your template. In this example, the stack name is `my-encrypted-bucket-stack`.

   ```
   $ aws cloudformation create-stack \
     --stack-name {{my-encrypted-bucket-stack}} \
     --template-body {{file://my-encrypted-bucket-stack.yml}} \
   ```

1. (Optional) View your stack progress by specifying the stack name.

   ```
   $ aws cloudformation describe-stack-events \
     --stack-name {{my-encrypted-bucket-stack}}
   ```

   Use the `describe-stack-events` command to view the response. The following is an example of the `describe-stack-events` command.

   ```
   {
       "StackEvents": [
       ...
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-CREATE_COMPLETE-2021-08-04T23:23:20.973Z",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "encryptedbucket-us-west-2-123456789012",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:23:20.973000+00:00",
               "ResourceStatus": "CREATE_COMPLETE",
               "ResourceProperties": "{\"BucketName\":\"encryptedbucket-us-west-2-123456789012\",\"BucketEncryption\":{\"ServerSideEncryptionConfiguration\":[{\"BucketKeyEnabled\":\"true\",\"ServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"aws:kms\",\"KMSMasterKeyID\":\"{{ENCRYPTION_KEY_ARN}}\"}}]}}",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-CREATE_IN_PROGRESS-2021-08-04T23:22:59.410Z",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "encryptedbucket-us-west-2-123456789012",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:22:59.410000+00:00",
               "ResourceStatus": "CREATE_IN_PROGRESS",
               "ResourceStatusReason": "Resource creation Initiated",
               "ResourceProperties": "{\"BucketName\":\"encryptedbucket-us-west-2-123456789012\",\"BucketEncryption\":{\"ServerSideEncryptionConfiguration\":[{\"BucketKeyEnabled\":\"true\",\"ServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"aws:kms\",\"KMSMasterKeyID\":\"{{ENCRYPTION_KEY_ARN}}\"}}]}}",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-6516081f-c1f2-4bfe-a0f0-cefa28679994",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:22:58.349000+00:00",
               "ResourceStatus": "CREATE_IN_PROGRESS",
               "ResourceStatusReason": "Hook invocations complete.  Resource creation initiated",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
       ...
       ]
   }
   ```

   *Results*: CloudFormation successfully created the stack. The Hook's logic verified that the `AWS::S3::Bucket` resource contained server-side encryption before provisioning the resource.

### Example 2: To provision a stack
<a name="provision-a-stack-example-2"></a>

**Provision a non-compliant stack**

1. Author a template that specifies an S3 bucket. For example `aes256-bucket.yml`.

   ```
   AWSTemplateFormatVersion: 2010-09-09
   Description: |
     This CloudFormation template provisions an encrypted S3 Bucket
   Resources:
     EncryptedS3Bucket:
       Type: AWS::S3::Bucket
       Properties:
         BucketName: !Sub encryptedbucket-${AWS::Region}-${AWS::AccountId}
         BucketEncryption:
           ServerSideEncryptionConfiguration:
             - ServerSideEncryptionByDefault:
                 SSEAlgorithm: AES256
               BucketKeyEnabled: true
   Outputs:
     EncryptedBucketName:
       Value: !Ref EncryptedS3Bucket
   ```

1. Create a stack, and specify your template in the AWS CLI. In the following example, specify the stack name as `my-hook-stack` and the template name as `aes256-bucket.yml`.

   ```
   $ aws cloudformation create-stack \
     --stack-name {{my-hook-stack}} \
     --template-body {{file://aes256-bucket.yml}}
   ```

1. (Optional) View your stack progress by specifying your stack name. In the following example, specify the stack name `my-hook-stack`.

   ```
   $ aws cloudformation describe-stack-events \
     --stack-name {{my-hook-stack}}
   ```

   Use the `describe-stack-events` operation to see the Hook failure while creating the bucket. The following is an example output of the command.

   ```
   {
       "StackEvents": [
       ...
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-hook-stack/2c693970-f57e-11eb-a0fb-061a2a83f0b9",
               "EventId": "S3Bucket-CREATE_FAILED-2021-08-04T23:47:03.305Z",
               "StackName": "my-hook-stack",
               "LogicalResourceId": "S3Bucket",
               "PhysicalResourceId": "",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:47:03.305000+00:00",
               "ResourceStatus": "CREATE_FAILED",
               "ResourceStatusReason": "The following hook(s) failed: [MyCompany::Testing::MyTestHook]",
               "ResourceProperties": "{}",
               "ClientRequestToken": "Console-CreateStack-abe71ac2-ade4-a762-0499-8d34d91d6a92"
           },
       ...
       ]
   }
   ```

   *Results*: The Hook invocation failed the stack configuration and stopped the resource from provisioning. The stack failed due to the S3 bucket encryption configured incorrectly. The Hook type configuration requires `aws:kms` while this bucket uses `AES256`.

**Use a CloudFormation template to pass Hook validation**

1. To create a stack and pass the Hook validation, update the template so that your resource uses an encrypted S3 bucket. This example uses the template `kms-bucket-and-queue.yml`.

   ```
   AWSTemplateFormatVersion: 2010-09-09
   Description: |
     This CloudFormation template provisions an encrypted S3 Bucket
   Resources:
     EncryptedS3Bucket:
       Type: AWS::S3::Bucket
       Properties:
         BucketName: !Sub encryptedbucket-${AWS::Region}-${AWS::AccountId}
         BucketEncryption:
           ServerSideEncryptionConfiguration:
             - ServerSideEncryptionByDefault:
                 SSEAlgorithm: 'aws:kms'
                 KMSMasterKeyID: !Ref EncryptionKey
               BucketKeyEnabled: true
     EncryptedQueue:
       Type: AWS::SQS::Queue
       Properties:
         QueueName: !Sub encryptedqueue-${AWS::Region}-${AWS::AccountId}
         KmsMasterKeyId: !Ref EncryptionKey
     EncryptionKey:
       Type: AWS::KMS::Key
       DeletionPolicy: Retain
       Properties:
         Description: KMS key used to encrypt the resource type artifacts
         EnableKeyRotation: true
         KeyPolicy:
           Version: 2012-10-17
           Statement:
             - Sid: Enable full access for owning account
               Effect: Allow
               Principal:
                 AWS: !Ref AWS::AccountId
               Action: 'kms:*'
               Resource: '*'
   Outputs:
     EncryptedBucketName:
       Value: !Ref EncryptedS3Bucket
     EncryptedQueueName:
       Value: !Ref EncryptedQueue
   ```
**Note**
Hooks won't be invoked for skipped resources.

1. Create a stack and specify your template. In this example, the stack name is `my-encrypted-bucket-stack`.

   ```
   $ aws cloudformation create-stack \
     --stack-name {{my-encrypted-bucket-stack}} \
     --template-body {{file://kms-bucket-and-queue.yml}}
   ```

1. (Optional) View your stack progress by specifying the stack name.

   ```
   $ aws cloudformation describe-stack-events \
     --stack-name {{my-encrypted-bucket-stack}}
   ```

   Use the `describe-stack-events` command to view the response. The following is an example of the `describe-stack-events` command.

   ```
   {
       "StackEvents": [
       ...
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-CREATE_COMPLETE-2021-08-04T23:23:20.973Z",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "encryptedbucket-us-west-2-123456789012",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:23:20.973000+00:00",
               "ResourceStatus": "CREATE_COMPLETE",
               "ResourceProperties": "{\"BucketName\":\"encryptedbucket-us-west-2-123456789012\",\"BucketEncryption\":{\"ServerSideEncryptionConfiguration\":[{\"BucketKeyEnabled\":\"true\",\"ServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"aws:kms\",\"KMSMasterKeyID\":\"{{ENCRYPTION_KEY_ARN}}\"}}]}}",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-CREATE_IN_PROGRESS-2021-08-04T23:22:59.410Z",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "encryptedbucket-us-west-2-123456789012",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:22:59.410000+00:00",
               "ResourceStatus": "CREATE_IN_PROGRESS",
               "ResourceStatusReason": "Resource creation Initiated",
               "ResourceProperties": "{\"BucketName\":\"encryptedbucket-us-west-2-123456789012\",\"BucketEncryption\":{\"ServerSideEncryptionConfiguration\":[{\"BucketKeyEnabled\":\"true\",\"ServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"aws:kms\",\"KMSMasterKeyID\":\"{{ENCRYPTION_KEY_ARN}}\"}}]}}",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
           {
               "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-encrypted-bucket-stack/82a97150-f57a-11eb-8eb2-06a6bdcc7779",
               "EventId": "EncryptedS3Bucket-6516081f-c1f2-4bfe-a0f0-cefa28679994",
               "StackName": "my-encrypted-bucket-stack",
               "LogicalResourceId": "EncryptedS3Bucket",
               "PhysicalResourceId": "",
               "ResourceType": "AWS::S3::Bucket",
               "Timestamp": "2021-08-04T23:22:58.349000+00:00",
               "ResourceStatus": "CREATE_IN_PROGRESS",
               "ResourceStatusReason": "Hook invocations complete.  Resource creation initiated",
               "ClientRequestToken": "Console-CreateStack-39df35ac-ca00-b7f6-5661-4e917478d075"
           },
       ...
       ]
   }
   ```

   *Results*: CloudFormation successfully created the stack. The Hook's logic verified that the `AWS::S3::Bucket` resource contained server-side encryption before provisioning the resource.
