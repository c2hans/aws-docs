---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credential-caching.html
---

# Credentials caching in the AWS SDK for Java 2.x
<a name="credential-caching"></a>

The AWS SDK for Java 2.x implements credential caching to improve performance and reduce calls to credentials sources. This section explains how credentials caching works and how you can configure it for your applications.

## Understanding credential provider caching
<a name="understanding-credential-provider-caching"></a>

Credential providers in the SDK for Java 2.x use different caching strategies:
+ **Internal credential caching**: Many providers cache credentials that they retrieve.
+ **Automatic refresh**: Providers with cached credentials implement refresh mechanisms.

### Providers with internal credentials caching
<a name="providers-with-internal-caching"></a>

The following credentials providers cache credentials internally, even when you create new instances:
+ **Instance profile credentials provider**: Caches credentials from the Amazon EC2 metadata service.
+ **Container credentials provider**: Caches credentials from the container metadata endpoint.
+ **STS-based providers**: Cache temporary credentials from AWS Security Token Service (STS).
+ **Web identity token providers**: Cache credentials obtained from web identity tokens.
+ **Process credentials provider**: Caches credentials from external processes.

### Providers without internal caching
<a name="providers-without-caching"></a>

The following providers don't implement internal caching:
+ **Environment Variable Credentials Provider**
+ **System Property Credentials Provider**
+ **Static Credentials Provider**

## Configuring credential caching
<a name="configuring-credential-caching"></a>

You can customize caching behavior when building credential providers:

### Stale Time
<a name="stale-time"></a>

Controls when credentials are considered stale and need refreshing:

```
.staleTime(Duration.ofMinutes(2))  // Consider stale 2 minutes before expiration.
```

### Prefetch Time
<a name="prefetch-time"></a>

Determines when to start refreshing credentials before they expire:

```
.prefetchTime(Duration.ofMinutes(10))  // Start refresh 10 minutes before expiration.
```

### Asynchronous Updates
<a name="async-updates"></a>

Enables background credential refreshing:

```
.asyncCredentialUpdateEnabled(true)  // Refresh credentials in background thread.
```

### Session Duration
<a name="session-duration"></a>

For STS-based providers, controls how long temporary credentials remain valid:

```
.refreshRequest(r -> r.durationSeconds(3600))  // 1 hour session.
```

## Caching credentials configuration example
<a name="example-optimized-sts-config"></a>

As an example of configuring caching for a credentials provider implementation, you might want to have the SDK use a background thread to pre-fetch (retrieve in advance) credentials before they expire. That way you can avoid the blocking call that retrieves fresh credentials.

The following shows an example that creates an `[StsAssumeRoleCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sts/auth/StsAssumeRoleCredentialsProvider.html)` that uses a background thread to pre-fetch credentials by setting the `[asyncCredentialUpdateEnabled](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sts/auth/StsCredentialsProvider.BaseBuilder.html#asyncCredentialUpdateEnabled(java.lang.Boolean))` property to `true` on the builder:

```
StsAssumeRoleCredentialsProvider provider = StsAssumeRoleCredentialsProvider.builder()
    .refreshRequest(r -> r
        .roleArn("arn:aws:iam::111122223333:role/example-role")
        .roleSessionName("example-session")
        .durationSeconds(3600))  // 1 hour session
    .staleTime(Duration.ofMinutes(5))  // Consider stale 5 minutes before expiration
    .prefetchTime(Duration.ofMinutes(10))  // Start refresh 10 minutes before expiration
    .asyncCredentialUpdateEnabled(true)  // Refresh in background
    .build();

S3Client s3 = S3Client.builder()
    .credentialsProvider(provider)
    .build();
```

When you invoke an operation on `s3Client` for the first time, an `[AssumeRoleRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sts/model/AssumeRoleRequest.html)` is sent to the AWS Security Token Service (STS). STS returns temporary credentials that are valid for 15 minutes (900 seconds). The `s3Client` instance uses the cached credentials until it's time to refresh them before the 15 minutes elapse. By default, the SDK attempts to retrieve new credentials for a new session between 5 minutes and 1 minute before the expiration time of the current session. The pre-fetch window is configurable by using the `[prefetchTime](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sts/auth/StsCredentialsProvider.BaseBuilder.html#prefetchTime(java.time.Duration))` and `[staleTime](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sts/auth/StsCredentialsProvider.BaseBuilder.html#staleTime(java.time.Duration))` properties.

You can configure the following session-based credentials providers similarly:
+ `StsWebIdentityTokenFileCredentialsProvider`
+ `StsGetSessionTokenCredentialsProvider`
+ `StsGetFederationTokenCredentialsProvider`
+ `StsAssumeRoleWithWebIdentityCredentialsProvider`
+ `StsAssumeRoleWithSamlCredentialsProvider`
+ `StsAssumeRoleCredentialsProvider`
+ `DefaultCredentialsProvider` (when it delegates to credentials provider that uses sessions)
+ `ProcessCredentialsProvider`
+ `WebIdentityTokenFileCredentialsProvider`
+ `ContainerCredentialsProvider`
+ `InstanceProfileCredentialsProvider`

Understanding credential caching helps you optimize your application's performance and reliability when working with AWS services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
