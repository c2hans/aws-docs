---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-events-languagechanged-sub.html
---

# Subscribe a callback function when an Connect Customer agent workspace user changes languages
<a name="3P-apps-user-events-languagechanged-sub"></a>

Subscribes a callback function to-be-invoked whenever a user LanguageChanged event occurs in the Connect Customer agent workspace.

 **Signature**

```
onLanguageChanged(handler: UserLanguageChangedHandler)
```

 **Usage**

```
const handler: UserLanguageChangedHandler = async (data: UserLanguageChanged) => {
    console.log("User LanguageChange occurred! " + data);
};

settingsClient.onLanguageChanged(handler);

// UserLanguageChanged Structure
{
  language: string;
  previous: {
    language: string;
  };
}
```

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
