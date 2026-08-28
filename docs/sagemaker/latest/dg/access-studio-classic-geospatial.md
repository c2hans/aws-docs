---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/access-studio-classic-geospatial.html
---

# Accessing SageMaker geospatial
<a name="access-studio-classic-geospatial"></a>

**Note**
Amazon SageMaker geospatial capabilities is no longer open to new customers. Offboard any previously saved jobs to Amazon S3 by using the [ExportEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html) and [ExportVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html) API operations.

**Note**
Currently, SageMaker geospatial capabilities are only supported in the US West (Oregon) Region and in Studio Classic.
If you don't see the SageMaker geospatial UI available in your current Studio Classic instance check to make sure you are currently in the US West (Oregon) Region.

A domain is required to access SageMaker geospatial. If you created a domain prior to November 30, 2023 the default experience is Studio Classic.

If you created a domain after November 30, 2023 or if you have migrated to Studio, then you can use the following procedure to activate Studio Classic from within Studio to use SageMaker geospatial features.

To learn more about creating a domain, see [Onboard to Amazon SageMaker AI domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html).

**To access Studio Classic from Studio**

1. Launch Amazon SageMaker Studio.

1. Under **Applications**, choose **Studio Classic**.

1. Then, choose **Create Studio Classic space**.

1. On the **Create Studio Classic space** page, enter a **Name**.

1. Disable the **Share with my domain** option. SageMaker geospatial is not available in shared domains.

1. Then choose **Create space**.

When successful the **Status** changes to **Updating**. When your Studio Classic application is ready to be used the status changes to **Stopped**.

To start your Studio Classic application, choose **Run**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
