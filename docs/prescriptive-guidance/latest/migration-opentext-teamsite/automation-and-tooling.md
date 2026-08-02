---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/automation-and-tooling.html
---

# Automation and tooling
<a name="automation-and-tooling"></a>

We recommend automating your migration by building automation scripts, running them in nonproduction environments, testing and adjusting, and then running them until the environment set-up, content migration, and code deployments happen smoothly and create a fully functional environment.

Automation scripts and tools are custom-made and based on existing assets from previous migrations. Some of the main assets that are developed for a typical migration include the following:
+ AWS CloudFormation scripts to fully provision the AWS services
+ AWS Database Migration Service (AWS DMS) configuration, including database migration scripts if required
+ Configuration of CI/CD tools according to your requirements (for example, [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html), Jenkins, or Bamboo).
+ Custom scripts (for example, .sh) for additional tasks

When you run and refine the whole migration process, you should also create a detailed step-by-step guide with scripts, manual actions, tests, and fallback options.
