---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/approach-1-decouple-by-using-a-standalone-api.html
---

# Approach 1: Decouple by using a standalone API
<a name="approach-1-decouple-by-using-a-standalone-api"></a>

When you use this approach, you instantiate a standalone API by converting the shared COBOL program AB.1 into a Java program. To minimize refactoring efforts, you can use automated refactoring tools provided by AWS Partners (see the [Resources](resources.md) section) to generate network APIs for the program. Some tools can automatically generate a facade layer from the selected program by using an integrated development environment (IDE) such as Eclipse.

We recommend this approach when the shared program can be instantiated as a standalone service. The remaining components of applications A and B are refactored into Java as a whole and migrated to the cloud. You can migrate the applications in the same wave or in different waves.

## Migrating applications in the same wave
<a name="migrating-applications-in-the-same-wave"></a>

In the following diagram, applications A and B are grouped to be migrated in the same wave.

![Applications A and B are grouped to be migrated in the same wave.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/3d583f33-df36-4ed8-9780-090f2943f988.png)

 If you're decoupling your code by using a standalone API and migrating applications in the same wave, follow these steps:

1. Refactor both applications with their respective programs and migrate them to the cloud.

1. Use the impact analysis report from the analysis phase to help developers and teams identify the refactored applications that call shared program AB.1. Replace the inner program call to shared program AB.1 with network API calls.

1. After the migration, retire the on-premises mainframe applications and their components.

## Migrating applications in different waves
<a name="migrating-applications-in-different-waves"></a>

When applications are too big to be grouped into the same migration wave, you can migrate them in multiple waves, as shown in the following diagram, and maintain service continuity during migration. With this approach, you can modernize your applications in phases without bundling them together. Migrating your applications in separate waves decouples them without requiring significant code changes on the mainframe.

![Applications A and B in separate migration waves.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/124e0f5e-1070-4302-a425-806d3a1ad408.png)

 If you're decoupling your code by using a standalone API and migrating applications in different waves, follow these steps:

1. Migrate (refactor) application A with its associated programs to the cloud while application B continues to reside on premises.

1. In application A, replace the inner program call to shared program AB.1 with an API call.

1. Maintain a copy of program AB.1 on the mainframe so application B can continue to operate.

1. Freeze the feature development of program AB.1 on the mainframe. After this point, all feature development will take place in refactored program AB.1 in the cloud.

1. After application A is migrated successfully, retire the on-premises application and its components (excluding the shared program). Application B and its components (including the shared program) continue to reside on premises.

1. In the next set of migration waves, migrate application B and its components. You can call the migrated, refactored program AB.1 to reduce refactoring efforts for application B.
