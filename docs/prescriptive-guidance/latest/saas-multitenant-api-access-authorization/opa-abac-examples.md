---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-abac-examples.html
---

# Example 1: Basic ABAC with OPA and Rego
<a name="opa-abac-examples"></a>

This section describes a scenario where OPA is used to make access decisions about which users are allowed to access information in a fictional Payroll microservice. Rego code snippets are provided to demonstrate how you can use Rego to render access control decisions. These examples are neither exhaustive nor a full exploration of Rego and OPA capabilities. For a more thorough overview of Rego, we recommend that you consult the [Rego documentation](https://www.openpolicyagent.org/docs/latest/#rego) on the OPA website.

![Basic ABAC with OPA and Rego](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/f536805f-7e7a-4fcc-8be6-ae4fc823f9d5.png)

**Basic OPA rules example**

In the previous diagram, one of the access control rules enforced by OPA for the Payroll microservice is:

*Employees can read their own salary.*

If Bob tries to access the Payroll microservice to see his own salary, the Payroll microservice can redirect the API call to the OPA RESTful API to make an access decision. The Payroll service queries OPA for a decision with the following JSON input:

```
{
    "user": "bob",
    "method": "GET",
    "path": ["getSalary", "bob"]
}
```

OPA selects a policy or policies based on the query. In this case, the following policy, which is written in Rego, evaluates the JSON input.

```
default allow = false
allow = true {
    input.method == "GET"
    input.path = ["getSalary", user]
    input.user == user
}
```

This policy denies access by default. It then evaluates the input in the query by binding it to the global variable `input`. The dot operator is used with this variable to access the variable's values. The Rego rule `allow` returns true if the expressions in the rule are also true. The Rego rule verifies that the `method` in the input is equal to GET. It then verifies that the first element in the list `path` is `getSalary` before assigning the second element in the list to the variable `user`*.* Lastly, it checks that the path being accessed is `/getSalary/bob` by checking that the `user` making the request, `input.user`, matches the *user *variable. The rule *allow* applies if-then logic to return a Boolean value, as shown in the output:

```
{
    "allow": true
}
```

**Partial rule using external data**

To demonstrate additional OPA capabilities, you can add requirements to the access rule you are enforcing. Let's assume that you want to enforce this access control requirement in the context of the previous illustration:

*Employees can read the salary of anyone who reports to them.*

In this example, OPA has access to external data that can be imported to help make an access decision:

```
"managers": {
        "bob": ["dave", "john"],
        "carol": ["alice"]
}
```

 You can generate an arbitrary JSON response by creating a partial rule in OPA, which returns a set of values instead of a fixed response. This is an example of a partial rule:

```
direct_report[user_ids] {
    user_ids = data.managers[input.user][_]
}
```

 This rule returns a set of all users that report to the value of *input.user*, which, in this case, is bob. The [\_] construct in the rule is used to iterate over the values of the set. This is the output of the rule:

```
{
    "direct_report": [
      "dave",
      "john"
    ]
}
```

Retrieving this information can help determine whether a user is a direct report of a manager. For some applications, returning dynamic JSON is preferable to returning a simple Boolean response.

**Putting it all together**

The last access requirement is more complex than the first two because it combines the conditions specified in both requirements:

*Employees can read their own salary and the salary of anyone who reports to them.*

To fulfill this requirement, you can use this Rego policy:

```
default allow = false

allow = true {
    input.method == "GET"
    input.path = ["getSalary", user]
    input.user == user
}

allow = true {
    input.method == "GET"
    input.path = ["getSalary", user]
    managers := data.managers[input.user][_]
    contains(managers, user)
}
```

The first rule in the policy allows access for any user who tries to see their own salary information, as discussed previously. Having two rules with the same name, *allow, *functions as a logical **or** operator in Rego. The second rule retrieves the list of all direct reports associated with *input.user *(from the data in the previous diagram) and assigns this list to the *managers* variable. Lastly, the rule checks whether the user who is trying to see their salary is a direct report of *input.user* by verifying that their name is contained in the *managers* variable.

The examples in this section are very basic and do not provide a complete or thorough exploration of the capabilities of Rego and OPA. For more information, review the [OPA documentation](https://www.openpolicyagent.org/docs/latest/), see the [OPA GitHub README](https://github.com/open-policy-agent/opa) file, and experiment in the [Rego playground](https://play.openpolicyagent.org/).
