---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/user-journeys.html
---

# User journeys workstream
<a name="user-journeys"></a>

The user journeys workstream also involves decisions that can be changed or reversed with little effort or impact. The emphasis is on starting with a basic build of the user journey and iterating frequently and rapidly to get to the final product. It is rare for the final user journey to look exactly like the first one proposed, so an agile and iterative approach makes sense for this workstream.

The user journeys workstream consists of five phases: discovery, design, build, test, deploy, and post go-live support.

![User journey workstream in contact center migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/4c0ff840-b4b5-4c87-b2d0-f754b61a2bbb.png)

## Discovery
<a name="discovery.81819d70-ac07-5b67-af38-ef789f39c47b"></a>

In this phase, you gather existing user journey flows and designs, and pass them to the contact flow build team. If these do not exist or you want to design a new user journey, gather stakeholders in a workshop and collaboratively develop a user journey framework in a visual capture tool such as the following:
+ Visual canvas tool** **– Use a tool such as Microsoft PowerPoint, Microsoft Visio, or draw.io. Screen-share the canvas to all stakeholders in a workshop. Add blocks and decision points to build an end-to-end user journey, and add placeholders for steps that should be confirmed later (for example, the exact wording or import of a queuing message audio file). Add the name of the owner who should confirm the placeholder.
+ Contact flow designer – Instead of using a drawing tool like draw.io or Visio, consider using the [contact flow designer](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-contact-flows.html#concepts-visual-editor) that's included in Amazon Connect Customer to develop and document the user journey over screen-share. Use [prompt block](https://docs.aws.amazon.com/connect/latest/adminguide/play.html) placeholders for steps that should be confirmed later (for example, the exact wording or import of queuing message audio file). Use a simple [text-to-speech (TTS)](https://docs.aws.amazon.com/connect/latest/adminguide/text-to-speech.html) prompt block to record the owner who is confirming the step (for example, "Queue A message .wav file to be provided by John Smith"). This enables you to perform end-to-end testing of the user journey and routing logic in parallel.

Workshop attendees:
+ Project managers
+ Business and solutions architects
+ Business analysts
+ Service line owner and operator

## Design
<a name="design.336cb0e3-6809-5b6a-972d-4e74bc273520"></a>

Design documentation is optional. It depends on the size and complexity of the contact flow. If you use the contact flow designer, which has an intuitive, easy-to-follow flowchart interface, the journey is self-documented and represents the actual build of the contact flows. This ensures a single source of truth during the rapid and agile development of the user journey. Otherwise, standalone design documents for contact flows must adhere to change control to avoid diverging from the actual build over time.

## Build
<a name="build.20b57d5f-e25f-5f95-8cbd-11fba57c3556"></a>

Connect Customer configuration is available by using [AWS CloudFormation templates and APIs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html) in infrastructure as code (IaC) tools. Use DevOps tools to build and manage Connect Customer components such as security profiles and contact flows. If you design flows by using the contact flow designer, you can include the flows in your IaC DevOps tools and manually export them as JSON files.

**Note**
You can also start building contact flows in a development environment while other AWS accounts are being created, and export the flows into the test and production environments when their Connect Customer instances are ready.

## Test
<a name="test.6fd4a275-3f6a-58b2-8db4-06f2140a453e"></a>

The test phase consists of two sequential subphases:
+ Functional testing – Performed iteratively over agile sprints as contact flows are created in Connect Customer. Performed by: functional test team
+ User acceptance testing (UAT) – Performed only after contact flows have passed functional tests. Performed by: client business users (a dedicated team or users from the service line business unit)

## Deploy
<a name="deploy.1000f732-752f-5a72-b35e-4c6b515a2d51"></a>

In this phase, agent and user credentials are uploaded into the Connect Customer production instance so that users can log in. You should upload contact flows only after they successfully pass UAT testing in the previous phase. Claim a temporary phone number in the Connect Customer dashboard and assign it to the contact flows. These phone numbers will be visible only to the project team, who will use them to place test calls. The project team often runs a selection of UAT scripts during this process. This approach provides preparatory (*pipe-clean*) testing of the user journey before the system goes live and real agents can access the workflow. At the scheduled go-live time, this temporary number is replaced by the publicly routable number used by customers―this is the point where you cut over to the new system. If necessary, you can roll back changes by swapping the number back to the legacy service line.

## Post go-live support (PGLS)
<a name="post-go-live-support--pgls-.525be35a-1667-5a63-b53b-5a23bf9502b5"></a>

The project team remains engaged with the service line stakeholders, the business as usual (BAU) support teams, and end users during the first few weeks after the new contact center goes live. The project team can help users get started on the new system, get involved in troubleshooting live issues alongside the BAU support team, and improve contact flows based on customer and agent feedback.
