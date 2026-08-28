---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/create-profile-rules.html
---

# Rules for channel parameters
<a name="create-profile-rules"></a>

There are two rules associated with channel parameters in the profile:
+ Generally, if a field is blue on the profile, setting up as a channel parameter is optional. On the profile, you could also enter a permanent value or no value.

  There are two exceptions to this rule: the SDI Direct Input field and the SDI Router Input field must be set up as channel parameters. See [Use case: Using SDI direct input in a profile and channel](using-sdi-direct-input-in-a-profile-and-channel.md) and [Use case: Using SDI router input in a profile and channel](using-sdi-router-input-in-a-profile-and-channel.md).
+ You shouldn't set up non-blue fields with a parameter. If you try to do so, you receive an error when you save the profile.

**Warning**
It is possible to create profiles with parameters in fields that aren't blue. But doing so can cause problems when you create channels from these profiles or when you import profiles after upgrades.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
