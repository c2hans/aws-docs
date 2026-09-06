---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/prioritization.html
---

# Task 3: Defining the application prioritization process
<a name="prioritization"></a>

*Application prioritization* is the process of determining the order in which applications should be migrated to the cloud. You assess priority based on the complexity of migrating the application to the cloud and the rules that you define. When discussing application prioritization, high priority does not necessarily correlate with the importance of the application to the business. In fact, applications that are business-critical are typically low priority for the migration because business-critical applications have higher risks. In a large migration, you prioritize low-complexity applications that are not business critical, and with each wave, you migrate increasingly more complex or business-critical applications.

In a large migration, where you have hundreds of applications lined up for migration, we don't recommend that you prioritize and plan every application all at once. This is one of the reasons why defining an application prioritization process is critical to a large migration project. To approach the migration in an agile way, you can pick the highest priority applications (3–10 applications), or you can select enough applications for 3–5 waves. You then complete application discovery and wave planning for only the selected applications. This approach saves a significant amount of time because application priority and waves often change during the course of a large migration.

One common myth about application priority is that the highest priority applications should be in the first wave. When you are performing wave planning, there is a high possibility that only a few of the 10 highest priority applications will be in the first wave because the others are not ready. This could be for a variety of valid reasons, such as dependencies, business constraints, or resource availability. Application priority is a critical factor in wave planning, but it shouldn't be the only factor you consider.

