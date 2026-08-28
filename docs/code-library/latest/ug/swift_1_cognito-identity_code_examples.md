---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/swift_1_cognito-identity_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Cognito Identity examples using SDK for Swift
<a name="swift_1_cognito-identity_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Swift with Amazon Cognito Identity.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateIdentityPool`
<a name="cognito-identity_CreateIdentityPool_swift_1_topic"></a>

The following code example shows how to use `CreateIdentityPool`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/cognito-identity/FindOrCreateIdentityPool#code-examples).

```
import AWSCognitoIdentity

    /// Create a new identity pool and return its ID.
    ///
    /// - Parameters:
    ///     - name: The name to give the new identity pool.
    ///
    /// - Returns: A string containing the newly created pool's ID, or `nil`
    ///   if an error occurred.
    ///
    func createIdentityPool(name: String) async throws -> String? {
        do {
            let cognitoInputCall = CreateIdentityPoolInput(developerProviderName: "com.exampleco.CognitoIdentityDemo",
                                                           identityPoolName: name)

            let result = try await cognitoIdentityClient.createIdentityPool(input: cognitoInputCall)
            guard let poolId = result.identityPoolId else {
                return nil
            }

            return poolId
        } catch {
            print("ERROR: createIdentityPool:", dump(error))
            throw error
        }
    }
```
+  For more information, see [AWS SDK for Swift developer guide](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/getting-started.html).
+  For API details, see [CreateIdentityPool](https://sdk.amazonaws.com/swift/api/awscognitoidentity/latest/documentation/awscognitoidentity/cognitoidentityclient/createidentitypool(input:)) in *AWS SDK for Swift API reference*.

### `DeleteIdentityPool`
<a name="cognito-identity_DeleteIdentityPool_swift_1_topic"></a>

The following code example shows how to use `DeleteIdentityPool`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/cognito-identity/FindOrCreateIdentityPool#code-examples).

```
import AWSCognitoIdentity

    /// Delete the specified identity pool.
    ///
    /// - Parameters:
    ///   - id: The ID of the identity pool to delete.
    ///
    func deleteIdentityPool(id: String) async throws {
        do {
            let input = DeleteIdentityPoolInput(
                identityPoolId: id
            )

            _ = try await cognitoIdentityClient.deleteIdentityPool(input: input)
        } catch {
            print("ERROR: deleteIdentityPool:", dump(error))
            throw error
        }
    }
```
+  For more information, see [AWS SDK for Swift developer guide](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/getting-started.html).
+  For API details, see [DeleteIdentityPool](https://sdk.amazonaws.com/swift/api/awscognitoidentity/latest/documentation/awscognitoidentity/cognitoidentityclient/deleteidentitypool(input:)) in *AWS SDK for Swift API reference*.

### `ListIdentityPools`
<a name="cognito-identity_ListIdentityPools_swift_1_topic"></a>

The following code example shows how to use `ListIdentityPools`.

**SDK for Swift**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/cognito-identity/FindOrCreateIdentityPool#code-examples).

```
import AWSCognitoIdentity

    /// Return the ID of the identity pool with the specified name.
    ///
    /// - Parameters:
    ///   - name: The name of the identity pool whose ID should be returned.
    ///
    /// - Returns: A string containing the ID of the specified identity pool
    ///   or `nil` on error or if not found.
    ///
    func getIdentityPoolID(name: String) async throws -> String? {
        let listPoolsInput = ListIdentityPoolsInput(maxResults: 25)
        // Use "Paginated" to get all the objects.
        // This lets the SDK handle the 'nextToken' field in "ListIdentityPoolsOutput".
        let pages = cognitoIdentityClient.listIdentityPoolsPaginated(input: listPoolsInput)

        do {
            for try await page in pages {
                guard let identityPools = page.identityPools else {
                    print("ERROR: listIdentityPoolsPaginated returned nil contents.")
                    continue
                }

                /// Read pages of identity pools from Cognito until one is found
                /// whose name matches the one specified in the `name` parameter.
                /// Return the matching pool's ID.

                for pool in identityPools {
                    if pool.identityPoolName == name {
                        return pool.identityPoolId!
                    }
                }
            }
        } catch {
            print("ERROR: getIdentityPoolID:", dump(error))
            throw error
        }

        return nil
    }
```
Get the ID of an existing identity pool or create it if it doesn't already exist.

```
import AWSCognitoIdentity

    /// Return the ID of the identity pool with the specified name.
    ///
    /// - Parameters:
    ///   - name: The name of the identity pool whose ID should be returned
    ///
    /// - Returns: A string containing the ID of the specified identity pool.
    ///   Returns `nil` if there's an error or if the pool isn't found.
    ///
    public func getOrCreateIdentityPoolID(name: String) async throws -> String? {
        // See if the pool already exists. If it doesn't, create it.

        do {
            guard let poolId = try await getIdentityPoolID(name: name) else {
                return try await createIdentityPool(name: name)
            }

            return poolId
        } catch {
            print("ERROR: getOrCreateIdentityPoolID:", dump(error))
            throw error
        }
    }
```
+  For more information, see [AWS SDK for Swift developer guide](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/getting-started.html).
+  For API details, see [ListIdentityPools](https://sdk.amazonaws.com/swift/api/awscognitoidentity/latest/documentation/awscognitoidentity/cognitoidentityclient/listidentitypools(input:)) in *AWS SDK for Swift API reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
