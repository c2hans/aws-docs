---
source_url: https://docs.aws.amazon.com/workmail/latest/adminguide/enable_interop_ms.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# Configure availability settings in Microsoft Exchange
<a name="enable_interop_ms"></a>

To redirect all calendar free/busy information requests for enabled users to Amazon WorkMail, set up an availability address space in Microsoft Exchange.

Use the following PowerShell command to create the address space:

```
$credentials = Get-Credential
```

At the prompt, enter the credentials of the Amazon WorkMail service account. The username should be entered as **domain\\username** (that is, **{{orgname}}.awsapps.com\\workmail\_service\_account\_{{username}}**. Here, **{{orgname}}** represents the name of the Amazon WorkMail organization. For more information, see [Create service accounts in Microsoft Exchange and Amazon WorkMail](interoperability.md#create-serviceacct).

```
Add-AvailabilityAddressSpace -ForestName {{orgname}}.awsapps.com -AccessMethod OrgWideFB -Credentials $credentials
```

For more information, see [Add-AvailabilityAddressSpace](https://technet.microsoft.com/en-us/library/bb124122.aspx) on Microsoft Docs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
