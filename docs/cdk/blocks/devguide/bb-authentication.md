---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-authentication.html
---

# Authentication

This section covers the `Auth` Block, which handles user identity and sessions. One `Auth` Block covers email and password sign-in, social sign-in, OpenID Connect (OIDC), and Security Assertion Markup Language (SAML) 2.0, and you configure it with one options object.

## Choosing a sign-in method
<a name="_choosing_a_sign_in_method"></a>

Each `Auth` Block first chooses where its users live, with the `store` option. Every sign-in provider then goes in one `providers` record, keyed by the provider ID that the frontend uses, and tagged with its `type`.

| Sign-in method | Configure with | Best for | Works under `npm run dev`  |
| --- | --- | --- | --- |
| Email and password | On by default (`emailPassword`), default store | Your own user directory, with MFA, passkeys, and groups | Yes |
| Social sign-in |  `providers` entry with `type: 'google'`, `'apple'`, `'facebook'`, or `'amazon'`, default store | Consumer sign-in through Amazon Cognito | No, deploy a sandbox to test it |
| OIDC, verified by your backend |  `store: 'builtin'` with `type: 'oidc'` entries, or `github()`, `customOauth2()`, and `stubIdp()`  | Any OIDC or OAuth 2.0 provider, with no user pool | Yes |
| OIDC through Cognito |  `type: 'oidc'` entry with a `clientSecret`, default store | OIDC users who must be in your user pool | No, deploy a sandbox to test it |
| SAML |  `type: 'saml'` entry, default store | An identity provider that supports only SAML 2.0 | No, deploy a sandbox to test it |

For a workforce identity provider, prefer a `store: 'builtin'` Block: it creates no Cognito resources and you can test it offline with `stubIdp()`.

## Auth
<a name="bb-auth"></a>

The `createApi()` method returns the sign-in API that the `Authenticator` UI component and your own forms call. Export its result to expose that API, for example `export const authApi = auth.createApi();`. Exporting the CDK Block instance itself exposes nothing.

With `store: 'cognito'`, the default, users are records in an Amazon Cognito user pool. Locally, the CDK Block runs a user pool in `.bb-data/`, so sign-up, sign-in, password reset, MFA, and passkeys work without AWS calls, and verification codes go to the optional `codeDelivery` callback instead of email. On AWS, Cognito sends the codes. Its default email sender sends at most 50 emails a day, so before launch, set the `email` option to send through your own Amazon Simple Email Service (Amazon SES) identity.

With `store: 'builtin'`, there is no user pool. Your backend verifies each sign-in and the CDK Block keeps only its sessions. A CDK Block holds one kind of user, so an app with both kinds uses two `Auth` Blocks.

```typescript
import { Auth, Scope, Secret } from 'aws-cdk-blocks';

const scope = new Scope('my-app');
// `generate` gives the first deploy a placeholder. Set the real value after deploy.
const googleSecret = new Secret(scope, 'google-client-secret', { generate: true });

// The default store: email and password, plus a social provider through Cognito.
const auth = new Auth(scope, 'auth', {
  users: { signInWith: ['email'], caseSensitive: false, groups: ['admin'] },
  providers: {
    google: { type: 'google', clientId: 'your-client-id', clientSecret: googleSecret },
  },
  removalPolicy: 'retain',
});
export const authApi = auth.createApi();

// No user pool: your backend verifies the sign-in.
const sso = new Auth(scope, 'sso', {
  store: 'builtin',
  providers: {
    corp: { type: 'oidc', issuer: 'https://idp.example.com', clientId: 'your-client-id' },
  },
  redirects: { callbackPath: '/aws-blocks/auth/sso/callback', signOutPath: '/aws-blocks/auth/sso/signout' },
});
export const ssoApi = sso.createApi();
```

