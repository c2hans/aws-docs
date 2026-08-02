---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/policy-not-being-applied.html
---

# Policy not being applied
<a name="policy-not-being-applied"></a>

 **Symptoms:** - Images not transformed according to policy - Default transformations applied instead of policy - Policy appears in Admin UI but doesn’t affect images

 **Solutions:**

 **Verify policy mapping:**
+ Check if policy is correctly associated with origin mapping
+ Ensure policy ID is specified correctly in requests
+ Verify default policy is set if no policy ID provided

 **Refresh configuration cache:**
+ Use Admin UI "Refresh Cache" button after policy changes
+ Wait 5 minutes for rolling update to complete
+ Check ECS task logs for cache refresh confirmation
