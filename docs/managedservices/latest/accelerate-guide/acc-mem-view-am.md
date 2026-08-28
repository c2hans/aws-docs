---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-view-am.html
---

# Viewing your Accelerate Alarm Manager configuration
<a name="acc-mem-view-am"></a>

Both the **AMSManagedAlarms** and **CustomerManagedAlarms** can be reviewed in AppConfig with [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html).

The following is an example of the `GetConfiguration` call:

```
aws appconfig get-configuration --application AMSAlarmManager --environment AMSInfrastructure --configuration AMSManagedAlarms --client-id
      {{any-string}} outfile.json
```
+ **Application**: this is AppConfig's logical unit to provide capabilities; for the Alarm Manager, this is `AMSAlarmManager`
+ **Environment**: this is the AMSInfrastructure environment
+ **Configuration**: to view AMS Accelerate baseline alarms, the value is `AMSManagedAlarms`; to view customer alarm definitions, the configuration is `CustomerManagedAlarms`
+ **Client ID**: this is a unique application instance identifier, which can be any string
+ The alarm definitions can be viewed in the specified output file, which in this case is `outfile.json`

 You can see which version of configuration is deployed to your account by viewing the past deployments in the AMSInfrastructure environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
