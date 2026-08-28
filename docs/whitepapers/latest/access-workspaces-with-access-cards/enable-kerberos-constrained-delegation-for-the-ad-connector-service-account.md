---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/enable-kerberos-constrained-delegation-for-the-ad-connector-service-account.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enable Kerberos Constrained Delegation for the AD Connector Service account
<a name="enable-kerberos-constrained-delegation-for-the-ad-connector-service-account"></a>

 To use smart card authentication with AD Connector, you must enable Kerberos Constrained Delegation (KCD) for the AD Connector Service account to the Lightweight Active Directory Protocol. (LDAP) service in the on-premises AD directory.

 Kerberos Constrained Delegation is a feature in Windows Server. This feature enables administrators to specify and enforce application trust boundaries by limiting the scope where application services can act on a user’s behalf. For more information, see [Kerberos constrained delegation](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_key_concepts_kerberos.html).

1.  Use the `SetSpn` command to set a Service Principal Name (SPN) for the AD Connector service account in the on-premises AD. This enables the service account for delegation configuration. The SPN can be any service or name combination, but not a duplicate of an existing SPN. The `-s` checks for duplicates.

1.  Open an elevated command prompt using “Run as administrator”.

1.  Run this command:

   ```
   setspn -s my/spn service_account
   ```

    The following figure shows the successful result of running of the `SetSpn` command.
![A screenshot of the SetSpn command running successfully.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard7.png)

    *`SetSpn` command running*

1.  In **AD Users and Computers**, right-click on the AD Connector service account and choose **Properties**.

1.  Choose the **Delegation** tab.

1.  Choose the **Trust this user for delegation to specified service only** and **Use any authentication protocol** radio buttons.

1.  Choose **Add**, **Users or Computers**, and then select **Advanced**.

1.  Select **Find Now** to list all available resources, and then find your domain controller (DC) in the list.
![A screenshot with a list of available resources.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/find-domain-controller.png)

1.  Select your domain controller and then choose **OK** to display a list of available services used for delegation.

1.  Choose the LDAP service type that has a description of your forest and select **OK**.

1.  Click **OK** again to save the configuration.

1.  Repeat this process for other domain controllers in AD. Alternatively, you can automate the process using PowerShell.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
