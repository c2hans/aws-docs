---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/migration-plan.html
---

# Migration planning
<a name="migration-plan"></a>

In order to successfully migrate an on-premises Avaya contact center to Amazon Connect Customer and Amazon Lex, you need to have an effective plan. The migration plan typically follows a multi-phased approach and includes the following steps and information:
+ [Building your team](#building-team)
+ [Preparing your data](#preparing-data)
+ [Porting telephone numbers](#porting-numbers)
+ [Choosing a target architecture](#choosing-architecture)
+ [Evaluating the current architecture](#evaluating-architecture)
+ [Managing IVR prompts](#managing-ivr-prompts)
+ [Defining cloud infrastructure and security requirements](#defining-requirements)

## Building your team
<a name="building-team"></a>

The contact center migration typically consists of the following specialties and participants:
+ **Discovery** – Product managers, project managers, business analysts, solution architects, implementation engineers, QA, agents, and supervisors
+ **Design** – Conversation designers, software developers, product managers, project managers
+ **Build** – Software developers
+ **Test** – QA
+ **Continuous integration and continuous delivery (CI/CD)** – Cloud enablement or DevOps
+ **Account provisioning** – Cloud enablement or DevOps
+ **Operations** – Support engineers
+ **Security** – Security architects

## Preparing your data
<a name="preparing-data"></a>

An IVR workload can be migrated in phases, such as by business units. You can work with business units in your organization to define business requirements and *replatform* or *refactor* the IVR platform to take full advantage of cloud-native features that can improve agility, performance, and scalability. Therefore, the decision about which business unit migrates first is extremely important. Document requirements, define success metrics, and provide progress updates to measure the overall project success.

## Porting telephone numbers
<a name="porting-numbers"></a>

If you want to retain your existing telephone numbers, you must port your telephone numbers to Connect Customer. This process requires some lead time, and it's helpful to plan for this beforehand.

## Choosing a target architecture
<a name="choosing-architecture"></a>

Depending upon the goal of your migration project, choose from the list of possible approaches discussed in the [Architecture options](architecture-options.md) section of this guide.

## Evaluating the current architecture
<a name="evaluating-architecture"></a>

You can either *rehost* (also known as *lift-and-shift*) your workloads to the AWS Cloud, or you can *replatform* or *rearchitect* your workloads to drive new experiences with cloud-native capabilities. For more information about how to choose between these strategies, see [Step 3: Choose a migration strategy](decision-making-processes.md#step-3) in this guide. In addition to understanding the target state, it's critical that you understand the current state and infrastructure components.

For example, if you're using [Avaya Experience Portal](https://www.devconnectprogram.com/site/global/products_resources/avaya_aura_experience_portal/overview/index.gsp), then you can use JavaScript for API integration. However, if you're using Concentrix for IVR, then such integrations might not be possible, and you must rely on database integrations. Additionally, you need to review all of the existing call flows in the migration plan. In a hybrid approach with two different telephony systems, make sure that you're not duplicating any part of the flows or ignoring any important logic.

## Managing IVR prompts
<a name="managing-ivr-prompts"></a>

Amazon DynamoDB is the most efficient way to store and manage prompts. The business and stakeholders can make changes on the fly without interrupting operations.

## Defining cloud infrastructure and security requirements
<a name="defining-requirements"></a>

Based on your requirements, make a list of the cloud services you will use to achieve your outcomes. Your security team needs to validate if the proposed target architecture meets organizational requirements, such as retention policies, and make sure that logging is considered and documented.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