In this task, you define the application prioritization process and rules. This task consists of the following steps:
+ [Step 1: Define the application prioritization process](#prioritization-1)
+ [Step 2: Define the application prioritization rules](#prioritization-2)
+ [Step 3: Finalize the application prioritization process](#prioritization-3)

The next section discusses complexity scoring. This playbook provides three process options for how to prioritize applications, and two of the three options use complexity scoring. For more information about the process options, see [Step 1: Define the application prioritization process](#prioritization-1). If you plan on using the application nomination process, then you do not need to define complexity scoring criteria, and you should proceed directly to [Step 1: Define the application prioritization process](#prioritization-1).

## About complexity scoring criteria
<a name="prioritization-complexity-scoring"></a>

*Complexity scoring* is the process used to assess the difficulty of migrating an application, which is a critical factor when prioritizing applications. Complexity scoring involves evaluating all applications against the same set of business and technical criteria, which you define. When evaluating an application, you assign a score to each criterion. When you sum the scores of the business criteria and technical criteria, you get a complexity score that reflects the overall complexity of migrating that application. You can then use the complexity score when prioritizing applications and planning waves.

There are two categories of complexity scoring criteria:
+ **Business criteria** – The criteria in this category relate to the business complexity of migrating the application, such as risk if the application becomes unavailable, security and compliance considerations, and resource availability.
+ **Technical criteria** – The criteria in this category relate to the technical complexity of migrating the application, such as operating systems and their versions, the number of servers and users, and the migration strategy.

You should determine the appropriate scoring criteria for your use case. If you are manually scoring application complexity, the attached *Score sheet template for application complexity* (Microsoft Excel format) contains a standard set of criteria and score values. You might want to start with these values and then customize them for your use case. If you are using a discovery tool for application prioritization, these tools commonly include a standard set of criteria, and you can add, remove, or modify the criteria, and you can weight them according to your needs. When you are establishing criteria, use the questions in the next two sections to help refine your criteria.

### Business criteria
<a name="business-criteria.74ee23a5-3135-5018-9182-12b072cd64ca"></a>

The following are business criteria that are commonly used in complexity scoring.

|
|
| Business criteria | Description |
| --- |--- |
| Business impact | Assess the impact to the business if this application becomes unavailable:+ Does it have financial impact?<br />+ Does it have operations impact?<br />+ Does it impact the customer experience?<br />+ Does it impact a product or company event? |
| Staff availability  | During the migration, you might need assistance from the application owner, a subject matter expert (SME), network or infrastructure administrators, testers, and developers. Assess the availability of these resources to help you during the migration:+ Will this staff be available during the migration to assist and provide guidance to the migration teams?<br />+ Will this staff be available to test and validate the application after it's migrated?<br />+ Will this staff be available to provision IP addresses or ports necessary for running the application in the target environment? |
| Business complexity | Having many interdependent and interconnected stakeholders, information technology systems, and organizational structures can increase the business complexity. Assess business complexity as follows:+ How long will it take for the business to approve the infrastructure and network changes, such as firewall changes or provisioning a new instance?<br />+ How long will it take for the business to approve new software or tool installations on their server, such as discovery tools?   |
| Readiness | Assess whether the application is ready for migration as follows:+ Is the application currently undergoing or scheduled to undergo a technology refresh?<br />+ Is maintenance scheduled, and will it overlap with the scheduled migration?<br />+ Is the application scheduled for decommission?<br />+ Is the application currently being upgraded, and are any new features being developed or integrated? |
| Security  | Assess the complexity of the application's security requirements and security policy as follows:+ Do you need to provision IP addresses and ports for accessing the application?<br />+ Does the application require infrastructure protection?<br />+ Does the application require data protection?<br />+ Is key management required?<br />+ Does the application require special access management policies?<br />+ Does the application require monitoring or logging?<br />+ Does the application require an incident response process and automation?<br />+ Are alerts and notifications required for this application? |
| Compliance | Compliance requirements might apply for the application, such as laws, regulations, and guidelines provided by the state, business industry, or company policy. Assess the complexity of the application's compliance requirements as follows:+ Are there any data privacy and residency requirements?<br />+ Should data at rest in the application be encrypted?<br />+ Should data in transit to or from the application be encrypted?<br />+ Is audit logging required?<br />+ Does the application need to be compliant with accounting and financial standards, such as System and Organization Controls (SOC)?<br />+ Does the application need to be compliant with payment security standards, such as Payment Card Industry (PCI)?<br />+ Does the application need to be compliant with patient health information regulations, such as Health Insurance Portability and Accountability Act (HIPAA)?<br />+ Does the application need to be compliant with public-cloud security programs, such as Information System Security Management and Assessment Program (ISMAP)? |
| Application knowledge | Does someone in the organization, such as the application owner, have the knowledge, skills, and experience to maintain, integrate, troubleshoot, and fix issues? And are you able to extend the application to meet business demand? |
| Migration skills | Does staff in your organization have the skills to migrate the workload to the target environment? |

### Technical criteria
<a name="technical-criteria.3ca73e77-ac48-56c3-8aea-30f832642ac7"></a>

The following are technical criteria that are commonly used in complexity scoring.

|
|
| Technical criteria | Description |
| --- |--- |
| Storage  | Assess the application's current storage as follows:+ Where is the application currently stored? Examples include a network-attached storage (NAS), a storage area network (SAN), or a local drive.<br />+ What is the total size of the current storage? |
| Number of users | How many users does this application have? You can use actual logs or estimate. |
| Server count | How many servers are in the application stack? |
| Connectivity | Assess how this application is connected to others in your organization as follows:+ How many other applications are dependent on this application?<br />+ What is the impact to other applications if this application is unavailable? |
| Application OS and version | Assess the operating system (OS) and version of the application's server as follows:+ Is the server's OS version no longer supported?<br />+ Is the server running a Unix or Linux OS?<br />+ Is the server running a Windows Server OS?<br />+ Is the application on a mainframe or on midrange servers? |
| Application dependencies | Assess how this application is dependent upon other resources in your environment:+ What resources is this application dependent upon? Resources can be other applications, components, OS-specific services (such as registries or web servers), or libraries.<br />+ What is the impact to this application if one or more of those resources is unavailable? |
| Data migration | Assess whether you need to migrate data or files for this application:+ How complex is the data migration?<br />+ How complex is the file migration? |
| Migration strategy | Assess the complexity of the selected migration strategy. For more information about the migration strategies, see the [Guide for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/). |
| COTS or custom | Assess whether the application is custom made or commercial off-the-shelf (COTS) as follows:+ Do you have the latest version of the source code?<br />+ Is the application vendor-supported?<br />+ Is the application outsourced? |

## Step 1: Define the application prioritization process
<a name="prioritization-1"></a>

This playbook includes three process options for prioritizing applications. You can select one of the options, or you might decide to combine two or more and build a custom process. Evaluate your use case and determine which of the following is the best fit for your environment:
+ **Option 1: Manual complexity scoring** – This is a manual prioritization process that can be completed by an individual or in a workshop-style session. In this process, you use complexity scoring criteria to assess the difficulty of migrating each application, which is an important factor in prioritizing applications. This manual process is well-suited to large migrations because it provides a consistent, quantitative approach for prioritizing a large application portfolio. However, evaluating each application against a defined set of criteria can be a slower process when compared with the other two options.
+ **Option 2: Application nomination** – This is a manual prioritization process that is typically completed a workshop-style session. In this process, the application owners nominate applications for migration. To be successful, this process requires that the application owners have comprehensive knowledge of their respective applications. This process is recommended if time is a factor and you need to quickly prioritize applications.
+ **Option 3: Discovery tool** – This is an automated prioritization process. If the discovery tool in your environment has an automated feature for automated application complexity scoring or prioritization, using this feature can save time and accelerate the application prioritization process. In this process, you typically define criteria within the parameters of the discovery tool, and then the tool analyzes the applications and provides a final complexity score. Before selecting this option, explore the features available in your discovery tool and verify that you can customize it to meet the needs of your use case.

### Option 1: Manual complexity scoring
<a name="option-1--manual-complexity-scoring.fe740f68-3534-550f-aa52-57f43eca7207"></a>

In this manual application prioritization process, you use a worksheet to evaluate the application against a defined set of complexity scoring criteria. We recommend that you complete the worksheet in a workshop-style session, or an individual can complete the worksheet by collaborating with stakeholders. You then use the final complexity score and the application prioritization rules in order to determine the application's priority. Of the manual processes, this provides the most consistent, quantitative approach to determining application complexity and using that information to prioritize applications.

For the complexity scoring steps in this process, we recommend you use the attached *Score sheet template for application complexity* (Excel format). This template includes predefined business and technical criteria. You can add, remove, or modify these criteria, or you can adjust the scoring values. For example, you might prefer a scoring range of 1–10 instead of 1–5. Note the following about the provided template:
+ You can hover over each criterion for a description of it.
+ When you are familiar with the template, you should delete the examples. These are for demonstration purposes only.

Keep the complexity score sheet updated throughout the initialization and implementation stages of the migration. You might change scores as you progress through the portfolio assessment. The application deep dive is a common time to update the score sheet because you learn more about each application as the team examines it in detail. During the migration, you might also change the application priority if you encounter issues, such as undiscovered dependencies and limitations that prevent you from migrating the application. By maintaining the score sheet throughout the migration, you can prioritize applications with greater accuracy.

Document your application prioritization process as follows:

1. Open the attached *Score sheet template for application complexity*.

1. On the **Applications **sheet, add, modify, or remove criteria as appropriate for your migration. When modifying the criteria, do the following:

   1. Review the guidance in the About complexity scoring criteria section of this playbook.

   1. Consider the impact each criterion has to the duration, resources, and cost of the migration.

   1. For a reliable complexity score, include criteria that represent varying levels of migration complexity in your organization.

1. On the **Scoring guide** sheet, update the default values and criteria as needed for your use case.

1. Save the score sheet.

1. Open your application prioritization runbook.

1. In the *Application complexity scoring criteria* section, update the section to reflect the location of your score sheet.

1. In the *Application prioritization process *section, do the following:

   1. Keep *Option 1: Manual complexity scoring* and delete the other options.

   1. Modify the process as needed for your use case.

   1. Remove any headings in this section that contain the word *Option*. Leaving these in the runbook might confuse users into thinking that the process is optional or that multiple options are available.

1. Save your application prioritization runbook.

### Option 2: Application nomination
<a name="option-2--application-nomination.f3ea200b-09ce-5d28-820d-b6644bfeb940"></a>

This manual application prioritization process is the easiest and fastest approach to prioritizing applications. In this process, you ask the application owners to nominate applications that can be easily migrated to the cloud. You and the application owners can then quickly prioritize the applications because you already have in-depth knowledge of the nominated applications. We recommend that you work with stakeholders in a workshop-style session, but you can also collaborate via email, shared documentation, and other communication platforms.

During the nomination process, you enter the nominated applications into the attached *Score sheet template for application complexity* (Excel format). You will not use all of the scoring and criteria features in this template, but we recommend using this sheet to record the nomination and prioritization decisions.

In some situations, the application nomination process is used to accelerate the prioritization, and the score sheet might not be needed. For example, if you are prioritizing only a handful of applications or if the application owners are very knowledgeable about their applications, the application owners and stakeholders can prioritize the applications based on their knowledge and experience. In this case, they can skip using the score sheet, and proceed directly to prioritization.

Document your application prioritization process as follows:

1. Open your application prioritization runbook.

1. Delete the *Application complexity scoring criteria* section. This process does not use application complexity scoring.

1. In the *Application prioritization process *section, do the following:

   1. Keep *Option 2: Application nomination* and delete the other options.

   1. Modify the process as needed for your use case.

   1. Remove any headings in this section that contain the word *Option*. Leaving these in the runbook might confuse users into thinking that the process is optional or that multiple options are available.

1. Save your application prioritization runbook.

### Option 3: Discovery tool
<a name="option-3--discovery-tool.7cd8f601-2cda-5a85-a582-8db07271e158"></a>

If your discovery tool has a feature for complexity scoring or application prioritization, this automated process requires few resources and can accelerate the application prioritization process. You customize the criteria in the discovery tool for your use case, and then the discovery tool automatically analyzes the applications and provides a final complexity score. Because the tool already has all of the application metadata, you don't need to enter it.

For example, the Flexera One Cloud Migration and Modernization (formerly Flexera Foundation and CloudScape) discovery tool has a complexity scoring features called the *Optimization Scorecard*. This feature allows you to select the criteria that you want to include in scoring and weigh each criterion based on your preference. After data discovery is complete, the discovery tool analyzes the data based on the weighted criteria you provided and, using the tool's proprietary formula, produces the final complexity scores. For more information, see the [Foundation and CloudScape User Guide](https://docs.flexera.com/foundationcloudscape/ug/Content/helplibrary/FoundationCloudscapeRoot.htm) (Flexera documentation) and [Optimization Scorecard](https://docs.flexera.com/foundationcloudscape/ug/Content/helplibrary/FCReports_OptScorecard.htm) (Flexera documentation).

The disadvantage of this process is that it requires time (4–8 weeks) to set up the scanning appliance for an agentless discovery tool in your environment or to install agents to all in-scope workloads. Before you can use the scoring feature in your discovery tool, you must allow additional time (4–12 weeks) for the discovery tool to collect metadata by scanning the application workloads and performing application stack analysis. However, you might find that the extra time needed to configure the discovery tool might be recovered by reducing the amount of time and resources needed for metadata collection and application prioritization. For example, if the discovery tool's data is still current, the portfolio workstream can reuse the discovery tool and its data from the mobilize phase to identify pilot applications.

**Note**
If you are using the discovery tool process, you can still use the manual *Score sheet template for application complexity* in order to analyze the application against a different set of criteria. This additional information might help you refine your application prioritization.

Document your application prioritization process as follows:

1. If you have not already done so, set up the discovery tool in your environment. For more information, see [Get started with automated portfolio discovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-started-with-automated-portfolio-discovery.html) on the AWS Prescriptive Guidance website.

1. Customize the complexity scoring or application prioritization criteria in your discovery tool according to the instructions for your tool. For more information about selecting criteria, see *About complexity scoring criteria*.

1. Open your application prioritization runbook.

1. In the *Application complexity scoring criteria* section, update the section to reflect that the scoring criteria is defined in the discovery tool.  Example: Complexity scoring criteria is defined in <your discovery tool>.

1. In the *Application prioritization process *section, do the following:

   1. Keep *Option 3: Discovery tool* and delete the other options.

   1. Modify the process as needed for your use case. It is important that you include step-by-step instructions for how to generate a report with the complexity scores. If available, you can include a link to the user guide.

   1. Remove any headings in this section that contain the word *Option*. Leaving these in the runbook might confuse users into thinking that the process is optional or that multiple options are available.

1. Save your application prioritization runbook.

## Step 2: Define the application prioritization rules
<a name="prioritization-2"></a>

In this step, you define *application prioritization rules*, which help you determine the migration order of the applications. Although an application's complexity score is an important factor in prioritizing applications and planning waves, business and technology factors also must be considered. You create rules to assess the priority of each application and help you schedule the application in the appropriate wave. Common business and technology rules include:
+ Specifying the order and schedule for migrating data centers
+ Prioritizing business units
+ Capturing deadlines for critical business applications

Define your application prioritization rules as follows:

1. Open your application prioritization runbook.

1. In the *Application prioritization rules* section, add the custom rules for your migration.

1. Save the application prioritization runbook.

1. Maintain the rules in the application prioritization runbook. Rules are subject to change as the migration progress, scope changes, or schedules shift.

The following is an example set of application prioritization rules.

|
|
| Priority | Rule |
| --- |--- |
| 1 | Applications in the New York data center should always have higher priority than applications in the Texas data center. |
| 2 | Applications in the IT department should always have higher priority than applications in the Marketing department. |
| 3 | Applications with high complexity scores should have higher priority. |
| 4 | SAP applications need to be migrated before the end of the year. |

## Step 3: Finalize the application prioritization process
<a name="prioritization-3"></a>

Now, you define how the portfolio workstream uses the rules and processes to prioritize applications. This is the process that the portfolio workstream references in the implementation stage of the migration.

Customize this process in the application prioritization runbook as follows:

1. Open your application prioritization runbook.

1. In the *Stage 2: Prioritize applications *section, modify the process as appropriate for your use case and environment.

1. Save the application prioritization runbook.

## Task exit criteria
<a name="prioritization-exit-criteria"></a>

Continue to the next task when you have completed the following:
+ You have selected an application prioritization process from the available options.
+ You have documented the following in your application prioritization runbook:
  + Application complexity scoring criteria (if applicable)
  + Application prioritization process
  + Application prioritization rules
+ You have updated the *Stage 2: Prioritize applications* section of your application runbook.
