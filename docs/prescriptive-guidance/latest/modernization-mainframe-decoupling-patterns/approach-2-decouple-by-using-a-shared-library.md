---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/approach-2-decouple-by-using-a-shared-library.html
---

# Approach 2: Decouple by using a shared library
<a name="approach-2-decouple-by-using-a-shared-library"></a>

In this approach, the shared program AB.1 is converted into a Java common library and is packaged with the applications for migration. We recommend this approach when the shared program is a supporting library instead of a standalone service.

The remaining components of applications A and B are refactored into Java programs and migrated to the cloud. You can migrate the applications in the same wave or in different waves.

## Migrating applications in the same wave
<a name="migrating-applications-in-the-same-wave"></a>

In the following diagram, applications A and B are grouped to be migrated in the same wave.

![Applications A and B are grouped to be migrated in the same wave.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/bf7d516d-fba2-4e93-b0df-f10d6dc8c276.png)

 If you're decoupling your code by using a shared library and migrating applications in the same wave, follow these steps:

1. Refactor applications A and B with their associated programs into Java and migrate them to the cloud.

1. Maintain the source code of the applications in a fully managed source control service, such as [AWS CodeCommit](https://aws.amazon.com/codecommit/). The teams that use the shared program can collaborate on code changes by using pull requests, branching, and merging, and can control the changes made to the shared program code.

1. After the migration, retire the on-premises mainframe applications and their components.

## Migrating applications in different waves
<a name="migrating-applications-in-different-waves"></a>

When applications are too big to be grouped into the same migration wave, you can migrate them in multiple waves, as shown in the following diagram, and maintain service continuity during migration. With this approach, you can modernize your applications in phases without bundling them together. Migrating your applications in separate waves decouples them without requiring significant code changes on the mainframe.

![Applications A and B in separate migration waves.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/bf1ba80a-5eda-4532-9817-7ba89e5f517c.png)

 If you're decoupling your code by using a shared library and migrating applications in different waves, follow these steps:

1. Migrate (refactor) application A with its associated programs to the cloud while application B continues to reside on premises.

1. Maintain a copy of program AB.1 on the mainframe so that application B can continue to operate.

1. Freeze the feature development of program AB.1 on the mainframe. At this point, all feature development will take place in refactored program AB.1 in the cloud.

1. When developing new features for program AB.1, maintain backward compatibility to support application B's migration in future waves.

1. After application A is migrated successfully, retire the on-premises application and its components (excluding the shared program). Application B and its components (including the shared program) continue to reside on premises.

1. In the next set of migration waves, migrate application B and its components. You can use the latest shared library of program AB.1 in the cloud to reduce the refactoring efforts for application B.
