---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/ba-endpoints-build-urls.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# Available endpoints for user when building URLs
<a name="ba-endpoints-build-urls"></a>

This topic lists the URLs with root paths for endpoints. Each web application below is defining a **root path**, shared by all endpoints. **Each endpoint then adds its own dedicated path**. The resulting URL to use is the result of the concatenation of the paths. For instance, considering the first endpoint for the Gapwalk application, we have:
+ `/gapwalk-application` for the root web-application path.
+ `/scripts` for the dedicated endpoint path.

The resulting URL to use will be `http://{{server}}:{{port}}/gapwalk-application/scripts`

**server**
points at the server name (the one hosting the given web-application).

**port**
the port exposed by the server.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
