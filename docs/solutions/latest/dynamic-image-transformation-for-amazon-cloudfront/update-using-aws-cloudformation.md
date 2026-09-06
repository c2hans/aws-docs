---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/update-using-aws-cloudformation.html
---

# Update using AWS CloudFormation
<a name="update-using-aws-cloudformation"></a>

**Important**
Dynamic Image Transformation for Amazon CloudFront version 6.0 and newer include significant changes, and you can’t update the solution from versions prior to 6.0 to version 6.0 or later. To use version 6.0 or later, launch a new stack using version 6.x of the CloudFormation template and [uninstall](uninstall-the-solution.md) your previous version of this solution.
S3 Object Lambda has been deprecated. Amazon S3 Object Lambda will no longer be open to new customers starting on November 7, 2025. If you were not an existing user of S3 Object Lambda before November 7, 2025, select ‘No'. For more information, see [Amazon S3 Object Lambda changes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html).
Modifying the architecture of an existing deployment by changing the value of the `Enable S3 Object Lambda` template parameter will cause a deletion and recreation of the CloudFront distribution associated with the deployment. This recreation will result in a new API endpoint URL and an empty cache. For information on a workaround to use an alternate architecture type while maintaining the current endpoint URL and cache, refer to the instructions on [maintaining the existing endpoint and cache when modifying architecture type](maintain-endpoint-cache-architecture.md).

**Important**
 **Version 8.0.0 Breaking Changes:**
Dynamic Image Transformation for Amazon CloudFront version 8.0.0 introduces significant architectural changes and is **not compatible** with previous versions. This release includes:
 **New ECS Architecture**: The new high-performance container-based architecture cannot be deployed as an update to existing stacks
 **Breaking Changes**: Version 8.0.0 includes fundamental changes to the solution architecture, configuration, and feature set
 **Clean Deployment Required**: To use the ECS architecture or any v8.0.0 features, you must deploy a **new stack** using the v8.0.0 CloudFormation template
 **Migration Path:** - **Lambda Architecture**: Existing deployments can be updated to v8.0.0 Lambda template for maintenance and security updates - **ECS Architecture**: Requires a completely new deployment - cannot be updated from any previous version - **Feature Access**: Advanced features (transformation policies, non-S3 origins, Admin UI) are only available in the new ECS architecture
 **Recommendation**: Deploy the new ECS architecture as a separate stack, test thoroughly, then migrate traffic and [uninstall](uninstall-the-solution.md) the previous version.
