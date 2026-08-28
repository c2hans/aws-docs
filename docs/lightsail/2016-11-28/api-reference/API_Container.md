---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Container.html
---

# Container
<a name="API_Container"></a>

Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

## Contents
<a name="API_Container_Contents"></a>

 ** command **   <a name="Lightsail-Type-Container-command"></a>
The launch command for the container.
Type: Array of strings
Required: No

 ** environment **   <a name="Lightsail-Type-Container-environment"></a>
The environment variables of the container.
Type: String to string map
Required: No

 ** image **   <a name="Lightsail-Type-Container-image"></a>
The name of the image used for the container.
Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (`:`). For example, if your container service name is `container-service-1`, the container image label is `mystaticsite`, and you want to use the third (`3`) version of the registered container image, then you should specify `:container-service-1.mystaticsite.3`. To use the latest version of a container image, specify `latest` instead of a version number (for example, `:container-service-1.mystaticsite.latest`). Lightsail will automatically use the highest numbered version of the registered container image.
Container images sourced from a public registry like Docker Hub don't start with a colon. For example, `nginx:latest` or `nginx`.
Type: String
Required: No

 ** ports **   <a name="Lightsail-Type-Container-ports"></a>
The open firewall ports of the container.
Type: String to string map
Valid Values: `HTTP | HTTPS | TCP | UDP`
Required: No

## See Also
<a name="API_Container_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Container)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Container)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Container)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
