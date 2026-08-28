---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_PL_reference_conventions.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# PL/pgSQL reference conventions
<a name="c_PL_reference_conventions"></a>

In this section, you can find the conventions that are used to write the syntax for the PL/pgSQL stored procedure language.

| Character  | Description  |
| --- | --- |
| CAPS  | Words in capital letters are keywords.  |
| [ ]  | Brackets denote optional arguments. Multiple arguments in brackets indicate that you can choose any number of the arguments. In addition, arguments in brackets on separate lines indicate that the Amazon Redshift parser expects the arguments to be in the order that they are listed in the syntax. |
| { }  | Braces indicate that you are required to choose one of the arguments inside the braces.  |
| \|  | Pipes indicate that you can choose between the arguments.  |
| {{red italics}}  | Words in red italics indicate placeholders. Insert the appropriate value in place of the word in red italics.  |
| . . .  | An ellipsis indicates that you can repeat the preceding element.  |
| '  | Words in single quotation marks indicate that you must type the quotes.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
