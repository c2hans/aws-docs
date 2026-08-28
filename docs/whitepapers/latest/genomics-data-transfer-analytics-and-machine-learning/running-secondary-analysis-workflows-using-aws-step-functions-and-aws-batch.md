---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/running-secondary-analysis-workflows-using-aws-step-functions-and-aws-batch.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Running secondary analysis workflows using AWS Step Functions and AWS Batch
<a name="running-secondary-analysis-workflows-using-aws-step-functions-and-aws-batch"></a>

 Running secondary analysis workflows to perform sequence alignment, variant calling, quality control (QC), annotation, and custom processing can be done in AWS using native AWS services. We’ll provide recommendations and a reference architecture for running secondary analysis workflows in AWS using AWS Step Functions and AWS Batch.

## Recommendations
<a name="recommendations-1"></a>

 When running secondary analysis workloads in the AWS Cloud, consider the following recommendations to optimally run secondary analysis.

 **Use AWS Batch to run tasks in your genomics workflows**—Most secondary analysis tasks are perfectly parallel, meaning that those tasks can be run independently and often in parallel. Provisioning resources on-demand for tasks in AWS Batch is more cost-effective and optimizes performance better than using a traditional High-Performance Computing (HPC) environment.

 **Use AWS Step Functions to orchestrate tasks in your secondary analysis workflows**— Keep task execution separate from task orchestration so that purpose-built solutions are used for each activity and tools and workflows can be deployed independently. This approach limits the impact of change which minimizes risk. AWS Step Functions is serverless which minimizes operational burden.

 **Package tools in Docker containers and use standard Amazon Machine Images (AMIs)**—Package tools in Docker containers so they are portable and you can take advantage of serverless container solutions to orchestrate your container execution. Using standard AMIs removes the operational burden of maintaining machine images.

 **Package tools independent of workflows in their own Docker container**—Package tools independently to right-size the compute for each tool, which can optimize performance and minimize cost when running each tool container. Multiple workflows can also use the same tool containers.

 **Treat configuration as code for secondary analysis tools and workflows**—Fully automate the build and deployment of secondary analysis tools and workflows. Automation empowers your teams to move quickly while maintaining control, providing a repeatable development process for advancing your genomics solution into production.

 **Use Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances to optimize for cost**—Amazon EC2 Spot Instances offers significant savings when you run jobs. You can fall back to on-demand instances if spot instances are not available.

## Reference architecture
<a name="reference-architecture-1"></a>

![Secondary analysis reference architecture using AWS Step Functions and AWS Batch](http://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/images/image3.png)

 Figure 2 shows the reference architecture for the secondary analysis workflow using AWS Step Functions and AWS Batch.

1.  A CloudWatch event triggers an AWS Lambda function to start an AWS Step Functions secondary analysis state machine.

1.  Step Functions submits jobs to AWS Batch to run in a Spot Instance compute environment. The Docker images for the tools are stored in private Amazon Elastic Container Registry (Amazon ECR) repositories in the customer’s account. The job output files are written to an Amazon S3 bucket, including the Variant Call File (VCF) and Binary Alignment Map (BAM) file. AWS Step Functions manages the execution of AWS Batch jobs for alignment, variant calling, QC, annotation, and custom processing steps.

 Running secondary analysis using AWS Step Functions and AWS Batch starts by triggering a Step Functions state machine to run. For example, you can use either the AWS Command Line Interface (AWS CLI) or an AWS API client. To fully automate the process, you can set up an Amazon CloudWatch rule to run the state machine when genomic sample FASTQ files are put in an Amazon S3 bucket. The rule could start the state machine execution directly or the event could be put in an Amazon Simple Queue Service (Amazon SQS) queue that is polled by an AWS Lambda function that starts the state machine execution. Using a Lambda function to start a state machine makes it easy to add quality checks or routing logic, that is, to check for missing files or route to a particular secondary analysis workflow.

 You can pass parameters when running a Step Functions state machine and use them for each job in your secondary analysis workflow. Use a convention to read and write objects to Amazon S3 so that you can compute, up front, the input and output paths for each tool when you execute the state machine.

 Once Step Functions submits a job to an AWS Batch queue, the job is scheduled by AWS Batch to run on an instance in a compute environment associated with the queue. Compute environments are used in the order they are listed in the compute environments list in the queue. The job will be scheduled to run on an instance that matches the resource requirements specified in the job definition, such as compute and memory required. Using EC2 Spot Instances and allowing AWS Batch to choose the optimal instance type can help optimize compute costs by increasing the pool of instances types to choose from in EC2 Spot Instances.

 To learn more about optimizing secondary analysis compute cost, see [Optimizing secondary analysis compute cost](appendix-g-optimizing-secondary-analysis-compute-cost.md).

 From time to time a secondary analysis job will fail. AWS Step Functions has support for job retries and try catch logic to handle job failures with custom code. To learn more about handling secondary analysis task errors or failures, see [Handling secondary analysis task errors and workflow failures](appendix-h-handling-secondary-analysis-task-errors-and-workflow-failures.md).

 Create an operational dashboard to monitor the status of your secondary analysis workflow. AWS Step Functions and AWS Batch are both integrated with Amazon CloudWatch so creating a secondary analysis dashboard in Amazon CloudWatch is easy to do. To learn more about creating a secondary analysis operational dashboard in Amazon CloudWatch, see [Monitoring secondary analysis workflow status, cost, and performance](appendix-i-monitoring-secondary-analysis-workflow-status-cost-and-performance.md).

**Note**
 To access an AWS Solutions Implementation providing an AWS CloudFormation template to automate the deployment of the solution in the AWS Cloud, see the [Genomics Secondary Analysis Using AWS Step Functions and AWS Batch Implementation Guide](https://docs.aws.amazon.com/solutions/latest/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch/welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
