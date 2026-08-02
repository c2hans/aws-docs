---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/high-level-migration-process-flow.html
---

# High-level migration process flow
<a name="high-level-migration-process-flow"></a>

The migration process occurs in five phases: discovery, design, development, testing and refinement, and implementation. The following table provides an overview of these five phases and the migration process flow.

|
|
|  | **Discovery** | **Design** | **Development** | **Testing and refinement** | **Implementation** |
| --- |--- |--- |--- |--- |--- |
| **Outcomes** | Existing system architectureMigration inventoryFunctional and non-functional requirementsFuture system architecture (High-level) | Migration strategy for each component (7 Rs)Target AWS architectureTCO analysis and assessmentHigh-level migration plan | Ready-to-deploy applicationsAutomation scripts in CloudFormationA step-by-step migration plan, including automated and non-automated tasksDetailed test plans | Testing reportsRefined automation scripts, migration plans, and testing plans | An OpenText Customer Experience platform running on the AWS CloudTesting reports |
| **Tasks** | Discovery workshopsDocumentation analysis | Multi-disciplinary subject matter expert (SME) meetingsCost analysisValidation workshops | Multi-disciplinary SME meetingsApplication refactoring and adaptationAdapt and create automation scriptsCreate or provision new services or functionalities | Automated testingAdapt automation and migration plans | Migration plan implementationAutomated testing |
| **Customer resources** | Technical and business documentationBusiness owners and technical architects – Participation in workshops and interviews | Current TCO dataBusiness owners and technical architects – Participation in validation workshops and interviews.Access to technical assets (environments, source code, or deployment pipelines) | Access to technical assets (environments, source code, or deployment pipelines)Technical teams – Support about current applications. | User testingInfrastructure teams – Support for migration activities | User testingInfrastructure teams – Support for migration activities |
| **Accelerators** | OpenText architecture analysis frameworkDiagramsFocus points | Existing knowledge about the most common migration strategies and target AWS products and services for each solution component | Existing automation assets for:Provisioning of AWS resourcesData migrationApplication installation and configuration | Automated testing assets creating during previous migrations, such as:System health checksPerformance and Load testing scripts | Automated testing assets creating during previous migrations, such as:System health checksPerformance and Load testing scripts |
