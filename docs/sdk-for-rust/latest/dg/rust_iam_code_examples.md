---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_iam_code_examples.html
---

# IAM examples using SDK for Rust
<a name="rust_iam_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with IAM.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello IAM
<a name="iam_Hello_rust_topic"></a>

The following code example shows how to get started using IAM.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).
From src/bin/hello.rs.

```
use aws_sdk_iam::error::SdkError;
use aws_sdk_iam::operation::list_policies::ListPoliciesError;
use clap::Parser;

const PATH_PREFIX_HELP: &str = "The path prefix for filtering the results.";

#[derive(Debug, clap::Parser)]
#[command(about)]
struct HelloScenarioArgs {
    #[arg(long, default_value="/", help=PATH_PREFIX_HELP)]
    pub path_prefix: String,
}

#[tokio::main]
async fn main() -> Result<(), SdkError<ListPoliciesError>> {
    let sdk_config = aws_config::load_from_env().await;
    let client = aws_sdk_iam::Client::new(&sdk_config);

    let args = HelloScenarioArgs::parse();

    iam_service::list_policies(client, args.path_prefix).await?;

    Ok(())
}
```
From src/iam-service-lib.rs.

```
pub async fn list_policies(
    client: iamClient,
    path_prefix: String,
) -> Result<Vec<String>, SdkError<ListPoliciesError>> {
    let list_policies = client
        .list_policies()
        .path_prefix(path_prefix)
        .scope(PolicyScopeType::Local)
        .into_paginator()
        .items()
        .send()
        .try_collect()
        .await?;

    let policy_names = list_policies
        .into_iter()
        .map(|p| {
            let name = p
                .policy_name
                .unwrap_or_else(|| "Missing Policy Name".to_string());
            println!("{}", name);
            name
        })
        .collect();

    Ok(policy_names)
}
```
+  For API details, see [ListPolicies](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_policies) in *AWS SDK for Rust API reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="iam_Scenario_CreateUserAssumeRole_rust_topic"></a>

The following code example shows how to create a user and assume a role.

**Warning**
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).
+ Create a user with no permissions.
+ Create a role that grants permission to list Amazon S3 buckets for the account.
+ Add a policy to let the user assume the role.
+ Assume the role and list S3 buckets using temporary credentials, then clean up resources.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
use aws_config::meta::region::RegionProviderChain;
use aws_sdk_iam::Error as iamError;
use aws_sdk_iam::{config::Credentials as iamCredentials, config::Region, Client as iamClient};
use aws_sdk_s3::Client as s3Client;
use aws_sdk_sts::Client as stsClient;
use tokio::time::{sleep, Duration};
use uuid::Uuid;

#[tokio::main]
async fn main() -> Result<(), iamError> {
    let (client, uuid, list_all_buckets_policy_document, inline_policy_document) =
        initialize_variables().await;

    if let Err(e) = run_iam_operations(
        client,
        uuid,
        list_all_buckets_policy_document,
        inline_policy_document,
    )
    .await
    {
        println!("{:?}", e);
    };

    Ok(())
}

async fn initialize_variables() -> (iamClient, String, String, String) {
    let region_provider = RegionProviderChain::first_try(Region::new("us-west-2"));

    let shared_config = aws_config::from_env().region(region_provider).load().await;
    let client = iamClient::new(&shared_config);
    let uuid = Uuid::new_v4().to_string();

    let list_all_buckets_policy_document = "{
                \"Version\": \"2012-10-17\",
                \"Statement\": [{
                    \"Effect\": \"Allow\",
                    \"Action\": \"s3:ListAllMyBuckets\",
                    \"Resource\": \"arn:aws:s3:::*\"}]
    }"
    .to_string();
    let inline_policy_document = "{
                \"Version\": \"2012-10-17\",
                \"Statement\": [{
                    \"Effect\": \"Allow\",
                    \"Action\": \"sts:AssumeRole\",
                    \"Resource\": \"{}\"}]
    }"
    .to_string();

    (
        client,
        uuid,
        list_all_buckets_policy_document,
        inline_policy_document,
    )
}

