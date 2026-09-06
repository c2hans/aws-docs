---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-extended-metrics-security.html
---

# Extended metrics authorization (ECS architecture)
<a name="ecs-extended-metrics-security"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

The Playground can display extended transformation metrics (such as pre- and post-optimization dimensions, compression ratio, and processing-time breakdown) alongside a transformed image. These metrics are gated behind authentication: the Playground sends the signed-in user’s Amazon Cognito access token with the request, and the ECS container verifies that token against the deployment’s Cognito user pool before including the metrics in the response.

This verification protects only the diagnostic metrics, not image delivery. If the token is missing, expired, or invalid, the solution returns the standard transformed image without metrics; image requests are never blocked. Standard image traffic, which carries no token, never includes diagnostic data.
