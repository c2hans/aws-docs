---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/detach-thing-principal.html
---

# Detach a principal from a thing
<a name="detach-thing-principal"></a>

You can use the `DetachThingPrincipal` command to detach a certificate from a thing:

```
$ aws iot detach-thing-principal \
    --thing-name "MyLightBulb" \
    --principal "arn:aws:iot:{{us-east-1:123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}"
```

The **DetachThingPrincipal** command doesn't produce any output.

For more information, see [detach-thing-principal](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachThingPrincipal.html) from the *AWS IoT Core API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
