---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/swift_iam_code_examples.html
---

# IAM examples using SDK for Swift
<a name="swift_iam_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Swift with IAM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `AttachRolePolicy`
<a name="iam_AttachRolePolicy_swift_topic"></a>

The following code example shows how to use `AttachRolePolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func attachRolePolicy(role: String, policyArn: String) async throws {
        let input = AttachRolePolicyInput(
            policyArn: policyArn,
            roleName: role
        )
        do {
            _ = try await client.attachRolePolicy(input: input)
        } catch {
            print("ERROR: Attaching a role policy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [AttachRolePolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/attachrolepolicy(input:)) in *AWS SDK for Swift API reference*.

### `CreateAccessKey`
<a name="iam_CreateAccessKey_swift_topic"></a>

The following code example shows how to use `CreateAccessKey`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func createAccessKey(userName: String) async throws -> IAMClientTypes.AccessKey {
        let input = CreateAccessKeyInput(
            userName: userName
        )
        do {
            let output = try await iamClient.createAccessKey(input: input)
            guard let accessKey = output.accessKey else {
                throw ServiceHandlerError.keyError
            }
            return accessKey
        } catch {
            print("ERROR: createAccessKey:", dump(error))
            throw error
        }
    }
```
+  For API details, see [CreateAccessKey](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createaccesskey(input:)) in *AWS SDK for Swift API reference*.

### `CreatePolicy`
<a name="iam_CreatePolicy_swift_topic"></a>

The following code example shows how to use `CreatePolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func createPolicy(name: String, policyDocument: String) async throws -> IAMClientTypes.Policy {
        let input = CreatePolicyInput(
            policyDocument: policyDocument,
            policyName: name
        )
        do {
            let output = try await iamClient.createPolicy(input: input)
            guard let policy = output.policy else {
                throw ServiceHandlerError.noSuchPolicy
            }
            return policy
        } catch {
            print("ERROR: createPolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [CreatePolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createpolicy(input:)) in *AWS SDK for Swift API reference*.

### `CreateRole`
<a name="iam_CreateRole_swift_topic"></a>

The following code example shows how to use `CreateRole`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func createRole(name: String, policyDocument: String) async throws -> String {
        let input = CreateRoleInput(
            assumeRolePolicyDocument: policyDocument,
            roleName: name
        )
        do {
            let output = try await client.createRole(input: input)
            guard let role = output.role else {
                throw ServiceHandlerError.noSuchRole
            }
            guard let id = role.roleId else {
                throw ServiceHandlerError.noSuchRole
            }
            return id
        } catch {
            print("ERROR: createRole:", dump(error))
            throw error
        }
    }
```
+  For API details, see [CreateRole](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createrole(input:)) in *AWS SDK for Swift API reference*.

### `CreateServiceLinkedRole`
<a name="iam_CreateServiceLinkedRole_swift_topic"></a>

The following code example shows how to use `CreateServiceLinkedRole`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func createServiceLinkedRole(service: String, suffix: String? = nil, description: String?)
                    async throws -> IAMClientTypes.Role {
        let input = CreateServiceLinkedRoleInput(
            awsServiceName: service,
            customSuffix: suffix,
            description: description
        )
        do {
            let output = try await client.createServiceLinkedRole(input: input)
            guard let role = output.role else {
                throw ServiceHandlerError.noSuchRole
            }
            return role
        } catch {
            print("ERROR: createServiceLinkedRole:", dump(error))
            throw error
        }
    }
```
+  For API details, see [CreateServiceLinkedRole](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createservicelinkedrole(input:)) in *AWS SDK for Swift API reference*.

### `CreateUser`
<a name="iam_CreateUser_swift_topic"></a>

The following code example shows how to use `CreateUser`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func createUser(name: String) async throws -> String {
        let input = CreateUserInput(
            userName: name
        )
        do {
            let output = try await client.createUser(input: input)
            guard let user = output.user else {
                throw ServiceHandlerError.noSuchUser
            }
            guard let id = user.userId else {
                throw ServiceHandlerError.noSuchUser
            }
            return id
        } catch {
            print("ERROR: createUser:", dump(error))
            throw error
        }
    }
```
+  For API details, see [CreateUser](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/createuser(input:)) in *AWS SDK for Swift API reference*.

