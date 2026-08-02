---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/modernization-process.html
---

# Modernization process
<a name="modernization-process"></a>

The goal of a phased approach to modernization is to provide incremental value by using modernization dimensions, to apply these to a subset of core, business-differentiating applications, and to accelerate modern technology adoption. The phased approach consists of three steps:

1. Evaluate the maturity of applications by using a modernization diagnostic playbook.  Take a comprehensive approach to adoption, and develop processes that are aligned to intended business outcomes.

1. Start small and prepare to deliver an MVP to gain momentum by driving business results early and incrementally. This phase typically takes 12 to 16 weeks.

1. Create a scalable modernization plan to work in a split-and-seed model.

The following sections discuss these steps in more detail.

## Step 1. Evaluate your applications
<a name="step-1-evaluate-your-applications"></a>

The goals of this phase are:
+ Thoroughly understand your application landscape and prepare your applications for modern data platforms, so you can accelerate the time to value without impacting your business, and then modernize, optimize, and scale.
+ Profile your application landscape to identify the benefits, risks, and costs associated with change.
+ Provide an end-to-end set of services: from strategy and planning; through deployment, migration, and application modernization; to ongoing support.
+ Build policies, recommendations, and controls that provide reusable practices and tools to deliver ongoing business value.

In the evaluation phase, application owners and architects use a modernization diagnostic playbook to validate their modernization goals and priorities.

### Using the modernization diagnostic playbook
<a name="using-the-modernization-diagnostic-playbook.509c24d5-f361-59f6-b1be-e41915ef4c22"></a>

A modernization diagnostic playbook provides a process for determining the value of moving from the current state to the future state for the enterprise. This is inclusive of technology changes that modernization involves.

You use the diagnostic playbook to determine the priority of your application or application  suite for cloud modernization, and to identify the components that need to addressed during modernization.

#### Diagnostic dimensions
<a name="diagnostic-dimensions.175f7f43-7b6a-5d97-99ca-6dfc58318be5"></a>

The modernization diagnostics playbook helps you understand the following dimensions of the current and target (post-migration) state of an application or a group of applications:
+ Application grouping – Is there a reason to group applications (for example, by technology or operating model) for modernization?
+ Sequencing – Is there an order in which applications should be modernized, based on dependencies?
+ Technology – What are the technology categories (for example, middleware, database, messaging)?
+ Dependencies –  Do the applications have key dependencies on other systems or middleware?
+ Environments –  How many  development, testing, and production environments are used?
+ Storage –  What are storage requirements (for example, the number of copies of the test data)?
+ Operating model – Can all components of the application adopt a continuous integration and continuous delivery (CI/CD) pipeline?
  + If so, what infrastructure responsibilities should be distributed to application teams and to whom?
  + If not, what infrastructure responsibilities (for example, patching) should remain with a operations team?
+ Delivery model:
  + Based on the application or group of applications, should you replatform, refactor, rewrite, or replace?
  + Which portion of the modernization should use cloud-native services?
+ Skill sets – What expertise is required? For example:
  + A cloud application background to build applications with a modular architecture by using container and serverless technologies from the ground up.
  + DevOps expertise to develop solutions in the areas of CI/CD processes, infrastructure as code, and automation or application observability by using open-source and AWS tools and services.
+ Modernization approach – Considering the current state of the applications, cloud technology choices, current technical debt, CI/CD, monitoring, skills, and operating model, what is the technical migration work that needs to be done?
+ Modernization timing – What are the business portfolio timing considerations or other planned work considerations that might affect modernization timing?
+ Unit and total cost of infrastructure – What is the annual cost of maintaining your workload on premises vs. on AWS, based on economic analysis?

Evaluating applications against these dimensions help you stay anchored in business, technology, and economics as you drive your modernization to the cloud.

#### Building blocks
<a name="building-blocks.ef6e62fe-6a00-5e26-9090-7e8802c86154"></a>

When you're modernizing applications, you can classify your observations into three building blocks: business agility, organizational agility, and engineering effectiveness.
+ **Business agility **─** **Practices that concern the effectiveness within the business to translate business needs into requirements.  How responsive the delivery organization is to business requests, and how much control the business has in releasing functionality into production environments.
+ **Organizational agility **─ Practices that define delivery processes. Examples include agile methodology and DevOps ceremonies as well as role assignment and clarity, and overall collaboration, communication, and enablement across the organization.
+ **Engineering effectiveness **─ Development practices related to quality assurance, testing, CI/CD, configuration management, application design, and source code management.

### Identifying metrics
<a name="identifying-metrics.57aaadc1-fa5b-5723-921b-c649bbaf5278"></a>

To learn if you are delivering what matters to your customers, you must implement measures that drive improvement and accelerate delivery. Goal, question, metric (GQM) provides an effective framework for ensuring that your measures meet these criteria. Use this framework to work back from your goals by following these steps:
+ Identify the goal or outcome that you are undertaking.
+ Derive the questions that must be answered to determine whether the goal is being met.
+ Decide what should or could be measured to answer the questions adequately. There are two categories of measures:
  + Product metrics, which ensure that you are delivering what matters to your customers.
  + Operational metrics, which ensure that you are improving your software delivery lifecycle.

#### Product metrics
<a name="product-metrics.880498f2-d16f-5371-bdc5-26d033a24bf4"></a>

Product metrics focus on business outcomes and should be established when the return on investment (ROI) for a new scope of work is determined. A useful technique for establishing a product metric is to ask what will change in the business when that new scope of work is implemented. It's helpful to formalize this thinking into the form of a test that focuses on what would be true when a modernization feature is delivered.

