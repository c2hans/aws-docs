---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/audit-trail-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Audit trail management
<a name="audit-trail-management"></a>

Operations against AWS services are logged by AWS CloudTrail, and log files are stored in S3. Access details such as Event Name, User Identity, Event Time, Event Source, and Source IP are all captured in CloudTrail.

![A diagram that shows a sample audit trail architecture.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-19.png)

*Sample audit trail architecture*

CloudTrail provides features for accessing and viewing CloudTrail events directly in the console. CloudTrail can also integrate with log analysis tools such as Splunk to further processing and reporting.

SageMaker AI services such as notebook, processing job, or training job report the IAM roles assumed by these individual services against the different API events. To associate these activities with each individual user, consider creating a separate IAM role for each user for the different SageMaker AI services to assume.
