---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/code-project.html
---

# Code your Kotlin project using the SDK for Kotlin
<a name="code-project"></a>

Now the fun begins. As you develop your application, you can refer to the [AWS SDK for Kotlin API Reference](/sdk-for-kotlin/api/latest/index.html) for complete information on the API operations. Use the following links for general Kotlin API information:
+  [Standard library API reference](https://kotlinlang.org/api/latest/jvm/stdlib/)
+  [Coroutines overview](https://kotlinlang.org/docs/coroutines-overview.html)
+  [Coroutines API](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/)

## Log in using the AWS CLI
<a name="code-project-login-cli"></a>

Whenever you run a program that accesses AWS services, you need an active AWS access portal session. You do this by running the following command.

```
aws sso login
```

Since you have a default profile setup, you do not need to call the command with a `--profile` option. If your IAM Identity Center single sign-on configuration uses a named profile, the command is `aws sso login --profile named-profile`.

To test if you already have an active session, run the following AWS CLI command.

```
aws sts get-caller-identity
```

The response to this command should report the IAM Identity Center account and permission set configured in the shared `config` file.
