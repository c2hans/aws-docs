---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-customer-profile-agent.html
---

# Update Customer Profiles permissions for agents
<a name="security-profile-customer-profile-agent"></a>

Assign the following **Customer profiles** permissions as needed to the agent's security profile:
+ **View**: Enables agents to see the Customer profiles application. They can:
  + View profiles that are autopopulated in the agent app.
  + Search for profiles.
  + View details stored in customer profiles (for example, Name, Address).
  + Associate contact records to profiles, as shown in the following image.
![The Customer profiles tab in the agent workspace, the Associate button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-associate.png)
+ **Edit**: Enables agents to edit details in the customer profile (for example, change address). They inherit **View** permissions by default.
+ **Create**: Enables agents to create and save a new profile. They inherit **View** permissions by default, but don't inherit **Edit** permissions.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

By default, the **Admin** security profile already has permissions to perform all Customer profiles activities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
