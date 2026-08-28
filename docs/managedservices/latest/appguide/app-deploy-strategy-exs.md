---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/app-deploy-strategy-exs.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Application maintenance
<a name="app-deploy-strategy-exs"></a>

Once infrastructure is deployed, updating it in a consistent way across all your AMS environments, from QA to staging to production, is the challenge.

This section provides an overview of the AMS workload ingestion process and some examples of different methods you can use to keep your cloud infrastructure layer up to date.

## Application maintenance strategies
<a name="aog-ams-app-maintain"></a>

How you deploy your applications impacts how you maintain them. This section provides some strategies for application maintenance.

Environment updates can involve any of these changes:
+ Security updates
+ New versions of your applications
+ Application configuration changes
+ Updates to dependencies

**Note**
For any application deployment, no matter the method, always file a service request beforehand to let AMS know that you are going to deploy an application.

**Immutable vs Mutable Application Installation Examples**
<a name="strategy-exs.table"></a>

- **Mutable**
  - **App Install Method:**
    - With CodeDeploy
    - Manually
    - With a Chef or Puppet, Pull-Based
    - With Ansible or Salt, Push-Based
  - **AMI:** AMS-provided

- **Immutable**
  - **App Install Method:** With a Golden AMI
  - **AMI:** Custom (based on AMS-provided)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
