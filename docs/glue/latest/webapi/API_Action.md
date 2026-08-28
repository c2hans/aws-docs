---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Action.html
---

# Action
<a name="API_Action"></a>

Defines an action to be initiated by a trigger.

## Contents
<a name="API_Action_Contents"></a>

 ** Arguments **   <a name="Glue-Type-Action-Arguments"></a>
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.
Type: String to string map
Required: No

 ** CrawlerName **   <a name="Glue-Type-Action-CrawlerName"></a>
The name of the crawler to be used with this action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobName **   <a name="Glue-Type-Action-JobName"></a>
The name of a job to be run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** NotificationProperty **   <a name="Glue-Type-Action-NotificationProperty"></a>
Specifies configuration properties of a job run notification.
Type: [NotificationProperty](API_NotificationProperty.md) object
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-Action-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Timeout **   <a name="Glue-Type-Action-Timeout"></a>
The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This overrides the timeout value set in the parent job.
Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.
When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.
Any existing AWS Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.
For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
