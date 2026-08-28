---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/srgs-sequence.html
---

# Sequences and encapsulation
<a name="srgs-sequence"></a>

The following example shows the supported sequences. For more information, see [Sequences and encapsulation](https://www.w3.org/TR/speech-grammar/#S2.3) in the *Speech recognition grammar specification version 1* W3C recommendation.

**Example**

```
<!-- sequence of tokens -->
this is a test

<!--sequence of rule references-->
<ruleref uri="#action"/> <ruleref uri="#object"/>

<!--sequence of tokens and rule references-->
the <ruleref uri="#object"/> is <ruleref uri="#color"/>

<!-- sequence container -->
<item>fly to <ruleref uri="#city"/> </item>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
