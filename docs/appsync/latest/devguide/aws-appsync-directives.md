---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-directives.html
---

# AWS AppSync directives
<a name="aws-appsync-directives"></a>

**Note**
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

AWS AppSync exposes directives to facilitate developer productivity when writing in VTL.

## Directive utils
<a name="utility-helpers-in-directives"></a>

****`#return(Object)`****
The `#return(Object)` allows you to prematurely return from any mapping template. `#return(Object)` is analogous to the *return* keyword in programming languages, as it will return from the closest scoped block of logic. Using `#return(Object)` inside of a resolver mapping template will return from the resolver. Additionally, using `#return(Object)` from a function mapping template will return from the function and will continue the run to either the next function in the pipeline or the resolver response mapping template.

****`#return`****
The `#return` directive exhibits the same behaviors as `#return(Object)`, but `null` will be returned instead.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
