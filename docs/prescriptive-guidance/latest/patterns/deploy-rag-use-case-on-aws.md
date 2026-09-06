---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-rag-use-case-on-aws.html
---

# Deploy a RAG use case on AWS by using Terraform and Amazon Bedrock
<a name="deploy-rag-use-case-on-aws"></a>

*Martin Maritsch, Nicolas Jacob Baer, Olivier Brique, Julian Ferdinand Grueber, Alice Morano, and Nicola D Orazio, Amazon Web Services*

## Summary
<a name="deploy-rag-use-case-on-aws-summary"></a>

AWS provides various options to build your [Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/)-enabled generative AI use cases. This pattern provides you with a solution for a RAG-based application based on LangChain and Amazon Aurora PostgreSQL-Compatible as a vector store. You can directly deploy this solution with Terraform into your AWS account and implement the following simple RAG use case:

1. The user manually uploads a file to an Amazon Simple Storage Service (Amazon S3) bucket, such as a Microsoft Excel file or a PDF document. (For more information about supported file types, see the [Unstructured](https://docs.unstructured.io/open-source/core-functionality/partitioning) documentation.)

1. The content of the file is extracted and embedded into a knowledge database that’s based on serverless Aurora PostgreSQL-Compatible, which supports near real-time ingestion of documents into the vector store. This approach enables the RAG model to access and retrieve relevant information for use cases where low latencies matter.

1. When the user engages with the text generation model, it enhances the interaction through retrieval augmentation of relevant content from the previously uploaded files.

The pattern uses [Amazon Titan Text Embeddings v2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) as the embedding model and [Anthropic Claude 3 Sonnet](https://aws.amazon.com/bedrock/claude/) as the text generation model, both available on Amazon Bedrock.

## Prerequisites and limitations
<a name="deploy-rag-use-case-on-aws-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) installed and configured with your AWS account. For installation instructions, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the AWS CLI documentation. To review your AWS credentials and your access to your account, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the AWS CLI documentation.
+ Model access that’s enabled for the required large language models (LLMs) in the Amazon Bedrock console of your AWS account. This pattern requires the following LLMs:
  + `amazon.titan-embed-text-v2:0`
  + `anthropic.claude-3-sonnet-20240229-v1:0`

**Limitations**
+ This sample architecture doesn't include an interface for programmatic question answering with the vector database. If your use case requires an API, consider adding [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide) with an AWS Lambda function that runs retrieval and question-answering tasks.
+ This sample architecture doesn't include monitoring features for the deployed infrastructure. If your use case requires monitoring, consider adding [AWS monitoring services](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html).
+ If you upload a lot of documents in a short time frame to the Amazon S3 bucket, the Lambda function might encounter rate limits. As a solution, you can decouple the Lambda function with an Amazon Simple Queue Service (Amazon SQS) queue where you can control the rate of Lambda invocations.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) version 2 or later
+ [Docker](https://docs.docker.com/get-started/) version 26.0.0 or later
+ [Poetry](https://pypi.org/project/poetry/) version 1.7.1 or later
+ [Python](https://www.python.org/downloads/) version 3.10 or later
+ [Terraform](https://developer.hashicorp.com/terraform/install) version 1.8.4 or later

## Architecture
<a name="deploy-rag-use-case-on-aws-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to create a RAG-based application using Aurora PostgreSQL and LLMs on Amazon Bedrock.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8f184945-7f17-4760-8806-6d0eaeef372a/images/3771b7a0-05bd-4eb3-ad5b-199e22f86184.png)

This diagram illustrates the following:

1. When an object is created in the Amazon S3 bucket `bedrock-rag-template-<account_id>`, an [Amazon S3 notification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) invokes the Lambda function `data-ingestion-processor`.

1. The Lambda function `data-ingestion-processor` is based on a Docker image stored in the Amazon Elastic Container Registry (Amazon ECR) repository `bedrock-rag-template`.

   The function uses the [LangChain S3FileLoader](https://python.langchain.com/v0.1/docs/integrations/document_loaders/aws_s3_file/) to read the file as a [LangChain Document](https://api.python.langchain.com/en/v0.0.339/schema/langchain.schema.document.Document.html). Then, the [LangChain RecursiveCharacterTextSplitter](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/) chunks each document, given a `CHUNK_SIZE` and a `CHUNK_OVERLAP` that depends on the maximum token size of the Amazon Titan Text Embedding V2 embedding model. Next, the Lambda function invokes the embedding model on Amazon Bedrock to embed the chunks into numerical vector representations. Lastly, these vectors are stored in the Aurora PostgreSQL database. To access the database, the Lambda function first retrieves the username and password from AWS Secrets Manager.

1. On the Amazon SageMaker AI [notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) `aws-sample-bedrock-rag-template`, the user can write a question prompt. The code invokes Claude 3 on Amazon Bedrock and adds the knowledge base information to the context of the prompt. As a result, Claude 3 provides responses using the information in the documents.

This pattern’s approach to networking and security is as follows:
+ The Lambda function `data-ingestion-processor` is in a private subnet within the virtual private cloud (VPC). The Lambda function isn’t allowed to send traffic to the public internet because of its security group. As a result, the traffic to Amazon S3 and Amazon Bedrock is routed through the VPC endpoints only. Consequently, the traffic doesn’t traverse the public internet, which reduces latency and adds an additional layer of security at the networking level.
+ All the resources and data are encrypted whenever applicable by using the AWS Key Management Service (AWS KMS) key with the alias `aws-sample/bedrock-rag-template`.

**Automation and scale**

This pattern uses Terraform to deploy the infrastructure from the code repository into an AWS account.

## Tools
<a name="deploy-rag-use-case-on-aws-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments. In this pattern, Aurora PostgreSQL-Compatible uses the pgvector plugin as the vector database.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command line shell.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable. In this pattern, Amazon ECR hosts the Docker image for the `data-ingestion-processor` Lambda function.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use. In this pattern, Lambda ingests data into the vector store.
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/?id=docs_gateway) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. The VPC includes subnets and routing tables to control traffic flow.

**Other tools**
+ [Docker](https://docs.docker.com/manuals/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [Poetry](https://pypi.org/project/poetry/) is a tool for dependency management and packaging in Python.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [terraform-rag-template-using-amazon-bedrock](https://github.com/aws-samples/terraform-rag-template-using-amazon-bedrock) repository.

## Best practices
<a name="deploy-rag-use-case-on-aws-best-practices"></a>
+ Although this code sample can be deployed into any AWS Region, we recommend that you use US East (N. Virginia) – `us-east-1` or US West (N. California) – `us-west-1`. This recommendation is based on the availability of foundation and embedding models in Amazon Bedrock at the time of this pattern’s publication. For an up-to-date list of Amazon Bedrock foundation model support in AWS Regions, see [Model support by AWS Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) in the Amazon Bedrock documentation. For information about deploying this code sample to other Regions, see [Additional information](#deploy-rag-use-case-on-aws-additional).
+ This pattern provides a proof-of-concept (PoC) or pilot demo only. If you want to take the code to production, be sure to use the following best practices:
  + Enable server access logging for Amazon S3.
  + Set up [monitoring and alerting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html) for the Lambda function.
  + If your use case requires an API, consider adding Amazon API Gateway with a Lambda function that runs retrieval and question-answering tasks.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the IAM documentation.

## Epics
<a name="deploy-rag-use-case-on-aws-epics"></a>

### Deploy the solution in an AWS account
<a name="deploy-the-solution-in-an-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the GitHub repository provided with this pattern, use the following command:<pre>git clone https://github.com/aws-samples/terraform-rag-template-using-amazon-bedrock</pre> | AWS DevOps |
| Configure the variables. | To configure the parameters for this pattern, do the following:1. On your computer, in the GitHub repository, use the following command to open the `terraform` folder:<pre>cd terraform</pre><br />2. Open the `commons.tfvars` file, and customize the parameters according to your needs. | AWS DevOps |
| Deploy the solution. | To deploy the solution, do the following:1. In the `terraform` folder, use the following command to run Terraform and pass in the variables that you customized:<pre>terraform init<br />terraform apply -var-file=commons.tfvars  </pre><br />2. Confirm that the resources shown in the [architecture](#deploy-rag-use-case-on-aws-architecture) diagram were deployed successfully.<br />The infrastructure deployment provisions an SageMaker AI instance inside the VPC and with the permissions to access the Aurora PostgreSQL database. | AWS DevOps |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the demo. | After the previous infrastructure deployment has succeeded, use the following steps to run the demo in a Jupyter notebook:1. Sign in to the AWS Management Console of the AWS account where the infrastructure is deployed.<br />2. Open the SageMaker AI notebook instance `aws-sample-bedrock-rag-template`.<br />3. Move the `rag_demo.ipynb` Jupyter notebook onto the SageMaker AI notebook instance by using drag and drop.<br />4. Open the `rag_demo.ipynb` on the SageMaker AI notebook instance, and choose the `conda_python3` kernel.<br />5. To run the demo, run the cells of the notebook.<br />The Jupyter notebook guides you through the following process:+ Installing requirements<br />+ Embedding definition<br />+ Database connection<br />+ Data ingestion<br />+ Retrieval augmented text generation<br />+ Relevant document queries | General AWS |

### Clean up infrastucture
<a name="clean-up-infrastucture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the infrastructure. | To remove all the resources that you created when they are no longer required, use the following command:<pre>terraform destroy -var-file=commons.tfvars</pre> | AWS DevOps |

## Related resources
<a name="deploy-rag-use-case-on-aws-resources"></a>

**AWS resources**
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
+ [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
+ [Access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
+ [The role of vector databases in generative AI applications](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/) (AWS Database Blog)
+ [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)

**Other resources**
+ [pgvector documentation](https://github.com/pgvector/pgvector)

## Additional information
<a name="deploy-rag-use-case-on-aws-additional"></a>

**Implementing a vector database**

This pattern uses Aurora PostgreSQL-Compatible to implement a vector database for RAG. As alternatives to Aurora PostgreSQL, AWS provides other capabilities and services for RAG, such as Amazon Bedrock Knowledge Bases and Amazon OpenSearch Service. You can choose the solution that best fits your specific requirements:
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) provides distributed search and analytics engines that you can use to store and query large volumes of data.
+ [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is designed for building and deploying knowledge bases as an additional abstraction to simplify the RAG ingestion and retrieval process. Amazon Bedrock Knowledge Bases can work with both Aurora PostgreSQL and Amazon OpenSearch Service.

**Deploying to other AWS Regions**

As described in [Architecture](#deploy-rag-use-case-on-aws-architecture), we recommend that you use either the Region US East (N. Virginia) – `us-east-1` or US West (N. California) – `us-west-1` to deploy this code sample. However, there are two possible ways to deploy this code sample to Regions other than `us-east-1` and `us-west-1`. You can configure the deployment Region in the `commons.tfvars` file. For cross-Region foundation model access, consider the following options:
+ **Traversing the public internet** – If the traffic can traverse the public internet, add internet gateways to the VPC. Then, adjust the security group assigned to the Lambda function `data-ingestion-processor` and the SageMaker AI notebook instance to allow outbound traffic to the public internet.
+ **Not traversing the public internet** – To deploy this sample to any Region other than `us-east-1` or `us-west-1`, do the following:

1. In either the `us-east-1` or `us-west-1` Region, create an additional VPC including a VPC endpoint for `bedrock-runtime`.

1. Create a peering connection by using [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or a [transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html) to the application VPC.

1. When configuring the `bedrock-runtime` boto3 client in any Lambda function outside of `us-east-1` or `us-west-1`, pass the private DNS name of the VPC endpoint for `bedrock-runtime` in `us-east-1` or us-west-1 as the `endpoint_url` to the boto3 client.
