---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/best-practices.html
---

# Best practices
<a name="best-practices"></a>

During the mobilization and planning stages of migration, we recommend the following best practices:
+ Perform code analysis to produce a dependency map for the mainframe applications. We recommend that you automate code analysis by using discovery tools (see the [Resources](resources.md) section) for this exercise.
+ Identify the list of programs and subprograms that are shared by applications by using the discovery tools. Group applications that share the same programs and subprograms together for the same migration wave, to reduce program calls between the on-premises environment and the cloud.
+ In the planning stage, run an impact analysis to identify applications that share programs and subprograms with the application that you're planning to migrate. Select one of the decoupling patterns described in this guide for application migration.
+ When possible, perform mainframe migration incrementally to reduce complexity and risk. By doing incremental migration, migration teams can provide faster feedback regarding the migration progress, and businesses can use the feedback to optimize internal processes to accelerate the pace of migration.
