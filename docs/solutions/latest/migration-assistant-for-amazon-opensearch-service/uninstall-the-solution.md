---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

Cleanup should happen last, not immediately after the first successful run. Wait until:
+ Production traffic has been stable on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.
+ You no longer need the source for rollback (typically 24–72 hours after cutover).
+ You no longer need replay or comparison checks.
+ Any snapshot artifacts you want to keep have been retained intentionally.

**Important**
After your migration is complete and the rollback window has passed, remove all solution resources to stop incurring costs. The default Amazon S3 migrations bucket and snapshot bucket are not automatically deleted, in case you have stored data to retain.

## Uninstall the Amazon EKS deployment
<a name="uninstall-eks"></a>

The Amazon EKS deployment is removed in two phases: first the Helm release on the cluster, then the AWS CloudFormation stack.

### Step 1: Uninstall the Helm release and clear PVCs
<a name="step-1-helm-uninstall"></a>

From a terminal with `kubectl` and `helm` configured for the Amazon EKS cluster:

```
helm uninstall -n ma ma
kubectl -n ma delete pvc --all
kubectl delete namespace ma
```

The `kubectl -n ma delete pvc --all` command removes the Apache Kafka persistent volumes used for capture and replay. Skip this step if you are not also deleting the cluster and want to redeploy Migration Assistant later with the same data.

### Step 2: Delete the AWS CloudFormation stack
<a name="step-2-delete-cfn"></a>

```
aws cloudformation delete-stack --stack-name <STACK_NAME>
aws cloudformation wait stack-delete-complete --stack-name <STACK_NAME>
```

This removes the Amazon EKS cluster, networking, IAM roles, and supporting AWS resources created by the bootstrap script.

### Step 3: Clean up Amazon S3 artifacts (optional)
<a name="step-3-clean-s3"></a>

The default migrations bucket is not automatically deleted. The bucket name follows the format:

```
s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>
```

Be deliberate about Amazon S3 cleanup. The bucket is often still useful for:
+ audit and rollback investigation,
+ preserving snapshots for future reference,
+ and comparing post-cutover behavior.

Delete it only after you are certain you no longer need the contents:

```
aws s3 rb s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION> --force
```

**Warning**
The `--force` flag deletes all objects in the bucket. Make sure you have copied any snapshots or artifacts you want to retain to another location first.

## Uninstall the legacy Amazon ECS deployment
<a name="uninstall-ecs"></a>

If you originally deployed the legacy Amazon ECS deployment of Migration Assistant, follow these steps instead. The Amazon ECS deployment has reached end of support (**July 15, 2026**).

### Using the AWS Management Console
<a name="ecs-using-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack. Depending on what options you enabled for the deployment, the solution creates different AWS CloudFormation stacks. The stacks must be deleted in the following order:

   1.  `MigrationConsole`

   1.  `TrafficReplayer`

   1.  `CaptureProxy`

   1.  `CaptureProxyES` (only available for demo install)

   1.  `ReindexFromSnapshot`

   1.  `MigrationInfra`

   1.  `NetworkInfra`

1. On the **Stacks** page, delete the bootstrap stack.

1. Choose **Delete** for each of the previous.

### Using the AWS Command Line Interface
<a name="ecs-using-cli"></a>

To remove all the AWS CDK stacks that the solution creates during a legacy Amazon ECS deployment, run a command similar to the following within the AWS CDK directory.

Log in to the `bootstrap` container, as described in [Deploy the solution](deploy-the-solution.md), and run the following commands:

```
cd deployment/cdk/opensearch-service-migration
 $ cdk destroy "*" --c contextId=default
```

After the Migration Assistant for Amazon OpenSearch Service solution stacks *(see step 2. in [Using the AWS Management Console](#ecs-using-console))* have been removed, remove the bootstrap AWS CloudFormation template.

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, set the default Region to the Region used for deployment. Then run the AWS CLI command to delete the AWS CloudFormation bootstrap stack:

```
export AWS_DEFAULT_REGION=<aws_region>
 $ aws cloudformation delete-stack --stack-name <bootstrap_stack_name>
```
