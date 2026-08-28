---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-listdialablecountries.html
---

# Get a list of dialable countries in Connect Customer agent workspace
<a name="3P-apps-voice-requests-listdialablecountries"></a>

 Get a list of `DialableCountry` that contains the country code and calling code that the Connect Customer instance is allowed to make calls to.

 **Signature**

```
listDialableCountries(): Promise<DialableCountry[]>
```

 **Usage**

```
const dialableCountries:DialableCountry[] = await voiceClient.listDialableCountries();
```

 **Output - *DialableCountry***

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  countryCode  |  string  |  The ISO country code  |
|  callingCode  |  string  |  The calling code for the country  |
|  label  |  string  |  The name of the country  |

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
