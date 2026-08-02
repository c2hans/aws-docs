---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-fargate-container-health-check.html
---

# AWS Fargate container health check
<a name="aws-fargate-container-health-check"></a>

Health check parameters that are specified in a container definition override any Docker health checks that exist in the container image. The following endpoint is used to check the health of the Prebid Server running containers: `HEALTH_ENDPOINT = "/status"`. The default interval and timeout parameters `HEALTH_CHECK_INTERVAL_SECS = 60` and `HEALTH_CHECK_TIMEOUT_SECS = 5` are used to set the time period in seconds between each health check run, and the time period in seconds to wait for a health check to succeed before it is considered a failure, respectively.
