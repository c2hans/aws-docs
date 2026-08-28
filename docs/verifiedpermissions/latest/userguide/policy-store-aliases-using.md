---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-store-aliases-using.html
---

# Using Amazon Verified Permissions policy store aliases in API operations
<a name="policy-store-aliases-using"></a>

Any Amazon Verified Permissions operation that accepts a `policyStoreId` parameter, such as [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html), and [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html), can accept a policy store alias name in place of the policy store ID.

**Important**
When you use a policy store alias as the value of a `policyStoreId` parameter, you must include the `policy-store-alias/` prefix. For example, use `policy-store-alias/example-policy-store`, not `example-policy-store`.

## Using Policy store aliases in Operations
<a name="alias-using-operations"></a>

The following `IsAuthorized` command uses a policy store alias with the name `example-policy-store` to identify a policy store.

------
#### [ AWS CLI ]

```
$ aws verifiedpermissions is-authorized \
    --policy-store-id policy-store-alias/example-policy-store \
    --principal entityType=User,entityId=alice \
    --action actionType=Action,actionId=view \
    --resource entityType=Photo,entityId=photo123
```

------

**Note**
You cannot use a policy store alias in place of the `policyStoreId` field for the [DeletePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStore.html) operation.

## Using Policy store aliases Across AWS Regions
<a name="alias-using-multi-region"></a>

One of the most powerful uses of aliases is in applications that run in multiple AWS Regions. For example, you might have a global application that uses different policy stores in each Region.
+ In us-east-1, you want to use `PSEXAMPLEabcdefg111111`.
+ In eu-west-1, you want to use `PSEXAMPLEabcdefg222222`.

You could create a different version of your application in each Region or use a dictionary or switch statement to select the right policy store for each Region. But it's much easier to create a policy store alias with the same policy store alias name in each Region. Remember that the policy store alias name is case-sensitive.

------
#### [ AWS CLI ]

```
$ aws --region us-east-1 verifiedpermissions create-policy-store-alias \
    --alias-name policy-store-alias/my-app \
    --policy-store-id PSEXAMPLEabcdefg111111

$ aws --region eu-west-1 verifiedpermissions create-policy-store-alias \
    --alias-name policy-store-alias/my-app \
    --policy-store-id PSEXAMPLEabcdefg222222
```

------

Then, use the policy store alias in your code. When your code runs in each Region, the policy store alias will refer to its associated policy store in that Region.

------
#### [ AWS CLI ]

```
$ aws verifiedpermissions is-authorized \
    --policy-store-id policy-store-alias/my-app \
    --principal entityType=User,entityId=alice \
    --action actionType=Action,actionId=view \
    --resource entityType=Photo,entityId=photo123
```

------

However, there is a risk that the policy store alias might be deleted. In that case, the application's attempts to use the policy store alias name will fail, and you might need to recreate or update the policy store alias. To mitigate this risk, be cautious about giving principals permission to manage the policy store aliases that you use in your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
