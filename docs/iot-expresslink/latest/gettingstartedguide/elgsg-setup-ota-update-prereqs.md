---
source_url: https://docs.aws.amazon.com/iot-expresslink/latest/gettingstartedguide/elgsg-setup-ota-update-prereqs.html
---

# Prerequisites
<a name="elgsg-setup-ota-update-prereqs"></a>

You must have received a firmware image signed by the manufacturer of your ExpressLink module. Along with the firmware image, you will also have additional signing metadata such as:
+ signature hashing algorithm used (Example: SHA-256)
+ signature encryption algorithm used (Example: ECDSA)
+ actual signature encoded using the base64 encoding format.
+ (Optional) path name (a string) which identifies the location where the certificate is provisioned in the ExpressLink module

Finally, before you proceed, you should create an OTA Update role in your AWS account using the steps outlined in [ Create an OTA Update service role](https://docs.aws.amazon.com/freertos/latest/userguide/create-service-role.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
