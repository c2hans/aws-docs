---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/list-principal-things.html
---

# List things associated with a principal
<a name="list-principal-things"></a>

To list the things associated with the specified principal, run the [`list-principal-things`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-things.htmls) command. Note that this command doesn't list the attachment type between the thing and the certificate. To list the attachment type, use the [`list-principal-things-v2`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-thingsv2.html) command. For more information, see [List things associated with a principal V2](list-principal-things-v2.md).

```
$ aws iot list-principal-things \
    --principal "arn:aws:iot:{{us-east-1:123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}"
```

The output can look like the following.

```
{
    "things": [
        "MyLightBulb1",
        "MyLightBulb2"
    ]
}
```

For more information, see [ListPrincipalThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThings.html) from the *AWS IoT Core API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
