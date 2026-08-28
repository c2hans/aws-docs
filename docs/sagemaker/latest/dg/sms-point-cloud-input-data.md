---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-input-data.html
---

# 3D Point Cloud Input Data
<a name="sms-point-cloud-input-data"></a>

**Note**
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

To create a 3D point cloud labeling job, you must create an input manifest file. Use this topic to learn the formatting requirements of the input manifest file for each task type. To learn about the raw input data formats Ground Truth accepts for 3D point cloud labeling jobs, see the section [Accepted Raw 3D Data Formats](sms-point-cloud-raw-data-types.md).

Use your [labeling job task type](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-task-types.html) to choose a topics on [Input Manifest Files for 3D Point Cloud Labeling Jobs](sms-point-cloud-input-manifest.md) to learn about the formatting requirements for each line of your input manifest file.

**Topics**
+ [Accepted Raw 3D Data Formats](sms-point-cloud-raw-data-types.md)
+ [Input Manifest Files for 3D Point Cloud Labeling Jobs](sms-point-cloud-input-manifest.md)
+ [Understand Coordinate Systems and Sensor Fusion](sms-point-cloud-sensor-fusion-details.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
