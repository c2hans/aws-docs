---
source_url: https://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/what-is-mbse-and-why-do-industries-start-to-use.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# What is MBSE and why do industries start to use?
<a name="what-is-mbse-and-why-do-industries-start-to-use"></a>

 Today’s multi-disciplinary, multi-supplier, and multi-application/tool product development environment encourages customers to adopt **agile practices** under firm deadlines. Agility is especially important in more traditional engineering environments such as **aerospace**, **energy**, and **automotive** industries, where *waterfall product development* has been long practiced and perfected.

 As these products are highly complex, following a build-based agile iteration is expensive. Moreover, these industries are highly regulated and exceptionally quality-driven. Hence, the agility should not bear "haste creates waste" but should bear technologies that allow data-driven decisions, visibility, traceability, simplicity, and preferably automation to “go fast” while “sticking to highest standards”.

 Complex product development requires inter-disciplinary and inter-supplier/company work. Hence, customers look for ways to be agile in this complex and dynamic environment. At the center of the complexity, we see **Systems Engineering (SE).**

 According to the [INCOSE (International Council on Systems Engineering)](https://www.incose.org/), [Systems Engineering](https://www.incose.org/archived-pages/systems-engineering_old) is *a transdisciplinary and integrative approach to enable the successful realization, use, and retirement of engineered systems, using systems principles and concepts, and scientific, technological, and management methods*.

 The term **system** here is a wide-range definition, including hardware, software, information, processes, people, configurations, supply chains, regulators and geographies. One of the fundamental functions of SE is to conduct the **V**erification and **V**alidation **(V&V)** of the product development and overall lifecycle.

![Diagrams showing Verification and Validation through a product development, MBSE, traditional SE cost and cost of defects to the project](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/verification-and-validation.png)![Diagrams showing Verification and Validation through a product development, MBSE, traditional SE cost and cost of defects to the project](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/cost-vs-time.png)![Diagrams showing Verification and Validation through a product development, MBSE, traditional SE cost and cost of defects to the project](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/mbse-effort-vs-time.png)

(V&V figures are adapted from [Clarus Concept of Operations](https://web.archive.org/web/20090705102848/http:/www.itsdocs.fhwa.dot.gov/jpodocs/repts_te/14158_files/14158.pdf), [Archived on 2009-07-05](https://web.archive.org/web/20090705102900/http:/www.itsdocs.fhwa.dot.gov/jpodocs/repts_te/14158.htm) at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), Publication No. FHWA-JPO-05-072, Federal Highway Administration (FHWA), 2005.)

 Above you can see the stages of a waterfall product development method with the V&V diagram.

 V&V is designed to follow the product development and the product itself in compliance with the **requirements**. Verification asks “are we building the product right?”, while Validation asks “are we building the right product?”.

 V&V helps minimize late defect discovery by engineering and manufacturing functions orchestrated by systems engineering costs more with issue discovery near the end. It is good to know about serious issues sooner, rather than later.

 Traditionally, Systems Engineers follow a **document-based approach**. The challenge is the inability to adapt to changes and complications with collaboration due to a large number of stakeholders and moving parts in the projects that overall slows down the product development process.

![Diagram showing Document Based SE MBSE](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/document-based-se-mbse.png)

 Meanwhile, in the diagram above, you can see on the left side the challenge of a traditional approach.

 It often involves lots of meetings, sharing of documents, emails with attachments, spreadsheets, pdfs and models “flying” between stakeholders in a document-based systems engineering setting. It can also mean that defects are prone to be discovered near the end of the project.

 As we established earlier, late defect discovery costs more. It is far better to become aware of serious issues sooner than later.

 Without this kind of approach, you could end up with multiple “sources of truths” for engineers - creating complications such as conflicting data, using inaccurate data, or late-minute correction of source data. This not only damages product quality, but also delays projects as it slows down overall product development.

 Finally, with the IoT/Industry 4.0 transition in these industries, there are - and will be -more data. The size of data further creates a burden on an already-complicated situation.

 At this triangle of complexity, speed and quality, systems engineers bring the "modeling" to replace documents.  **Model-Based Systems Engineering (MBSE)** handshakes “**behaviors**”, “**requirements**” and “**structures & relationships**” expressed with “**models"**.

 INCOSE describes **MBSE** as “*the formalized application of modeling to support system requirements, design, analysis, verification, and validation activities beginning in the conceptual design phase and continuing throughout development and later life cycle phases.”*

 The **model** here corresponds to an abstracted concept such as a phenomenon, relationship, structure, or system which can be represented graphically, mathematically, or physically.

 The model facilitates concepts to aid decision-making processes by explaining the behaviors and simulating events. Models are low-fidelity *system models*, rather than high-fidelity engineering discipline models such as CAD models, Finite Element Models, etc. We will talk about system models in the “MBSE Under the Hood” section.

 The other component of MBSE is the structures. **Structures** are any information (data or metadata) that exhibits a tree-like representation made of semi-static components. For example, the structures can be abstract concepts such as **Product Variations** and **Configurations,** or it can be as physical as a Bill-of-materials (BOM) or an assembly of components and moving systems such as an engine.

 **Behaviors** define the relationship between structures or the parts inside the structures. The whole validation process in MBSE is automated by low-fidelity simulations like this one. Those bounding parameters are based on **requirements**. The diagram on page 7 shows how structures, behaviors, and requirements are connected under MBSE.

 In this whitepaper, we have incorporated “**people**” into the MBSE framework. This is because the projects adopting MBSE are working in a highly multi-disciplinary environment in multi-stakeholder (internal & external) settings. Since we talk about automation and agility, people/user responsibilities, access and identity management, provided functionalities, work scope, and more are embedded parts of the MBSE workflows.

 The term, “*Model-Based*”, varies by its scope and domain. For example, in software engineering, **Model-Based ‘*Software’* Engineering (MB‘*S’*E)** has its unique features such as **automatic code generation** for system behavior and testing**.** MBSE’s auto code generation feature is especially important for highly regulated and safety critical industries such as aerospace industries.** **

 On the other hand, the ‘model-based’ approach can be extended to a **Model Based Enterprise (or Engineering)** which covers the complete lifecycle of the product, not limited to virtualization but including physical space such as products, manufacturing, and more. MBE will be discussed in the following sections.

 From the public sector perspective, [US DoD 2018 Digital Engineering Strategy](https://www.defense.gov/Newsroom/Releases/Release/Article/1567723/the-department-of-defense-announces-its-digital-engineering-strategy/) can be referenced. That document describes that MBSE is a core enabler of the strategy, whose first of five pillars is *to formalize the development, integration, and use of models to inform enterprise and program decision making*. Hence, AWS customers in complex discrete manufacturing are looking to MBSE to:
+  Reduce time to field capabilities (time-to-market)
+  Improve efficiency and reuse across life cycle phases and programs with digital traceability
+  Enable early risk identification (quality) and cost reduction
+  Leverage data and models as an authoritative source of truth
+  The goal of an integrated digital ecosystem where stakeholders can access the data, functions, and elements needed to work in a purely digital manner

## MBSE under the Hood: SysML, Digital Threads and Ontology
<a name="mbse-under-the-hood-sysml-digital-threads-and-ontology"></a>

 The main purpose of MBSE is to replace documents with reusable models. Therefore, the models should be *system (i.e. discipline, type)* and *platform (i.e. tools, routines) agnostic*. Hence, this creates the complication while connecting these into a common language and schema.

 To do that, MBSE follows **[Unified Modeling Language (UML)](https://www.omg.org/spec/UML/2.5.1/PDF)** standard. Some examples are SysML (see *Flexible Views for View-based Model-driven Development* By Burger, Erik. KIT Scientific Publishing, Nov 14, 2014. Pg. 250), OPM (see Dori, Dov. "Object-process analysis: maintaining the balance between system structure and behaviour." *Journal of Logic and Computation* 5, no. 2 (1995): 227-249), [ARCADIA](https://www.eclipse.org/capella/arcadia.html), and others where the popular is **SysML (System Modeling Language)**. SysML is an extension to UML specialized for SE applications and originally created as open-source. Currently, AWS does not have native SysML libraries. However, you can bring your own library (BYOL) and build SDKs for your needs. AWS Solutions Architects, AWS Partners, and/or AWS Professional Services will help you in every step.

![Diagram showing Harnessing requirements, structures and behaviors with MBSE](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/harnessing-requirements.png)

 The next important concept in MBSE is **Ontology. ** Ontology establishes well-defined domain concepts in terms of the *objects*, *definitions*, and *relationships* inside and among the systems by bringing **formal semantics**. It is especially the case since these are **“systems of systems**” where each system is made of multitude of systems.

 The meaning of the models, not the details but the emergent properties and metadata, needs to be expressed and understandable without calling their subject domain experts. Hence, ontology is a necessary step towards standardization and enabling data interchange which enables *flexibility* and *interoperability*.

 This formalized application of modeling and simulation improves system requirements definition, design, verification and validation, operation, and overall performance.

![A graph model made of different types of objects (nodes) and relations with each has different metadata changing in time (left), a change in the object propagating changes backwards and forwards and new object addition compatibility analysis (right).](http://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/images/graph-model.png)

 The other concept that enables an MBSE model is called **Digital Thread**. The “thread” should be a standardized way to “connect” or “plug” the different types of models into a system of systems model. You may notice the overall features of the MBSE forms a “**graph**” or “network topography” as shown in the diagram above.

 It shows a few examples for the impact of an engineering change in an object or a newly added object and relation.

 In this model, MBSE can simulate the propagation of changes forwards and backwards as well as perform compatibility analysis based on the requirements sets. Hence, MBSE is a key to the **traceability** and **change management** as well as automation to discover defects and issues earlier.

 The other feature of the MBSE is to provide **Integrated (System) Design Environments (ISDEs)** that provides a visual environment for the stakeholders to build, interact and work with system models.

 The above discussion and concepts will be critical to see the benefit of cloud and AWS technologies to enable MBSE and MBSE related technologies as discussed in the following sections.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
