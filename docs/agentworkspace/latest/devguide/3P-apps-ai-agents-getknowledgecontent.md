---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-ai-agents-getknowledgecontent.html
---

# Retrieve knowledge article content
<a name="3P-apps-ai-agents-getknowledgecontent"></a>

Retrieves the full content of a knowledge article, including a pre-signed URL for rendering. Use this to display the source content referenced by citations in AI Agent responses.

 **Signature**

```
getKnowledgeContent(params: GetContentParams): Promise<ContentResult>
```

 **Usage**

```
const content = await aiAgentsClient.getKnowledgeContent({
    knowledgeBaseId: "kb-12345",
    contentId: "content-67890"
});

console.log("Title:", content.title);
console.log("URL:", content.url);

// GetContentParams Structure
{
  knowledgeBaseId: string;  // Knowledge base ID or ARN (max 256 characters)
  contentId: string;        // Content ID or ARN (max 256 characters)
}

// ContentResult Structure
{
  contentId: string;
  contentArn: string;
  title?: string;
  contentType?: KnowledgeContentType;
  url?: string;             // Pre-signed URL, re-fetch if expired
  body?: string;            // Populated for text/plain and text/html
}
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
