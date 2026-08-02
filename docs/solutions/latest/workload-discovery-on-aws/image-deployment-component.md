---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/image-deployment-component.html
---

# Image deployment component
<a name="image-deployment-component"></a>

![workload discovery image deployment component](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-image-deployment-component.png)

**Workload Discovery on AWS image deployment component**
The image deployment component builds the container image that the discovery component uses. The `DiscoveryBucket` and Amazon S3 bucket host the code which can be downloaded at time of deployment by an AWS CodeBuild job that builds the container image and uploads it to Amazon ECR.
