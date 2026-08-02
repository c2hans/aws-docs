---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](launch-the-stack.md) in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the in the *AWS CloudFormation User’s Guide*.

## MediaConvert quotas
<a name="mediaconvert-quotas"></a>

All MediaConvert jobs run in a queue. If you don’t specify a queue when you create your job, MediaConvert sends it to the default on-demand queue. For information about how many queues you can create and how many jobs those queues can run, refer to [Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html) in the *MediaConvert User Guide* and see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/mediaconvert.html#limits_mediaconvert) in the *AWS General Reference Guide*.

## MediaPackage quotas
<a name="mediapackage-quotas"></a>

This solution includes the option to use MediaPackage as part of the workflow. Customers who ingest large quantities of files may exceed MediaPackage limits for video-on-demand content. For more information and instructions on how to request a limit increase, refer to [VOD Content Limits](https://docs.aws.amazon.com/mediapackage/latest/ug/limits-vod.html) in the *AWS Elemental MediaPackage User Guide*.
