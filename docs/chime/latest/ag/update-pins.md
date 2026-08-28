---
source_url: https://docs.aws.amazon.com/chime/latest/ag/update-pins.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Update user personal PINs
<a name="update-pins"></a>

The following example shows how to reset the personal meeting PIN for a specified Amazon Chime user.

```
ResetPersonalPINRequest request = new ResetPersonalPINRequest()
    .withAccountId("{{chimeAccountId}}")
    .withUserId("{{userId}}");

ResetPersonalPINResult result = chime.resetPersonalPIN(request);

User user = result.getUser();
user.getPersonalPIN()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
