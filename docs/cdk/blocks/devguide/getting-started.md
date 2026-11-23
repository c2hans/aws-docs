---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/getting-started.html
---

# Getting started with AWS CDK Blocks

In this tutorial, you set up your development environment, create a todo application with user authentication, data persistence, and a type-safe API. The application runs locally and can optionally deploy to AWS.

## Prerequisites
<a name="getting-started-prerequisites"></a>

To develop with AWS CDK Blocks, you need the following on your local machine:
+  **Node.js** version 22 or later. Download from https://nodejs.org/.
+  **npm** version 10 or later (included with Node.js).
+ A code editor with TypeScript support, such as Visual Studio Code or Kiro.

To verify your Node.js and npm versions:

```bash
node --version
npm --version
```

For the optional deployment step, you also need:
+  AWS CLI configured with credentials
+  AWS CDK bootstrapped in your account

For deployment details, see [Deploy your application to AWS](deploy-to-aws.md).

## Create your CDK Blocks project
<a name="getting-started-create"></a>

Create a new CDK Blocks application:

```bash
npm create @aws-cdk-blocks/blocks-app@latest my-todo-app
cd my-todo-app
```

The command copies the `default` template into `my-todo-app` and installs its dependencies. The project has the following structure:

```
my-todo-app/
├── .cdk-blocks/
│   └── config.json
├── cdk-blocks/
│   ├── index.ts
│   ├── index.cdk.ts
│   ├── index.handler.ts
│   ├── client.js
│   ├── package.json
│   └── tsconfig.json
├── public/
│   └── favicon.svg
├── src/
│   └── index.ts
├── test/
│   └── e2e.test.ts
├── .gitignore
├── AGENTS.md
├── README.md
├── cdk.json
├── index.html
├── package.json
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

A unique stack ID for this project. Deployments use it to name your stacks, so commit this file.

The backend: CDK Block instantiations and API definitions in `index.ts`.

The CDK app that defines your AWS deployment.

The AWS Lambda entry point for your backend.

The typed frontend client. The development server regenerates it, so do not edit it.

The frontend: imports and calls the backend API directly.

An end-to-end test. Run it with `npm run test:e2e`.

Instructions for coding agents that work in this project.

## Run the application locally
<a name="getting-started-run-locally"></a>

Start the development server:

```bash
npm run dev
```

In your web browser, navigate to `http://localhost:3000`. You see a todo application with authentication, CRUD operations, priorities, and sorting.

All CDK Blocks are running with local implementations:
+  `KVStore` uses file-backed storage in `.bb-data/` for structured data
+  `Auth` runs a local user pool in `.bb-data/` and prints sign-up codes in the terminal instead of sending email
+  `Realtime` runs a local WebSocket server for pub/sub channels
+  `ApiNamespace` routes calls through a local HTTP server

No AWS account is needed. Changes to your code are reflected immediately through hot reload.

## Explore the backend code
<a name="getting-started-explore-backend"></a>

The `cdk-blocks/index.ts` file defines your backend and API in a single place. The listings in this section show its code without the template’s comments. The first part creates the CDK Blocks:

```typescript
import { ApiNamespace, ApiError, Scope, Auth, KVStore, Realtime } from 'aws-cdk-blocks';
import { z } from 'zod';

const scope = new Scope('my-app');

const auth = new Auth(scope, 'auth', {
  users: { signInWith: ['email'], caseSensitive: false },
  codeDelivery: async (username, code, purpose) => {
    console.log(`[auth] ${purpose} code for ${username}: ${code}`);
  },
});
export const authApi = auth.createApi();

const todoSchema = z.object({
  userSub: z.string(),
  todoId: z.string(),
  title: z.string(),
  completed: z.boolean(),
  priority: z.number(),     // 1=high, 2=medium, 3=low
  version: z.number(),
  createdAt: z.number(),
});

const todos = new KVStore(scope, 'todos', {
  schema: todoSchema,
  key: { partitionKey: 'userSub', sortKey: 'todoId' },
});

const rt = new Realtime(scope, 'live', {
  namespaces: {
    todos: Realtime.namespace(z.object({
      action: z.enum(['created', 'updated', 'deleted']),
      todoId: z.string(),
    })),
  },
});

const todosChannel = (userSub: string) => encodeURIComponent(userSub);
```

This code creates three CDK Blocks:
+  `new Auth(scope, 'auth', {…​})` creates email and password sign-in, where users sign in with their email address. Sign-up confirms the address with a 6-digit code. Locally, `codeDelivery` prints the code in the terminal. On AWS, this provisions an Amazon Cognito user pool, which emails the code. The line `export const authApi = auth.createApi();` exposes the sign-up and sign-in API that the frontend uses. Exporting the `auth` instance itself would expose nothing.
+  `new KVStore(scope, 'todos', {…​})` creates structured data storage with a Zod schema for validation. The `key` option keys each todo by user and todo ID, so the API can list one user’s todos. The `version` field supports optimistic locking. Locally, this is a file-backed store in the `.bb-data/` directory. On AWS, this provisions a DynamoDB table.
+  `new Realtime(scope, 'live', {…​})` creates a pub/sub namespace named `todos`. The API publishes an event to it whenever a todo changes, so your other open tabs reload their lists. Each user has their own channel. The `todosChannel` helper encodes the user ID, so a user ID can’t add `/` segments that place one user’s channel under another’s. Locally, this runs a WebSocket server inside the development server. On AWS, this provisions an Amazon API Gateway WebSocket API and a DynamoDB table for connections.

