---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/jobs-schedules-control-m.html
---

# Create jobs and schedules in Control-M Planning
<a name="jobs-schedules-control-m"></a>

Now that you have the job type deployed and a connection profile for AWS connectivity, you can start creating and running jobs.

Each AWS Mainframe Modernization service job consists of a set of attributes, in four sections. Each section can have many attributes. The following list shows some of the more commonly used attributes.
+ General:
  + The job name
  + The application and sub-application that the job belongs to
  + The JCL to submit
  + A link to documentation
+ Scheduling:
  + Months and Days this job is eligible to run
  + Calendars such as a business accounting periods, holidays, or other special dates that cannot be defined algorithmically
  + Time windows
  + Cyclic behavior
+ Prerequisites:
  + Upstream dependencies (usually jobs, which must be completed successfully before this job becomes eligible to run)
  + Resources that might be required
  + User action that might be required
+ Actions performed by Control-M upon completion of the job:
  + Determining job success or failure (usually based on the job's completion codes, but you can override that setting to use output text or checks for a specific status)
  + Notifications, such as email, for failure or success
  + Publishing status for downstream dependencies

As with connection profiles, jobs can be created and deployed [in the GUI](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_Job.htm) or [in JSON](https://docs.bmc.com/docs/automation-api/monthly/code-reference-1116950299.html) and deployed by using Control-M Automation API.

The following sections examine some common workflow scenarios:
+ [Initiate jobs based on the status code of previous jobs](status-code.md)
+ [Automate job runs on a scheduled frequency](scheduled.md)
+ [Base job runs on events](event-based.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
