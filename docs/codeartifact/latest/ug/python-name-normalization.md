---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/python-name-normalization.html
---

# Python package name normalization
<a name="python-name-normalization"></a>

CodeArtifact normalizes package names before storing them, which means the package names in CodeArtifact may be different than the name provided when the package was published.

For Python packages, when performing normalization the package name is lowercased and all instances of the characters `.`, `-`, and `_` are replaced with a single `-` character. So the package names `pigeon_cli` and `pigeon.cli` are normalized and stored as `pigeon-cli`. The non-normalized name can be used by pip and twine but the normalized name must be used in CodeArtifact CLI or API requests (such as `list-package-versions`) and in ARNs. For more information about Python package name normalization, see [PEP 503](https://www.python.org/dev/peps/pep-0503/#normalized-names) in the Python documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
