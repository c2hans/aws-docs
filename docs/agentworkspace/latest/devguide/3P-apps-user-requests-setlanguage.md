---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-requests-setlanguage.html
---

# Set the language of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-setlanguage"></a>

Sets the language preference for the user that's currently logged in to the Connect Customer agent workspace. The promise resolves once the language change has been persisted, with the resulting language echoed back in the result.

 **Signature**

```
setLanguage(language: Locale): Promise<SetLanguageResult>
```

 **Usage**

```
const result: SetLanguageResult = await settingsClient.setLanguage("en_US");
```

 **Input**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| language Required | Locale | The locale to set for the current user. One of en\_US, de\_DE, es\_ES, fr\_FR, ja\_JP, it\_IT, ko\_KR, pt\_BR, zh\_CN, or zh\_TW. |

 **Output - SetLanguageResult**

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| language | Locale (optional) | The locale that was set, echoed from the request. |

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