For example, if you believe that migrating transactions out of legacy systems will unlock new opportunities to onboard clients, what is the improvement? How much capacity has to be created to onboard the next client? How would a test be constructed to validate that outcome? For this scenario, your product metrics might include the following:
+ Identify the business value test or hypothesis (for example, freeing *x* percent of transaction capacity will onboard *y* percent of new business).
+ Establish the baseline (for example, the current capacity of *x* transactions supports *y* customers).
+ Validate the outcome (for example, you have improved capacity by *x* percent, so can you now onboard *y* percent new business?)

#### Operational metrics
<a name="operational-metrics.8a52e67f-5767-544e-8e33-74c139b85fc9"></a>

To determine whether you are improving your software delivery lifecycle and accelerating your modernization, you must know your lead time and implementation time for delivering software. That is, how quickly can you convert a business need into functionality in production?

Useful operational metrics include:
+ Lead time – How much time does it take for a scope of work to go from request to production?
+ Cycle time – How long does it take to implement a scope of work, from start to finish?
+ Deployment frequency – How often do you deploy changes to production?
+ Time to restore service – How long does it take to recover from failure (measured as the mean time to repair or MTTR)?
+ Change failure rate – What is the mean time between failures (MTBF)?

## Step 2. Start small and build momentum
<a name="step-2-start-small-and-build-momentum"></a>

The goal of this step is to deliver an initial minimal viable product (MVP) to gain momentum. This approach enables you to drive business results early and incrementally.

### Validating priority drivers
<a name="validating-priority-drivers.66dd7417-8105-5535-a70e-43a1e1ef347e"></a>

Before you start the modernization work with application teams, we recommend that you validate the priority drivers that you determined earlier. Follow these steps:

1. Compile the information you need from the diagnostic playbook.
   + Gather the priority drivers and feasibility assessment from the priority applications list.
   + Gather the transition and goal state dispositions for your applications.
   + Identify the application owners, architects, and stakeholders in cloud modernization planning.
   + Solicit information on dependencies or application suite sequencing, if known.
   + Determine how inventory entries relate to dependencies or application suite groupings. Applications might have individual components that are tightly coupled with, or dependent on, other components, and you might want to modernize these components together.

1. Schedule a one-hour or two-hour meeting with the people from step 1 to validate priority drivers.
   + Try to group multiple (up to three or four) applications by solution engineer or architect, and discuss them in one meeting, based on application dependency or application suite information.
   + Determine the roles and expectations for each team member for this upcoming meeting.

1. Conduct the meeting.

### Finalizing details
<a name="finalizing-details.cd820818-6b78-5d88-b05f-0e2d34e5b006"></a>

After you follow the process in the previous section to validate the priority drivers, you can gather the details to determine the modernization approach and timing.

In this phase, the core team works side by side with application teams in short, two-day sprints to design a future state for their applications on the AWS Cloud. Activities include product definition, product discovery, story writing, value stream mapping, and designing CI/CD processes. Here are some ideas:
+ Model each individual component of the application (for example, network configurations, storage configurations, databases, servers, and how the application is deployed on the servers).
+ Deconstruct that model into its different building blocks and configurations by using tools such as containers or serverless technologies.
+ Separate application functionality from any dependencies on underlying infrastructure. Abstract the functions of an application into components that you can move without changing any source code.
+ Tightly integrate with DevOps by using CI/CD tools and mechanisms.

### Building foundational platform services and modernizing applications
<a name="building-foundational-platform-services-and-modernizing-applications.33fd19f9-6d35-5a63-8e56-deeddf700256"></a>

In this 12-week phase, the core team is supported by full-stack teams to deliver the prioritized business use case. This work is carried out by multiple two-pizza teams. For example, a platform engineering team is formed to develop foundational platform services, and a product team is formed to deliver new business outcomes:
+ The platform engineering team configures, integrates, and customizes the AWS services that support the cloud foundation, developer workflow, and data analytics capabilities. Larger and more complex enterprises might have multiple teams supporting each of these capabilities.
+ The product team develops new services and experiences for the business outcomes prioritized in the inception phase. As the product team develops new services, they also modernize core business capabilities.

The platform engineering and product teams deliver a minimal viable product (MVP) that you can evaluate. Upon the success of the initial MVP, you can scale your modernization program by using a split-and-seed approach, whereby new applications are identified and initial team members are split up to create new product teams.

## Step 3. Create a scalable modernization roadmap
<a name="step-3-create-a-scalable-modernization-roadmap"></a>

After the initial MVP release of the prioritized outcomes and applications, we recommend that you develop a roadmap for scaling and accelerating your modernization efforts, improving developer productivity, and innovating rapidly. The core team splits and seeds new teams in order to scale your organization's capabilities and services across multiple engineering teams that are focused on business outcomes. By employing the split-and-seed approach over time, your organization can take on more development and accelerate the velocity of modernization.

The modernization roadmap should outline a pragmatic and continuous approach to application modernization with clearly defined patterns such as event-driven, strangler, domain-driven designs, decomposition, modern database options, and so on.

The roadmap should include a decision tree matrix, as shown in the following diagram, to identify a component of an application and move it to a managed service (such as a database service) with no changes to business logic, or to make code-level changes to improve performance, scalability, manageability, reliability, and resource usage.

![Migration and modernization decisions](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/images/guide-img/69307648-d397-477c-b1c6-ddfde0be4a2f/images/de606299-274f-49cc-9752-46a714f692a7.png)
