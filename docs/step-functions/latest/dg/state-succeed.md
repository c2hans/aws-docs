---
source_url: https://docs.aws.amazon.com/step-functions/latest/dg/state-succeed.html
---

# Succeed workflow state
<a name="state-succeed"></a>

A `Succeed` state (`"Type": "Succeed"`) either terminates a state machine successfully, ends a branch of a [Parallel workflow state](state-parallel.md), or ends an iteration of a [Map workflow state](state-map.md). The `Succeed` state is a useful target for `Choice` state branches that don't do anything except terminate the state machine.

Because `Succeed` states are terminal states, they have no `Next` field, and don't need an `End` field, as shown in the following example.

```
"SuccessState": {
  "Type": "Succeed"
}
```

**`Output` (Optional, JSONata only)**
In addition to the [common state fields](statemachine-structure.md#amazon-states-language-common-fields), `Succeed` states that use JSONata can include an Output field to specify and transform output from the state. When specified, the `Output` value overrides the state output default.
The output field accepts any JSON value (object, array, string, number, boolean, null). Any string value, including those inside objects or arrays, will be evaluated as JSONata if surrounded by `{% %}` characters.
 Output also accepts a JSONata expression directly, for example:

```
"Output" : "{% jsonata expression %}"
```
For more information on JSONata, see [Transforming data with JSONata in Step Functions](transforming-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
