---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/cli-reference.html
---

# CLI reference

 AWS CDK Blocks uses standard npm scripts for all development and deployment workflows. After scaffolding a project, all commands run from your project root.

For more information about CLI commands and options, see [CDK Blocks CLI documentation on GitHub](https://github.com/aws/cdk-blocks).

## Create a project
<a name="cli-create"></a>

```bash
npm create @aws-cdk-blocks/blocks-app@latest <project-name> [-- --template <template>]
```

Scaffolds a new CDK Blocks project. The command picks its mode from the target directory:
+  **Empty or new directory:** creates a standalone app from a template.
+  **Existing project (has a `package.json`):** adds the `cdk-blocks/` backend workspace, `cdk.json`, and the CDK Blocks scripts to your project. Works with any frontend framework.
+  **Amplify Gen 2 project (has `amplify/backend.ts`):** adds CDK Blocks to your Amplify backend, using the `amplify` template.

| Option | Description |
| --- | --- |
|  `--template <name>`  | Template to use (default: `default`). In an existing project, it selects which `cdk-blocks/` workspace to copy, for example `nextjs` for a Next.js dev server. |
|  `--yes`, `-y`  | Skip confirmation prompts |
|  `--skip-install`  | Skip installing dependencies |
|  `--help`, `-h`  | Show usage and the list of templates |

| Template | Description |
| --- | --- |
|  `default`  | Vite frontend with auth, KVStore, and Realtime (todo app) |
|  `bare`  | Vite frontend with a single `greet()` API (smallest starter) |
|  `react`  | Vite and React 19 frontend with auth, KVStore, and Realtime (todo app) |
|  `nextjs`  | Next.js 16 App Router with Server and Client Components that call CDK Blocks |
|  `auth`  | Vite frontend that tours the `Auth` Block: email sign-up with a code, groups, and profile attributes. `--template auth-cognito` still works and creates this template |
|  `auth-oidc`  | Vite frontend with OIDC sign-in, using a local stub identity provider for development |
|  `demo`  | Fuller example with Auth, KVStore, FileBucket, AppSetting, Secret, AsyncJob, EmailClient, KnowledgeBase, and Database |
|  `backend`  | Backend only: a CDK Blocks API and CDK, no frontend |
|  `api-only`  | Headless JSON API with a public health check and CRUD routes that require sign-in, no frontend |
|  `sql`  | PostgreSQL backend using the `Database` Block with SQL migrations, foreign keys, and transactions (Aurora DSQL) |
|  `agent`  | Vite frontend with an AI agent and a tool, using a canned model for development |
|  `cron`  | Backend only: scheduled CronJobs that record each run, no frontend |
|  `observability`  | Backend only: Logger, Metrics, Tracer, and a CloudWatch dashboard on one API call, no frontend |
|  `amplify`  | Overlay for an existing Amplify Gen 2 app. Selected automatically; you cannot use it for a new app. |

## Local development
<a name="cli-dev"></a>

```bash
npm run dev
```

Starts the local development server, which runs your app and every CDK Block on your machine, with hot reload. CDK Blocks use local in-memory and filesystem storage. No AWS account required.
+ Templates with a frontend: The dev server serves the frontend and API from a single front door at `http://localhost:3000`. The frontend dev server runs on port 3100 behind it. The API lives under `http://localhost:3000/aws-blocks/api/`, with one path for each exported namespace, for example `/aws-blocks/api/api`.
+  `backend`, `api-only`, `sql`, `cron`, and `observability` templates: The dev server serves the API on `http://localhost:3001`.
+ Amplify projects (the `amplify` overlay): CDK Blocks does not add an `npm run dev` script. Run `npm run blocks:dev` to serve the API on `http://localhost:3001`, and `npm run blocks:stop` to stop it.

 `npm run dev` frees its ports at startup by stopping whatever process listens on them. If a dev server for this project is already running, the new one exits instead. For more information, see [Port 3000 or 3001 already in use](troubleshooting.md#ts-port-in-use). To stop the dev server from another terminal, run `npm run dev:stop`.

## Sandbox deployment
<a name="cli-sandbox"></a>

```bash
npm run sandbox
```

Deploys your own sandbox backend to AWS with a full CloudFormation deployment, which can take several minutes the first time. It then runs `cdk watch`, which hotswaps code changes into the Lambda function, and starts the local dev server against the deployed backend. Each developer gets an isolated sandbox.

```bash
npm run sandbox:deploy
```

Deploys the sandbox once and exits. Use it in scripts and CI.

```bash
npm run sandbox:preview
```

Deploys the sandbox with your frontend hosted in preview shape, prints the preview URL, and exits. Only templates with a frontend have this script.

```bash
npm run sandbox:destroy
```

Deletes every stack the sandbox deployed. A `us-east-1` support stack that holds a Lambda@Edge function cannot be deleted for a few hours after its CloudFront distribution is gone; if the command reports this, run it again later.

## Production deployment
<a name="cli-deploy"></a>

```bash
npm run deploy
```

Deploys every stack in the application to AWS with CDK (CloudFormation), without an approval prompt for IAM changes. It always updates the production stack, `<stackId>-prod`. Add `-- --wait-live` to wait until CloudFront serves the new frontend build. For more information about staged deployments, see [Staged deployments with a pipeline](deploy-to-aws.md#deploy-pipeline).

```bash
npm run destroy
```

Deletes the production stack. It keeps stateful resources such as tables, buckets, and `Auth` user pools. An `Auth` Block with `removalPolicy: 'destroy'` and `deletionProtection: false` loses its user pool. If a delete attempt fails, the command empties the buckets in every stack before it retries. On an app with more than one top-level stack, such as one with a `us-east-1` support stack, the first attempt always fails. Do not use this command there. For more information, see [Full deployment](deploy-to-aws.md#deploy-production).

## Other project scripts
<a name="cli-scripts"></a>

Projects created from a template also have these scripts. Adding CDK Blocks to an existing project adds only the `dev:server`, `dev:stop`, `sandbox`, `sandbox:destroy`, `sandbox:console`, `deploy`, and `destroy` scripts.

| Script | Description |
| --- | --- |
|  `npm run dev:stop`  | Stops the dev server that `npm run dev` started. Add `-- --port <n>` for a port other than the default. |
|  `npm run sandbox:console`  | Opens the CloudFormation console’s stack list, filtered to the stack from your last deploy, in the Region from your AWS configuration (`us-east-1` if none is set) |
|  `npm run db`  | Runs the commands of the `Database` Block. `types --block <id>` writes a `Tables` interface for Kysely from the CDK Block’s migration files, and `status --block <id>` lists the applied and pending files in the local database. For an existing database, `connect` stores the connection string and `migrate` applies pending files. Pass the command after a `--` separator, as shown after this table. |
|  `npm run cleanup`  | Stops every process with a connection on ports 3000 to 3003 (3001 to 3003 in templates without a frontend), whatever the process is. This includes processes that only connect to those ports, such as a browser. |
|  `npm run secret`  | Manages the values for Hosting `secret()` in AWS Secrets Manager with the `set <KEY>`, `list`, and `remove <KEY>` subcommands. These are not `Secret` Block values. `set` prompts for the value, or reads it from standard input with `--value-stdin`. Pass the subcommand after a `--` separator, as shown after this table. |
|  `npm run typegen`  | Generates typed keys for `getSecret()` and `getConfig()`. Add `-- --check` in CI to fail when the file is stale. |
|  `npm run spec`  | Generates the API spec file, `cdk-blocks/blocks.spec.json`  |
|  `npm run typecheck`  | Runs the TypeScript compiler without emitting files |
|  `npm run test:e2e`  | Runs the template’s end-to-end tests |
|  `npm run vendorize`  | Copies a CDK Block package’s source into your project. Pass the package name after a `--` separator, as shown after this table. For more information, see [Pattern 4: Vendorize](existing-infrastructure.md#existing-vendorize). |

For example, to set a secret value, to list the migration files of the `Database` Block `main`, and to vendorize the `KVStore` package:

```bash
npm run secret -- set <KEY>
npm run db -- status --block main
npm run vendorize -- @aws-cdk-blocks/bb-kv-store
```

## Related resources
<a name="cli-further-reading"></a>

For more information about advanced CLI options, environment variables, and CI/CD configuration, see [CDK Blocks CLI reference on GitHub](https://github.com/aws/cdk-blocks).
