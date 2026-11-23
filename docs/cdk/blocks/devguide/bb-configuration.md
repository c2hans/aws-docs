---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-configuration.html
---

# Configuration

This section covers AWS CDK Blocks for application settings and secrets.

## AppSetting
<a name="bb-app-setting"></a>

A single configuration value that is not sensitive, such as a feature flag, an API URL, or a threshold. Read and update values at runtime. Values are typed and can be read in your API handlers without environment variable boilerplate.

Feature flags and runtime config for the whole app go in `AppSetting`. `KVStore` is for data your app writes. Production secrets, such as API keys, go in [Secret](#bb-secret).

Locally, AppSetting persists values to the filesystem in the `.bb-data/` directory. On AWS, it provisions an SSM Parameter Store parameter. Best for feature flags and any configuration that might change without a redeploy.

You can mark a setting as `secret: true` to store it as an SSM SecureString. This is a fallback for a secret of little value in a prototype, not for production secrets. A `secret: true` setting cannot take a `value` in code. CDK Blocks seeds it with a random string on first deploy, and you set the real value later.

For more information, see [bb-app-setting on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-app-setting).

## Secret
<a name="bb-secret"></a>

A single secret stored in AWS Secrets Manager. Use `Secret` for production credentials such as third-party API keys, OAuth client secrets, connection strings, and signing keys. This includes the client secret of an `Auth` provider. Each `Secret` is one Secrets Manager secret. The declaration holds only the name, never the value.

```typescript
// Read-only (the default). Set the value after deploy.
const paymentsKey = new Secret(scope, 'payments-api-key');

// Random value created on first deploy, for keys nobody needs to read.
const signingKey = new Secret(scope, 'session-signing-key', { generate: true });

// The app writes this value itself, so it opts in to put().
const partnerToken = new Secret(scope, 'partner-token', { allowRuntimeWrite: true });

// A secret created and managed outside this app.
const sharedKey = new Secret(scope, 'shared-key', {
  secret: Secret.fromExisting('arn:aws:secretsmanager:us-east-1:111122223333:secret:shared-key-AbCdEf'),
});

export const billing = new ApiNamespace(scope, 'billing', () => ({
  async charge(amount: number) {
    const key = await paymentsKey.get();
    if (key === null) throw new ApiError('Payments are not configured', 503);
    // Call the payment API with key and amount.
  },
}));
```

 `get()` returns `null` when no value is set. A new secret starts empty unless you pass `generate: true`. Don’t combine `generate` with `schema`, because a random string is not valid JSON.

### Runtime access
<a name="bb-secret-access"></a>

A `Secret` is read-only at runtime by default. The object has only `get()` and `listVersions()`, and the app’s execution role can only read the secret. Pass `allowRuntimeWrite: true` to add `put()` and grant write access. This also applies to a secret wrapped with `fromExisting()`.

### Secret options
<a name="bb-secret-options"></a>

 `Secret` also takes these options:
+  `name`: a fixed Secrets Manager name, so a script or CI pipeline can set the value with the AWS CLI. By default, CDK Blocks derives a name that is unique in your stack.
+  `schema`: a schema from any Standard Schema library, such as Zod, for a typed JSON secret. Values are checked on `get()` and `put()`.
+  `cacheTtlSeconds`: how long the runtime reuses a fetched value before it reads again. The default is 300 seconds, so a value rotated outside the app is picked up within 5 minutes without a redeploy. Set `0` to turn off caching. A `put()` from the app clears the cache.
+  `secret`: pass `Secret.fromExisting(arn)` to use a secret that already exists, such as one shared by many apps. CDK Blocks does not create, seed, tag, or delete it. It only reads it, writes it if you allow, and grants access.

### Secret versions
<a name="bb-secret-versions"></a>

Each change keeps the old value as the previous version. Locally, only changes that you make with `put()` do. A hand edit of `.bb-data/settings.json` does not. Read it with `get({ version: 'previous' })`, for example to accept tokens signed with the old key during a rotation. `listVersions()` returns the current and previous versions (metadata only), and you can pass one back to `get({ version })`.

### Setting a secret value
<a name="bb-secret-set-value"></a>

To set a value after deploy, open the `/aws-blocks/settings` route of your API. It redirects to your stack’s settings resource group in the AWS Resource Groups console, where `Secret` values appear next to `AppSetting` parameters. You can also give the secret a fixed `name` and set it with `aws secretsmanager put-secret-value`. Scaffolded apps include an `npm run secret` script, but it manages a separate set of secrets under the app’s `blocks/<stackId>/secrets/` prefix. It does not set `Secret` values.

### Secrets in local development
<a name="bb-secret-local"></a>

Locally, `Secret` stores the current value as plain text in `.bb-data/settings.json`, the same file `AppSetting` uses, and the previous value in `.bb-data/secret-versions.json`. The local `/aws-blocks/settings` route opens that file in your editor. `generate: true` seeds a random value locally too, and `cacheTtlSeconds` has no effect. Never use real credentials locally. `Secret` runs only on the server. `aws-cdk-blocks` does not export it to browser code, so browser code that imports it from there fails to build or to load. The browser build of `@aws-cdk-blocks/bb-secret` throws `SecretErrors.NotSupported` when you construct a `Secret`.

For more information, see [bb-secret package source](https://github.com/aws/cdk-blocks/tree/main/packages/bb-secret).