async fn run_iam_operations(
    client: iamClient,
    uuid: String,
    list_all_buckets_policy_document: String,
    inline_policy_document: String,
) -> Result<(), iamError> {
    let user = iam_service::create_user(&client, &format!("{}{}", "iam_demo_user_", uuid)).await?;
    println!("Created the user with the name: {}", user.user_name());
    let key = iam_service::create_access_key(&client, user.user_name()).await?;

    let assume_role_policy_document = "{
        \"Version\": \"2012-10-17\",
                \"Statement\": [{
                    \"Effect\": \"Allow\",
                    \"Principal\": {\"AWS\": \"{}\"},
                    \"Action\": \"sts:AssumeRole\"
                }]
            }"
    .to_string()
    .replace("{}", user.arn());

    let assume_role_role = iam_service::create_role(
        &client,
        &format!("{}{}", "iam_demo_role_", uuid),
        &assume_role_policy_document,
    )
    .await?;
    println!("Created the role with the ARN: {}", assume_role_role.arn());

    let list_all_buckets_policy = iam_service::create_policy(
        &client,
        &format!("{}{}", "iam_demo_policy_", uuid),
        &list_all_buckets_policy_document,
    )
    .await?;
    println!(
        "Created policy: {}",
        list_all_buckets_policy.policy_name.as_ref().unwrap()
    );

    let attach_role_policy_result =
        iam_service::attach_role_policy(&client, &assume_role_role, &list_all_buckets_policy)
            .await?;
    println!(
        "Attached the policy to the role: {:?}",
        attach_role_policy_result
    );

    let inline_policy_name = format!("{}{}", "iam_demo_inline_policy_", uuid);
    let inline_policy_document = inline_policy_document.replace("{}", assume_role_role.arn());
    iam_service::create_user_policy(&client, &user, &inline_policy_name, &inline_policy_document)
        .await?;
    println!("Created inline policy.");

    //First, fail to list the buckets with the user.
    let creds = iamCredentials::from_keys(key.access_key_id(), key.secret_access_key(), None);
    let fail_config = aws_config::from_env()
        .credentials_provider(creds.clone())
        .load()
        .await;
    println!("Fail config: {:?}", fail_config);
    let fail_client: s3Client = s3Client::new(&fail_config);
    match fail_client.list_buckets().send().await {
        Ok(e) => {
            println!("This should not run. {:?}", e);
        }
        Err(e) => {
            println!("Successfully failed with error: {:?}", e)
        }
    }

    let sts_config = aws_config::from_env()
        .credentials_provider(creds.clone())
        .load()
        .await;
    let sts_client: stsClient = stsClient::new(&sts_config);
    sleep(Duration::from_secs(10)).await;
    let assumed_role = sts_client
        .assume_role()
        .role_arn(assume_role_role.arn())
        .role_session_name(format!("iam_demo_assumerole_session_{uuid}"))
        .send()
        .await;
    println!("Assumed role: {:?}", assumed_role);
    sleep(Duration::from_secs(10)).await;

    let assumed_credentials = iamCredentials::from_keys(
        assumed_role
            .as_ref()
            .unwrap()
            .credentials
            .as_ref()
            .unwrap()
            .access_key_id(),
        assumed_role
            .as_ref()
            .unwrap()
            .credentials
            .as_ref()
            .unwrap()
            .secret_access_key(),
        Some(
            assumed_role
                .as_ref()
                .unwrap()
                .credentials
                .as_ref()
                .unwrap()
                .session_token
                .clone(),
        ),
    );

    let succeed_config = aws_config::from_env()
        .credentials_provider(assumed_credentials)
        .load()
        .await;
    println!("succeed config: {:?}", succeed_config);
    let succeed_client: s3Client = s3Client::new(&succeed_config);
    sleep(Duration::from_secs(10)).await;
    match succeed_client.list_buckets().send().await {
        Ok(_) => {
            println!("This should now run successfully.")
        }
        Err(e) => {
            println!("This should not run. {:?}", e);
            panic!()
        }
    }

    //Clean up.
    iam_service::detach_role_policy(
        &client,
        assume_role_role.role_name(),
        list_all_buckets_policy.arn().unwrap_or_default(),
    )
    .await?;
    iam_service::delete_policy(&client, list_all_buckets_policy).await?;
    iam_service::delete_role(&client, &assume_role_role).await?;
    println!("Deleted role {}", assume_role_role.role_name());
    iam_service::delete_access_key(&client, &user, &key).await?;
    println!("Deleted key for {}", key.user_name());
    iam_service::delete_user_policy(&client, &user, &inline_policy_name).await?;
    println!("Deleted inline user policy: {}", inline_policy_name);
    iam_service::delete_user(&client, &user).await?;
    println!("Deleted user {}", user.user_name());

    Ok(())
}
```
+ For API details, see the following topics in *AWS SDK for Rust API reference*.
  + [AttachRolePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.attach_role_policy)
  + [CreateAccessKey](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_access_key)
  + [CreatePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_policy)
  + [CreateRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_role)
  + [CreateUser](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_user)
  + [DeleteAccessKey](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_access_key)
  + [DeletePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_policy)
  + [DeleteRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_role)
  + [DeleteUser](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user)
  + [DeleteUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user_policy)
  + [DetachRolePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.detach_role_policy)
  + [PutUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.put_user_policy)

## Actions
<a name="actions"></a>

### `AttachRolePolicy`
<a name="iam_AttachRolePolicy_rust_topic"></a>

The following code example shows how to use `AttachRolePolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn attach_role_policy(
    client: &iamClient,
    role: &Role,
    policy: &Policy,
) -> Result<AttachRolePolicyOutput, SdkError<AttachRolePolicyError>> {
    client
        .attach_role_policy()
        .role_name(role.role_name())
        .policy_arn(policy.arn().unwrap_or_default())
        .send()
        .await
}
```
+  For API details, see [AttachRolePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.attach_role_policy) in *AWS SDK for Rust API reference*.

### `AttachUserPolicy`
<a name="iam_AttachUserPolicy_rust_topic"></a>

The following code example shows how to use `AttachUserPolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn attach_user_policy(
    client: &iamClient,
    user_name: &str,
    policy_arn: &str,
) -> Result<(), iamError> {
    client
        .attach_user_policy()
        .user_name(user_name)
        .policy_arn(policy_arn)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [AttachUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.attach_user_policy) in *AWS SDK for Rust API reference*.

### `CreateAccessKey`
<a name="iam_CreateAccessKey_rust_topic"></a>

The following code example shows how to use `CreateAccessKey`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn create_access_key(client: &iamClient, user_name: &str) -> Result<AccessKey, iamError> {
    let mut tries: i32 = 0;
    let max_tries: i32 = 10;

    let response: Result<CreateAccessKeyOutput, SdkError<CreateAccessKeyError>> = loop {
        match client.create_access_key().user_name(user_name).send().await {
            Ok(inner_response) => {
                break Ok(inner_response);
            }
            Err(e) => {
                tries += 1;
                if tries > max_tries {
                    break Err(e);
                }
                sleep(Duration::from_secs(2)).await;
            }
        }
    };

    Ok(response.unwrap().access_key.unwrap())
}
```
+  For API details, see [CreateAccessKey](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_access_key) in *AWS SDK for Rust API reference*.

### `CreatePolicy`
<a name="iam_CreatePolicy_rust_topic"></a>

The following code example shows how to use `CreatePolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn create_policy(
    client: &iamClient,
    policy_name: &str,
    policy_document: &str,
) -> Result<Policy, iamError> {
    let policy = client
        .create_policy()
        .policy_name(policy_name)
        .policy_document(policy_document)
        .send()
        .await?;
    Ok(policy.policy.unwrap())
}
```
+  For API details, see [CreatePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_policy) in *AWS SDK for Rust API reference*.

### `CreateRole`
<a name="iam_CreateRole_rust_topic"></a>

The following code example shows how to use `CreateRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn create_role(
    client: &iamClient,
    role_name: &str,
    role_policy_document: &str,
) -> Result<Role, iamError> {
    let response: CreateRoleOutput = loop {
        if let Ok(response) = client
            .create_role()
            .role_name(role_name)
            .assume_role_policy_document(role_policy_document)
            .send()
            .await
        {
            break response;
        }
    };

    Ok(response.role.unwrap())
}
```
+  For API details, see [CreateRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_role) in *AWS SDK for Rust API reference*.

### `CreateServiceLinkedRole`
<a name="iam_CreateServiceLinkedRole_rust_topic"></a>

The following code example shows how to use `CreateServiceLinkedRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn create_service_linked_role(
    client: &iamClient,
    aws_service_name: String,
    custom_suffix: Option<String>,
    description: Option<String>,
) -> Result<CreateServiceLinkedRoleOutput, SdkError<CreateServiceLinkedRoleError>> {
    let response = client
        .create_service_linked_role()
        .aws_service_name(aws_service_name)
        .set_custom_suffix(custom_suffix)
        .set_description(description)
        .send()
        .await?;

    Ok(response)
}
```
+  For API details, see [CreateServiceLinkedRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_service_linked_role) in *AWS SDK for Rust API reference*.

### `CreateUser`
<a name="iam_CreateUser_rust_topic"></a>

The following code example shows how to use `CreateUser`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn create_user(client: &iamClient, user_name: &str) -> Result<User, iamError> {
    let response = client.create_user().user_name(user_name).send().await?;

    Ok(response.user.unwrap())
}
```
+  For API details, see [CreateUser](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.create_user) in *AWS SDK for Rust API reference*.

### `DeleteAccessKey`
<a name="iam_DeleteAccessKey_rust_topic"></a>

The following code example shows how to use `DeleteAccessKey`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_access_key(
    client: &iamClient,
    user: &User,
    key: &AccessKey,
) -> Result<(), iamError> {
    loop {
        match client
            .delete_access_key()
            .user_name(user.user_name())
            .access_key_id(key.access_key_id())
            .send()
            .await
        {
            Ok(_) => {
                break;
            }
            Err(e) => {
                println!("Can't delete the access key: {:?}", e);
                sleep(Duration::from_secs(2)).await;
            }
        }
    }
    Ok(())
}
```
+  For API details, see [DeleteAccessKey](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_access_key) in *AWS SDK for Rust API reference*.

### `DeletePolicy`
<a name="iam_DeletePolicy_rust_topic"></a>

The following code example shows how to use `DeletePolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_policy(client: &iamClient, policy: Policy) -> Result<(), iamError> {
    client
        .delete_policy()
        .policy_arn(policy.arn.unwrap())
        .send()
        .await?;
    Ok(())
}
```
+  For API details, see [DeletePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_policy) in *AWS SDK for Rust API reference*.

### `DeleteRole`
<a name="iam_DeleteRole_rust_topic"></a>

The following code example shows how to use `DeleteRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_role(client: &iamClient, role: &Role) -> Result<(), iamError> {
    let role = role.clone();
    while client
        .delete_role()
        .role_name(role.role_name())
        .send()
        .await
        .is_err()
    {
        sleep(Duration::from_secs(2)).await;
    }
    Ok(())
}
```
+  For API details, see [DeleteRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_role) in *AWS SDK for Rust API reference*.

### `DeleteServiceLinkedRole`
<a name="iam_DeleteServiceLinkedRole_rust_topic"></a>

The following code example shows how to use `DeleteServiceLinkedRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_service_linked_role(
    client: &iamClient,
    role_name: &str,
) -> Result<(), iamError> {
    client
        .delete_service_linked_role()
        .role_name(role_name)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [DeleteServiceLinkedRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_service_linked_role) in *AWS SDK for Rust API reference*.

### `DeleteUser`
<a name="iam_DeleteUser_rust_topic"></a>

The following code example shows how to use `DeleteUser`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_user(client: &iamClient, user: &User) -> Result<(), SdkError<DeleteUserError>> {
    let user = user.clone();
    let mut tries: i32 = 0;
    let max_tries: i32 = 10;

    let response: Result<(), SdkError<DeleteUserError>> = loop {
        match client
            .delete_user()
            .user_name(user.user_name())
            .send()
            .await
        {
            Ok(_) => {
                break Ok(());
            }
            Err(e) => {
                tries += 1;
                if tries > max_tries {
                    break Err(e);
                }
                sleep(Duration::from_secs(2)).await;
            }
        }
    };

    response
}
```
+  For API details, see [DeleteUser](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user) in *AWS SDK for Rust API reference*.

### `DeleteUserPolicy`
<a name="iam_DeleteUserPolicy_rust_topic"></a>

The following code example shows how to use `DeleteUserPolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn delete_user_policy(
    client: &iamClient,
    user: &User,
    policy_name: &str,
) -> Result<(), SdkError<DeleteUserPolicyError>> {
    client
        .delete_user_policy()
        .user_name(user.user_name())
        .policy_name(policy_name)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [DeleteUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.delete_user_policy) in *AWS SDK for Rust API reference*.

### `DetachRolePolicy`
<a name="iam_DetachRolePolicy_rust_topic"></a>

The following code example shows how to use `DetachRolePolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn detach_role_policy(
    client: &iamClient,
    role_name: &str,
    policy_arn: &str,
) -> Result<(), iamError> {
    client
        .detach_role_policy()
        .role_name(role_name)
        .policy_arn(policy_arn)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [DetachRolePolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.detach_role_policy) in *AWS SDK for Rust API reference*.

### `DetachUserPolicy`
<a name="iam_DetachUserPolicy_rust_topic"></a>

The following code example shows how to use `DetachUserPolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn detach_user_policy(
    client: &iamClient,
    user_name: &str,
    policy_arn: &str,
) -> Result<(), iamError> {
    client
        .detach_user_policy()
        .user_name(user_name)
        .policy_arn(policy_arn)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [DetachUserPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.detach_user_policy) in *AWS SDK for Rust API reference*.

### `GetAccountPasswordPolicy`
<a name="iam_GetAccountPasswordPolicy_rust_topic"></a>

The following code example shows how to use `GetAccountPasswordPolicy`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn get_account_password_policy(
    client: &iamClient,
) -> Result<GetAccountPasswordPolicyOutput, SdkError<GetAccountPasswordPolicyError>> {
    let response = client.get_account_password_policy().send().await?;

    Ok(response)
}
```
+  For API details, see [GetAccountPasswordPolicy](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.get_account_password_policy) in *AWS SDK for Rust API reference*.

### `GetRole`
<a name="iam_GetRole_rust_topic"></a>

The following code example shows how to use `GetRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn get_role(
    client: &iamClient,
    role_name: String,
) -> Result<GetRoleOutput, SdkError<GetRoleError>> {
    let response = client.get_role().role_name(role_name).send().await?;
    Ok(response)
}
```
+  For API details, see [GetRole](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.get_role) in *AWS SDK for Rust API reference*.

### `ListAttachedRolePolicies`
<a name="iam_ListAttachedRolePolicies_rust_topic"></a>

The following code example shows how to use `ListAttachedRolePolicies`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_attached_role_policies(
    client: &iamClient,
    role_name: String,
    path_prefix: Option<String>,
    marker: Option<String>,
    max_items: Option<i32>,
) -> Result<ListAttachedRolePoliciesOutput, SdkError<ListAttachedRolePoliciesError>> {
    let response = client
        .list_attached_role_policies()
        .role_name(role_name)
        .set_path_prefix(path_prefix)
        .set_marker(marker)
        .set_max_items(max_items)
        .send()
        .await?;

    Ok(response)
}
```
+  For API details, see [ListAttachedRolePolicies](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_attached_role_policies) in *AWS SDK for Rust API reference*.

### `ListGroups`
<a name="iam_ListGroups_rust_topic"></a>

The following code example shows how to use `ListGroups`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_groups(
    client: &iamClient,
    path_prefix: Option<String>,
    marker: Option<String>,
    max_items: Option<i32>,
) -> Result<ListGroupsOutput, SdkError<ListGroupsError>> {
    let response = client
        .list_groups()
        .set_path_prefix(path_prefix)
        .set_marker(marker)
        .set_max_items(max_items)
        .send()
        .await?;

    Ok(response)
}
```
+  For API details, see [ListGroups](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_groups) in *AWS SDK for Rust API reference*.

### `ListPolicies`
<a name="iam_ListPolicies_rust_topic"></a>

The following code example shows how to use `ListPolicies`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_policies(
    client: iamClient,
    path_prefix: String,
) -> Result<Vec<String>, SdkError<ListPoliciesError>> {
    let list_policies = client
        .list_policies()
        .path_prefix(path_prefix)
        .scope(PolicyScopeType::Local)
        .into_paginator()
        .items()
        .send()
        .try_collect()
        .await?;

    let policy_names = list_policies
        .into_iter()
        .map(|p| {
            let name = p
                .policy_name
                .unwrap_or_else(|| "Missing Policy Name".to_string());
            println!("{}", name);
            name
        })
        .collect();

    Ok(policy_names)
}
```
+  For API details, see [ListPolicies](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_policies) in *AWS SDK for Rust API reference*.

### `ListRolePolicies`
<a name="iam_ListRolePolicies_rust_topic"></a>

The following code example shows how to use `ListRolePolicies`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_role_policies(
    client: &iamClient,
    role_name: &str,
    marker: Option<String>,
    max_items: Option<i32>,
) -> Result<ListRolePoliciesOutput, SdkError<ListRolePoliciesError>> {
    let response = client
        .list_role_policies()
        .role_name(role_name)
        .set_marker(marker)
        .set_max_items(max_items)
        .send()
        .await?;

    Ok(response)
}
```
+  For API details, see [ListRolePolicies](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_role_policies) in *AWS SDK for Rust API reference*.

### `ListRoles`
<a name="iam_ListRoles_rust_topic"></a>

The following code example shows how to use `ListRoles`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_roles(
    client: &iamClient,
    path_prefix: Option<String>,
    marker: Option<String>,
    max_items: Option<i32>,
) -> Result<ListRolesOutput, SdkError<ListRolesError>> {
    let response = client
        .list_roles()
        .set_path_prefix(path_prefix)
        .set_marker(marker)
        .set_max_items(max_items)
        .send()
        .await?;
    Ok(response)
}
```
+  For API details, see [ListRoles](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_roles) in *AWS SDK for Rust API reference*.

### `ListSAMLProviders`
<a name="iam_ListSAMLProviders_rust_topic"></a>

The following code example shows how to use `ListSAMLProviders`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_saml_providers(
    client: &Client,
) -> Result<ListSamlProvidersOutput, SdkError<ListSAMLProvidersError>> {
    let response = client.list_saml_providers().send().await?;

    Ok(response)
}
```
+  For API details, see [ListSAMLProviders](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_saml_providers) in *AWS SDK for Rust API reference*.

### `ListUsers`
<a name="iam_ListUsers_rust_topic"></a>

The following code example shows how to use `ListUsers`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iam#code-examples).

```
pub async fn list_users(
    client: &iamClient,
    path_prefix: Option<String>,
    marker: Option<String>,
    max_items: Option<i32>,
) -> Result<ListUsersOutput, SdkError<ListUsersError>> {
    let response = client
        .list_users()
        .set_path_prefix(path_prefix)
        .set_marker(marker)
        .set_max_items(max_items)
        .send()
        .await?;
    Ok(response)
}
```
+  For API details, see [ListUsers](https://docs.rs/aws-sdk-iam/latest/aws_sdk_iam/client/struct.Client.html#method.list_users) in *AWS SDK for Rust API reference*.
