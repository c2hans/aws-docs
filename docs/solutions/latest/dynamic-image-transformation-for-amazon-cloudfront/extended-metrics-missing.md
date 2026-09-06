---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/extended-metrics-missing.html
---

# Extended metrics are missing in the Playground
<a name="extended-metrics-missing"></a>

 **Symptoms:**
+ The Playground shows the transformed image but no extended metrics overlay (dimensions, compression ratio, processing-time breakdown, and so on).
+ Metrics appeared earlier in the session but stopped.

 **Cause:**

Extended metrics are returned only when the request carries a valid Amazon Cognito access token, which the Playground obtains from your signed-in Admin UI session. If the token is expired, missing, or invalid, the solution returns the standard image response without metrics; the image itself is unaffected. An expired session is the most common cause.

 **Solution:**

Refresh your Admin UI session to obtain a current Cognito token (sign out and sign back in if needed), then reload the Playground. The image transformation works regardless; only the diagnostic metrics depend on the token.
