---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/metrics.html
---

# Metrics
<a name="metrics"></a>

This solution currently writes Prebid Server metrics log data to the mounted EFS, which is shared across containers, and ingests and archives the data using a variety of data management tools continuously or as a batch process. The patch file registers a new logger stream to periodically write metrics data from Prebid Server to files using the standard Java logging mechanism.
