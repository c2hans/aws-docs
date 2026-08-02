---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html
---

# GuardDuty RDS Protection
<a name="rds-protection"></a>

**Note**
You can configure RDS Protection along with all other protection plans from a single page in the GuardDuty console. For more information, see [Configuring protection plans](protection-plans.md).

RDS Protection in Amazon GuardDuty analyzes and profiles RDS login activity for potential access threats to your [Amazon Aurora databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) (Amazon Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition) and [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

RDS Protection helps you identify potentially suspicious login behavior on these supported databases. GuardDuty continuously monitors and profiles [RDS login activity](#guardduty-rds-login-events) for anomalous activity. For example, a previously unseen external actor has unauthorized access to your database, or adversary attempts brute-force access by guessing the database's password.

With the launch of [Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html), GuardDuty expands RDS Protection to now also support monitoring login activity from Limitless Databases. For AWS accounts that have already enabled RDS Protection, GuardDuty will automatically start monitoring login data from their Limitless Databases. For accounts that have not yet enabled RDS Protection, you can learn more about the [30-day free trial](#gdu-rds-protection-30-day-free-trial) and choose to enable this feature. To enable this feature, see [Enabling RDS Protection in multiple-account environments](configure-rds-pro-multi-account.md) or [Enabling RDS Protection for a standalone account](configure-rds-pro-standalone.md).

**Note**
RDS for PostgreSQL read replica instances require the primary database instance to be on a supported database version, and to be successfully replicated from primary database. For information about read replicas, see [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) in *Amazon RDS User Guide*.

RDS Protection doesn't require additional infrastructure; it is designed so as not to affect the performance of your database instances. When RDS Protection detects a potentially suspicious or anomalous login attempt, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md) with details about the potentially compromised database.

**30-day free trial**
+ When you enable GuardDuty in an AWS account in a new Region for the first time, you get a 30-day free trial. In this case, GuardDuty will also enable RDS Protection, which is included in the free trial. RDS Protection will start monitoring the login behavior of your database.
+ When you are already using GuardDuty and decide to enable RDS Protection in a new Region for the first time, your account in this Region will get a 30-day free trial for RDS Protection.
+ If you have already enabled RDS Protection, then with the launch of [Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html), GuardDuty will automatically start monitoring login activity for the Limitless Databases. If your RDS Protection 30-day free trial has expired already, then you will start incurring usage costs related to monitoring of Limitless Databases.
+ You can choose to disable RDS Protection in any Region at any time.
+ During the 30-day free trial, you can get an estimate of your usage costs in that account and Region. After the 30-day free trial ends, RDS Protection doesn't get disabled automatically. Your account in this Region will start incurring usage cost. For more information, see [Monitoring GuardDuty Usage and Estimating Costs](monitoring_costs.md).

When the RDS Protection feature is not enabled, GuardDuty does't detect anomalous or suspicious login behavior. If you disable RDS Protection, GuardDuty immediately stops monitoring RDS login activity, and will not detect any potential threat to your supported database instances or generate associated finding types.

For AWS Regions where Aurora PostgreSQL Limitless Databases are supported, see [Requirements for Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.html#limitless-requirements).

## Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases
<a name="rds-pro-supported-db"></a>

The following table shows the supported Aurora and Amazon RDS database versions for RDS Protection.

| Amazon Aurora and Amazon RDS DB engine | Supported engine versions |
| --- | --- |
| Aurora MySQL |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)  |
| Aurora PostgreSQL |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)  |
| RDS for PostgreSQL | [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html) |
| Amazon Aurora PostgreSQL Limitless Database |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)  |
| Amazon RDS for MariaDB |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)  |
| Amazon RDS for MySQL |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)  |

## RDS login activity
<a name="guardduty-rds-login-events"></a>

When you enable the RDS Protection feature, GuardDuty automatically starts monitoring RDS login activity for your databases, directly from the Aurora and Amazon RDS services. RDS login activity captures both successful and failed login attempts made to the [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](#rds-pro-supported-db) in your AWS environment. If there is an indication of anomalous login behavior, GuardDuty generates a finding with details about the potentially compromised database. When you enable RDS Protection for the first time or you have a newly created database instance, there is a learning period to baseline normal behavior. For this reason, newly enabled or newly created database instances may not have an associated anomalous login finding for up to two weeks.

When RDS Protection detects a potential threat, such as an unusual pattern in a series of successful, failed, or incomplete login attempts, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md). Based on the finding type, it may include details about the anomalous behavior, such as [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly).

GuardDuty doesn't manage your [Supported databases](#rds-pro-supported-db) or RDS login activity, or make RDS login activity available to you.
