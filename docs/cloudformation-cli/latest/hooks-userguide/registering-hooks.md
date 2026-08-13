---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/registering-hooks.html
---

# Registering a custom Hook with CloudFormation
<a name="registering-hooks"></a>

Once you have created a custom Hook, you need to register it with CloudFormation so you can use it. In this section, you'll learn to package and register your Hook for use in your AWS account.

## Package a Hook (Java)
<a name="registering-hooks-package"></a>

If you've developed your Hook with Java, use Maven to package it.

In the directory of your Hook project, run the following command to build your Hook, run unit tests, and package your project as a `JAR` file that you can use to submit your Hook to the CloudFormation registry.

```
mvn clean package
```

## Register a custom Hook
<a name="registering-hooks-register"></a>

**To register a Hook**

1. (Optional) Configure your default AWS Region name to `us-west-2`, by submitting the [configure](https://docs.aws.amazon.com/cli/latest/reference/configure/) operation.

   ```
   $ aws configure
   AWS Access Key ID [None]: {{<Your Access Key ID>}}
   AWS Secret Access Key [None]: {{<Your Secret Key>}}
   Default region name [None]: {{us-west-2}}
   Default output format [None]: {{json}}
   ```

1. (Optional) The following command builds and packages your Hook project without registering it.

   ```
   $ cfn submit --dry-run
   ```

1. Register your Hook by using the CloudFormation CLI [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) operation.

   ```
   $ cfn submit --set-default
   ```

   The command returns the following command.

   ```
   {‘ProgressStatus’: ‘COMPLETE’}
   ```

   *Results*: You've successfully registered your Hook.

## Verifying Hooks are accessible in your account
<a name="verifying-hooks"></a>

Verify that your Hook is available in your AWS account and in the Regions to which you have submitted it.

1. To verify your Hook, use the [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) command to list your newly registered Hook and return a summary description of it.

   ```
   $ aws cloudformation list-types
   ```

   The command returns the following output and will also show you publicly available Hooks you can activate in your AWS account and Regions.

   ```
   {
       "TypeSummaries": [
           {
               "Type": "HOOK",
               "TypeName": "MyCompany::Testing::MyTestHook",
               "DefaultVersionId": "00000001",
               "TypeArn": "arn:aws:cloudformation:us-west-2:{{ACCOUNT_ID}}/type/hook/MyCompany-Testing-MyTestHook",
               "LastUpdated": "2021-08-04T23:00:03.058000+00:00",
               "Description": "Verifies S3 bucket and SQS queues properties before creating or updating"
           }
       ]
   }
   ```

1. Retrieve the `TypeArn` from the `list-type` output for your Hook and save it.

   ```
   export HOOK_TYPE_ARN=arn:aws:cloudformation:us-west-2:{{ACCOUNT_ID}}/type/hook/MyCompany-Testing-MyTestHook
   ```

To learn how to publish Hooks for public use, see [Publishing Hooks for public use](hooks-publishing.md).

### Configure Hooks
<a name="configure-hooks"></a>

After you've developed and registered your Hook, you can configure your Hook in your AWS account by publishing it to the registry.
+ To configure a Hook in your account, use the [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) operation. This operation enables the Hook’s properties that are defined in the Hook’s schema `properties` section. In the following example, the `minBuckets` property is set to `1` in the configuration.
**Note**
By enabling Hooks in your account, you are authorizing a Hook to use defined permissions from your AWS account. CloudFormation removes non-required permissions before passing your permissions to the Hook. CloudFormation recommends customers or Hook users to review the Hook permissions and be aware of what permissions the Hooks are allowed to before enabling Hooks in your account.

  Specify the configuration data for your registered Hook extension in the same account and AWS Region.

  ```
  $ aws cloudformation set-type-configuration --region us-west-2
    --configuration '{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus":"ENABLED","FailureMode":"FAIL","Properties":{"minBuckets": "1","minQueues": "1", "encryptionAlgorithm": "aws:kms"}}}}'
    --type-arn ${{HOOK_TYPE_ARN}}
  ```
**Important**
To enable your Hook to proactively inspect the configuration of your stack, you must set the `HookInvocationStatus` to `ENABLED` in the `HookConfiguration` section, after the Hook has been registered and activated in your account.

## Accessing AWS APIs in handlers
<a name="accessing-apis-in-handlers"></a>

If your Hooks uses an AWS API in any of its handlers, the CFN-CLI automatically creates an IAM execution role template, `hook-role.yaml`. The `hook-role.yaml` template is based on the permissions specified for each handler in the handler's section of the Hook schema. If the `--role-arn` flag is not used during the [generate](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-generate.html) operation, the role in this stack will be provisioned and used as the execution role of the Hook.

For more information, see [Accessing AWS APIs from a resource type.](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-develop.html#resource-type-develop-executionrole)

### hook-role.yaml template
<a name="resource-role.yaml"></a>

**Note**
If you choose to create your own execution role, we highly recommend practicing the principle of least privilege by allow listing only `hooks.cloudformation.amazonaws.com` and `resources.cloudformation.amazonaws.com`.

The following template uses the IAM, Amazon S3, and Amazon SQS permissions.

```
AWSTemplateFormatVersion: 2010-09-09
Description: >
  This CloudFormation template creates a role assumed by CloudFormation during
  Hook operations on behalf of the customer.
Resources:
  ExecutionRole:
    Type: 'AWS::IAM::Role'
    Properties:
      MaxSessionDuration: 8400
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - resources.cloudformation.amazonaws.com
                - hooks.cloudformation.amazonaws.com
            Action: 'sts:AssumeRole'
            Condition:
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
              StringLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:cloudformation:${AWS::Region}:${AWS::AccountId}:type/hook/MyCompany-Testing-MyTestHook/*
      Path: /
      Policies:
        - PolicyName: HookTypePolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 's3:GetEncryptionConfiguration'
                  - 's3:ListBucket'
                  - 's3:ListAllMyBuckets'
                  - 'sqs:GetQueueAttributes'
                  - 'sqs:GetQueueUrl'
                  - 'sqs:ListQueues'
                Resource: '*'
Outputs:
  ExecutionRoleArn:
    Value: !GetAtt
      - ExecutionRole
      - Arn
```
