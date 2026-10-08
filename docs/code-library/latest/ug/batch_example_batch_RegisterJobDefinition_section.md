---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_RegisterJobDefinition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterJobDefinition` with an AWS SDK or CLI
<a name="batch_example_batch_RegisterJobDefinition_section"></a>

The following code examples show how to use `RegisterJobDefinition`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To register a job definition**
This example registers a job definition for a simple container job.
Command:

```
aws batch register-job-definition --job-definition-name {{sleep30}} --type {{container}} --container-properties '{{{ "image": "busybox", "vcpus": 1, "memory": 128, "command": [ "sleep", "30"]}}}'
```
Output:

```
{
    "jobDefinitionArn": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep30:1",
    "jobDefinitionName": "sleep30",
    "revision": 1
}
```
+  For API details, see [RegisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Registers a new job definition asynchronously in AWS Batch.
     * <p>
     * When using Fargate as the compute environment, it is crucial to set the
     * {@link NetworkConfiguration} with {@link AssignPublicIp#ENABLED} to
     * ensure proper networking configuration for the Fargate tasks. This
     * allows the tasks to communicate with external services, access the
     * internet, or communicate within a VPC.
     *
     * @param jobDefinitionName the name of the job definition to be registered
     * @param executionRoleARN the ARN (Amazon Resource Name) of the execution role
     *                         that provides permissions for the containers in the job
     * @param cpuArch a value of either X86_64 or ARM64 required for the service call
     * @return a CompletableFuture that completes with the ARN of the registered
     *         job definition upon successful execution, or completes exceptionally with
     *         an error if the registration fails
     */
    public CompletableFuture<String> registerJobDefinitionAsync(String jobDefinitionName, String executionRoleARN, String image, String cpuArch) {
        NetworkConfiguration networkConfiguration = NetworkConfiguration.builder()
                .assignPublicIp(AssignPublicIp.ENABLED)
                .build();

        ContainerProperties containerProperties = ContainerProperties.builder()
                .image(image)
                .executionRoleArn(executionRoleARN)
                .resourceRequirements(
                        Arrays.asList(
                                ResourceRequirement.builder()
                                        .type(ResourceType.VCPU)
                                        .value("1")
                                        .build(),
                                ResourceRequirement.builder()
                                        .type(ResourceType.MEMORY)
                                        .value("2048")
                                        .build()
                        )
                )
                .networkConfiguration(networkConfiguration)
               .runtimePlatform(b -> b
                        .cpuArchitecture(cpuArch)
                        .operatingSystemFamily("LINUX"))
                .build();

        RegisterJobDefinitionRequest request = RegisterJobDefinitionRequest.builder()
                .jobDefinitionName(jobDefinitionName)
                .type(JobDefinitionType.CONTAINER)
                .containerProperties(containerProperties)
                .platformCapabilities(PlatformCapability.FARGATE)
                .build();

        CompletableFuture<String> future = new CompletableFuture<>();
        getAsyncClient().registerJobDefinition(request)
                .thenApply(RegisterJobDefinitionResponse::jobDefinitionArn)
                .whenComplete((result, ex) -> {
                    if (ex != null) {
                        future.completeExceptionally(ex);
                    } else {
                        future.complete(result);
                    }
                });

        return future;
    }
```
+  For API details, see [RegisterJobDefinition](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/RegisterJobDefinition) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def register_job_definition(
        self,
        job_definition_name: str,
        execution_role_arn: str,
        image: str = "public.ecr.aws/amazonlinux/amazonlinux:2023",
        command: Optional[list] = None,
        vcpus: str = "0.25",
        memory: str = "512",
    ) -> dict:
        """
        Registers a Fargate job definition.

        :param job_definition_name: The name for the job definition.
        :param execution_role_arn: The ARN of the IAM execution role that grants
            the Fargate agent permission to pull the container image and write
            logs. This is required for Fargate jobs; without it the API call
            fails with "executionRoleArn is required for Fargate jobs."
        :param image: The container image to use.
        :param command: The command to run in the container.
        :param vcpus: The number of vCPUs (as a string). Fargate accepts
            fractional values such as "0.25".
        :param memory: The memory in MiB (as a string).
        :return: A dictionary with the job definition name, ARN, and revision.
        """
        if command is None:
            command = ["echo", "Hello from AWS Batch!"]
        try:
            container_properties = {
                "image": image,
                "command": command,
                "resourceRequirements": [
                    {"type": "VCPU", "value": vcpus},
                    {"type": "MEMORY", "value": memory},
                ],
                "networkConfiguration": {"assignPublicIp": "ENABLED"},
                "fargatePlatformConfiguration": {"platformVersion": "LATEST"},
                "executionRoleArn": execution_role_arn,
            }
            response = self.batch_client.register_job_definition(
                jobDefinitionName=job_definition_name,
                type="container",
                # platformCapabilities must be FARGATE; otherwise Batch treats
                # this as an EC2 job definition and rejects fractional vCPUs.
                platformCapabilities=["FARGATE"],
                containerProperties=container_properties,
            )
            logger.info(
                "Registered job definition %s revision %d: %s",
                response["jobDefinitionName"],
                response["revision"],
                response["jobDefinitionArn"],
            )
            return response
        except ClientError as err:
            logger.error(
                "Error registering job definition %s: %s",
                job_definition_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [RegisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/RegisterJobDefinition) in *AWS SDK for Python (Boto3) API Reference*.

------
