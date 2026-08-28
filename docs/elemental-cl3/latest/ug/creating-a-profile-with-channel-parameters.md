---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-profile-with-channel-parameters.html
---

# Working with channel parameters in a profile
<a name="creating-a-profile-with-channel-parameters"></a>

You can create an AWS Elemental Live profile in which some fields have values that are variable rather than absolute. Then when you create a channel using that profile, you assign real values to those fields. In AWS Elemental Conductor Live, these variable fields are called *channel parameters*.

Setting up a profile in this way makes the profile more flexible. You can use it with multiple channels simply by entering different values in the channel parameters.

Fields that can be set up with parameters have a blue background in the web interface. For a list of these fields, go to the AWS Elemental User Community and search for *supported channel parameters*. You will definitely need this list if you create profiles using the REST API.

**Topics**
+ [Rules for channel parameters](create-profile-rules.md)
+ [The procedure](create-profile-procedure.md)
+ [Planning ahead for bulk changes](profile-channel-params-plan-ahead.md)
+ [Use case: Using SDI direct input in a profile and channel](using-sdi-direct-input-in-a-profile-and-channel.md)
+ [Use case: Using SDI router input in a profile and channel](using-sdi-router-input-in-a-profile-and-channel.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
