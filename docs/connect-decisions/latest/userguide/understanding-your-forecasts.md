---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/userguide/understanding-your-forecasts.html
---

# Understanding Your Forecasts
<a name="understanding-your-forecasts"></a>

AWS Connect Decisions provides forecast explainability to help you understand why the system generated particular forecasts.

**To understand why a forecast was generated:**

1. Navigate to the chat interface (right panel) in Plans. This is an AI-powered Demand Planning Teammate that can explain how your baseline forecast was calculated and what factors influenced it. You can also use it to edit forecasts or provide feedback to improve future predictions.

1. Ask a specific question: "Why is this final forecast X?"

1. Include the following information in your question:
   + Product name
   + Site name (if applicable)
   + Time range

The system will analyze the forecast and explain key influencing factors:
+ Historical trends and patterns
+ Seasonality effects
+ Pattern changes and anomalies
+ Product lifecycle stages

Use this explanation to validate whether the forecast makes sense based on your business knowledge.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
