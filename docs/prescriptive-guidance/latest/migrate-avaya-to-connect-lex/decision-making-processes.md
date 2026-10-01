---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/decision-making-processes.html
---

# Decision-making processes
<a name="decision-making-processes"></a>

Use the following steps to define your strategy for migrating from an on-premises Avaya contact center to Amazon Lex V2 and Amazon Connect Customer:
+ [Step 1: Define the business goals and schedule](#step-1)
+ [Step 2: Choose between a phased approach or a full migration](#step-2)
+ [Step 3: Choose a migration strategy](#step-3)
+ [Step 4: Select your architecture](#step-4)

## Step 1: Define the business goals and schedule
<a name="step-1"></a>

This is the first step in the migration decision-making process. If the goal of the project is to increase self-service and use Amazon Lex V2 for IVR only, you have to strategize how calls will transfer between Avaya and Amazon Lex V2. Understanding the limitations of the existing on-premises systems helps you design an efficient architecture. The following are examples of high-level business goals and the time frames in which you might expect to achieve them:
+ Within three months, migrate Avaya IVRs to Amazon Lex V2 in phases for each business unit.
+ Within one year, migrate completely from Avaya on-premises systems to Amazon Connect Customer and Amazon Lex V2.

## Step 2: Choose between a phased approach or a full migration
<a name="step-2"></a>

When considering migration for contact center systems, there are two possible approaches:
+ **Phased approach – **In this approach, you don't transition all at once. Instead, you strategically move specific components or functions, step by step. This might mean migrating one IVR business function at a time, which provides more control and can help you minimize disruption. This approach offers the opportunity to test, learn, and adjust as you proceed. For organizations that have complex systems or want to minimize risk, this is often the preferred option.
+ **Full migration** –** **In this approach, instead of breaking the migration down into parts, you make a complete switch and transition all contact center systems simultaneously. This approach might be faster, but it comes with its own set of challenges. It requires meticulous planning and preparation. If you're confident in your migration plan and want a quicker transition, this might be the approach for you.

When choosing between these approaches, it's essential to assess the size, complexity, and specific needs of your business operations. The key is to strike a balance between minimizing disruption and ensuring a smooth transition to the new system.

## Step 3: Choose a migration strategy
<a name="step-3"></a>

Legacy, on-premises contact centers are generally built on a dual-tone multi-frequency (DTMF) approach or a speech-to-text based approach. Replicating your on-premises experience with Amazon Lex V2 is not recommended, especially if your call flows are extremely complex. Instead, you can focus on using the AI capabilities of Amazon Lex V2 to drive an exceptional experience. However, if the goal of your project is to migrate to the cloud and your existing call flows are very basic, you can choose to rehost and then modernize the experience in the future.

## Step 4: Select your architecture
<a name="step-4"></a>

Depending upon the goal of your migration project, choose from the list of possible approaches discussed in the [Architecture options](architecture-options.md) section of this guide.
