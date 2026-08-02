---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/readiness-assessment-process.html
---

# Readiness assessment process
<a name="readiness-assessment-process"></a>

A readiness assessment consists of these four tasks, spread over two weeks:

1. Schedule the readiness assessment meeting and require attendance.

1. Conduct interviews with key stakeholders or personas for each application suite.

1. Gather information by using the application modernization questionnaire (see the [appendix](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/questionnaire.html)), analyze the gathered information, document observations, and determine next steps.

1. Schedule and conduct a debrief meeting.

The following sections discuss these tasks in more detail.

## Scheduling the readiness assessment meeting
<a name="scheduling-the-readiness-assessment-meeting"></a>

The first step of the readiness assessment process is to schedule the readiness assessment meeting with required attendees. Suggested attendees are:
+ CEO
+ CTO / chief architect
+ CIO
+ Managing director
+ Business unit owners
+ IT finance
+ Security leader
+ Network leader
+ Application development leader
+ Infrastructure leader
+ Operations leader
+ Application owners (for first few applications)

## Conducting interviews
<a name="conducting-interviews"></a>

In this step, you conduct interviews with key stakeholders or personas, starting with a one-hour or two-hour discussion with the executive team. This kick-off meeting starts the whole process, and it is a critical component of the assessment.
+ During the kick-off meeting, understand the organization's business priorities, and identify the set of core applications that should be assessed during the two-week readiness assessment. The goal is to align with business priorities.
+ When business and technology leaders are in alignment with respect to priorities, host a two-day vision workshop to define the details of the modernization strategy, and to drive alignment and executive commitment to resource allocation. The vision workshop has these specific goals:
  + Identify a prioritized short list of critical business outcomes that could be delivered as part of a modernization initiative.
  + Capture current technical capabilities, architectures, and skill sets in relation to the identified business outcomes.
  + Identify key stakeholders (such as a cloud leadership team, cloud business office, and cloud platform engineering team) to participate in critical operating model mechanisms.

The workshop should be led by a modernization program manager, and should include a modernization architect, infrastructure specialist, and data specialist. (Specialist roles may be combined depending on your organization's size and structure.) Executive sponsors might choose to include directors and VPs, but might not delegate full participation to their teams.
+ After the vision workshop, the stakeholders agree on success factors, a methodology, and typical output. This ensures that there is a full understanding of the organization's commitment and focus during the next phase.

## Gathering information
<a name="gathering-information"></a>

In this step, use the application modernization questionnaire (see the [appendix](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/questionnaire.html)) to better understand and assess the current portfolio. You can assess applications through five lenses:
+ Strategic or business fit
+ Functional adequacy
+ Technical adequacy
+ Financial fit
+ Digital readiness

Develop a journey guide so that everyone has a common understanding of the ecosystem, and focus on applications that will be replatformed, refactored, and replaced. Prioritize one or two workloads for modernization, and create a blueprint to modernize those applications.
+ Check prerequisites. Confirm that all prerequisite steps have been completed before you create your blueprint. Prerequisites include confirming the drivers for application modernization, such as code remediation, performance, integration, serviceability, and decision for adoption path (replatform, refactor, or replace).
+ Align assets. Identify which proposed or existing assets are required to support the prioritized workloads.
+ Define iterations and releases. Determine the time blocks (iterations) allocated for the modernization work. Define releases (work to be done) before you change production processes.
+ Identify actions for each area to help your organization get ready for modernization. The key is to ensure a smooth migration experience for the first few applications you are planning to modernize. During this first pass, don't attempt to provide an action plan to solve every aspect of every application. An iterative approach will help maintain quality and security while providing agility and speed.
+ Identify deadlines and owners. For each action, provide a due date and one owner at the minimum. Ideally, you should create and start a project to ensure the timely closing of actions.

## Presenting the results
<a name="presenting-the-results"></a>

Discuss (validate) the findings in a debrief meeting to build a roadmap that outlines the business plans discussed, risk factors identified, and paths for each application. Your analysis and observations might include:
+ Grouping, ranking, and sequencing for applications
+ Target and interim operating models
+ Key technology and regulatory requirements
+ Applications that have extensive data migration requirements
+ The scope and volume of data to be converted

This helps set the right tone for the observations and activities that follow, which help deliver those outcomes. The objective of the debrief session is alignment and agreement on next steps, which will dive deeper into certain areas and start implementing and building momentum.
