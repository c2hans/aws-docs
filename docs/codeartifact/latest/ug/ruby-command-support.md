---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/ruby-command-support.html
---

# RubyGems command support
<a name="ruby-command-support"></a>

CodeArtifact supports the `gem install` and `gem push` commands.

CodeArtifact does not support the following `gem` commands:
+ `gem fetch`
+ `gem info --remote`
+ `gem list --remote`
+ `gem mirror`
+ `gem outdated`
+ `gem owner`
+ `gem query`
+ `gem search`
+ `gem signin`
+ `gem signout`
+ `gem sources --add`
+ `gem sources --update`
+ `gem specification --remote`
+ `gem update`
+ `gem yank`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
