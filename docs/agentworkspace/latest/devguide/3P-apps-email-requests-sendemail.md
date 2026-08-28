---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-sendemail.html
---

# Send a draft email contact in Connect Customer agent workspace
<a name="3P-apps-email-requests-sendemail"></a>

Sends both agent initiated and agent reply draft email contacts. Upon successfully sending the email, the contact will transition to ENDED state.

 **Signature**

```
sendEmail(emailContact: DraftEmailContact): Promise<void>
```

 **DraftEmailContact Properties**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| to | EmailAddress[] | An array of destination email addresses; max length supported is 1 |
| emailContent | EmailContent | The content of the email |
| from | EmailAddress | The email contact will be sent from this email address; if no from address is provided in the request, the queue MUST have a default email address specified in the Outbound email configuration |
| cc | EmailAddress[] | Additional recipients to receive a carbon copy of the email; Max length supported is 10 |
| contactId | string | The id of the draft email contact |

 **EmailAddress Properties**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| emailAddress | string | The email address |
| displayName | string | The name that is displayed inside the recipient's mailbox |

 **EmailContent Properties**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| subject | string | The email contact's subject |
| body | string | The body/content of the email, either in plain text or HTML |
| bodyType | "text/plain" \| "text/html" | The body type of the email; can either be "text/plain" or "text/html" |

 **Error Handling**

When sending draft emails, agents may encounter issues. The @amazon-connect/email library provides methods to handle common errors:
+ `isOutboundEmailAddressNotConfiguredError()`: Handle errors when the routing profile's default outbound queue does not have a default outbound email address and the sendEmail() request does not include a from address.
+ `isEmailBodySizeExceededError()`: Handle errors when the size of the email body exceeds the limit.
+ `isTotalEmailSizeExceededError()`: Handle errors when the total size of the email (email body and all attachments) exceeds the limit.

 **Usage**

```
import {
    isOutboundEmailAddressNotConfiguredError,
    isEmailBodySizeExceededError,
    isTotalEmailSizeExceededError,
} from "@amazon-connect/email";

/* ... */

const toEmailAddress = {
  emailAddress: sampleRecipientAddress,
};

const emailContent = {
  subject: "Hello!",
  body: "Thank you!",
  bodyType: "text/plain",
}

const draftContact = {
  to: [toEmailAddress]
  emailContent,
  contactId: draftContactId, // This is the contact ID of the draft contact created via createDraftEmail()
};

try {
  await emailClient.sendEmail(draftContact);
} catch (e) {
  if (isOutboundEmailAddressNotConfiguredError(e)) {
    // Handle error when the routing profile's default outbound queue does not have a default
    // outbound email address and the request to `sendEmail` does not include a `from` address.
  } else if (isEmailBodySizeExceededError(e)) {
    // Handle error when the size of the email body exceeds the limit
  } else if (isTotalEmailSizeExceededError(e)) {
    // Handle error when total size of the email (email body and all attachments) exceeds the limit
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
