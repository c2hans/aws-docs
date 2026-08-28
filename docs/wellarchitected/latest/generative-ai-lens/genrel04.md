---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04.html
---

# Prompt management
<a name="genrel04"></a>

| GENREL04: How do you maintain versions for prompts, model parameters, and foundation models? |
| --- |
|   |

 Prompts differentiate model performance from one workload to another. Curating prompts can be a time-consuming process, and it is important to have a reliable store for prompts. Foundation model performance differs from version to version, as does the impact of inference hyperparameters on model performance. Standardize and version these variations to create a more reliable experience.

**Topics**
+ [GENREL04-BP01 Implement a prompt catalog](genrel04-bp01.md)
+ [GENREL04-BP02 Implement a model catalog](genrel04-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
