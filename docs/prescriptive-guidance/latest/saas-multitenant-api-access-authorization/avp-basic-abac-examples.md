---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-basic-abac-examples.html
---

# Example 1: Basic ABAC with Verified Permissions and Cedar
<a name="avp-basic-abac-examples"></a>

In this example scenario, Amazon Verified Permissions is used to determine which users are allowed to access information in a fictional Payroll microservice. This section includes Cedar code snippets to demonstrate how you can use Cedar to render access control decisions. These examples aren't intended to provide a full exploration of the capabilities provided by Cedar and Verified Permissions. For a more thorough overview of Cedar, see the [Cedar documentation](https://docs.cedarpolicy.com/).

In the following diagram, we would like to enforce two general business rules that are associated with the `viewSalary` `GET` method: *Employees can view their own salary *and *Employees can view the salary of anyone who reports to them.* You can enforce these business rules by using Verified Permissions policies.

![Example of a basic ABAC implementation with Amazon Verified Permissions and Cedar to implement a PDP](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/28c86fd7-9b79-47f2-adca-32d1fe19c056.png)

 *Employees can view their own salary.*

In Cedar, the basic construct is an *entity*, which represents a principal, action, or a resource. To make an authorization request and start an evaluation with a Verified Permissions policy, you need to provide a *principal,* an *action*, a *resource,* and a* list of entities.*
+ The principal (`principal`) is the logged in user or role.
+ The action (`action`) is the operation that is evaluated by the request.
+ The resource (`resource`) is the component that the action is accessing.
+ The list of entities (`entityList`) contains all the required entities needed to evaluate the request.

To satisfy the business rule *Employees can view their own salary*, you can provide a Verified Permissions policy such as the following.

```
permit (
    principal,
    action == Action::"viewSalary",
    resource
)
when {
    principal == resource.owner
};
```

This policy evaluates to `ALLOW` if the `Action` is `viewSalary` and the resource in the request has an attribute owner that is equal to the principal. For example, if Bob is the logged in user who requested the salary report and is also the owner of the salary report, the policy evaluates to `ALLOW`.

The following authorization request is submitted to Verified Permissions to be evaluated by the sample policy. In this example, Bob is the logged in user who makes the `viewSalary` request. Therefore, Bob is the principal of the entity type `Employee`. The action Bob is trying to perform is `viewSalary,` and the resource that `viewSalary` will display is `Salary-Bob` with the type `Salary`. In order to evaluate if Bob can view the `Salary-Bob` resource, you need to provide an entity structure that links the type `Employee` with a value of `Bob` (the principal) to the owner attribute of the resource that has the type `Salary` . You provide this structure in an `entityList`, where the attributes associated with `Salary` include an owner, which specifies an `entityIdentifier` that contains the type `Employee` and value `Bob`. Verified Permissions compares the `principal` provided in the authorization request to the `owner` attribute that is associated with the `Salary` resource to make a decision.

```
{
  "policyStoreId": "PAYROLLAPP_POLICYSTOREID",
  "principal": {
    "entityType": "PayrollApp::Employee",
    "entityId": "Bob"
  },
  "action": {
    "actionType": "PayrollApp::Action",
    "actionId": "viewSalary"
  },
  "resource": {
    "entityType": "PayrollApp::Salary",
    "entityId": "Salary-Bob"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
          "entityType": "PayrollApp::Salary",
          "entityId": "Salary-Bob"
        },
        "attributes": {
          "owner": {
            "entityIdentifier": {
              "entityType": "PayrollApp::Employee",
              "entityId": "Bob"
            }
          }
        }
      },
      {
        "identifier": {
          "entityType": "PayrollApp::Employee",
          "entityId": "Bob"
        },
        "attributes": {}
      }
    ]
  }
}
```

The authorization request to Verified Permissions returns the following as output, where the attribute `decision` is either `ALLOW` or `DENY`.

```
{
    "determiningPolicies":
        [
            {
                "determiningPolicyId": "PAYROLLAPP_POLICYSTOREID"
            }
        ],
    "decision": "ALLOW",
    "errors": []
}
```