The API methods use these CDK Blocks. This listing is shortened. The template also defines `updatePriority` and `deleteTodo`.

```typescript
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async subscribeTodos() {
    const user = await auth.requireAuth(context);
    return rt.getChannel('todos', todosChannel(user.userSub));
  },

  async createTodo(title: string, priority: number = 2) {
    const user = await auth.requireAuth(context);
    const todoId = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
    const todo = {
      userSub: user.userSub,
      todoId,
      title,
      completed: false,
      priority,
      version: 1,
      createdAt: Date.now(),
    };
    await todos.put({ userSub: user.userSub, todoId }, todo);
    await rt.publish('todos', todosChannel(user.userSub), { action: 'created' as const, todoId });
    return todo;
  },

  async listTodos(sortBy?: 'priority' | 'title') {
    const user = await auth.requireAuth(context);
    const list = await Array.fromAsync(
      todos.query({ where: { userSub: { equals: user.userSub } } }),
      (entry) => entry.value,
    );
    if (sortBy === 'priority') return list.sort((a, b) => a.priority - b.priority);
    if (sortBy === 'title') return list.sort((a, b) => a.title.localeCompare(b.title));
    return list;
  },

  async toggleTodo(todoId: string) {
    const user = await auth.requireAuth(context);
    const todo = await todos.get({ userSub: user.userSub, todoId });
    if (!todo) throw new ApiError('Todo not found', 404, { name: 'TodoNotFoundException' });
    await todos.put(
      { userSub: user.userSub, todoId },
      { ...todo, completed: !todo.completed, version: todo.version + 1 },
      { ifFieldEquals: { version: todo.version } },
    );
    await rt.publish('todos', todosChannel(user.userSub), { action: 'updated' as const, todoId });
    return { success: true };
  },

  // updatePriority and deleteTodo follow the same pattern.
}));
```

Every method starts with `auth.requireAuth(context)`. Each `ApiNamespace` method is a public endpoint until it calls `requireAuth`, and the local implementation does not warn you if you forget. The `toggleTodo` method throws an `ApiError` with status 404 so the client gets a named error, and it uses `ifFieldEquals` to reject a write if another request changed the todo first.

The template keys each user’s data on `user.userSub`, which stays the same for the user’s lifetime. Key your own data on it too.

## Explore the frontend code
<a name="getting-started-explore-frontend"></a>

The frontend in `src/index.ts` imports the backend API directly:

```typescript
import { api, authApi } from 'cdk-blocks';
```

There is no client generation step, no API URL configuration, and no SDK initialization. TypeScript provides full type safety. If you change a method signature in the backend, the frontend shows a compile error immediately.

## Make a change
<a name="getting-started-make-change"></a>

Add a method that deletes all completed todos. In `cdk-blocks/index.ts`, add it inside the `ApiNamespace` definition, after `deleteTodo`:

```typescript
  async clearCompleted() {
    const user = await auth.requireAuth(context);
    const list = await Array.fromAsync(
      todos.query({ where: { userSub: { equals: user.userSub } } }),
      (entry) => entry.value,
    );
    const done = list.filter((todo) => todo.completed);
    for (const todo of done) {
      await todos.delete({ userSub: user.userSub, todoId: todo.todoId });
      await rt.publish('todos', todosChannel(user.userSub), { action: 'deleted' as const, todoId: todo.todoId });
    }
    return { cleared: done.length };
  },
```

The development server hot-reloads. You can immediately call the new method from the frontend with full type safety:

```typescript
const { cleared } = await api.clearCompleted();
```

## Available CDK Blocks
<a name="getting-started-available-bbs"></a>

The following table lists the CDK Blocks used in this tutorial and other commonly used CDK Blocks:

| Block | Purpose |
| --- | --- |
|  `KVStore`  | Key-value and structured data with indexes and queries |
|  `Auth`  | Email and password, social, OIDC, and SAML sign-in with sessions |
|  `ApiNamespace`  | Type-safe RPC from browser to backend |
|  `Database`  | SQL on PostgreSQL with migrations and transactions |
|  `FileBucket`  | File uploads and downloads |
|  `Realtime`  | WebSocket pub/sub channels |
|  `AsyncJob`  | Background job processing |
|  `Agent`  | AI agent with tool calling |

For the complete list of all available CDK Blocks, see [CDK Blocks reference](building-blocks-reference.md).

## Optional: Deploy your application to AWS
<a name="getting-started-deploy"></a>

When you’re ready to deploy to a real AWS environment, see [Deploy your application to AWS](deploy-to-aws.md) for the full setup and deployment steps.

## Clean up
<a name="getting-started-cleanup"></a>

To stop the local development server, press `Ctrl+C` in your terminal.

If you deployed to AWS and want to remove all resources:

```bash
# Remove production deployment
npm run destroy

# Remove sandbox environment
npm run sandbox:destroy
```

## Next steps
<a name="getting-started-next-steps"></a>
+  [AWS CDK Blocks concepts](concepts.md): Learn about CDK Blocks, scopes, the app definition, and how code maps to resources.
+  [CDK Blocks reference](building-blocks-reference.md): Explore all available CDK Blocks and their APIs.
+  [Examples and patterns](examples.md): See common application patterns and sample code.
