---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-object-tracking-adjustment-verification.html
---

# Information for creating a 3D point cloud object tracking adjustment or verification labeling job
<a name="sms-point-cloud-object-tracking-adjustment-verification"></a>

**Note**
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

You can create an adjustment and verification labeling job using the Ground Truth console or `CreateLabelingJob` API. To learn more about adjustment and verification labeling jobs, and to learn how create one, see [Label verification and adjustment](sms-verification-data.md).

When you create an adjustment labeling job, your input data to the labeling job can include labels, and yaw, pitch, and roll measurements from a previous labeling job or external source. In the adjustment job, pitch, and roll will be visualized in the worker UI, but cannot be modified. Yaw is adjustable.

Ground Truth uses Tait-Bryan angles with the following intrinsic rotations to visualize yaw, pitch and roll in the worker UI. First, rotation is applied to the vehicle according to the z-axis (yaw). Next, the rotated vehicle is rotated according to the intrinsic y'-axis (pitch). Finally, the vehicle is rotated according to the intrinsic x''-axis (roll).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
