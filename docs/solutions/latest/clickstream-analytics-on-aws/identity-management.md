---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/identity-management.html
---

# Identity Management
<a name="identity-management"></a>

 Clickstream Analytics on AWS supports a built-in Cognito user pool or third-party OpenID Connect (OIDC) for user management based on your [deployment type](deployment.md).

## User management
<a name="user-management"></a>

 If you use built-in Cognito for user management, you can find the [Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) starting with `userPoolDC9497E0` in your deployment Region. When you deploy the web console of the guidance, a user with the required email address will be created as the first user with administrator permission. For more information about user management, refer to [Managing users in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html). You can also follow [Adding user pool sign-in through a third party](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html) to add federated third-party providers, such as SAML and OIDC.

 If you are using an OIDC provider, you need to follow the documentation of the OIDC provider to manage users.

## User roles
<a name="user-roles"></a>

 There are four different types of roles that you can assign to users:

|  **Role**  |  **Description**  |
| --- | --- |
|  Administrator  |  Have full access to the guidance, including identity management  |
|  Operator  |  Manage projects, alarms, and plug-ins  |
|  Analyst  |  View and update in Analytics Studio  |
|  Analyst Reader  |  View in Analytics Studio  |

 The specific features for roles are shown in the following table:

|  **Feature**  |  **Administrator**  |  **Operator**  |  **Analyst**  |  **Analyst Reader**  |
| --- | --- | --- | --- | --- |
|  Project management  |  Read/Write  |  Read/Write  |  Read\*  |  Read\*  |
|  Operation and Alarm  |  Read/Write  |  Read/Write  |  Read\*  |  Read\*  |
|  Plugin Management  |  Read/Write  |  Read/Write  |  Read\*  |  Read\*  |
|  Identity Management  |  Read/Write  |  None  |  None  |  None  |
|  Analytics Studio - Dashboards  |  Read/Write  |  None  |  Read/Write  |  Read  |
|  Analytics Studio - Exploration |  Read/Write  |  None  |  Read/Write  |  Read  |
|  Analytics Studio - Analyses  |  Read/Write  |  None  |  Read/Write  |  None  |
|  Analytics Studio - Data Management  |  Read/Write  |  None  |  Read/Write  |  Read  |

 \* Accessable through the API only

### User role management
<a name="user-roles-management"></a>

 By default, the authenticated users do not have a role in the guidance. You have two options to manage the user roles in the guidance:

**Option 1:**

 Choose **System** - **Users** in the web console of the guidance as Administrator user. Then, add, update, or remove the user roles. This setting has precedence over other settings.

**Option 2:**

 Choose **Setting** in **System** - **Users** in the web console of the guidance as Administrator user. Configure the roles of the guidance mapping to the groups or roles in your OIDC provider.

 By default, the guidance supports mapping [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html) to multiple roles in the guidance with the following rules:

|  **Group name in Cognito**  |  **Solution role**  |
| --- | --- |
|  ClickstreamAdmin  |  Administrator  |
|  ClickstreamOperator  |  Operator  |
|  ClickstreamAnalyst  |  Analyst  |
|  ClickstreamAnalystReader  |  Analyst Reader  |

 For example, you create a group named ClickstreamAnalyst, then add users in the user pool to that group. After those users log in to the guidance, the user has an analyst role to access Analyst Studio.

The guidance supports mapping multiple groups to a single system role, with various group names separated by commas. For example, by modifying the **Operator Role Name**: Group1,Group2, both user groups can be mapped to the **Operator** role of the system.

 If you need to support other OIDC providers, modify **User Role Json Path**.

 **Example**: Modify **User Role Json Path** to $.payload.realm\_access.roles. It can support the mapping of Keycloak roles to solution roles, where the token format of Keycloak is as follows:

```
{
  "exp": 1701070445,
  "iat": 1701063245,
  "auth_time": 1701062050,
  "jti": "4a892061-56e1-4997-a5f3-84a5d38215f0",
  "iss": "https://keycloak.xxxx.cn/auth/realms/xxx",
  "aud": "P****************Y",
  "sub": "29563a2d-****-43bb-b861-c163da7fe984",
  "typ": "ID",
  "azp": "P****************Y",
  "session_state": "4df36df4-****-4e53-9c1a-43e6d27ffbb9",
  "at_hash": "P****************Y",
  "acr": "0",
  "sid": "4df36df4-****-4e53-9c1a-43e6d27ffbb9",
  "email_verified": false,
  "realm_access": {
    "roles": [
      "role1",
      "role2",
      "role3",
    ]
  },
  "preferred_username": "your name",
  "email": "your-name@example.com"
}
```
