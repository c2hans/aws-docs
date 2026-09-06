---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/amazon-rekognition-result-cache.html
---

# Amazon Rekognition result cache
<a name="amazon-rekognition-result-cache"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

Smart cropping and content moderation use Amazon Rekognition to analyze your images. The solution caches the Amazon Rekognition results for each source image in a dedicated DynamoDB table so that repeated transformations of the same image reuse the stored analysis instead of calling Amazon Rekognition again. This reduces Amazon Rekognition costs and request latency. AWS CloudFormation generates the table’s physical name at deployment time; it contains `RekognitionCacheTable` (for example, `<stack-name>-ImageProcessingNestedStack…​-RekognitionCacheTable<id>`). To find the exact name, open the deployed stack’s **Resources** tab and look for the `RekognitionCacheTable` resource.

The cache applies automatically; there is nothing to configure to use it. Cached results are keyed by the contents of the source image, so replacing an image (even at the same path) is analyzed fresh on its next request. Cached entries expire after 24 hours by default. If the cache is ever unavailable, the solution calls Amazon Rekognition directly, so image requests are never blocked.
