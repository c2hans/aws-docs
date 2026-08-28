---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/migration-plan.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration plan
<a name="migration-plan"></a>

 This section steps through an example migration, broken into four phases.

## Planning
<a name="planning"></a>

 Planning in migration involves identifying goals, scope and business requirements. Often overlooked, and related to these items, are having quantifiable goals as measures of success, specifically with regard to performance (for example, performance shall remain the same or be improved by *x* margin) as well as a full understanding of the components that comprise the to-be-migrated environments.

 To solve for the first, you can use the existing monitoring used in your enterprise or use AWS monitoring capabilities. Rather than focusing on machine-level statistics (such as CPU, memory, storage consumption, storage IO, and network consumption), which are important with regard to machine configuration, focus on the end-user experience, for example, response times for key activities, such as adding to cart, checking out, and payment.

 To solve for the second, you can use existing financial records, inventories, or monitoring to identify the components that comprise each environment, including those that might not be evident, for example, virtualized solutions, or those delivered as a third-party solution, such as DNS or CDN).

## Staging
<a name="staging"></a>

 After you have identified measures of success and completed the discovery, you should have a sense of the baseline services required to support your application. Compared to your existing AWS footprint (if there is one) you may opt to create an entirely new AWS account or Amazon VPC, use an existing AWS account or Amazon VPC, or go through the collective supporting characteristics for first time AWS adoption found in the [AWS Landing Zone Solution](https://aws.amazon.com/solutions/aws-landing-zone/).

 Once this work is complete, you can begin prototyping your environment on AWS – familiarizing yourself with some of the services mentioned above and identifying potential replacements to share service, appliance or server based services. This is the re-platforming approach.

 Once this is setup, you can begin to stage an environment for your first test migration. This environment would essentially replicate your current production environment from a software, configuration, code, and management perspective and aim to test both basic functionality of the platform as well as your data backup/restore and/or data replication processes that will be leveraged during the actual migration.

 This would be your second decision point for rehosting versus re-platforming: there are multiple approaches you can take to migrating your servers to AWS – from as basic as exporting a virtual machine and importing it into AWS, to using [CloudEndure Migration](https://aws.amazon.com/cloudendure-migration/) for real time replication of the machine. While opinions vary on the subject, the reader is strongly encouraged to take an approach biased to re-platforming as it presents an opportunity to significantly improve operations of the platform with minimal (but not nonexistent) up front work.

 This first attempt at the migration provides you with a harness to execute, record, measure and modify the previously defined plans and tests, understand baseline performance as well as capture step-timings and improve the overall cutover plan. This step can be repeated as often or as frequently as needed until a comfort level is obtained to move into the next step.

## Cutover
<a name="cutover"></a>

 The final step of the migration process is the live migration from the current on-premises environment to the AWS based environment. Essentially the process is similar as the previous step, though you will likely place the store in maintenance mode and/or use a static maintenance site to prevent live transactions during the most critical parts of the cutover.

 An important part of this step is to have agreement with all participating parties around the maximum time to be spent on each step as well as critical milestone steps having pass/fail criteria along with rollback criteria in the event of a failure. Having these steps defined ahead of time avoid last minute decisions based on arbitrary criteria from being made in the event an unanticipated challenge is met (game days, tabletop exercises or simulations attempt to drive a similar thought process).

 At this point you’ve effectively migrated your Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service platform to AWS, and you can begin the decommissioning process – first through soft methods (e.g. stopping services) on to harder methods (decommissioning of virtual machines and servers).

 The cutover process varies based on the specific Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service installations architecture, but in general, you want to stop existing Magento processes as well as disable any scheduled `cron` jobs.

 You can redirect traffic by changing the current content delivery network (CDN) configuration, the current DNS configuration (ensuring as part of premigration you’ve lowered the TTL) or, optionally, using the EC2 instances on AWS as new upstream targets for your current load balancer (this being the least preferred option).

 Some customers might use this as an opportunity to change DNS or CDN providers and these migration activities can be performed as part of a pre-migration or post-migration, following their own migration process and steps.

## Optimization
<a name="optimization"></a>

 Previously made architecture decisions can also be revisited post-migration. For example, if you used a rehost approach, you can evaluate and re-platform post-migration services, or right-size services based on current and forecasted load. This period of time is an excellent period to evaluate potential opportunities for reserved instance purchases, which offer a discount to service cost in trade for commitment to use a service for a period of time (ideal for Amazon RDS, Amazon ElastiCache and permanent Amazon EC2 instances in production).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
