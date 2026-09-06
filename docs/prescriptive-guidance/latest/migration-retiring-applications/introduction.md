---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/introduction.html
---

# Best practices for assessing applications to be retired during a migration to the AWS Cloud
<a name="introduction"></a>

*Damien Renner, Amazon Web Services*

Choosing to retire applications during a migration to the Amazon Web Services (AWS) Cloud can be a complex decision. By following this guide's best practices you can implement a smoother and more efficient retirement process for your applications.

This guide is for technology or application owners who have analyzed their estate and identified applications that can be retired or decommissioned.

## Overview
<a name="overview"></a>

The purpose of this guide is to provide best practices for applications categorized as "retire" in a migration plan for the AWS Cloud.

A critical first step in creating a migration strategy is collecting application portfolio data, such as extracts from a configuration management database. This data must be evaluated against the seven common migration strategies (7 Rs) for moving applications to the AWS Cloud. These strategies are rehost, relocate, replatform, refactor, repurchase, retain, and retire.

After you complete this initial portfolio analysis, you should have an initial plan for how each application will be migrated. This plan should be regularly optimized for future migration waves and teams, based on lessons learned and new data that becomes available during the migration process. The following diagram illustrates the strategy planning process.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/images/guide-img/11b5b0ce-2bf2-40a9-9f55-c87adb6560a5/images/fc1da705-63cc-405b-8e86-650886d4c129.png)

Deciding if applications should be retired can often become complex and involves a level of risk. This can result in action being postponed, especially if subject matter experts (SMEs) have left an organization. Also, documentation about legacy systems can be sparse.

However, identifying and retiring applications that are no longer useful helps boost your business case and directs your team's attention toward maintaining resources that are more widely used. This guide outlines six best practices to use when assessing applications to be retired in your migration strategy.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

After you assign a migration strategy to each application, it may become apparent that some of those applications can be retired. It's not unusual to find that more than 10 percent of workloads in an enterprise IT portfolio are no longer useful and can be turned off, thereby creating savings for your organization.

These savings can help direct your team's attention to systems or applications that provide value to your business; it also reduces the scope of applications you have to migrate, secure, and operate. Additionally, it's worth evaluating the long-term benefits of keeping unused applications, because they might still need to be licensed, maintained, and upgraded to remain operational.

Retiring applications can cause uncertainty and a level of risk. Because institutional knowledge about legacy systems can often be limited by outdated documentation or personnel changes, there's a risk that IT assets labeled as "no longer required" are, in fact, being consumed elsewhere within your organization.

To avoid this situation, you must fully understand all upstream dependencies of an application within your organization. This is especially important when you are working toward a business outcome, such as migrating workloads to the AWS Cloud so a data center can be closed by a defined date.

Deploying this guide's six best practices and its data-driven methodology will help reduce this risk level when choosing to retire applications.
