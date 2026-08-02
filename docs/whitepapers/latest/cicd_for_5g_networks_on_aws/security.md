---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/security.html
---

# Security
<a name="security"></a>

Security is a critical element. Following is a list of security steps that the AWS CI/CD process takes into account when deploying an application.
+ **Source** — The ECR repository allocated to the vendor is configured with a “Scan on Push” flag enabled, so that any uploads of Docker images will be immediately subjected to a security scan. Any known common vulnerabilities and exposures (CVE) will be flagged with notifications. Apart from ECR, when vendors put charts into the AWS CodeCommit repository, they are requested to encrypt any passwords used with Secrets Manager rather than with plain text.
+ **Artifacts integrity** — The artifacts used across the pipeline are encrypted whether at rest (using AWS managed keys) or transit (using SSL/TLS).
+ **Users and roles** — The permissions provided to the users or resources are based on the principle of least privilege. There should be a cross-role trust relationship that may need to be configured if you are operating across resources in different services. For example, AWS CodeBuild needs permission to run commands on an Amazon EKS cluster.
+ **Audit** — The auditing capability offered by [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)tracks each and every API call across services and user operations, and enables the evaluation of past events.
+ **Image vulnerability scanning** — CNF images that are uploaded to Amazon ECR are automatically scanned for security vulnerabilities. A report of the scan findings is available in the [AWS Management Console](https://aws.amazon.com/console/), and can also be retrieved via API. The findings can then be sent to CSP operators for corrective action, including replacement of the CNF image.

Security checks occur at various stages of the pipeline to ensure that the newly uploaded image is secure and complies with the desired compliance checks so a notification can be sent to CSPs for approval:
+ The container registry scans for any open CVE vulnerabilities.
+ The configuration is checked for information leaks, known personally identifiable information (PII) patterns, during the test stage, triggering compliance check rules for problems such as unexpected open TCP/UDP ports and DOS vulnerabilities.
+ Backward and forward compatibility is verified for upgrade/rollback safety.

Apart from the application, it is critical to provision pipeline security by ensuring the encrypted transfer of artifacts across stages, whether at rest or in transit.
