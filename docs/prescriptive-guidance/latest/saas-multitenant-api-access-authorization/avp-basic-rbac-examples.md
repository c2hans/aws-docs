---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-basic-rbac-examples.html
---

# Example 2: Basic RBAC with Verified Permissions and Cedar
<a name="avp-basic-rbac-examples"></a>

This example uses Verified Permissions and Cedar to demonstrate basic RBAC. As mentioned previously, Cedar's basic construct is an entity. Developers define their own entities and can optionally create relationships between entities. The following example includes three type of entities: `Users`, `Roles`, and `Problems`. `Students` and `Teachers` can be considered entities of the type `Role,` and each `User` can be associated with zero or any of the `Roles`.

![Example of a basic RBAC implementation with Amazon Verified Permissions and Cedar to implement a PDP](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/d46a0b34-79c7-4169-948f-35e16cca934d.png)

In Cedar, these relationships are expressed by linking the `Role` `Student` to the `User` `Bob` as its parent. This association logically groups all the student users in one group. For more information about grouping in Cedar, see the [Cedar documentation](https://docs.cedarpolicy.com/overview/terminology.html#term-group).

The following policy evaluates to the decision `ALLOW` for the action `submitProblem,` for all principals that are linked to the logical group `Students` of the type `Role`.

```
permit (
    principal in ElearningApp::Role::"Students",
    action == ElearningApp::Action::"submitProblem",
    resource
);
```

The following policy evaluates to the decision `ALLOW` for the action `submitProblem` or `answerProblem`, for all principals that are linked to the logical group `Teachers` of the type `Role`.

```
permit (
    principal in ElearningApp::Role::"Teachers",
    action in [
        ElearningApp::Action::"submitProblem",
        ElearningApp::Action::"answerProblem"
    ],
    resource
);
```

In order to evaluate requests with these policies, the evaluation engine needs to know whether the principal referenced within the authorization request is a member of the appropriate group. Therefore, the application has to pass relevant group membership information to the evaluation engine as part of the authorization request. This is done through the `entities` property, which enables you to provide the Cedar evaluation engine with attribute and group membership data for the principal and resource involved in the authorization call. In the following code, group membership is indicated by defining `User::"Bob"` as having a parent called `Role::"Students"`.

```
{
  "policyStoreId": "ELEARNING_POLICYSTOREID",
  "principal": {
    "entityType": "ElearningApp::User",
    "entityId": "Bob"
  },
  "action": {
    "actionType": "ElearningApp::Action",
    "actionId": "answerProblem"
  },
  "resource": {
    "entityType": "ElearningApp::Problem",
    "entityId": "SomeProblem"
  },
  "entities": {
    "entityList": [
        {
            "identifier": {
                "entityType": "ElearningApp::User",
                "entityId": "Bob"
            },
            "attributes": {},
            "parents": [
                {
                    "entityType": "ElearningApp::Role",
                    "entityId": "Students"
                }
            ]
        },
        {
          "identifier": {
            "entityType": "ElearningApp::Problem",
            "entityId": "SomeProblem"
          },
          "attributes": {},
          "parents": []
        }
      ]
  }
}
```

In this example, Bob is the logged in user who makes the `answerProblem` request. Therefore, Bob is the principal and the entity is of the type `User`. The action Bob is trying to perform is `answerProblem`. In order to evaluate if Bob can perform the `answerProblem` action, you need to provide an entity structure that links the entity `User` with a value of `Bob` and assigns his group membership by listing a parent entity as `Role::"Students"`. Because entities in the user group `Role::"Students"` are allowed only to perform the action `submitProblem`, this authorization request evaluates to `DENY`.

On the other hand, if the type `User` that has a value of `Alice` and is a part of the group `Role::"Teachers"`  tries to perform the `answerProblem` action, the authorization request evaluates to `ALLOW`, because the policy dictates that principals in the group `Role::"Teachers"` are allowed to perform the action `answerProblem` on all resources. The following code shows this type of  authorization request that evaluates to `ALLOW`.

```
{
  "policyStoreId": "ELEARNING_POLICYSTOREID",
  "principal": {
    "entityType": "ElearningApp::User",
    "entityId": "Alice"
  },
  "action": {
    "actionType": "ElearningApp::Action",
    "actionId": "answerProblem"
  },
  "resource": {
    "entityType": "ElearningApp::Problem",
    "entityId": "SomeProblem"
  },
  "entities": {
    "entityList": [
        {
            "identifier": {
                "entityType": "ElearningApp::User",
                "entityId": "Alice"
            },
            "attributes": {},
            "parents": [
                {
                    "entityType": "ElearningApp::Role",
                    "entityId": "Teachers"
                }
            ]
        },
        {
            "identifier": {
                "entityType": "ElearningApp::Problem",
                "entityId": "SomeProblem"
            },
            "attributes": {},
            "parents": []
        }
      ]
  }
}
```
