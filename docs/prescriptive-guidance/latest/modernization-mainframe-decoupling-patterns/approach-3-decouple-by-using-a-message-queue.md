---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/approach-3-decouple-by-using-a-message-queue.html
---

# Approach 3: Decouple by using a message queue
<a name="approach-3-decouple-by-using-a-message-queue"></a>

In this approach, the shared program AB.1 is converted into a Java program and migrated to the cloud as part of application A. A message queue is used as an interface between the refactored application in the cloud and the legacy application on premises. By using this approach, you can break up tightly coupled mainframe applications into producers and consumers, and make them more modular so they can function independently. The additional advantage is that you can migrate the applications in different waves.

We recommend that you use this approach when:
+ Applications residing on the mainframe can communicate with the migrated applications in the cloud through a message queue.
+ Multiple copies of program AB.1 (for example, an on-premises copy and a cloud copy, as in the two previous approaches) can't be maintained.
+ The queuing architecture pattern meets the business requirements for the applications that reside on the mainframe, because it involves re-architecting the existing applications.
+ The applications that aren't part of the first wave require a longer time (six months or more) to be migrated to the cloud.

## Migrating applications in different waves
<a name="migrating-applications-in-different-waves"></a>

When applications are too big to be grouped into the same migration wave, you can migrate them in multiple waves, as shown in the following diagram, and maintain service continuity during migration. With this approach, you can modernize your applications in phases without bundling them together.

![Applications A and B grouped in the save wave.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/eb1ad205-be1b-4f0a-ac99-f6235df4eb0d.png)

 If you're using this approach, follow these steps:

1. Migrate (refactor) application A with its associated programs to the cloud while application B continues to reside on premises.

1. Refactor application A (in the cloud) to communicate with application B (on premises) through a message queue.

1. Refactor application B on premises to replace the shared program AB.1 with a proxy program that sends messages to, and receives messages from, application A through the message queue.

1. After application A is migrated successfully, retire the on-premises application A and its components (including the shared program). Application B and its components continue to reside on premises.

1. In the next set of migration waves, migrate application B and its components. The loosely coupled queuing architecture continues to act as an interface between applications A and B on the cloud. This reduces the refactoring efforts for application B without impacting application A.
