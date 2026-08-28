---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-support.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Supported regular expression syntax in AWS WAF
<a name="waf-regex-pattern-support"></a>

AWS WAF supports the regular expression pattern syntax used by the PCRE library `libpcre`. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/).

AWS WAF doesn't support all constructs of the library. For example, it supports some zero-width assertions, but not all. We do not have comprehensive list of the constructs that are supported. However, if you provide a regex pattern that isn't valid or use unsupported constructs, the AWS WAF API reports a failure.

AWS WAF does not support the following PCRE patterns:
+ Backreferences and capturing subexpressions
+ Subroutine references and recursive patterns
+ Conditional patterns
+ Backtracking control verbs
+ The \\C single-byte directive
+ The \\R newline match directive
+ The \\K start of match reset directive
+ Callouts and embedded code
+ Atomic grouping and possessive quantifiers

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
