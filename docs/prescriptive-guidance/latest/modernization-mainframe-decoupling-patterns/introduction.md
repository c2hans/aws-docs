---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/introduction.html
---

# Mainframe modernization: Decoupling patterns for migrating application code
<a name="introduction"></a>

*Krithika Palani Selvam and Kevin Yung, Amazon Web Services*

Many enterprises are moving their mainframe workloads to the cloud to take advantage of factors such as cost reduction, increased agility, technical debt deduction, digital strategy support, mainframe legacy skills gap, and data analytics. Mainframe workloads are more challenging to migrate than x86-based workloads, because legacy mainframe applications are often developed and deployed in a tightly coupled manner. For example, a mainframe application might include programs that are used by a number of subsystems or are directly called by other applications. In these cases, changes made to the underlying programs also affect the associated subsystems and applications.

For legacy applications, Amazon Web Services (AWS) recommends an incremental approach, where the migration is planned in waves, as a best practice. This approach helps reduce risk, because you select and prioritize applications that are closely related to be migrated together. However, this approach sometimes isn't as straightforward for mainframe migrations as they are for x86-based migrations, especially because the mainframe application code can be temporal coupled (invoked synchronously) or deployment coupled (using linked modules). Migrating the coupled application code affects dependent applications and therefore carries some risks. To reduce such risks, you can decouple the mainframe application code without impacting dependent applications. This guide explains some of the commonly used patterns to decouple mainframe application code for migration.

The guide is for IT and business executives, architects and business analysts, migration and technical leads, development teams, program and project managers, product owners, and operations and infrastructure managers who are planning to migrate and modernize their mainframe applications in the AWS Cloud.

## Objectives
<a name="targeted-business-outcomes"></a>

This guide addresses common challenges you might face when you migrate coupled programs from mainframes to AWS. It presents code decoupling patterns that AWS Professional Services consultants frequently encounter in their engagements with AWS customers. When you use these patterns, both your migrated and legacy applications can continue to function during the migration process.

## Definitions
<a name="definitions"></a>

In this guide:
+ A *mainframe application* refers to a set of related mainframe programs and subprograms that accomplish and facilitate a set of business processes. Mainframe applications can be batch processing systems or online transaction processing (OLTP) systems.
+ A *mainframe component* refers to a group of programs and subprograms that achieve specific functionality.
+ A *mainframe program* refers to a set of statements that implement business logic. Programs can be run independently.
+ A *subprogram* is usually written to handle a reusable operation or business logic that multiple applications require. A program calls its subprograms either statically or dynamically.
+ A *business domain* refers to a specific sphere that represents an autonomous unit of business that is modeled during analysis. For example, the business domain of software refers to the subject area to which the user applies that program.

## Assumptions
<a name="assumptions"></a>

The examples and diagrams in this guide reflect the following assumptions:
+ The mainframe application that is being migrated might run a single program or multiple programs. For simplicity, the diagrams in this guide display two programs for each application, and a single subprogram.
+ The mainframe programs and subprograms are written in COBOL, and the code is migrated to Java on AWS. However, you can use these decoupling patterns with your programming languages of choice.
+ The migration pattern is *legacy automated refactoring*, where code, data, and dependencies are automatically converted to a modern language, data store, and framework while guaranteeing functional equivalence with the same business functions. Refactoring involves using automated tools to convert the mainframe programming language (such as COBOL) into modern programming languages (such as Java or .NET).
+ Refactored applications are deployed on containers that are provisioned and managed by [AWS Fargate](https://aws.amazon.com/fargate/). Fargate is a serverless compute engine for containers that works with both [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/). Fargate makes it easy for you to focus on building your applications because it removes the need to provision and manage servers.
+ Mainframe database tables and mainframe files will be migrated with the application.

## Code migration scenarios
<a name="code-migration-scenarios"></a>

The two main types of legacy mainframe applications, from a code migration perspective, are:
+ Standalone applications
+ Applications that share programs with other applications

The following sections describe the decoupling patterns for these two scenarios.
