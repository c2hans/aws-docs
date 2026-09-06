---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-architecture-planning.html
---

# ECS Architecture
<a name="ecs-architecture-planning"></a>

This high-performance container-based architecture supports demanding workloads and provides access to the solution’s full feature set.

 **Key characteristics:**
+  **Image size limit**: Up to 100 MB per image
+  **Pricing model**: Fixed infrastructure costs with usage-based scaling
+  **Scaling**: Configurable auto-scaling with t-shirt sizing options
+  **Feature set**: Complete feature set including transformation policies, smart cropping, content moderation, multi-tier device detection, and non-S3 origins
+  **Management**: Administrative web interface included

 **Best suited for:**
+ Large images (6 MB to 100 MB)
+ Enterprise deployments requiring advanced features
+ Non-S3 origin requirements
+ Consistent high-volume traffic
+ Complex transformation workflows
+ Migration from other CDN providers

 **Advanced capabilities:**
+ Transformation policies with conditional logic
+ Multi-origin support (S3 and external)
+ Administrative interface for configuration management
+ In-memory caching for optimal performance
