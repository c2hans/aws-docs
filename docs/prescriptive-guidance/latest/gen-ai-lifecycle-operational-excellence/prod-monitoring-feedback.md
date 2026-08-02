---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html
---

# Architecting the production feedback loops
<a name="prod-monitoring-feedback"></a>

Balancing generative AI application autonomy with human oversight is central to good agent design. Generative AI applications should be able to work autonomously because independent operation is what makes it valuable. However, humans should retain control over how they achieve their objectives, especially for high-stake decisions. A foundation of continuous improvement is a well-architected data pipeline that captures and centralizes all forms of user feedback. This feedback is the most valuable source of ground truth data about the application's real-world performance. This section provides several approaches to involve humans in the generative AI application to validate that the agents are working within the defined operational parameters and are safe and reliable.

## User feedback loop
<a name="prod-monitoring-feedback-user"></a>

Teams comprehensively test through robust testing and the use of synthetic events to simulate real-world scenarios. However, it can be difficult to emulate some of real-world behaviors, or certain scenarios might be missed in testing. For an interactive generative AI system, it is recommended that you implement a feedback mechanism that captures user feedback when the application is not functioning as intended. This can be as simple as a binary good or not-good response. It could also be a more comprehensive open-text system where users can provide verbose feedback. The Driving continuous improvement through data and feedback loops section of this guide discusses how to implement a comprehensive feedback strategy that captures explicit and implicit user feedback. The same concepts also apply to the production stage. The following image shows a feedback loop in a production stage.

![Feedback loop for a generative AI application in a production environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/images/guide-img/5b6a3e4a-ff13-48e9-83d7-177629049c97/images/33e7c512-3e4f-48fd-a6b6-77524d1c7a91.png)

The diagram shows the following workflow:

1. The user performs an action in the generative AI application.

1. The generative AI application prompts the user for feedback.

1. The user provides feedback in the form of a thumbs-up or thumbs-down response or in the form of commentary.

1. A human reviewer evaluates the feedback responses.

1. The human reviewer fine-tunes the model and updates the generative AI application.

1. The updated application is deployed to the production environment.

## Human in the loop
<a name="prod-monitoring-feedback-human-in-loop"></a>

Generative AI applications can be non-deterministic. When these applications are making autonomous decisions or actions, they can make incorrect decisions. It's imperative that you design for these failures through the implementation of safety guardrails. One approach to balance the autonomy of the generative AI application is to allow the application to make automated actions only in well-defined and low-risk scenarios. You incorporate a human-in-the-loop mechanism for high-risk or unfamiliar scenarios that are not previously covered in testing scenarios. The following diagram shows how you can include a human in the loop to review high-stakes actions.

![A human in the loop reviewing a high-stakes action for a generative AI application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/images/guide-img/5b6a3e4a-ff13-48e9-83d7-177629049c97/images/401aeca7-6e33-4099-b443-fd86bb2385b7.png)

## Feedback data pipeline and schema
<a name="prod-monitoring-feedback-pipeline"></a>

Collecting feedback is only useful if it is structured and linked to the interaction that generated it. A robust feedback system requires a well-defined data pipeline and a corresponding data schema that makes sure that every piece of feedback can be traced back to its origin.

### The feedback pipeline
<a name="the-feedback-pipeline.955f8e2c-aaed-55b8-a5a8-3f5e1379a9f7"></a>

The architecture should consist of a dedicated, centralized service that ingests all feedback events from the application frontend and backend. This service is responsible for validating the data and storing it in a structured format, such as a data warehouse or a dedicated analytics database.

### Essential data schema
<a name="essential-data-schema.bf385ab2-966a-525f-bde2-491be00da909"></a>

The power of the feedback loop comes from correlating feedback with the full context of the interaction. Therefore, the schema for storing feedback must link each feedback event to the complete application trace. An example schema includes the following fields:
+ `feedback_id` – A unique identifier for the feedback event.
+ `trace_id` – A foreign key that links to the unique ID of the end-to-end application trace. This is the single most important field. It allows retrieval of the exact prompt, retrieved documents, model response, latency, model version, prompt template version, and any tool calls associated with the interaction.
+ `timestamp` – The time the feedback was submitted.
+ `user_id` – An identifier for the user providing the feedback.
+ `feedback_type` – An enum that indicates the source of the feedback, such as `explicit_thumb`, `implicit_copy`, or `explicit_comment`.
+ `feedback_value` – The value of the feedback, such as a 1 for a thumbs up, a 0 for a thumbs down, or a numeric score from 1–5.
+ `feedback_comment` – An optional string for storing free-text user comments.

This structured schema transforms feedback from a collection of isolated opinions into a powerful dataset that you can query for debugging, analysis, and the creation of new evaluation sets.
