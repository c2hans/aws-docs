---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/create-jobs-schedules-control-m-planning.html
---

# Create jobs and schedules in Control-M Planning
<a name="create-jobs-schedules-control-m-planning"></a>

Now that you have the plug-in deployed and a connection profile for Micro Focus connectivity, you can start creating and running jobs.

Each Control-M for Micro Focus job consists of a set of attributes, in four sections. Each section can have many attributes. The following list shows some of the more commonly used attributes.
+ General:
  + The job name
  + The application and sub-application that the job belongs to
  + The JCL to submit
  + A link to site-provided operational documentation
+ Scheduling:
  + Months and Days this job is eligible to run
  + Calendars such as a business accounting periods, holidays, or other special dates that cannot be defined algorithmically
  + Time windows
  + Cyclic behavior such as running every hour
+ Prerequisites
  + Upstream dependencies (usually jobs, which must be completed successfully before this job becomes eligible to run)
  + Resources that might be required
  + User action that might be required
+ Actions performed by Control-M upon completion of the job:
  + Determining job success or failure (usually based on the job's completion codes, but you can override that setting to use output text or checks for a specific status)
  + Notifications, such as email, for failure or success
  + Publishing status for downstream dependencies

As with connection profiles, jobs can be created and deployed by [using Control-M Web](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_Job.htm) or [written in JSON](https://docs.bmc.com/docs/automation-api/monthly/code-reference-1116950299.html) and deployed by using Control-M Automation API.

The following sections examine some common workflow scenarios:
+ [Initiate jobs based on the status of previous jobs](initiate-jobs.md)
+ [Automate job runs on a scheduled frequency](automate-jobs.md)
