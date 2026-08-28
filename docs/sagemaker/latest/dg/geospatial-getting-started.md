---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-getting-started.html
---

# Getting started with Amazon SageMaker geospatial
<a name="geospatial-getting-started"></a>

**Note**
Amazon SageMaker geospatial capabilities is no longer open to new customers. Offboard any previously saved jobs to Amazon S3 by using the [ExportEarthObservationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportEarthObservationJob.html) and [ExportVectorEnrichmentJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ExportVectorEnrichmentJob.html) API operations.

 SageMaker geospatial provides a purpose built **Image** and **Instance type** for Amazon SageMaker Studio Classic notebooks. You can use either CPU or GPU enabled notebooks with the SageMaker geospatial **Image**. You can also visualize your geospatial data using a purpose built visualizer. Furthermore, SageMaker geospatial also provides APIs that allow you to query raster data collections.You can also use pre-trained models to analyze geospatial data, reverse geocoding, and map matching.

**Note**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. If prior to November 30, 2023 you created a Amazon SageMaker AI domain, Studio Classic remains the default experience. domains created after November 30, 2023 default to the new Studio experience.
Amazon SageMaker geospatial features and resources are *only* available in Studio Classic. To learn more about setting up a domain and getting started with Studio, see [Getting started with Amazon SageMaker geospatial](#geospatial-getting-started).

To access and get started using Amazon SageMaker geospatial, do the following:

**Topics**
+ [Accessing SageMaker geospatial](access-studio-classic-geospatial.md)
+ [Create an Amazon SageMaker Studio Classic notebook using the geospatial image](geospatial-launch-notebook.md)
+ [Access the Sentinel-2 raster data collection and create an earth observation job to perform land segmentation](geospatial-demo.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
