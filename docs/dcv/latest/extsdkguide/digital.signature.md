---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/digital.signature.html
---

# Digital signature
<a name="digital.signature"></a>

On Windows, Amazon DCV starts only digitally signed extension executables. There is no digital signature verification on Linux and macOS. Digital signatures are verified using the `WinVerifyTrust` function with the `WINTRUST_ACTION_GENERIC_VERIFY_V2` parameter.

**Important**
During the development, it is possible to disable the verification for testing purposes. It is advisable not to set the following registry key outside of a development environment.

Adding the following registry key will allow DCV to load unsigned extensions executables on the server:

`[HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\extensions] load-policy=all `

![Registry Editor showing the extensions folder with load-policy set to all.](http://docs.aws.amazon.com/dcv/latest/extsdkguide/images/digital-sign.jpg)

To start unsigned extensions on the client, use the following command line parameter:

`--extensions-load-policy="all"`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
