---
source_url: https://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/innovation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Innovation
<a name="innovation"></a>

 In this chapter, we go beyond and above conventional MBSE software and applications of which high-level architecture is shown in the diagram below. Please note that you see “AWS … Services” icons in the figure to indicate a family of services rather than individual service not to confine the architecture into a specific service and to simplify the figure.

 Since the needs for MBSE are diverse for our customers, the following technologies are **modular** where each module is **mutually inclusive** and **independent**. Therefore, we recommend that the reader investigates each option separately, while keeping the overall perspective unified in case all of the solutions can be applied at the same time.

 This chapter explains how you can:
+  Bring **Digital Continuity** layer to connect to your offices, edge, and vehicle devices – as well as ingest data from thousands of internal and external resources in petabyte scale.  Manage complexity with an **Orchestration layer for Digital Thread** as a part of digital continuity.
+  Extend multi-disciplinary/multi-supplier collaboration in micro-process scale with **Extended Workforce Collaboration** **built on MBSE**.
+  Adopt **Intelligent** **Datalake for MBSE (“Artifact-Store with Artifact Catalog”)** as single source of data where engineers can put their excels, pdfs, model data, etc.
+  Bring **AI/ML for MBSE** to provide NLP for MBSE for ontology, legacy document integration, obtain valuable insights and analytics based on overall operations/events and data mentioned before.
+  Employ **Shared Services Platform (SSP)** to centrally manage, govern your applications as well provide secure environment for IT and engineering experimentation.

![Diagram showing Modules and AWS services for MBSE on AWS (High-level Architecture)](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/mbse-architecture-diagram.png)

