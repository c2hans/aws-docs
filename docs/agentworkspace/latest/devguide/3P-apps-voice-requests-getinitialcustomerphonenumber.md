---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getinitialcustomerphonenumber.html
---

# Gets the phone number of the initial customer connection in Connect Customer agent workspace
<a name="3P-apps-voice-requests-getinitialcustomerphonenumber"></a>

 Gets the phone number of the initial customer connection. Applicable only for voice contacts.

 **Signature**

```
getInitialCustomerPhoneNumber(contactId: string): Promise<string>
```

 **Usage**

```
const initialCustomerPhoneNumber: string = await voiceClient.getInitialCustomerPhoneNumber(contactId);
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
|  contactId Required  |  string  |  The id of the contact for which the data is requested.  |

 **Permissions required:**

```
Contact.CustomerDetails.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