In this case, because Bob was trying to view his own salary, the authorization request sent to Verified Permissions evaluates to `ALLOW`. However, our objective was to use Verified Permissions to enforce two business rules. The business rule that states the following should also be true:

*Employees can view the salary of anyone who reports to them.*

To satisfy this business rule, you can provide another policy. The following policy evaluates to `ALLOW` if the action is `viewSalary` and the resource in the request has an attribute `owner.manager` that is equal to the principal. For example, if Alice is the logged in user who requested the salary report and Alice is the manager of the report's owner, the policy evaluates to `ALLOW`.

```
permit (
    principal,
    action == Action::"viewSalary",
    resource
)
when {
    principal == resource.owner.manager
};
```

The following authorization request is submitted to Verified Permissions to be evaluated by the sample policy. In this example, Alice is the logged in user who makes the `viewSalary` request. Therefore Alice is the principal and the entity is of the type `Employee`. The action Alice is trying to perform is `viewSalary`, and the resource that `viewSalary` will display is of the type `Salary` with a value of `Salary-Bob`. In order to evaluate if Alice can view the `Salary-Bob` resource, you need to provide an entity structure that links the type `Employee` with a value of `Alice` to the `manager` attribute, which must then be associated with the `owner` attribute of the type `Salary` with a value of `Salary-Bob`. You provide this structure in an `entityList`, where the attributes associated with `Salary` include an owner, which specifies an `entityIdentifier` that contains the type `Employee` and value `Bob`. Verified Permissions first checks the `owner` attribute, which evaluates to the type `Employee` and the value `Bob`. Then, Verified Permissions evaluates the `manager` attribute that's associated with `Employee` and compares it to the provided principal to make an authorization decision. In this case, the decision is `ALLOW` because the `principal `and `resource.owner.manager` attributes are equivalent.

```
{
  "policyStoreId": "PAYROLLAPP_POLICYSTOREID",
  "principal": {
    "entityType": "PayrollApp::Employee",
    "entityId": "Alice"
  },
  "action": {
    "actionType": "PayrollApp::Action",
    "actionId": "viewSalary"
  },
  "resource": {
    "entityType": "PayrollApp::Salary",
    "entityId": "Salary-Bob"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
          "entityType": "PayrollApp::Employee",
          "entityId": "Alice"
        },
        "attributes": {
          "manager": {
            "entityIdentifier": {
              "entityType": "PayrollApp::Employee",
              "entityId": "None"
            }
          }
        },
        "parents": []
      },
      {
        "identifier": {
          "entityType": "PayrollApp::Salary",
          "entityId": "Salary-Bob"
        },
        "attributes": {
          "owner": {
            "entityIdentifier": {
              "entityType": "PayrollApp::Employee",
              "entityId": "Bob"
            }
          }
        },
        "parents": []
      },
      {
        "identifier": {
          "entityType": "PayrollApp::Employee",
          "entityId": "Bob"
        },
        "attributes": {
          "manager": {
            "entityIdentifier": {
              "entityType": "PayrollApp::Employee",
              "entityId": "Alice"
            }
          }
        },
       "parents": []
      }
    ]
  }
}
```

So far in this example, we provided the two business rules associated with the `viewSalary` method, *Employees can view their own salary* and *Employees can view the salary of anyone who reports to them*, to Verified Permissions as policies to satisfy the conditions of each business rule independently. You can also use a single Verified Permissions policy to satisfy the conditions of both business rules:

*Employees can view their own salary and the salary of anyone who reports to them.*

When you use the previous authorization request, the following policy evaluates to `ALLOW` if the action is `viewSalary` and the resource in the request has an attribute `owner.manager` that is equal to the `principal`, or an attribute `owner` that is equal to the `principal`.

```
permit (
    principal,
    action == PayrollApp::Action::"viewSalary",
    resource
)
when {
    principal == resource.owner.manager ||
    principal == resource.owner
};
```

For example, if Alice is the logged in user who requests the salary report, and if Alice is either the manager of the owner or the owner of the report, then the policy evaluates to `ALLOW`.

For more information about using logical operators with Cedar policies, see the [Cedar documentation](https://docs.cedarpolicy.com/policies/syntax-operators.html).
