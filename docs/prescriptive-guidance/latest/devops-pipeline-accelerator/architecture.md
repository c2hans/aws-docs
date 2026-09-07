---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/architecture.html
---

# Architecture of the DevOps Pipeline Accelerator
<a name="architecture"></a>

In the DevOps Pipeline Accelerator, *accelerators* are a collection of jobs that are managed in stages. A *stage* contains the building blocks that form a *job*. There are multiple *wrappers* that form an entry point for a specific IaC pipeline. The application consumes the *entry point*, which is the start of the pipeline. The entry point consists of *aggregators* and various stages. The following image shows how stages interact with wrappers, aggregators, and the entry point.

![How stages interact with wrappers, aggregators, and the entry point](https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/images/guide-img/e56ba347-e180-48ee-bbf9-0b76e10e70f2/images/8b5ca6e3-3dbf-4971-be26-9250b4d439e7.png)

This section describes the building blocks of the DPA solution architecture, as shown in the following image.

![Building blocks of the DPA solution architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/images/guide-img/e56ba347-e180-48ee-bbf9-0b76e10e70f2/images/106e947a-1c73-483c-8ac0-7dfb0575183c.png)

The diagram shows the following workflow and features:

1. The DPA primary component is a centralized pipeline that contains different stages and jobs that are based on the configuration of the application.

1. DPA supports four commonly used CI/CD services and tools. This is where the centralized pipeline is constructed.

1. The pipeline jobs use reusable scripts, which are independent of the CI/CD services and tools.

1. Each pipeline job runs in a relevant Docker image, for portability. An Amazon Elastic Container Registry (Amazon ECR) repository hosts these Docker images.

1. DPA contains built-in security controls, which you can customize.

1. The pipeline deploys applications into the AWS Cloud.

1. The entry point is a single entity that represents the entire centralized pipeline. The configurations vary based on the type of technology stack.

1. The application imports or includes the entry points. Each technology stack represents a separate entry point.

1. The application configures parameters based on the type of entry point. These config parameters define the behavior and operation of pipeline jobs.
