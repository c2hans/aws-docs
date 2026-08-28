---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/single-thing-provisioning.html
---

# Single thing provisioning
<a name="single-thing-provisioning"></a>

To provision a thing, use the [RegisterThing](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterThing.html) API or the `register-thing` CLI command. The `register-thing` CLI command takes the following arguments:

--template-body
The provisioning template.

--parameters
A list of name-value pairs for the parameters used in the provisioning template, in JSON format (for example, `{"ThingName" : "MyProvisionedThing", "CSR" : "{{csr-text}}"}`).

See [Provisioning templates](provision-template.md).

[RegisterThing](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterThing.html) or `register-thing` returns the ARNs for the resources and the text of the certificate it created:

```
{
    "certificatePem": "{{certificate-text}}",
    "resourceArns": {
    "PolicyLogicalName": "arn:aws:iot:us-west-2:123456789012:policy/2A6577675B7CD1823E271C7AAD8184F44630FFD7",
    "certificate": "arn:aws:iot:us-west-2:123456789012:cert/cd82bb924d4c6ccbb14986dcb4f40f30d892cc6b3ce7ad5008ed6542eea2b049",
    "thing": "arn:aws:iot:us-west-2:123456789012:thing/MyProvisionedThing"
    }
}
```

If a parameter is omitted from the dictionary, the default value is used. If no default value is specified, the parameter is not replaced with a value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
