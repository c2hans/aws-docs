---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/best-practices.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Best practices
<a name="best-practices"></a>

## Retention period configuration
<a name="retention-period"></a>
+ **Compliance Requirements**: Set retention period based on regulatory requirements (e.g., 90 days, 7 years)
+ **Storage Costs**: Longer retention periods increase S3 storage costs
+ **Lifecycle Policies**: Configure S3 lifecycle policies to transition older data to cheaper storage classes (S3 Glacier)

## Storage management
<a name="storage-management"></a>
+ **Monitor Bucket Size**: Set up CloudWatch alarms for bucket size thresholds
+ **Enable Versioning**: Protect against accidental deletions
+ **Cross-Region Replication**: Replicate to another region for disaster recovery
+ **Encryption**: Ensure S3 bucket encryption is enabled (automatic with KMS)

## Access control
<a name="access-control"></a>
+ **Least Privilege**: Grant S3 bucket access only to compliance officers and authorized personnel
+ **MFA Delete**: Enable MFA delete on S3 bucket to prevent unauthorized data deletion
+ **Bucket Policies**: Use bucket policies to restrict access by IP address or VPC endpoint
+ **Audit Access**: Regularly review CloudTrail logs for S3 access patterns

## Audit logging
<a name="audit-logging"></a>
+ **Enable CloudTrail**: Ensure CloudTrail is logging all API calls
+ **S3 Access Logs**: Enable S3 server access logging for bucket access audit
+ **KMS Key Usage**: Monitor CloudTrail for KMS key usage patterns
+ **Regular Reviews**: Conduct regular reviews of access logs and retention data

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
