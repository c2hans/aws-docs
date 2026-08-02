---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

Represents one or more dates and times when a job is to run.

## Contents
<a name="API_Schedule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-Schedule-Name"></a>
The name of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** AccountId **   <a name="databrew-Type-Schedule-AccountId"></a>
The ID of the AWS account that owns the schedule.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="databrew-Type-Schedule-CreateDate"></a>
The date and time that the schedule was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-Schedule-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the schedule.
Type: String
Required: No

 ** CronExpression **   <a name="databrew-Type-Schedule-CronExpression"></a>
The dates and times when the job is to run. For more information, see [Working with cron expressions for recipe jobs](https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron) in the * AWS Glue DataBrew Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** JobNames **   <a name="databrew-Type-Schedule-JobNames"></a>
A list of jobs to be run, according to the schedule.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-Schedule-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the schedule.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-Schedule-LastModifiedDate"></a>
The date and time when the schedule was last modified.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="databrew-Type-Schedule-ResourceArn"></a>
The Amazon Resource Name (ARN) of the schedule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Tags **   <a name="databrew-Type-Schedule-Tags"></a>
Metadata tags that have been applied to the schedule.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Schedule)