Two AWS CDK Blocks that both have `providers` need different `redirects` paths, because they would otherwise mount the same callback route. A provider secret is a reference, never a string. Use a `Secret`, and set its value as described in [Setting a secret value](bb-configuration.md#bb-secret-set-value).

The compiler checks the combinations. For example, `mfa` and a `type: 'google'` entry are compile errors on a `store: 'builtin'` Block. A method that the options turn off, such as `signIn` with `emailPassword: false`, is a compile error too.

Cognito fixes `users.signInWith` and `users.caseSensitive` when the user pool is created, so choose them before real users sign up.

### Protecting API methods
<a name="_protecting_api_methods"></a>

Every `ApiNamespace` method is public until it awaits a guard. `await auth.requireAuth(context)` returns the signed-in user, or responds with a 401 `NotAuthenticatedException` error. `await auth.requireRole(context, 'admin')` also responds with a 403 `NotAuthorizedException` error when the user is not in the group. Declare the groups in `users.groups`. On the default store, `requireRole` reads groups from the user pool on each request. On a `store: 'builtin'` Block, it reads them from the provider’s `groupsClaim`.

To make a forgotten guard impossible, define the namespace with `auth.protect`. Its `methods` run only after the session check, with the signed-in user, and its optional `public` methods need no session. The following example uses the `auth` Block from the earlier example and a `notes` store:

```typescript
const notes = new KVStore(scope, 'notes');

export const notesApi = auth.protect(scope, 'notesApi', {
  public: () => ({
    async health() {
      return { ok: true };
    },
  }),
  methods: (context, user) => ({
    async addNote(text: string) {
      await notes.put(`${user.userSub}:${crypto.randomUUID()}`, text);
    },
  }),
}, { role: 'admin' });
```

Key each user’s data on `user.userSub`, which is stable for the user’s lifetime. On the default store, `userSub` is the Cognito `sub` and `userId` is the Cognito username. On a `store: 'builtin'` Block, both are the provider’s issuer and subject.

To manage users from your own methods, opt in with `admin: {}`. The `auth.admin` handle is never served as an API method, so every method that calls it must check its caller first. To add the first admin, run `npx @aws-cdk-blocks/bb-auth users add-to-group <user> admin`, with `--stage prod --yes` for a deployed user pool. To keep end users from writing an attribute that you use for authorization, such as a role, declare it in `users.attributes` with `userWritable: false`.

### Local sign-in with stubIdp
<a name="_local_sign_in_with_stubidp"></a>

 `stubIdp()` runs a small OIDC provider inside your app. It needs no credentials, works offline, and shows a page where you pick a test user. It works only under `npm run dev` and in sandbox deployments, and synth fails for any other deployment that uses it. To keep the stub locally and a real provider in production, choose the entry with `getDeploymentType()`, which returns `'local'`, `'sandbox'`, or `'production'`. The following example uses the stub everywhere except production:

```typescript
import { Auth, Scope, getDeploymentType, stubIdp } from 'aws-cdk-blocks';

const scope = new Scope('my-app');

const auth = new Auth(scope, 'auth', {
  store: 'builtin',
  providers: {
    corp:
      getDeploymentType() === 'production'
        ? { type: 'oidc', issuer: 'https://login.example.com', clientId: 'your-client-id' }
        : stubIdp({ users: [{ sub: 'u-1', email: 'jane_doe@example.com', name: 'Jane Doe' }] }),
  },
});
export const authApi = auth.createApi();
```

Providers on the default store sign in through Cognito managed login, which needs a deployed user pool, so test them in a sandbox.

### Native apps and other clients
<a name="_native_apps_and_other_clients"></a>

Sessions are HTTP-only cookies. With `allowBearerAuth: true`, native apps and command line clients can send `Authorization: Bearer <access token>` instead: a Cognito access token on the default store, or the provider’s access token on a `store: 'builtin'` Block. To accept tokens from other app clients of the same user pool, pass `allowBearerAuth: { clientIds }`. For native apps that sign in with a federated provider, also export `auth.createOidcApi()`.

### Keep the Block ID
<a name="_keep_the_block_id"></a>

The CDK Block ID, `'auth'` in `new Auth(scope, 'auth')`, is part of every resource name. If you change it or move the CDK Block under another scope, CloudFormation creates a new user pool and deletes the old one with every user in it. At synth, the CDK Block refuses user pool changes that Cognito can’t apply and changes that would remove the user pool, such as renaming the CDK Block. It compares against a baseline file in `cdk-blocks/baselines/`, so commit that file. The user pool and session table follow the stack’s `removalPolicy` default unless you set the option. Set `removalPolicy: 'retain'` for any user pool that holds real users.

### Migrating from AuthBasic, AuthCognito, or AuthOIDC
<a name="_migrating_from_authbasic_authcognito_or_authoidc"></a>

 `Auth` replaces the `AuthBasic`, `AuthCognito`, and `AuthOIDC` Blocks, which are removed. A codemod does the mechanical part of the migration. It never changes a CDK Block ID, and it leaves a `TODO(aws-blocks-auth-migrate)` comment wherever you need to decide something. Run these shell commands from your app’s root directory:

```bash
npx @aws-cdk-blocks/bb-auth migrate --dry-run   # print the changes, write nothing
npx @aws-cdk-blocks/bb-auth migrate             # rewrite the files
```

An `AuthCognito` app that keeps the same CDK Block ID keeps its user pool and users, but each user signs in once more. `AuthBasic` users can’t be moved and must sign up again. For more information about each CDK Block’s steps and what happens on the first deploy, see the [Auth migration guide on GitHub](https://github.com/aws/cdk-blocks/blob/main/packages/bb-auth/MIGRATION.md).

For more information, see [bb-auth on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-auth).
