---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DateRange.html
---

# DateRange
<a name="API_DateRange"></a>

This is a resource filter containing FromDate: DateTime and ToDate: DateTime. Both values are required. Future DateTime values are not permitted.

The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds ((milliseconds are optional). For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

## Contents
<a name="API_DateRange_Contents"></a>

 ** FromDate **   <a name="Backup-Type-DateRange-FromDate"></a>
This value is the beginning date, inclusive.
The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).
Type: Timestamp
Required: Yes

 ** ToDate **   <a name="Backup-Type-DateRange-ToDate"></a>
This value is the end date, inclusive.
The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).
Type: Timestamp
Required: Yes

## See Also
<a name="API_DateRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DateRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DateRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DateRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
