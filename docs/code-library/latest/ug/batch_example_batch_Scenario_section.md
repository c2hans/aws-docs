---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_Scenario_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Learn the basics of AWS Batch with an AWS SDK
<a name="batch_example_batch_Scenario_section"></a>

The following code examples show how to:
+ Create an AWS Batch compute environment.
+ Check the status of the compute environment.
+ Set up an AWS Batch job queue and job definition.
+ Register a job definition.
+ Submit an AWS Batch Job.
+ Get a list of jobs applicable to the job queue.
+ Check the status of job.
+ Delete AWS Batch resources.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).
Run an interactive scenario demonstrating AWS Batch features.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.batch.model.BatchException;
import software.amazon.awssdk.services.batch.model.ClientException;
import software.amazon.awssdk.services.batch.model.CreateComputeEnvironmentResponse;
import software.amazon.awssdk.services.batch.model.JobSummary;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeSecurityGroupsRequest;
import software.amazon.awssdk.services.ec2.model.DescribeSecurityGroupsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeSubnetsRequest;
import software.amazon.awssdk.services.ec2.model.DescribeSubnetsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeVpcsRequest;
import software.amazon.awssdk.services.ec2.model.Filter;
import software.amazon.awssdk.services.ec2.model.SecurityGroup;
import software.amazon.awssdk.services.ec2.model.Subnet;
import software.amazon.awssdk.services.ec2.model.Vpc;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * NOTE
 * This scenario submits a job that pulls a Docker image named echo-text from Amazon ECR to Amazon Fargate.
 *
 * To place this Docker image on Amazon ECR, run the following Basics scenario.
 *
 * https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr
 *
 */
public class BatchScenario {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");

    // Define two stacks used in this Basics Scenario.
    private static final String ROLES_STACK = "RolesStack";
    private static String defaultSubnet;
    private static String defaultSecurityGroup;

    private static final Logger logger = LoggerFactory.getLogger(BatchScenario.class);

