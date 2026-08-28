---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-security.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# Configure security for Gapwalk applications
<a name="ba-runtime-security"></a>

The following topics describe how to secure Gapwalk applications.

It is your responsibility to provide the right configuration to ensure that the use of the AWS Transform for mainframe framework is secure.

All security-related features are disabled by default. To enable authentication (and CSRF,XSS,CSP, and so on), set `gapwalk-application.security` to `enabled` and `gapwalk-application.security.identity` to `oauth`.

**Topics**
+ [Configure URI accessibility for Gapwalk applications](ba-runtime-filteringURIs.md)
+ [Configure authentication for Gapwalk applications](ba-runtime-auth.md)
+ [Configure rate limiting for AWS Transform for mainframe Runtime](ba-runtime-rate-limiting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
