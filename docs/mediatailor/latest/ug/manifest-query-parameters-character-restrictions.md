---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-character-restrictions.html
---

# MediaTailor parameter character restrictions and URL-encoding
<a name="manifest-query-parameters-character-restrictions"></a>

AWS Elemental MediaTailor supports specific characters in manifest query parameters. You can use URL-encoding for special characters.

**Supported characters with URL-encoding**
The following special characters are supported with URL-encoding:
+ period (.) = %2E
+ dash (-) = %2D
+ underscore (\_) = %5F
+ percent (%) = %25
+ tilde (\~) = %7E
+ forward slash (/) = %2F
+ asterisk (\*) = %2A
+ equals (=) = %3D
+ question (?) = %3F

**URL-encoding support**
MediaTailor supports the percent (%) sign when you use it in URL-encoding (for example, hello%20world = hello world). You can use any URL-encoded characters, as long as they are valid URL-encodings according to the HTTP specification.

**Important**
MediaTailor doesn't support double characters such as %%% or ==.

**Security considerations**
MediaTailor implements the following security measures for parameter handling:

1. Input size limitations to prevent database bloat

1. Proper encoding and sanitization of user input

1. URL-encoding of input to prevent response corruption

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
