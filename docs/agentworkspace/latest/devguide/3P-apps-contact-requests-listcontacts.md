---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-listcontacts.html
---

# List all contacts for the current agent in Connect Customer agent workspace
<a name="3P-apps-contact-requests-listcontacts"></a>

Lists all contacts for the current agent.

 **Signature**

```
listContacts(): Promise<ListContactsResult>
```

 **Usage**

```
const contacts = await contactClient.listContacts();
console.log(`Active contacts: ${contacts.length}`);
contacts.forEach((contact) => {
    console.log(`Contact ${contact.contactId}: ${contact.type}`);
});
```

 **Output - ListContactsResult**

Returns an array of contact data objects (currently typed as CoreContactData[]).

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
