---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ts-faq-dep-conflict-resolution.html
---

# How do I resolve dependency conflicts?
<a name="ts-faq-dep-conflict-resolution"></a>

When you use the AWS SDK for Kotlin, it needs certain AWS and third-party dependencies to work properly. If these dependencies are missing or unexpected versions at runtime, you might see errors like `NoSuchMethodError` or `NoClassDefFoundError`. These dependency issues usually fall into two groups:
+ SDK/Smithy dependency conflicts
+ Third-party dependency conflicts

When you build your Kotlin application, you’ll likely use Gradle to manage dependencies. Adding a dependency on an SDK service client to your project automatically includes all necessary related dependencies. However, if your application has other dependencies, they might clash with those required by the SDK. For example, the SDK relies on OkHttp, a popular HTTP client that your application might also use. To help you spot these conflicts, Gradle offers a handy task the lists your project’s dependencies:

```
./gradlew dependencies
```

When you encounter dependency conflicts, you might need to take action. You can either specify a particular version of a dependency or shadow dependencies into a local namespace. Gradle dependency resolution is a complex topic that is discussed in the following sections of the *Gradle User Manual*:
+  [Understanding dependency resolution](https://docs.gradle.org/current/userguide/dependency_resolution.html)
+  [Dependency constraints and conflict resolution](https://docs.gradle.org/current/userguide/dependency_constraints_conflicts.html)
+  [Aligning dependency versions](https://docs.gradle.org/current/userguide/dependency_version_alignment.html)

## Managing SDK and Smithy dependencies in your project
<a name="sdk-smithy-dep-conflicts"></a>

When you use the SDK, keep in mind that its modules typically depend on other SDK modules with matching version numbers. For example, `aws.sdk.kotlin:s3:1.2.3` depends on a `ws.sdk.kotlin:aws-http:1.2.3`, which depends on `aws.sdk.kotlin:aws-core:1.2.3`, and so on.

The SDK modules also use specific Smithy module versions. While Smithy module versions don’t sync with SDK version numbers, they must match the SDK’s expected version. For example, `aws.sdk.kotlin:s3:1.2.3` might depend on `aws.smithy.kotlin:serde:1.1.1`, which depends on `aws.smithy.kotlin:runtime-core:1.1.1`, and so on.

To avoid dependency conflicts, upgrade all your SDK dependencies together, and do the same for any explicit Smithy dependencies. Consider using our [Gradle version catalog](setup-create-project-file.md) to keep versions in sync and eliminate guesswork in mapping between SDK and Smithy versions.

Remember that minor version updates in SDK/Smithy modules may include breaking changes, as outlined in our [versioning policy](https://github.com/awslabs/aws-sdk-kotlin/blob/main/VERSIONING.md#versioning-policy). When upgrading between minor versions, carefully review changelogs and thoroughly test runtime behavior.

## Resolving OkHttp version conflicts in your application
<a name="okhttp-dep-conflicts"></a>

 [OkHttp](https://square.github.io/okhttp/) is a popular HTTP engine that the SDK uses by default on JVM. Your application might include other dependencies or frameworks that bring in a different OkHttp version. This can cause a `NoClassDefFoundError` for classes in the `okhttp3` namespace, such as `okhttp/coroutines/ExecuteAsyncKt` or `okhttp3/ConnectionListener`. When this happens, you should generally choose the newer version to resolve conflicts. To help you trace the sources of these conflicts, Gradle offers a useful task. You can list all dependencies by running:

```
./gradlew dependencies
```

For instance, if the SDK depends on OkHttp `5.0.0-alpha.14` and another dependency such as Spring Boot depends on OkHttp `4.12.0` then you should use the `5.0.0-alpha.14 version`. You can do this with a `constraints` block in Gradle:

```
dependencies {
    constraints {
        implementation("com.squareup.okhttp3:okhttp:4.12.0")
    }
}
```

Alternatively, if you must use OkHttp 4.x, the SDK provides an [`OkHttp4Engine`](/smithy-kotlin/api/latest/http-client-engine-okhttp4/aws.smithy.kotlin.runtime.http.engine.okhttp4/-ok-http4-engine/index.html). See the [documentation](https://github.com/smithy-lang/smithy-kotlin/tree/main/runtime/protocol/http-client-engines/http-client-engine-okhttp4) for information on how to configure Gradle and use [`OkHttp4Engine`](/smithy-kotlin/api/latest/http-client-engine-okhttp4/aws.smithy.kotlin.runtime.http.engine.okhttp4/-ok-http4-engine/index.html) in your code.
