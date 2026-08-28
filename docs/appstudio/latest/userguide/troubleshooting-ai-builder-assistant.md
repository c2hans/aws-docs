---
source_url: https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-ai-builder-assistant.html
---

# Troubleshooting AI builder assistant and chat
<a name="troubleshooting-ai-builder-assistant"></a>

This topic contains troubleshooting guidance for common issues when using the AI builder assistant.

## Error when creating an app with AI
<a name="troubleshooting-ai-builder-assistant-error-creation"></a>

When using the AI prompt to create an app, the following error may occur:

```
We apologize, but we cannot proceed with your request. The request may contain content that violates our policies and guidelines. Please revise your prompt before trying again.
```

**Problem:** The request is blocked due to potentially harmful content.

**Solution:** Rephrase the prompt and try again.

## App generated using AI is empty app or missing components.
<a name="troubleshooting-ai-builder-assistant-missing"></a>

**Problem:** This can be caused by an unexpected service error.

**Solution:** Retry creating the app using AI, or create the components manually in the generated app.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstudio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
