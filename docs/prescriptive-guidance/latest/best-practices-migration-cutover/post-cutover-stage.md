---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/post-cutover-stage.html
---

# Post-cutover stage
<a name="post-cutover-stage"></a>

## Setting up a monitoring dashboard
<a name="monitoring-dashboard"></a>

After an application is migrated to the cloud, we recommend that you work with your stakeholders to determine the information or parameters which should be monitored and published to a monitoring dashboard. Typically, dashboards monitor key service-level agreement (SLA) metrics and service-level indicators (SLIs) that are required for operations. You can monitor reachability, availability, security, traffic patterns, and other relevant data points. Monitoring this data not only validates that your application is performing as expected but also reveals if your application is delivering the expected quality.

## Understanding and communicating success
<a name="communicating-success"></a>

After you successfully complete your workload migrations, we recommend communicating this success to the relevant stakeholders. Your stakeholders could include a single threaded leader, sponsors, end users, workload application owners, and any other dependent application owner.

Additionally, it's worth considering any learnings that will help improve the process for future application migrations. You can use a migration score card to measure the success of your migration and communicate overall migration progress across applications and business units. This effort can act as a catalyst for teams to look for opportunities to learn from each other, minimize migration risks, and adopt best practices.

## Defining a warranty period
<a name="warranty-period"></a>

It's common for migration projects to have a warranty period in which the migration teams provide support in the event that an issue occurs within a predefined window (typically from one day to one week). It's important to agree on a suitable timeframe based on the application that you're migrating. For example, a one-week warranty might not be sufficient if your application runs on a quarterly batch schedule. Furthermore, we recommend that your migration team uses the warranty period to validate that business continuity and disaster recovery elements are configured and working as expected.
