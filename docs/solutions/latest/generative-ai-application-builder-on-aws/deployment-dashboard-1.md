---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deployment-dashboard-1.html
---

# Deployment dashboard
<a name="deployment-dashboard-1"></a>

## API Gateway custom authorizers
<a name="api-gateway-custom-authorizers"></a>

Beneath the surface, Lambda custom authorizers for API Gateway are used for all API calls (both RESTful and WebSocket based) to validate if a given user has permission to perform an action based on the group(s) they belong to. This custom authorizer is backed by a DynamoDB table containing the policies for each group. On invocation of an API, API Gateway invokes the custom authorizer Lambda function, which decodes the provided Amazon Cognito access token to determine which user groups the user belongs to. The policy table is then queried by group name to return the relevant policy for that group.

On every new use case deployment, the admin policy is updated to store a new statement allowing the **execute-api:Invoke** action on that use case’s API. When use cases are deleted, the corresponding statement is removed from the policy.

For the groups created for an individual use case, only a single statement is present in the policy, allowing the **execute-api:Invoke** action on only that use case’s API.

Due to this structure, any user belonging to a use case’s group can access that use case’s API. A single user can also be manually added to multiple groups to allow that user to use multiple use cases.

**Warning**
You can also manually edit the policies for a given group in the policy table if you want to grant access to a new use case to an existing group of users. The use case group is deleted when the use case is deleted (even if you have made manual edits), so proceed with caution when deleting a use case.

In the case where a use case stack is deployed standalone (without the use of the Deployment dashboard), an [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) is created for that deployment containing a single user with access to that use case’s API. This user pool belongs only to this use case and is not shared across other standalone deployments.
