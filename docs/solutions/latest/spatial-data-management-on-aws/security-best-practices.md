---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/security-best-practices.html
---

# Security Best Practices
<a name="security-best-practices"></a>

The solution provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

## Detective Controls
<a name="detective-controls"></a>

 **Built-in Monitoring Dashboard**

The solution deploys a CloudWatch dashboard (`SpatialDataManagementDashboard`) that provides visibility into operational and security metrics. Regularly review the following security-relevant metrics:

 **Authentication Metrics**:
+ Cognito Authentication Failures - Spikes may indicate brute force attacks or credential issues
+ Cognito Authentication Success - Establish baseline for normal authentication patterns

 **API Error Rates**:
+ Response By Status Code (4xx/5xx errors) - High 4xx rates may indicate unauthorized access attempts
+ Operation-specific 5xx Errors (Create, Read, Update, Delete) - May indicate service issues or attacks
+ Operation Success Rate (%) - Should remain consistently high (>99%)

 **Access Patterns**:
+ Total Requests - Unusual spikes may indicate automated attacks or data exfiltration
+ Client Files Downloaded/Uploaded - Monitor for abnormal data transfer patterns
+ Client Bytes Downloaded/Uploaded - Large unexpected transfers may indicate data exfiltration

 **Performance Anomalies**:
+ Operation Latency (ms) for each operation type - Sudden increases may indicate resource exhaustion attacks
+ Search Operation Latency - Unusually complex queries may indicate reconnaissance

 **Recommended Actions**

1. Review the dashboard daily during initial deployment, then weekly for established deployments

1. Establish baseline metrics for normal operation to identify anomalies

1. Configure CloudWatch alarms for critical security metrics (see recommendations below)

1. Export dashboard data to S3 for long-term trend analysis and compliance reporting

 **Monitoring and Logging**

1. Configure CloudWatch Logs retention to meet compliance requirements (default: 90 days)

1. Set up CloudWatch alarms for security-relevant metrics:

1. Failed authentication attempts

1. Unauthorized API calls (403 errors)

1. KMS key usage anomalies

1. S3 bucket policy changes

1. IAM policy changes

## File Upload Security
<a name="file-upload-security"></a>

The solution allows users to upload files of any type to project assets. Uploaded files are stored in Amazon S3 and are downloadable by other users with read access to the project. The solution does not restrict file types or scan uploaded files for malware by default.

To reduce the risk of malicious files being uploaded and subsequently downloaded by other users, consider the following:

 **Malware Scanning**

Enable [Amazon GuardDuty Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) on the solution’s asset bucket. GuardDuty continuously scans newly uploaded objects for malware and generates findings for any threats detected. You can configure an EventBridge rule to automatically quarantine or delete objects that fail the malware scan.

 **File Type Restrictions**

Use [asset templates](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/core-concepts.html#asset-template) to define `allowedFileTypes` for projects. This restricts uploads to permitted file extensions and reduces the attack surface for malicious file uploads.

 **Cross-Platform Filename Compatibility**

The solution displays a warning when files with Windows-incompatible characters (`< > : " | ? *`) are uploaded from macOS or Linux systems. These files can be uploaded successfully but may fail to download on Windows systems. When uploading content intended for cross-platform use, ensure filenames are compatible with all target operating systems.

## Content Derivation
<a name="content-derivation"></a>

### AWS Deadline Cloud
<a name="aws-deadline-cloud"></a>

When using AWS Deadline Cloud for content derivation jobs, the solution uses service-managed fleets. For security details on Deadline Cloud, see [AWS Deadline Cloud Documentation](https://docs.aws.amazon.com/deadline-cloud/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
