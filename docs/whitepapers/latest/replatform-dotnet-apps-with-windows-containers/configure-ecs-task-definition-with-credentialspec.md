---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/configure-ecs-task-definition-with-credentialspec.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Configure ECS Task Definition with CredentialSpec
<a name="configure-ecs-task-definition-with-credentialspec"></a>

 After you have created the credential spec file, you will reference it in your ECS task definition. Keeping the gMSA metadata in a credential spec file (separate from the Dockerfile) gives you the ability to change the gMSA used by your application in the future without the need for code changes in the application.

 Amazon ECS supports the following ways to reference the credential spec file in the **dockerSecurityOptions** field of a task definition. For more information and example task definitions, refer to the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-gmsa.html).

 Add the credential spec to an Amazon S3 bucket, then reference the ARN of the Amazon S3 bucket in the **dockerSecurityOptions** field of the task definition. Your [Amazon ECS task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) must have the `s3:Get*` and `s3:List*` permissions on your S3 bucket and the credential spec object.

```
{
    "family": "",
    "executionRoleArn": "",
    "containerDefinitions": [
        {
            "name": "",
            ...
            "dockerSecurityOptions": [
                "credentialspec:arn:aws:s3:::${BucketName}/${ObjectName}"
            ],
            ...
        }
    ],
    ...
}
```