    public static void main(String[] args) throws InterruptedException {

        BatchActions batchActions = new BatchActions();
        Scanner scanner = new Scanner(System.in);
        String computeEnvironmentName = "my-compute-environment";
        String jobQueueName = "my-job-queue";
        String jobDefinitionName = "my-job-definition";

        // See the NOTE in this Java code example (at start).
        String dockerImage = "dkr.ecr.us-east-1.amazonaws.com/echo-text:echo-text";

        logger.info("""
            AWS Batch is a fully managed batch processing service that dynamically provisions the required compute
            resources for batch computing workloads. The Java V2 `BatchAsyncClient` allows
            developers to automate the submission, monitoring, and management of batch jobs.

            This scenario provides an example of setting up a compute environment, job queue and job definition,
            and then submitting a job.

            This scenario submits a job that pulls a Docker image named echo-text from Amazon ECR to Amazon Fargate.

            To place this Docker image on Amazon ECR, run the following Basics scenario.

            https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr

            Let's get started...

            You have two choices:

            1 - Run the entire program.
            2 - Delete an existing Compute Environment (created from a previous execution of
            this program that did not complete).
            """);

        while (true) {
            String input = scanner.nextLine();
            if (input.trim().equalsIgnoreCase("1")) {
                logger.info("Continuing with the program...");
               // logger.info("");
                break;
            } else if (input.trim().equalsIgnoreCase("2")) {
                String jobQueueARN = String.valueOf(batchActions. describeJobQueueAsync(computeEnvironmentName));
                if (!jobQueueARN.isEmpty()) {
                    batchActions.disableJobQueueAsync(jobQueueARN);
                    countdown(1);
                    batchActions.deleteJobQueueAsync(jobQueueARN);
                }

                try {
                    batchActions.disableComputeEnvironmentAsync(computeEnvironmentName)
                        .exceptionally(ex -> {
                            logger.info("Disable compute environment failed: " + ex.getMessage());
                            return null;
                        })
                        .join();
                } catch (CompletionException ex) {
                    logger.info("Failed to disable compute environment: " + ex.getMessage());
                }
                countdown(2);
                batchActions.deleteComputeEnvironmentAsync(computeEnvironmentName).join();
                return;
            } else {
                // Handle invalid input.
                logger.info("Invalid input. Please try again.");
            }
        }
        System.out.println(DASHES);

        waitForInputToContinue(scanner);
        // Get an AWS Account id used to retrieve the docker image from Amazon ECR.
        // Create a single-element array to store the `accountId` value.
        String[] accId = new String[1];
        CompletableFuture<String> accountIdFuture = batchActions.getAccountId();
        accountIdFuture.thenAccept(accountId -> {
            logger.info("Account ID: " + accountId);
            accId[0] = accountId;
        }).join();

        dockerImage = accId[0]+"."+dockerImage;

        // Get a default subnet and default security associated with the default VPC.
        getSubnetSecurityGroup();

        logger.info("Use AWS CloudFormation to create two IAM roles that are required for this scenario.");
        CloudFormationHelper.deployCloudFormationStack(ROLES_STACK);

        Map<String, String> stackOutputs = CloudFormationHelper.getStackOutputs(ROLES_STACK);
        String batchIAMRole = stackOutputs.get("BatchRoleArn");
        String executionRoleARN = stackOutputs.get("EcsRoleArn");

        logger.info("The IAM role needed to interact with AWS Batch is "+batchIAMRole);
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("1. Create a Batch compute environment");
        logger.info("""
            A compute environment is a resource where you can run your batch jobs.
            After creating a compute environment, you can define job queues and job definitions to submit jobs for
            execution.

            The benefit of creating a compute environment is it allows you to easily configure and manage the compute
            resources that will be used to run your Batch jobs. By separating the compute environment from the job definitions,
            you can easily scale your compute resources up or down as needed, without having to modify your job definitions.
            This makes it easier to manage your Batch workloads and ensures that your jobs have the necessary
            compute resources to run efficiently.
            """);

        waitForInputToContinue(scanner);
        try {
            CompletableFuture<CreateComputeEnvironmentResponse> future = batchActions.createComputeEnvironmentAsync(computeEnvironmentName, batchIAMRole, defaultSubnet, defaultSecurityGroup);
            CreateComputeEnvironmentResponse response = future.join();
            logger.info("Compute Environment ARN: " + response.computeEnvironmentArn());
        } catch (RuntimeException rte) {
            Throwable cause = rte.getCause();
            if (cause instanceof ClientException batchExceptionEx) {
                String myErrorCode = batchExceptionEx.awsErrorDetails().errorMessage();
                if ("Object already exists".contains(myErrorCode)) {
                    logger.info("The compute environment '" + computeEnvironmentName + "' already exists. Moving on...");
                } else {
                    logger.info("Batch error occurred: {} (Code: {})", batchExceptionEx.getMessage(), batchExceptionEx.awsErrorDetails().errorCode());
                    return;
                }
            } else {
                    logger.info("An unexpected error occurred: {}", (cause != null ? cause.getMessage() : rte.getMessage()));
            }
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("2. Check the status of the "+computeEnvironmentName +" Compute Environment.");
        waitForInputToContinue(scanner);
        try {
            CompletableFuture<String> future = batchActions.checkComputeEnvironmentsStatus(computeEnvironmentName);
            String status = future.join();
            logger.info("Compute Environment Status: " + status);

        } catch (RuntimeException rte) {
            Throwable cause = rte.getCause();
            if (cause instanceof ClientException batchExceptionEx) {
                logger.info("Batch error occurred: {} (Code: {})", batchExceptionEx.getMessage(), batchExceptionEx.awsErrorDetails().errorCode());
                return;
            } else {
                logger.info("An unexpected error occurred: " + (cause != null ? cause.getMessage() : rte.getMessage()));
                return;
            }
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("3. Create a job queue");
        logger.info("""
             A job queue is an essential component that helps manage the execution of your batch jobs.
             It acts as a buffer, where jobs are placed and then scheduled for execution based on their
             priority and the available resources in the compute environment.
             """);
        waitForInputToContinue(scanner);

        String jobQueueArn = null;
        try {
            CompletableFuture<String> jobQueueFuture = batchActions.createJobQueueAsync(jobQueueName, computeEnvironmentName);
            jobQueueArn = jobQueueFuture.join();
            logger.info("Job Queue ARN: " + jobQueueArn);

        } catch (RuntimeException rte) {
            Throwable cause = rte.getCause();
            if (cause instanceof BatchException batchExceptionEx) {
                String myErrorCode = batchExceptionEx.awsErrorDetails().errorMessage();
                if ("Object already exists".contains(myErrorCode)) {
                    logger.info("The job queue '" + jobQueueName + "' already exists. Moving on...");
                    // Retrieve the ARN of the job queue.
                    CompletableFuture<String> jobQueueArnFuture = batchActions.getJobQueueARN(jobQueueName);
                    jobQueueArn = jobQueueArnFuture.join();
                    logger.info("Job Queue ARN: " + jobQueueArn);
                } else {
                    logger.info("Batch error occurred: {} (Code: {})", batchExceptionEx.getMessage(), batchExceptionEx.awsErrorDetails().errorCode());
                    return;
                }
            } else {
                logger.info("An unexpected error occurred: " + (cause != null ? cause.getMessage() : rte.getMessage()));
                return; // End the execution
            }
        }
        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info("4. Register a Job Definition.");
        logger.info("""
            Registering a job in AWS Batch using the Fargate launch type ensures that all
            necessary parameters, such as the execution role, command to run, and so on
            are specified and reused across multiple job submissions.

             The job definition pulls a Docker image from Amazon ECR and executes the Docker image.
            """);

        waitForInputToContinue(scanner);
        String jobARN;
        try {
            String platform = "";
            while (true) {
                logger.info("""
                    On which platform/CPU architecture combination did you build the Docker image?:
                    1. Windows       X86_64
                    2. Mac or Linux  ARM64
                    3. Mac or Linux  X86_64

                    Please select 1, 2, or 3.
                    """);
                String platAns = scanner.nextLine().trim();
                if (platAns.equals("1")) {
                    platform = "X86_64";
                    break; // Exit loop since a valid option is selected
                } else if (platAns.equals("2")) {
                    platform = "ARM64";
                    break; // Exit loop since a valid option is selected
                } else if (platAns.equals("3")) {
                    platform = "X86_64";
                    break; // Exit loop since a valid option is selected
                } else {
                    System.out.println("Invalid input. Please select either 1 or 2.");
                }
            }

            jobARN = batchActions.registerJobDefinitionAsync(jobDefinitionName, executionRoleARN, dockerImage, platform)
                .exceptionally(ex -> {
                    System.err.println("Register job definition failed: " + ex.getMessage());
                    return null;
                })
                .join();
            if (jobARN != null) {
                logger.info("Job ARN: " + jobARN);
            }
        } catch (RuntimeException rte) {
            logger.error("A Batch exception occurred while registering the job: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
            return;
        }
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("5. Submit an AWS Batch job from a job definition.");
        waitForInputToContinue(scanner);
        String jobId;
        try {
            jobId = batchActions.submitJobAsync(jobDefinitionName, jobQueueName, jobARN)
                .exceptionally(ex -> {
                    System.err.println("Submit job failed: " + ex.getMessage());
                    return null;
                })
                .join();

            logger.info("The job id is "+jobId);
            logger.info("Let's wait 2 minutes for the job to complete");
            countdown(2);

        } catch (RuntimeException rte) {
            logger.error("A Batch exception occurred while submitting the job: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
            return;
        }
        waitForInputToContinue(scanner);
        System.out.println(DASHES);

        logger.info(DASHES);
        logger.info("6. Get a list of jobs applicable to the job queue.");

        waitForInputToContinue(scanner);
        try {
            List<JobSummary> jobs = batchActions.listJobsAsync(jobQueueName);
            jobs.forEach(job ->
                logger.info("Job ID: {}, Job Name: {}, Job Status: {}", job.jobId(), job.jobName(), job.status()));

        } catch (RuntimeException rte) {
            logger.info("A Batch exception occurred while submitting the job: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
            return;
        }

        waitForInputToContinue(scanner);
        logger.info(DASHES);

        logger.info(DASHES);
        logger.info("7. Check the status of job "+jobId);
        waitForInputToContinue(scanner);
        try {
            CompletableFuture<String> future = batchActions.describeJobAsync(jobId);
            String jobStatus = future.join();
            logger.info("Job Status: " + jobStatus);

        } catch (RuntimeException rte) {
            logger.info("A Batch exception occurred while submitting the job: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
            return;
        }

        waitForInputToContinue(scanner);
        System.out.println(DASHES);

        logger.info("8. Delete Batch resources");
        logger.info(
            """
            When deleting an AWS Batch compute environment, it does not happen instantaneously.
            There is typically a delay, similar to some other AWS resources.
            AWS Batch starts the deletion process.
            """);
        logger.info("Would you like to delete the AWS Batch resources such as the compute environment? (y/n)");
        String delAns = scanner.nextLine().trim();
        if (delAns.equalsIgnoreCase("y")) {
            logger.info("You selected to delete the AWS ECR resources.");
            logger.info("First, we will deregister the Job Definition.");
            waitForInputToContinue(scanner);
            try {
                batchActions.deregisterJobDefinitionAsync(jobARN)
                    .exceptionally(ex -> {
                        logger.info("Deregister job definition failed: " + ex.getMessage());
                        return null;
                    })
                    .join();
                logger.info(jobARN + " was deregistered");
            } catch (RuntimeException rte) {
                logger.error("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }

            logger.info("Second, we will disable and then delete the Job Queue.");
            waitForInputToContinue(scanner);
            try {
                batchActions.disableJobQueueAsync(jobQueueArn)
                    .exceptionally(ex -> {
                        logger.info("Disable job queue failed: " + ex.getMessage());
                        return null;
                    })
                    .join();
                logger.info(jobQueueArn + " was disabled");
            } catch (RuntimeException rte) {
                logger.info("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }

            batchActions.waitForJobQueueToBeDisabledAsync(jobQueueArn);
            try {
                CompletableFuture<Void> future = batchActions.waitForJobQueueToBeDisabledAsync(jobQueueArn);
                future.join();
                logger.info("Job queue is now disabled.");
            } catch (RuntimeException rte) {
                logger.info("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }

            waitForInputToContinue(scanner);
            try {
                batchActions.deleteJobQueueAsync(jobQueueArn);
                logger.info(jobQueueArn +" was deleted");
            } catch (RuntimeException rte) {
                logger.info("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }
            logger.info("Let's wait 2 minutes for the job queue to be deleted");
            countdown(2);
            waitForInputToContinue(scanner);

            logger.info("Third, we will delete the Compute Environment.");
            waitForInputToContinue(scanner);
            try {
                batchActions.disableComputeEnvironmentAsync(computeEnvironmentName)
                    .exceptionally(ex -> {
                        System.err.println("Disable compute environment failed: " + ex.getMessage());
                        return null;
                    })
                    .join();
                logger.info("Compute environment disabled") ;
            } catch (RuntimeException rte) {
                logger.info("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }

            batchActions.checkComputeEnvironmentsStatus(computeEnvironmentName).thenAccept(state -> {
                logger.info("Current State: " + state);
            }).join();

            logger.info("Lets wait 1 min for the compute environment to be deleted");
            countdown(1);

            try {
                batchActions.deleteComputeEnvironmentAsync(computeEnvironmentName).join();
                logger.info(computeEnvironmentName +" was deleted.");

            } catch (RuntimeException rte) {
                logger.info("A Batch exception occurred: {}", rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage());
                return;
            }
            waitForInputToContinue(scanner);
            CloudFormationHelper.destroyCloudFormationStack(ROLES_STACK);
        }

        logger.info(DASHES);
        logger.info("This concludes the AWS Batch SDK scenario");
        logger.info(DASHES);
    }

    private static void waitForInputToContinue(Scanner scanner) {
        while (true) {
            logger.info("");
            logger.info("Enter 'c' followed by <ENTER> to continue:");
            String input = scanner.nextLine();

            if (input.trim().equalsIgnoreCase("c")) {
                logger.info("Continuing with the program...");
                logger.info("");
                break;
            } else {
                // Handle invalid input.
                logger.info("Invalid input. Please try again.");
            }
        }
    }

    public static void countdown(int minutes) throws InterruptedException {
        int seconds = 0;
        for (int i = minutes * 60 + seconds; i >= 0; i--) {
            int displayMinutes = i / 60;
            int displaySeconds = i % 60;
            System.out.print(String.format("\r%02d:%02d", displayMinutes, displaySeconds));
            Thread.sleep(1000); // Wait for 1 second
        }
        logger.info("Countdown complete!");
    }

    private static void getSubnetSecurityGroup() {
        try (Ec2AsyncClient ec2Client = Ec2AsyncClient.create()) {
            CompletableFuture<Vpc> defaultVpcFuture = ec2Client.describeVpcs(DescribeVpcsRequest.builder()
                            .filters(Filter.builder()
                                    .name("is-default")
                                    .values("true")
                                    .build())
                            .build())
                    .thenApply(response -> response.vpcs().stream()
                            .findFirst()
                            .orElseThrow(() -> new RuntimeException("Default VPC not found")));

            CompletableFuture<String> defaultSubnetFuture = defaultVpcFuture
                    .thenCompose(vpc -> ec2Client.describeSubnets(DescribeSubnetsRequest.builder()
                                    .filters(Filter.builder()
                                                    .name("vpc-id")
                                                    .values(vpc.vpcId())
                                                    .build(),
                                            Filter.builder()
                                                    .name("default-for-az")
                                                    .values("true")
                                                    .build())
                                    .build())
                            .thenApply(DescribeSubnetsResponse::subnets)
                            .thenApply(subnets -> subnets.stream()
                                    .findFirst()
                                    .map(Subnet::subnetId)
                                    .orElseThrow(() -> new RuntimeException("No default subnet found"))));

            CompletableFuture<String> defaultSecurityGroupFuture = defaultVpcFuture
                    .thenCompose(vpc -> ec2Client.describeSecurityGroups(DescribeSecurityGroupsRequest.builder()
                                    .filters(Filter.builder()
                                                    .name("group-name")
                                                    .values("default")
                                                    .build(),
                                            Filter.builder()
                                                    .name("vpc-id")
                                                    .values(vpc.vpcId())
                                                    .build())
                                    .build())
                            .thenApply(DescribeSecurityGroupsResponse::securityGroups)
                            .thenApply(securityGroups -> securityGroups.stream()
                                    .findFirst()
                                    .map(SecurityGroup::groupId)
                                    .orElseThrow(() -> new RuntimeException("No default security group found"))));

            defaultSubnet = defaultSubnetFuture.join();
            defaultSecurityGroup = defaultSecurityGroupFuture.join();
        }
    }
}
```
A wrapper class for AWS Batch SDK methods.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.core.retry.RetryPolicy;
import software.amazon.awssdk.http.async.SdkAsyncHttpClient;
import software.amazon.awssdk.http.nio.netty.NettyNioAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.batch.BatchAsyncClient;
import software.amazon.awssdk.services.batch.BatchClient;
import software.amazon.awssdk.services.batch.model.AssignPublicIp;
import software.amazon.awssdk.services.batch.model.BatchException;
import software.amazon.awssdk.services.batch.model.CEState;
import software.amazon.awssdk.services.batch.model.CEType;
import software.amazon.awssdk.services.batch.model.CRType;
import software.amazon.awssdk.services.batch.model.ComputeEnvironmentOrder;
import software.amazon.awssdk.services.batch.model.ComputeResource;
import software.amazon.awssdk.services.batch.model.ContainerProperties;
import software.amazon.awssdk.services.batch.model.CreateComputeEnvironmentRequest;
import software.amazon.awssdk.services.batch.model.CreateComputeEnvironmentResponse;
import software.amazon.awssdk.services.batch.model.CreateJobQueueRequest;
import software.amazon.awssdk.services.batch.model.DeleteComputeEnvironmentRequest;
import software.amazon.awssdk.services.batch.model.DeleteComputeEnvironmentResponse;
import software.amazon.awssdk.services.batch.model.DeleteJobQueueRequest;
import software.amazon.awssdk.services.batch.model.DeleteJobQueueResponse;
import software.amazon.awssdk.services.batch.model.DeregisterJobDefinitionRequest;
import software.amazon.awssdk.services.batch.model.DeregisterJobDefinitionResponse;
import software.amazon.awssdk.services.batch.model.DescribeComputeEnvironmentsRequest;
import software.amazon.awssdk.services.batch.model.DescribeComputeEnvironmentsResponse;
import software.amazon.awssdk.services.batch.model.DescribeJobQueuesRequest;
import software.amazon.awssdk.services.batch.model.DescribeJobQueuesResponse;
import software.amazon.awssdk.services.batch.model.DescribeJobsRequest;
import software.amazon.awssdk.services.batch.model.DescribeJobsResponse;
import software.amazon.awssdk.services.batch.model.JQState;
import software.amazon.awssdk.services.batch.model.JobDefinitionType;
import software.amazon.awssdk.services.batch.model.JobDetail;
import software.amazon.awssdk.services.batch.model.JobQueueDetail;
import software.amazon.awssdk.services.batch.model.JobStatus;
import software.amazon.awssdk.services.batch.model.JobSummary;
import software.amazon.awssdk.services.batch.model.ListJobsRequest;
import software.amazon.awssdk.services.batch.model.RegisterJobDefinitionResponse;
import software.amazon.awssdk.services.batch.model.NetworkConfiguration;
import software.amazon.awssdk.services.batch.model.PlatformCapability;
import software.amazon.awssdk.services.batch.model.RegisterJobDefinitionRequest;
import software.amazon.awssdk.services.batch.model.ResourceRequirement;
import software.amazon.awssdk.services.batch.model.ResourceType;
import software.amazon.awssdk.services.batch.model.RuntimePlatform;
import software.amazon.awssdk.services.batch.model.SubmitJobRequest;
import software.amazon.awssdk.services.batch.model.CreateJobQueueResponse;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.atomic.AtomicBoolean;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.services.batch.model.SubmitJobResponse;
import software.amazon.awssdk.services.batch.model.UpdateComputeEnvironmentRequest;
import software.amazon.awssdk.services.batch.model.UpdateComputeEnvironmentResponse;
import software.amazon.awssdk.services.batch.model.UpdateJobQueueRequest;
import software.amazon.awssdk.services.batch.model.UpdateJobQueueResponse;
import software.amazon.awssdk.services.batch.paginators.ListJobsPublisher;
import software.amazon.awssdk.services.sts.StsAsyncClient;
import software.amazon.awssdk.services.sts.model.GetCallerIdentityResponse;

public class BatchActions {
    private static BatchAsyncClient batchClient;

    private static final Logger logger = LoggerFactory.getLogger(BatchActions.class);

    private static BatchAsyncClient getAsyncClient() {
        if (batchClient == null) {
            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                .maxConcurrency(100)
                .connectionTimeout(Duration.ofSeconds(60))
                .readTimeout(Duration.ofSeconds(60))
                .writeTimeout(Duration.ofSeconds(60))
                .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                .apiCallTimeout(Duration.ofMinutes(2))
                .apiCallAttemptTimeout(Duration.ofSeconds(90))
                .retryPolicy(RetryPolicy.builder()
                    .numRetries(3)
                    .build())
                .build();

            batchClient = BatchAsyncClient.builder()
                .region(Region.US_EAST_1)
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return batchClient;
    }

    /**
     * Asynchronously creates a new compute environment in AWS Batch.
     *
     * @param computeEnvironmentName the name of the compute environment to create
     * @param batchIAMRole the IAM role to be used by the compute environment
     * @param subnet the subnet ID to be used for the compute environment
     * @param secGroup the security group ID to be used for the compute environment
     * @return a {@link CompletableFuture} representing the asynchronous operation, which will complete with the
     *         {@link CreateComputeEnvironmentResponse} when the compute environment has been created
     * @throws BatchException if there is an error creating the compute environment
     * @throws RuntimeException if there is an unexpected error during the operation
     */
    public CompletableFuture<CreateComputeEnvironmentResponse> createComputeEnvironmentAsync(
        String computeEnvironmentName, String batchIAMRole, String subnet, String secGroup) {
        CreateComputeEnvironmentRequest environmentRequest = CreateComputeEnvironmentRequest.builder()
            .computeEnvironmentName(computeEnvironmentName)
            .type(CEType.MANAGED)
            .state(CEState.ENABLED)
            .computeResources(ComputeResource.builder()
                .type(CRType.FARGATE)
                .maxvCpus(256)
                .subnets(Collections.singletonList(subnet))
                .securityGroupIds(Collections.singletonList(secGroup))
                .build())
            .serviceRole(batchIAMRole)
            .build();

        CompletableFuture<CreateComputeEnvironmentResponse> response = getAsyncClient().createComputeEnvironment(environmentRequest);
        response.whenComplete((resp, ex) -> {
            if (ex != null) {
               String errorMessage = "Unexpected error occurred: " + ex.getMessage();
               throw new RuntimeException(errorMessage, ex);
            }
        });

        return response;
    }

    public CompletableFuture<DeleteComputeEnvironmentResponse> deleteComputeEnvironmentAsync(String computeEnvironmentName) {
        DeleteComputeEnvironmentRequest deleteComputeEnvironment = DeleteComputeEnvironmentRequest.builder()
            .computeEnvironment(computeEnvironmentName)
            .build();

        return getAsyncClient().deleteComputeEnvironment(deleteComputeEnvironment)
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof BatchException) {
                        throw new RuntimeException(cause);
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                }
            });
    }

    /**
     * Checks the status of the specified compute environment.
     *
     * @param computeEnvironmentName the name of the compute environment to check
     * @return a CompletableFuture containing the status of the compute environment, or "ERROR" if an exception occurs
     */
    public CompletableFuture<String> checkComputeEnvironmentsStatus(String computeEnvironmentName) {
        if (computeEnvironmentName == null || computeEnvironmentName.isEmpty()) {
            throw new IllegalArgumentException("Compute environment name cannot be null or empty");
        }

        DescribeComputeEnvironmentsRequest environmentsRequest = DescribeComputeEnvironmentsRequest.builder()
            .computeEnvironments(computeEnvironmentName)
            .build();

        CompletableFuture<DescribeComputeEnvironmentsResponse> response = getAsyncClient().describeComputeEnvironments(environmentsRequest);
        response.whenComplete((resp, ex) -> {
            if (ex != null) {
                String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                throw new RuntimeException(errorMessage, ex);
            }
        });

        return response.thenApply(resp -> resp.computeEnvironments().stream()
            .map(env -> env.statusAsString())
            .findFirst()
            .orElse("UNKNOWN"));
    }

    /**
     * Creates a job queue asynchronously.
     *
     * @param jobQueueName the name of the job queue to create
     * @param computeEnvironmentName the name of the compute environment to associate with the job queue
     * @return a CompletableFuture that completes with the Amazon Resource Name (ARN) of the job queue
     */
    public CompletableFuture<String> createJobQueueAsync(String jobQueueName, String computeEnvironmentName) {
        if (jobQueueName == null || jobQueueName.isEmpty()) {
            throw new IllegalArgumentException("Job queue name cannot be null or empty");
        }
        if (computeEnvironmentName == null || computeEnvironmentName.isEmpty()) {
            throw new IllegalArgumentException("Compute environment name cannot be null or empty");
        }

        CreateJobQueueRequest request = CreateJobQueueRequest.builder()
            .jobQueueName(jobQueueName)
            .priority(1)
            .computeEnvironmentOrder(ComputeEnvironmentOrder.builder()
                .computeEnvironment(computeEnvironmentName)
                .order(1)
                .build())
            .build();

        CompletableFuture<CreateJobQueueResponse> response = getAsyncClient().createJobQueue(request);
        response.whenComplete((resp, ex) -> {
            if (ex != null) {
                String errorMessage = "Unexpected error occurred: " + ex.getMessage();
                throw new RuntimeException(errorMessage, ex);
            }
        });

        return response.thenApply(CreateJobQueueResponse::jobQueueArn);
    }

    /**
     * Asynchronously lists the jobs in the specified job queue with the given job status.
     *
     * @param jobQueue the name of the job queue to list jobs from
     * @return a List<JobSummary> that contains the jobs that succeeded
     */
    public List<JobSummary> listJobsAsync(String jobQueue) {
        if (jobQueue == null || jobQueue.isEmpty()) {
            throw new IllegalArgumentException("Job queue cannot be null or empty");
        }

        ListJobsRequest listJobsRequest = ListJobsRequest.builder()
            .jobQueue(jobQueue)
            .jobStatus(JobStatus.SUCCEEDED)  // Filter jobs by status.
            .build();

        List<JobSummary> jobSummaries = new ArrayList<>();
        ListJobsPublisher listJobsPaginator = getAsyncClient().listJobsPaginator(listJobsRequest);
        CompletableFuture<Void> future = listJobsPaginator.subscribe(response -> {
            jobSummaries.addAll(response.jobSummaryList());
        });
        future.join();
        return jobSummaries;
    }

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

    /**
     * Deregisters a job definition asynchronously.
     *
     * @param jobDefinition the name of the job definition to be deregistered
     * @return a CompletableFuture that completes when the job definition has been deregistered
     * or an exception has occurred
     */
    public CompletableFuture<DeregisterJobDefinitionResponse> deregisterJobDefinitionAsync(String jobDefinition) {
        DeregisterJobDefinitionRequest jobDefinitionRequest = DeregisterJobDefinitionRequest.builder()
            .jobDefinition(jobDefinition)
            .build();

        CompletableFuture<DeregisterJobDefinitionResponse> responseFuture = getAsyncClient().deregisterJobDefinition(jobDefinitionRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        });

        return responseFuture;
    }

    /**
     * Disables the specified job queue asynchronously.
     *
     * @param jobQueueArn the Amazon Resource Name (ARN) of the job queue to be disabled
     * @return a {@link CompletableFuture} that completes when the job queue update operation is complete,
     *         or completes exceptionally if an error occurs during the operation
     */
    public CompletableFuture<Void> disableJobQueueAsync(String jobQueueArn) {
        UpdateJobQueueRequest updateRequest = UpdateJobQueueRequest.builder()
            .jobQueue(jobQueueArn)
            .state(JQState.DISABLED)
            .build();

        CompletableFuture<UpdateJobQueueResponse> responseFuture = getAsyncClient().updateJobQueue(updateRequest);
        return responseFuture.whenComplete((updateResponse, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to update job queue: " + ex.getMessage(), ex);
            }
        }).thenApply(updateResponse -> null);
    }

    /**
     * Deletes a Batch job queue asynchronously.
     *
     * @param jobQueueArn The Amazon Resource Name (ARN) of the job queue to delete.
     * @return A CompletableFuture that represents the asynchronous deletion of the job queue.
     *         The future completes when the job queue has been successfully deleted or if an error occurs.
     *         If successful, the future will be completed with a {@code Void} value.
     *         If an error occurs, the future will be completed exceptionally with the thrown exception.
     */
    public CompletableFuture<Void> deleteJobQueueAsync(String jobQueueArn) {
        DeleteJobQueueRequest deleteRequest = DeleteJobQueueRequest.builder()
            .jobQueue(jobQueueArn)
            .build();

        CompletableFuture<DeleteJobQueueResponse> responseFuture = getAsyncClient().deleteJobQueue(deleteRequest);
        return responseFuture.whenComplete((deleteResponse, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to delete job queue: " + ex.getMessage(), ex);
            }
        }).thenApply(deleteResponse -> null);
    }

    /**
     * Asynchronously describes the job queue associated with the specified compute environment.
     *
     * @param computeEnvironmentName the name of the compute environment to find the associated job queue for
     * @return a {@link CompletableFuture} that, when completed, contains the job queue ARN associated with the specified compute environment
     * @throws RuntimeException if the job queue description fails
     */
    public CompletableFuture<String> describeJobQueueAsync(String computeEnvironmentName) {
        DescribeJobQueuesRequest describeJobQueuesRequest = DescribeJobQueuesRequest.builder()
            .build();

        CompletableFuture<DescribeJobQueuesResponse> responseFuture = getAsyncClient().describeJobQueues(describeJobQueuesRequest);
        return responseFuture.whenComplete((describeJobQueuesResponse, ex) -> {
            if (describeJobQueuesResponse != null) {
                String jobQueueARN;
                for (JobQueueDetail jobQueueDetail : describeJobQueuesResponse.jobQueues()) {
                    for (ComputeEnvironmentOrder computeEnvironmentOrder : jobQueueDetail.computeEnvironmentOrder()) {
                        String computeEnvironment = computeEnvironmentOrder.computeEnvironment();
                        String name = getComputeEnvironmentName(computeEnvironment);
                        if (name.equals(computeEnvironmentName)) {
                            jobQueueARN = jobQueueDetail.jobQueueArn();
                            logger.info("Job queue ARN associated with the compute environment: " + jobQueueARN);
                        }
                    }
                }
            } else {
                throw new RuntimeException("Failed to describe job queue: " + ex.getMessage(), ex);
            }
        }).thenApply(describeJobQueuesResponse -> {
            String jobQueueARN = "";
            for (JobQueueDetail jobQueueDetail : describeJobQueuesResponse.jobQueues()) {
                for (ComputeEnvironmentOrder computeEnvironmentOrder : jobQueueDetail.computeEnvironmentOrder()) {
                    String computeEnvironment = computeEnvironmentOrder.computeEnvironment();
                    String name = getComputeEnvironmentName(computeEnvironment);
                    if (name.equals(computeEnvironmentName)) {
                        jobQueueARN = jobQueueDetail.jobQueueArn();
                    }
                }
            }
            return jobQueueARN;
        });
    }

    /**
     * Disables the specified compute environment asynchronously.
     *
     * @param computeEnvironmentName the name of the compute environment to disable
     * @return a CompletableFuture that completes when the compute environment is disabled
     */
    public CompletableFuture<UpdateComputeEnvironmentResponse> disableComputeEnvironmentAsync(String computeEnvironmentName) {
        UpdateComputeEnvironmentRequest updateRequest = UpdateComputeEnvironmentRequest.builder()
            .computeEnvironment(computeEnvironmentName)
            .state(CEState.DISABLED)
            .build();

        CompletableFuture<UpdateComputeEnvironmentResponse> responseFuture = getAsyncClient().updateComputeEnvironment(updateRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to disable compute environment: " + ex.getMessage(), ex);
            }
        });

        return responseFuture;
    }

    /**
     * Submits a job asynchronously to the AWS Batch service.
     *
     * @param jobDefinitionName the name of the job definition to use
     * @param jobQueueName the name of the job queue to submit the job to
     * @param jobARN the Amazon Resource Name (ARN) of the job definition
     * @return a CompletableFuture that, when completed, contains the job ID of the submitted job
     */
    public CompletableFuture<String> submitJobAsync(String jobDefinitionName, String jobQueueName, String jobARN) {
        SubmitJobRequest jobRequest = SubmitJobRequest.builder()
            .jobDefinition(jobARN)
            .jobName(jobDefinitionName)
            .jobQueue(jobQueueName)
            .build();

        CompletableFuture<SubmitJobResponse> responseFuture = getAsyncClient().submitJob(jobRequest);
        responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        });

        return responseFuture.thenApply(SubmitJobResponse::jobId);
    }

    /**
     * Asynchronously retrieves the status of a specific job.
     *
     * @param jobId the ID of the job to retrieve the status for
     * @return a CompletableFuture that completes with the job status
     */
    public CompletableFuture<String> describeJobAsync(String jobId) {
        DescribeJobsRequest describeJobsRequest = DescribeJobsRequest.builder()
            .jobs(jobId)
            .build();

        CompletableFuture<DescribeJobsResponse> responseFuture = getAsyncClient().describeJobs(describeJobsRequest);
        return responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        }).thenApply(response -> response.jobs().get(0).status().toString());
    }

    /**
     * Disables the specific job queue using the asynchronous Java client.
     *
     * @param jobQueueArn the Amazon Resource Name (ARN) of the job queue to wait for
     * @return a {@link CompletableFuture} that completes when the job queue is disabled
     */
    public CompletableFuture<Void> waitForJobQueueToBeDisabledAsync(String jobQueueArn) {
        AtomicBoolean isDisabled = new AtomicBoolean(false);
        return CompletableFuture.runAsync(() -> {
            while (!isDisabled.get()) {
                DescribeJobQueuesRequest describeRequest = DescribeJobQueuesRequest.builder()
                    .jobQueues(jobQueueArn)
                    .build();

                CompletableFuture<DescribeJobQueuesResponse> responseFuture = getAsyncClient().describeJobQueues(describeRequest);
                responseFuture.whenComplete((describeResponse, ex) -> {
                    if (describeResponse != null) {
                        for (JobQueueDetail jobQueue : describeResponse.jobQueues()) {
                            if (jobQueue.jobQueueArn().equals(jobQueueArn) && jobQueue.state() == JQState.DISABLED) {
                                isDisabled.set(true);
                                break;
                            }
                        }
                    } else {
                        throw new RuntimeException("Error describing job queues", ex);
                    }
                }).join();

                if (!isDisabled.get()) {
                    try {
                        logger.info("Waiting for job queue to be disabled...");
                        Thread.sleep(5000);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        throw new RuntimeException("Thread interrupted while waiting for job queue to be disabled", e);
                    }
                }
            }
        }).whenComplete((result, throwable) -> {
            if (throwable != null) {
                throw new RuntimeException("Error while waiting for job queue to be disabled", throwable);
            }
        });
    }

    public CompletableFuture<String> getJobQueueARN(String jobQueueName) {
        // Describe the job queue asynchronously
        CompletableFuture<DescribeJobQueuesResponse> describeJobQueuesFuture = batchClient.describeJobQueues(
            DescribeJobQueuesRequest.builder()
                .jobQueues(jobQueueName)
                .build()
        );

        // Handle the asynchronous response and return the Job Queue ARN in the CompletableFuture<String>
        CompletableFuture<String> jobQueueArnFuture = new CompletableFuture<>();
        describeJobQueuesFuture.whenComplete((response, error) -> {
            if (error != null) {
                if (error instanceof BatchException) {
                    logger.info("Batch error: " + ((BatchException) error).awsErrorDetails().errorMessage());
                } else {
                    logger.info("Error describing job queue: " + error.getMessage());
                }
                jobQueueArnFuture.completeExceptionally(new RuntimeException("Failed to retrieve Job Queue ARN", error));
            } else {
                if (response.jobQueues().isEmpty()) {
                    jobQueueArnFuture.completeExceptionally(new RuntimeException("Job queue not found: " + jobQueueName));
                } else {
                    // Assuming only one job queue is returned for the given name
                    String jobQueueArn = response.jobQueues().get(0).jobQueueArn();
                    jobQueueArnFuture.complete(jobQueueArn);
                }
            }
        });

        return jobQueueArnFuture;
    }

    private static String getComputeEnvironmentName(String computeEnvironment) {
        String[] parts = computeEnvironment.split("/");
        if (parts.length == 2) {
            return parts[1];
        }
        return null;
    }

    public CompletableFuture<String> getAccountId() {
        StsAsyncClient stsAsyncClient = StsAsyncClient.builder()
            .region(Region.US_EAST_1)
            .build();

        return stsAsyncClient.getCallerIdentity()
            .thenApply(GetCallerIdentityResponse::account);
    }

}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [CreateComputeEnvironment](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateComputeEnvironment)
  + [CreateJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateJobQueue)
  + [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeleteComputeEnvironment)
  + [DeleteJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeleteJobQueue)
  + [DeregisterJobDefinition](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DeregisterJobDefinition)
  + [DescribeComputeEnvironments](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeComputeEnvironments)
  + [DescribeJobQueues](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobQueues)
  + [DescribeJobs](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobs)
  + [ListJobsPaginator](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListJobsPaginator)
  + [RegisterJobDefinition](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/RegisterJobDefinition)
  + [SubmitJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/SubmitJob)
  + [UpdateComputeEnvironment](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateComputeEnvironment)
  + [UpdateJobQueue](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateJobQueue)

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).
Run an interactive scenario at a command prompt.

```
class BatchScenario:
    """Runs the AWS Batch Basics scenario."""

    def __init__(
        self,
        batch_wrapper: BatchWrapper,
        iam_client=None,
        ec2_client=None,
    ) -> None:
        """
        Initializes the scenario.

        The scenario self-provisions the networking (default VPC subnet and
        security group) and the ECS task execution role that Fargate jobs
        require, so it can be run with only AWS credentials. All provisioned
        resources are removed in ``cleanup``.

        :param batch_wrapper: A BatchWrapper instance for Batch operations.
        :param iam_client: A Boto3 IAM client (created if not supplied).
        :param ec2_client: A Boto3 EC2 client (created if not supplied).
        """
        self.batch_wrapper = batch_wrapper
        self.iam_client = iam_client or boto3.client("iam")
        self.ec2_client = ec2_client or boto3.client("ec2")
        self.ce_name = None
        self.ce_arn = None
        self.jq_name = None
        self.jq_arn = None
        self.jd_name = None
        self.jd_arn = None
        self.jd_revision = None
        self.job_id = None
        self.subnet_ids = None
        self.security_group_ids = None
        self.execution_role_name = None
        self.execution_role_arn = None

    def discover_networking(self) -> None:
        """
        Finds a subnet and security group in the default VPC.

        This lets the scenario run without the user supplying networking IDs,
        matching the self-contained behavior of the other Batch Basics examples.

        :raises RuntimeError: If no default VPC or no subnet is found.
        """
        vpcs = self.ec2_client.describe_vpcs(
            Filters=[{"Name": "isDefault", "Values": ["true"]}]
        ).get("Vpcs", [])
        if not vpcs:
            raise RuntimeError(
                "No default VPC found. Create a default VPC or run this scenario "
                "in a region that has one."
            )
        vpc_id = vpcs[0]["VpcId"]

        subnets = self.ec2_client.describe_subnets(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        ).get("Subnets", [])
        if not subnets:
            raise RuntimeError(f"No subnets found in default VPC {vpc_id}.")
        # Prefer a subnet that assigns public IPs so the Fargate task can pull
        # its public ECR image; fall back to the first subnet otherwise. One
        # subnet is sufficient for the Basics scenario.
        public_subnets = [s for s in subnets if s.get("MapPublicIpOnLaunch")]
        chosen = public_subnets[0] if public_subnets else subnets[0]
        self.subnet_ids = [chosen["SubnetId"]]

        groups = self.ec2_client.describe_security_groups(
            Filters=[
                {"Name": "vpc-id", "Values": [vpc_id]},
                {"Name": "group-name", "Values": ["default"]},
            ]
        ).get("SecurityGroups", [])
        if not groups:
            raise RuntimeError(f"No default security group found in VPC {vpc_id}.")
        self.security_group_ids = [groups[0]["GroupId"]]

    def create_execution_role(self) -> None:
        """
        Creates an ECS task execution role for Fargate jobs.

        Fargate requires an execution role that trusts ecs-tasks.amazonaws.com
        and has the AmazonECSTaskExecutionRolePolicy so the agent can pull the
        container image and write logs. The role is deleted in ``cleanup``.
        """
        response = self.iam_client.create_role(
            RoleName=self.execution_role_name,
            AssumeRolePolicyDocument=json.dumps(ECS_TASKS_TRUST_POLICY),
            Description="ECS task execution role for the Batch Basics scenario.",
        )
        self.execution_role_arn = response["Role"]["Arn"]
        self.iam_client.attach_role_policy(
            RoleName=self.execution_role_name,
            PolicyArn=ECS_EXECUTION_POLICY_ARN,
        )
        # IAM is eventually consistent; give the role a moment to propagate
        # before Batch/Fargate tries to assume it.
        time.sleep(10)
        print(f"Created execution role: {self.execution_role_arn}")

    def setup(self, timestamp: str) -> None:
        """
        Provisions all prerequisites: networking discovery and the ECS task
        execution role, and derives the resource names.

        :param timestamp: A unique timestamp string for naming resources.
        """
        self.ce_name = f"batch-basics-fargate-ce-{timestamp}"
        self.jq_name = f"batch-basics-job-queue-{timestamp}"
        self.jd_name = f"batch-basics-job-def-{timestamp}"
        self.execution_role_name = f"batch-basics-exec-role-{timestamp}"

        print("\nDiscovering default VPC networking...")
        self.discover_networking()
        print(
            f"  Subnets: {', '.join(self.subnet_ids)}\n"
            f"  Security Group: {', '.join(self.security_group_ids)}"
        )
        print("Creating ECS task execution role...")
        self.create_execution_role()

    def create_compute_environment(self) -> None:
        """Step 1: Create a Fargate compute environment."""
        print("\n" + "-" * 80)
        print("Step 1: Create a Fargate compute environment")
        print(f"Creating compute environment: {self.ce_name}")

        response = self.batch_wrapper.create_compute_environment(
            compute_environment_name=self.ce_name,
            subnet_ids=self.subnet_ids,
            security_group_ids=self.security_group_ids,
        )
        self.ce_arn = response["computeEnvironmentArn"]
        print(f"Compute environment ARN: {self.ce_arn}")

        print("Waiting for compute environment to become VALID...")
        env = self.batch_wrapper.wait_for_compute_environment_valid(self.ce_name)
        print(
            f"Compute environment is VALID.\n"
            f"  Name: {env['computeEnvironmentName']}\n"
            f"  Type: {env.get('type', 'N/A')}\n"
            f"  State: {env.get('state', 'N/A')}\n"
            f"  Status: {env.get('status', 'N/A')}"
        )
        print("-" * 80)

    def create_job_queue(self) -> None:
        """Step 2: Create a job queue."""
        print("\n" + "-" * 80)
        print("Step 2: Create a job queue")
        print(f"Creating job queue: {self.jq_name}")

        response = self.batch_wrapper.create_job_queue(
            job_queue_name=self.jq_name,
            compute_environment_name=self.ce_name,
        )
        self.jq_arn = response["jobQueueArn"]
        print(f"Job queue ARN: {self.jq_arn}")
        # A newly created job queue is briefly in CREATING status; submit_job
        # requires it to be VALID, so wait before continuing.
        print("Waiting for job queue to become VALID...")
        self.batch_wrapper.wait_for_job_queue_valid(self.jq_name)
        print("Job queue is ready.")
        print("-" * 80)

    def register_job_definition(self) -> None:
        """Step 3: Register a job definition."""
        print("\n" + "-" * 80)
        print("Step 3: Register a job definition")
        print(f"Registering job definition: {self.jd_name}")

        response = self.batch_wrapper.register_job_definition(
            job_definition_name=self.jd_name,
            execution_role_arn=self.execution_role_arn,
        )
        self.jd_arn = response["jobDefinitionArn"]
        self.jd_revision = response["revision"]
        print(f"Job definition ARN: {self.jd_arn}")
        print(f"Revision: {self.jd_revision}")
        print("-" * 80)

    def submit_job(self) -> None:
        """Step 4: Submit a job."""
        print("\n" + "-" * 80)
        print("Step 4: Submit a job")

        job_name = "batch-basics-hello-job"
        print(f"Submitting job: {job_name}")
        response = self.batch_wrapper.submit_job(
            job_name=job_name,
            job_queue=self.jq_name,
            job_definition=f"{self.jd_name}:{self.jd_revision}",
        )
        self.job_id = response["jobId"]
        print(
            f"Job submitted successfully.\n"
            f"  Job Name: {response['jobName']}\n"
            f"  Job ID: {self.job_id}\n"
            f"  Job ARN: {response.get('jobArn', 'N/A')}"
        )
        print("-" * 80)

    def monitor_job(self) -> None:
        """Step 5: Monitor the job."""
        print("\n" + "-" * 80)
        print("Step 5: Monitor the job")
        print(f"Waiting for job {self.job_id} to complete...")

        job = self.batch_wrapper.wait_for_job_complete(self.job_id)
        status = job.get("status", "UNKNOWN")
        if status == "SUCCEEDED":
            print("Job completed successfully!")
        else:
            print(f"Job ended with status: {status}")
            reason = job.get("statusReason", "No reason provided")
            print(f"  Status Reason: {reason}")

        print(f"  Final Status: {status}")
        container = job.get("container", {})
        exit_code = container.get("exitCode", "N/A")
        print(f"  Exit Code: {exit_code}")
        print("-" * 80)

    def list_jobs(self) -> None:
        """Step 6: List jobs in the queue."""
        print("\n" + "-" * 80)
        print("Step 6: List jobs in the queue")
        print(f"Listing SUCCEEDED jobs in queue: {self.jq_name}")

        job_summaries = self.batch_wrapper.list_jobs(
            job_queue=self.jq_name, job_status="SUCCEEDED"
        )
        if job_summaries:
            print(f"Found {len(job_summaries)} job(s):")
            for js in job_summaries:
                print(
                    f"  - Job ID: {js['jobId']} | "
                    f"Name: {js['jobName']} | "
                    f"Status: {js.get('status', 'N/A')}"
                )
        else:
            print("No SUCCEEDED jobs found.")
        print("-" * 80)

    def cleanup(self) -> None:
        """
        Cleans up all resources in reverse dependency order.

        Uses only Batch service operations (no CloudFormation). Each resource
        is waited into a stable state before the next transition so deletes do
        not fail with "resource is being modified". A success message is only
        printed when every step succeeds; otherwise the resources that could
        not be removed are listed so the user can delete them manually.
        """
        print("\n" + "-" * 80)
        print("Cleaning up resources...")

        leftovers = []

        # Deregister job definition.
        if self.jd_arn:
            try:
                print(f"Deregistering job definition: {self.jd_arn} ... ", end="")
                self.batch_wrapper.deregister_job_definition(self.jd_arn)
                print("done.")
            except Exception as e:
                logger.error("Error deregistering job definition: %s", e)
                print(f"error: {e}")
                leftovers.append(f"job definition {self.jd_arn}")

        # Disable and delete the job queue. The queue must be VALID before it
        # can be updated, and DISABLED/VALID before it can be deleted.
        if self.jq_name:
            queue_deleted = False
            try:
                print(f"Disabling job queue: {self.jq_name} ... ", end="")
                self.batch_wrapper.wait_for_job_queue_valid(self.jq_name)
                self.batch_wrapper.update_job_queue(self.jq_name, state="DISABLED")
                self.batch_wrapper.wait_for_job_queue_disabled(self.jq_name)
                print("done.")
            except Exception as e:
                logger.error("Error disabling job queue: %s", e)
                print(f"error: {e}")

            try:
                print(f"Deleting job queue: {self.jq_name} ... ", end="")
                self.batch_wrapper.delete_job_queue(self.jq_name)
                # The queue is fully gone only after it leaves the DELETING
                # state; wait so the compute environment can be deleted next.
                self.batch_wrapper.wait_for_job_queue_disabled(self.jq_name)
                print("done.")
                queue_deleted = True
            except Exception as e:
                logger.error("Error deleting job queue: %s", e)
                print(f"error: {e}")
            if not queue_deleted:
                leftovers.append(f"job queue {self.jq_name}")

        # Disable and delete the compute environment. It must be DISABLED and
        # VALID before deletion, otherwise AWS Batch rejects the delete.
        if self.ce_name:
            ce_deleted = False
            try:
                print(f"Disabling compute environment: {self.ce_name} ... ", end="")
                self.batch_wrapper.wait_for_compute_environment_valid(self.ce_name)
                self.batch_wrapper.update_compute_environment(
                    self.ce_name, state="DISABLED"
                )
                self.batch_wrapper.wait_for_compute_environment_disabled(self.ce_name)
                print("done.")
            except Exception as e:
                logger.error("Error disabling compute environment: %s", e)
                print(f"error: {e}")

            try:
                print(f"Deleting compute environment: {self.ce_name} ... ", end="")
                self.batch_wrapper.delete_compute_environment(self.ce_name)
                print("done.")
                ce_deleted = True
            except Exception as e:
                logger.error("Error deleting compute environment: %s", e)
                print(f"error: {e}")
            if not ce_deleted:
                leftovers.append(f"compute environment {self.ce_name}")

        # Delete the ECS task execution role the scenario created. Detach the
        # managed policy first; a role cannot be deleted while policies are
        # attached.
        if self.execution_role_name:
            role_deleted = False
            try:
                print(
                    f"Deleting execution role: {self.execution_role_name} ... ",
                    end="",
                )
                self.iam_client.detach_role_policy(
                    RoleName=self.execution_role_name,
                    PolicyArn=ECS_EXECUTION_POLICY_ARN,
                )
                self.iam_client.delete_role(RoleName=self.execution_role_name)
                print("done.")
                role_deleted = True
            except ClientError as e:
                logger.error("Error deleting execution role: %s", e)
                print(f"error: {e}")
            if not role_deleted:
                leftovers.append(f"IAM role {self.execution_role_name}")

        if leftovers:
            print(
                "\nCleanup incomplete. The following resources were NOT deleted "
                "and must be removed manually to avoid charges:"
            )
            for item in leftovers:
                print(f"  - {item}")
        else:
            print("All resources cleaned up successfully.")
        print("-" * 80)

    def run(self) -> None:
        """Runs the full scenario."""
        print("=" * 80)
        print("Welcome to the AWS Batch Basics scenario!")
        print("=" * 80)

        self.create_compute_environment()
        self.create_job_queue()
        self.register_job_definition()
        self.submit_job()
        self.monitor_job()
        self.list_jobs()
```
Create a class that wraps Batch operations.

```
class BatchWrapper:
    """Encapsulates AWS Batch operations."""

    def __init__(self, batch_client: Any) -> None:
        """
        Initializes the BatchWrapper with an AWS Batch client.

        :param batch_client: A Boto3 AWS Batch client.
        """
        self.batch_client = batch_client
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateComputeEnvironment)
  + [CreateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateJobQueue)
  + [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteComputeEnvironment)
  + [DeleteJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteJobQueue)
  + [DeregisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeregisterJobDefinition)
  + [DescribeComputeEnvironments](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeComputeEnvironments)
  + [DescribeJobQueues](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobQueues)
  + [DescribeJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobs)
  + [ListJobsPaginator](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobsPaginator)
  + [RegisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/RegisterJobDefinition)
  + [SubmitJob](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitJob)
  + [UpdateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateComputeEnvironment)
  + [UpdateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateJobQueue)

------
