---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/seeing-cached-images.html
---

# Seeing cached images even after making configuration changes on Admin UI
<a name="seeing-cached-images"></a>

 **Problem:** Images continue to show previous transformations even after updating origins, policies, or mappings through the Admin UI.

 **Cause:** CloudFront caches processed images based on the request URL and headers. Configuration changes don’t automatically invalidate existing cached images.

 **Solution:** Create a CloudFront invalidation to clear cached images:

1. Navigate to the CloudFront console

1. Select the distribution created by the solution

1. Go to the **Invalidations** tab

1. Choose **Create invalidation**

1. Enter the path pattern for images to invalidate:
   + For all images: `/*`
   + For specific paths: `/images/*` or `/mobile/*`

1. Choose **Create invalidation**

The invalidation will clear cached images, forcing CloudFront to request fresh images with the new configuration applied.