## Digital Continuity Layer
<a name="digital-continuity-layer"></a>

 MBSE works in a complex environment under different expectations. This fact requires any MBSE environment to exhibit interoperability in a wide variety of software, workflow, and environments. The “environment” would cover a wide variety of APIs to work in hybrid on-prem/cloud configurations. The digital continuity layer brings simplification with standardization and orchestration that enhance interoperability and flexibility to extend the MBSE. One of the enablers for Digital Continuity is the orchestration of APIs. Standardizing digital threads with APIs and message payloads with JSON can be performed.

 As shown in the diagram above, one of the first components is **data gateway**. MBSE can be extended into the field via **AWS for the Edge **technologies such as **AWS Outposts**, **AWS Wavelength**, **AWS IoT** and **AWS Storage Gateway** and **Amazon SageMaker AI** that can bring compute, storage, business logic, contend delivery, offline-mode or machine learning to the edge.

 One of the applications would be **data ingestion**. There could be a wide variety of data sources ingested. **Amazon Kinesis** would bring petabyte-scale data ingestion capability with real-time processing power as part of digital continuity on the cloud.

 If you would like to use an open-source platform for building real-time streaming data pipelines for your MBSE such as **Apache Kafka** but still would like to use AWS, you can consider using **Amazon MSK**. The other part of the digital continuity layer is the **ETL (Extract – Transform - Load) **operations.

 **AWS Glue** can perform ETL in a serverless mode. You can create **AWS Glue Workflows** and end to end data-pipelines, encompassing other AWS services such as Amazon SageMaker AI or external endpoints including on-premises. The digital continuity would also cover existing data centers or design offices where the hybrid cloud environment can be supported by the Digital Continuity, such as via **AWS Storage Gateway**.

 Moreover, as discussed before, you can leverage more than **[230 global points of presence](https://aws.amazon.com/about-aws/global-infrastructure/)** of AWS to further decrease the latency and increase the reliability of the interactions. Technologies such as **Amazon CloudFront** and **AWS Global Accelerator** can take over the traffic from the public internet through these edge locations.

 The simulations in MBSE are high-level (low-fidelity) and discreet. Moreover, the processes are transactional, rather than running continuously. For example, a change in a product design or a change in a requirement would correspond to an “event: change” with the message content of “change: metadata”.

 The model data can be standardized as well, following UML (Unified Modeling Language) compliance. Hence, the overall processes can be expressed in terms of events and short simulations based on transactions (messages and events) and attached metadata (body). Hence, your MBSE can transform model metadata into machine-readable lightweight interpretable representations. *Simplification* and *standardization* enable **event-driven architectures** for the MBSE.

 You can use **Amazon EventBridge** as a serverless event-bus without using any code. Amazon EventBridge would be one of the fundamental parts of an event driven architecture that manages complexity through events chorography.

 Along with Amazon EventBridge, **AWS Step Functions** or **AWS Managed Apache Airflow** for an open-source approach are AWS managed technologies to build orchestration and manage the complexity of MBSE and derivative workloads as the orchestration.

 **Digital Continuity **will act as a “hub” location of orchestration MBSE and MBSE-related services, which would, otherwise, look like “point-to-point” as shown in the diagram below. However, this approach would not allow flexibility, such as any change in the “points” (services, APIs, edge-locations, etc.) would hinder the overall performance and availability of the solution. As a result, every new service or replacement of an existing service (“point”) would be plugged into the **orchestrator**.

![Diagram showing Orchestration and continuity of tools, locations and platforms via Digital Continuity.](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/digital-continuity.png)

 Under the hood, **message broker/event orchestrator** acts as the single source - like a “hub” in the hub-and-spoke architecture. The orchestrator is made of **messaging/queuing** and **translator**.

 Message broker is required to distribute the messages to the recipients or conduct pub/sub relationship in the software and API orchestration. **Amazon Simple Notification Service (Amazon SNS)** and **Amazon Simple Queue Service (SQS)** provides managed serverless messaging and queuing services, respectively, with no-administration required from you. If you would like to employ a managed service but with an open source message broker such as Apache ActiveMQ or RabbitMQ, you can choose **Amazon MQ**. The translator part is required to complete the interoperability piece. Different types of applications and services require different formats.

 Standardization comes with JSON, but effort is needed to build the translator for the digital continuity. You can always work with your AWS Solutions Architect and other resources such as [https://aws.amazon.com/partners/](https://aws.amazon.com/partners/) and [https://aws.amazon.com/professional-services/](https://aws.amazon.com/professional-services/) who can help you on tasks that require hands-on development.

## Extending Workforce Collaboration built on MBSE
<a name="extending-workforce-collaboration-built-on-mbse"></a>

 Even though MBSE is slowly getting adopted by industries, existing engineering practices persist. In other words, engineers and practitioners may resist employing MBSE thoroughly. Of course, one of the reasons for this is the limitations of MBSE on interoperability and flexibility to adapt existing engineering workflows already being practiced and perfected by companies.

 At this point, you can extend the activities as mentioned earlier to stage **engineering workflows**. People from different disciplines and different suppliers can cooperate in micro-level engineering transactions. For example, suppose the team would like to iterate on a design before committing anything to MBSE or PLM. In that case, they can perform local optimizations or “trial-and-errors” by using traditional ways of working.

 Even though there are tools for almost every activity, they are not always used by all engineers, so this is the place where you can bring more macro to micro-level activities. Eventually, this will bring **automation** to repeatable processes, enable **transparency in daily activities**, employing single-source of data resources for those daily outputs **without worrying about cataloging them**.

![Diagram showing Workflow Management built on MBSE](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/workload-management-on-mbse.png)

 The diagram above explains the concept of engineering collaboration based on MBSE. Here, MBSE is treated as the “single source of truth”. Then, the **workflows** are a combination of **automation** and **human workflows**.

 For example, if a team works on an FEA (finite element analysis) operation and asks for a supplier to quickly do a test, they can collaborate over an extension of workflow platform where an MBSE is called when necessary. In this case, the team receives the requirements from the MBSE or simulate the requirements through the MBSE, while performing their optimizations.

 Meanwhile, the interim data (e.g. spreadsheets, presentations and documents) can be stored in an **Artifact Store** (i.e. datalake). The diagram below offers examples of some “artifacts”. AWS Glue Crawler can then catalog these objects (artifacts)** **to form a data catalog that can be accessed via **Amazon Athena**. Technologies such as **Amazon Textract** may be needed if these artifacts include hand-written documents or “pictures” of tables.

 One of the most important contributions to such an approach would be the insights derived from old designs (and the analysis of their strengths and weaknesses). This concept is called “**commonality**” in industries where the common parts and strategies (analysis, simulations included) can be employed by other teams, future projects, and other departments. Thanks to the artifact store working with MBSE ontology, commonality in design can be enhanced.

 For example, a team of structural analysis engineers can query the stress results of an older design to see how they can use the lessons learned from it. The overall workflow can be defined using **AWS Step Functions** or **AWS Managed Apache Airflow**, if open-source is preferred. Please note that you can specify the authorization and authentication in that process if you would like to provide **granular access management and control** to engineers due to confidentiality issues.

![Diagram showing Artifact Store and Artifact Catalog](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/artifact-store-and-catalog.png)

 You can bring almost any workflow in this setting. For example, if the team requires an automatically-deployed HPC cluster to perform the simulation, the deployment can be integrated into this workflow. The results and the operation status can alert the engineering or relevant stakeholders. The human workflow then kicks in and the operation continues like this.

 The overall **visibility** of transactions, statuses and artifacts cataloged during the process can increase the speed of product development.

 Another application would be **auto-document (report) generation stemming from MBSE**. This process can also be automated and can be further enhanced, especially using serverless computing. This can bring more **agile practices** to waterfall types of engineering practices, such as aerospace and automotive industries. Automation also improves the quality of work due to the reduction of human errors in the processes.

 The workflows can bear other AWS technologies and microservices. For example, suppose the team would like to embed an automatic HPC simulation in batches, store the simulation results into an Amazon S3 bucket (Artifact Store) and get cataloging automatically so that they can directly query the results. Here the process can be performed automatically and on-demand.

 Meanwhile, the HPC deployed to perform the simulation can be “dismantled,” and you only pay for the compute time you used. The cataloging part performed by AWS Glue has its serverless step-up that also allows you to pay only the part being used (e.g. x minutes of cataloging).

 The process is automated and** granulated so that you only pay for the activities being used**, and the team **does not spend time on processes that do not create direct value for your business**. The key to success in making such a process happen for you is to embed these scenarios using AWS workflow management tools (e.g. AWS Step Functions, AWS managed Apache Airflow, etc.) and AWS infrastructure stacks (e.g. Cloudformation, Terraform, etc.).

 As discussed in the next section, NLP AI services such as Amazon Textract, Amazon Comprehend, Amazon Translate and Amazon SageMaker AI with Hugging Face algorithms especially provide value in the Artifact Store. You can put your old documents and the afore mentioned AI services will help you to read the content. You can also create your own

 The final part is to bring this monitoring and transparency to engineers and all stakeholders. Since the overall process explained above is based on artifacts (i.e. objects, documents, files, etc.) and metadata (events, messages, etc), visibility would be possible.

 A **mobile application** using **AWS mobile technologies** that is asynchronous with the **activity tracker** on the cloud would enable engineers to go faster. Moreover, if there is an issue happening, **the engineering teams and management can react more quickly to the problems** due to better visibility.

 We mean “**visibility**” here as the **transparency in micro-processes**, for which you would define the details based on your needs. We believe the “devil is in the details” in activities; therefore, we recommend granular visibility. Yet, all of the components explained above are defined by you.

## AI/ML Services for MBSE
<a name="aiml-services-for-mbse"></a>

 MBSE is designed to be at the center of engineering operations. With that in mind, it offers data about products, engineering activities, project activities, requirements, human resources, telemetry data, and more during the months and years of operations. Hence, MBSE and the supporting functions described in the previous sections can provide **unique insights about your products, operations, **and** projects**.

 You can use AWS embedded Analytics such as **Amazon Redshift** and **Amazon Quick** to monitor, observe and receive business intelligence and analytics.

 Machine Learning and AI can deliver even more insights. These are the operational data that can predict delivery dates, possible bottlenecks in the products and projects, and detection of potential defects based on history.
+  **Amazon SageMaker AI** to provide insights about anomaly detection in activities and products, pattern detection, and advanced machine learning applications.
+  **Amazon Forecast** to perform forecasting using historical data. The activities in the MBSE and MBSE-related workloads would build up a historical dataset. This can be used to forecast delivery dates, timelines and estimation of engineering resources.
+  **Amazon Neptune ML **to perform graph-based machine learning on your data ontology. Possible applications include pattern detection in ontology, patterns in design architectures, shortest-path and single-point-of-failure identification in processes.
+  **Amazon Kendra **to extend data reach to the overall enterprise database on the hands of your engineers.
+  **Amazon Lookout for Metric **to get AI-driven insights about metrics (any quantitative data) related to or correlated to each other. This is especially important to identify anomalies, edge case detection and pattern detection, and defects.

 We especially see value in NLP technologies harnessed with data cataloging (such as AWS Glue) to incorporate your legacy documents and build your own semantics.
+  **Amazon Textract **extracts text, handwriting, and data from scanned documents beyond simple optical character recognition (OCR) to identify, understand, and extract data from forms and tables. This is especially useful for scanning old design documents, reports, syntaxed drawings and pdf files, which can be a useful tool for your artifact store.
+  **Amazon Comprehend **provides insight about your text. Amazon Comprehend Custom Entities can be used to create formal semantics and used in ontology.
+  **Amazon Translate **can be used to translate text for 71\+ languages. This service can be harnessed on the top of Amazon Comprehend and Amazon Textract to bring better collaboration in multi-language collaboration environments.

## Shared Services Platform (SSP)
<a name="shared-services-platform-ssp"></a>

 MBSE must have uniform standards to make it secure, compliant, and highly available. A centralized **Shared Service Platform (SSP)**, sometimes also referred to as a **Platform-as-a-Service (PaaS)**, can be used as a self-service interface streamlined for deploying code. You can also use Service Catalog in this section to make a PaaS available to your engineers.

 With SSP, operators will have complete control on defining the standards on security, software delivery, monitoring, and networking related to MBSE and beyond. This allows your development teams to be more productive since they do not need to configure and manage the underlying cloud resources by themselves.

 An SSP is typically built by your central IT team, or through **Cloud Center of Excellence (CCOE)** team or cloud infrastructure team. The SSP is composed of multiple AWS or open source products.

 It typically supports multiple targets for running applications (e.g. Amazon EC2, containers, serverless), CI/CD pipelines, capturing logs/metrics, and security enforcement. The SSP packages these tools into a cohesive whole and makes them available to development teams via a simplified interface(typically a command line interface, graphical user interface or manifest file).