### `DeleteAccessKey`
<a name="iam_DeleteAccessKey_swift_topic"></a>

The following code example shows how to use `DeleteAccessKey`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func deleteAccessKey(user: IAMClientTypes.User? = nil,
                                key: IAMClientTypes.AccessKey) async throws
    {
        let userName: String?

        if user != nil {
            userName = user!.userName
        } else {
            userName = nil
        }

        let input = DeleteAccessKeyInput(
            accessKeyId: key.accessKeyId,
            userName: userName
        )
        do {
            _ = try await iamClient.deleteAccessKey(input: input)
        } catch {
            print("ERROR: deleteAccessKey:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DeleteAccessKey](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleteaccesskey(input:)) in *AWS SDK for Swift API reference*.

### `DeletePolicy`
<a name="iam_DeletePolicy_swift_topic"></a>

The following code example shows how to use `DeletePolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func deletePolicy(policy: IAMClientTypes.Policy) async throws {
        let input = DeletePolicyInput(
            policyArn: policy.arn
        )
        do {
            _ = try await iamClient.deletePolicy(input: input)
        } catch {
            print("ERROR: deletePolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DeletePolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deletepolicy(input:)) in *AWS SDK for Swift API reference*.

### `DeleteRole`
<a name="iam_DeleteRole_swift_topic"></a>

The following code example shows how to use `DeleteRole`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func deleteRole(role: IAMClientTypes.Role) async throws {
        let input = DeleteRoleInput(
            roleName: role.roleName
        )
        do {
            _ = try await iamClient.deleteRole(input: input)
        } catch {
            print("ERROR: deleteRole:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DeleteRole](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleterole(input:)) in *AWS SDK for Swift API reference*.

### `DeleteUser`
<a name="iam_DeleteUser_swift_topic"></a>

The following code example shows how to use `DeleteUser`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func deleteUser(user: IAMClientTypes.User) async throws {
        let input = DeleteUserInput(
            userName: user.userName
        )
        do {
            _ = try await iamClient.deleteUser(input: input)
        } catch {
            print("ERROR: deleteUser:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DeleteUser](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleteuser(input:)) in *AWS SDK for Swift API reference*.

### `DeleteUserPolicy`
<a name="iam_DeleteUserPolicy_swift_topic"></a>

The following code example shows how to use `DeleteUserPolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    func deleteUserPolicy(user: IAMClientTypes.User, policyName: String) async throws {
        let input = DeleteUserPolicyInput(
            policyName: policyName,
            userName: user.userName
        )
        do {
            _ = try await iamClient.deleteUserPolicy(input: input)
        } catch {
            print("ERROR: deleteUserPolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DeleteUserPolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/deleteuserpolicy(input:)) in *AWS SDK for Swift API reference*.

### `DetachRolePolicy`
<a name="iam_DetachRolePolicy_swift_topic"></a>

The following code example shows how to use `DetachRolePolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func detachRolePolicy(policy: IAMClientTypes.Policy, role: IAMClientTypes.Role) async throws {
        let input = DetachRolePolicyInput(
            policyArn: policy.arn,
            roleName: role.roleName
        )

        do {
            _ = try await iamClient.detachRolePolicy(input: input)
        } catch {
            print("ERROR: detachRolePolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [DetachRolePolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/detachrolepolicy(input:)) in *AWS SDK for Swift API reference*.

### `GetPolicy`
<a name="iam_GetPolicy_swift_topic"></a>

The following code example shows how to use `GetPolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func getPolicy(arn: String) async throws -> IAMClientTypes.Policy {
        let input = GetPolicyInput(
            policyArn: arn
        )
        do {
            let output = try await client.getPolicy(input: input)
            guard let policy = output.policy else {
                throw ServiceHandlerError.noSuchPolicy
            }
            return policy
        } catch {
            print("ERROR: getPolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [GetPolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/getpolicy(input:)) in *AWS SDK for Swift API reference*.

### `GetRole`
<a name="iam_GetRole_swift_topic"></a>

The following code example shows how to use `GetRole`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func getRole(name: String) async throws -> IAMClientTypes.Role {
        let input = GetRoleInput(
            roleName: name
        )
        do {
            let output = try await client.getRole(input: input)
            guard let role = output.role else {
                throw ServiceHandlerError.noSuchRole
            }
            return role
        } catch {
            print("ERROR: getRole:", dump(error))
            throw error
        }
    }
```
+  For API details, see [GetRole](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/getrole(input:)) in *AWS SDK for Swift API reference*.

### `GetUser`
<a name="iam_GetUser_swift_topic"></a>

The following code example shows how to use `GetUser`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func getUser(name: String? = nil) async throws -> IAMClientTypes.User {
        let input = GetUserInput(
            userName: name
        )
        do {
            let output = try await iamClient.getUser(input: input)
            guard let user = output.user else {
                throw ServiceHandlerError.noSuchUser
            }
            return user
        } catch {
            print("ERROR: getUser:", dump(error))
            throw error
        }
    }
```
+  For API details, see [GetUser](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/getuser(input:)) in *AWS SDK for Swift API reference*.

### `ListAttachedRolePolicies`
<a name="iam_ListAttachedRolePolicies_swift_topic"></a>

The following code example shows how to use `ListAttachedRolePolicies`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    /// Returns a list of AWS Identity and Access Management (IAM) policies
    /// that are attached to the role.
    ///
    /// - Parameter role: The IAM role to return the policy list for.
    ///
    /// - Returns: An array of `IAMClientTypes.AttachedPolicy` objects
    ///   describing each managed policy that's attached to the role.
    public func listAttachedRolePolicies(role: String) async throws -> [IAMClientTypes.AttachedPolicy] {
        var policyList: [IAMClientTypes.AttachedPolicy] = []

        // Use "Paginated" to get all the attached role polices.
        // This lets the SDK handle the 'isTruncated' in "ListAttachedRolePoliciesOutput".
        let input = ListAttachedRolePoliciesInput(
            roleName: role
        )
        let output = client.listAttachedRolePoliciesPaginated(input: input)

        do {
            for try await page in output {
                guard let attachedPolicies = page.attachedPolicies else {
                    print("Error: no attached policies returned.")
                    continue
                }
                for attachedPolicy in attachedPolicies {
                    policyList.append(attachedPolicy)
                }
            }
        } catch {
            print("ERROR: listAttachedRolePolicies:", dump(error))
            throw error
        }

        return policyList
    }
```
+  For API details, see [ListAttachedRolePolicies](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listattachedrolepolicies(input:)) in *AWS SDK for Swift API reference*.

### `ListGroups`
<a name="iam_ListGroups_swift_topic"></a>

The following code example shows how to use `ListGroups`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func listGroups() async throws -> [String] {
        var groupList: [String] = []

        // Use "Paginated" to get all the groups.
        // This lets the SDK handle the 'isTruncated' property in "ListGroupsOutput".
        let input = ListGroupsInput()

        let pages = client.listGroupsPaginated(input: input)
        do {
            for try await page in pages {
                guard let groups = page.groups else {
                    print("Error: no groups returned.")
                    continue
                }

                for group in groups {
                    if let name = group.groupName {
                        groupList.append(name)
                    }
                }
            }
        } catch {
            print("ERROR: listGroups:", dump(error))
            throw error
        }
        return groupList
    }
```
+  For API details, see [ListGroups](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listgroups(input:)) in *AWS SDK for Swift API reference*.

### `ListPolicies`
<a name="iam_ListPolicies_swift_topic"></a>

The following code example shows how to use `ListPolicies`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func listPolicies() async throws -> [MyPolicyRecord] {
        var policyList: [MyPolicyRecord] = []

        // Use "Paginated" to get all the policies.
        // This lets the SDK handle the 'isTruncated' in "ListPoliciesOutput".
        let input = ListPoliciesInput()
        let output = client.listPoliciesPaginated(input: input)

        do {
            for try await page in output {
                guard let policies = page.policies else {
                    print("Error: no policies returned.")
                    continue
                }

                for policy in policies {
                    guard let name = policy.policyName,
                          let id = policy.policyId,
                          let arn = policy.arn
                    else {
                        throw ServiceHandlerError.noSuchPolicy
                    }
                    policyList.append(MyPolicyRecord(name: name, id: id, arn: arn))
                }
            }
        } catch {
            print("ERROR: listPolicies:", dump(error))
            throw error
        }

        return policyList
    }
```
+  For API details, see [ListPolicies](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listpolicies(input:)) in *AWS SDK for Swift API reference*.

### `ListRolePolicies`
<a name="iam_ListRolePolicies_swift_topic"></a>

The following code example shows how to use `ListRolePolicies`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func listRolePolicies(role: String) async throws -> [String] {
        var policyList: [String] = []

        // Use "Paginated" to get all the role policies.
        // This lets the SDK handle the 'isTruncated' in "ListRolePoliciesOutput".
        let input = ListRolePoliciesInput(
            roleName: role
        )
        let pages = client.listRolePoliciesPaginated(input: input)

        do {
            for try await page in pages {
                guard let policies = page.policyNames else {
                    print("Error: no role policies returned.")
                    continue
                }

                for policy in policies {
                    policyList.append(policy)
                }
            }
        } catch {
            print("ERROR: listRolePolicies:", dump(error))
            throw error
        }
        return policyList
    }
```
+  For API details, see [ListRolePolicies](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listrolepolicies(input:)) in *AWS SDK for Swift API reference*.

### `ListRoles`
<a name="iam_ListRoles_swift_topic"></a>

The following code example shows how to use `ListRoles`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func listRoles() async throws -> [String] {
        var roleList: [String] = []

        // Use "Paginated" to get all the roles.
        // This lets the SDK handle the 'isTruncated' in "ListRolesOutput".
        let input = ListRolesInput()
        let pages = client.listRolesPaginated(input: input)

        do {
            for try await page in pages {
                guard let roles = page.roles else {
                    print("Error: no roles returned.")
                    continue
                }

                for role in roles {
                    if let name = role.roleName {
                        roleList.append(name)
                    }
                }
            }
        } catch {
            print("ERROR: listRoles:", dump(error))
            throw error
        }
        return roleList
    }
```
+  For API details, see [ListRoles](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listroles(input:)) in *AWS SDK for Swift API reference*.

### `ListUsers`
<a name="iam_ListUsers_swift_topic"></a>

The following code example shows how to use `ListUsers`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    public func listUsers() async throws -> [MyUserRecord] {
        var userList: [MyUserRecord] = []

        // Use "Paginated" to get all the users.
        // This lets the SDK handle the 'isTruncated' in "ListUsersOutput".
        let input = ListUsersInput()
        let output = client.listUsersPaginated(input: input)

        do {
            for try await page in output {
                guard let users = page.users else {
                    continue
                }
                for user in users {
                    if let id = user.userId, let name = user.userName {
                        userList.append(MyUserRecord(id: id, name: name))
                    }
                }
            }
        }
        catch {
            print("ERROR: listUsers:", dump(error))
            throw error
        }
       return userList
    }
```
+  For API details, see [ListUsers](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/listusers(input:)) in *AWS SDK for Swift API reference*.

### `PutUserPolicy`
<a name="iam_PutUserPolicy_swift_topic"></a>

The following code example shows how to use `PutUserPolicy`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/iam#code-examples).

```
import AWSIAM
import AWSS3

    func putUserPolicy(policyDocument: String, policyName: String, user: IAMClientTypes.User) async throws {
        let input = PutUserPolicyInput(
            policyDocument: policyDocument,
            policyName: policyName,
            userName: user.userName
        )
        do {
            _ = try await iamClient.putUserPolicy(input: input)
        } catch {
            print("ERROR: putUserPolicy:", dump(error))
            throw error
        }
    }
```
+  For API details, see [PutUserPolicy](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient/putuserpolicy(input:)) in *AWS SDK for Swift API reference*.
