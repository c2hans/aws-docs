---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_transit_auto_unintended_access.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC09-BP03 Automate detection of unintended data access
<a name="sec_protect_data_transit_auto_unintended_access"></a>

 Use tools such as Amazon GuardDuty to automatically detect suspicious activity or attempts to move data outside of defined boundaries. For example, GuardDuty can detect Amazon Simple Storage Service (Amazon S3) read activity that is unusual with the [Exfiltration:S3/AnomalousBehavior finding](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-objectreadunusual). In addition to GuardDuty, [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), which capture network traffic information, can be used with Amazon EventBridge to trigger detection of abnormal connections–both successful and denied. [Amazon S3 Access Analyzer](http://aws.amazon.com/blogs/storage/protect-amazon-s3-buckets-using-access-analyzer-for-s3) can help assess what data is accessible to who in your Amazon S3 buckets.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate detection of unintended data access: Use a tool or detection mechanism to automatically detect attempts to move data outside of defined boundaries, for example, to detect a database system that is copying data to an unrecognized host.
  + [ VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  Consider Amazon Macie: Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS.
  + [ Amazon Macie ](https://aws.amazon.com/macie/)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+ [ Amazon Macie ](https://aws.amazon.com/macie/)
