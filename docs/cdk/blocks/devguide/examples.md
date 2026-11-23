---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/examples.html
---

# Examples and patterns

This topic shows common application patterns you can build with AWS CDK Blocks. Each example demonstrates how CDK Blocks compose together to solve real-world problems.

For complete projects you can start from, see the [CDK Blocks project templates on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/create-blocks-app/templates).

## CRUD API with authentication
<a name="example-crud-api"></a>

A typical data-driven application with user authentication and scoped data access. The app stores notes in a `KVStore` with a `key` whose partition field is the user ID, so listing a user’s notes reads only that user’s items. A `scan()` would read every item in the table.

```typescript
import { ApiNamespace, Scope, KVStore, Auth } from 'aws-cdk-blocks';
import { z } from 'zod';

const scope = new Scope('notes-app');
const auth = new Auth(scope, 'auth');
export const authApi = auth.createApi();

const notes = new KVStore(scope, 'notes', {
  schema: z.object({
    userId: z.string(), // partition key: one partition per user
    id: z.string(),     // sort key
    title: z.string(),
    body: z.string(),
    createdAt: z.number(),
  }),
  key: { partitionKey: 'userId', sortKey: 'id' },
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async create(title: string, body: string) {
    const user = await auth.requireAuth(context);
    const note = { userId: user.userSub, id: crypto.randomUUID(), title, body, createdAt: Date.now() };
    await notes.put({ userId: note.userId, id: note.id }, note);
    return note;
  },

  async list() {
    const user = await auth.requireAuth(context);
    // Reads only this user's partition, not the whole table
    return Array.fromAsync(notes.query({ where: { userId: { equals: user.userSub } } }), (entry) => entry.value);
  },

  async delete(id: string) {
    const user = await auth.requireAuth(context);
    await notes.delete({ userId: user.userSub, id });
  },
}));
```

 **CDK Blocks used:** `Auth`, `KVStore`, `ApiNamespace`

## Realtime chat
<a name="example-realtime-chat"></a>

A chat application with WebSocket pub/sub and message history.

```typescript
import { ApiNamespace, Scope, KVStore, Auth, Realtime } from 'aws-cdk-blocks';
import { z } from 'zod';

const scope = new Scope('chat-app');
const auth = new Auth(scope, 'auth');
export const authApi = auth.createApi();

const messageSchema = z.object({ id: z.string(), user: z.string(), text: z.string(), ts: z.number() });

// One partition per chat room; the sort key starts with the timestamp, so messages sort by time
const messages = new KVStore(scope, 'messages', {
  schema: messageSchema.extend({ room: z.string() }),
  key: { partitionKey: 'room', sortKey: 'id' },
});

const realtime = new Realtime(scope, 'realtime', {
  namespaces: { chat: Realtime.namespace(messageSchema) },
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async sendMessage(text: string) {
    const user = await auth.requireAuth(context);
    const ts = Date.now();
    const msg = { id: `${ts}-${crypto.randomUUID()}`, user: user.username, text, ts };
    await messages.put({ room: 'general', id: msg.id }, msg);
    await realtime.publish('chat', 'general', msg);
    return msg;
  },

  async getHistory() {
    await auth.requireAuth(context);
    // The 50 newest messages, read from one partition
    const latest = await Array.fromAsync(
      messages.query({ where: { room: { equals: 'general' } }, order: 'desc', limit: 50 }),
      (entry) => entry.value,
    );
    return latest.reverse();
  },

  async subscribeChat() {
    await auth.requireAuth(context); // Ensure caller is authenticated
    return realtime.getChannel('chat', 'general');
  },
}));
```

### Frontend integration
<a name="frontend-integration"></a>

The frontend subscribes to realtime updates:

```typescript
import { api } from 'cdk-blocks';

// Subscribe to messages via API method
const channel = await api.subscribeChat();
channel.subscribe((msg) => {
  console.log(`${msg.user}: ${msg.text}`);
});

// Send a message
await api.sendMessage('Hello, world!');

// Load history
const history = await api.getHistory();
```

 **CDK Blocks used:** `Auth`, `KVStore`, `Realtime`, `ApiNamespace`

## File uploads with metadata
<a name="example-file-uploads"></a>

An application that lets users upload files from the browser and lists them with their size and upload time.

API methods take and return JSON, so do not pass file contents through them. Instead, an API method returns a file handle. The browser uses the handle to upload or download the file directly with a presigned URL. You can also return a presigned URL yourself with `putUrl()` or `getUrl()`.

```typescript
import { ApiNamespace, ApiError, Scope, FileBucket, Auth } from 'aws-cdk-blocks';

const scope = new Scope('files-app');
const auth = new Auth(scope, 'auth');
export const authApi = auth.createApi();

const files = new FileBucket(scope, 'uploads', {
  // Lets the deployed frontend upload and download with the presigned URLs
  corsRules: [{
    allowedOrigins: ['http://localhost:3000', 'https://app.example.com'],
    allowedMethods: ['GET', 'PUT'],
    allowedHeaders: ['Content-Type'],
  }],
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async startUpload(name: string, contentType: string) {
    const user = await auth.requireAuth(context);
    // The browser sends the file straight to storage with this handle
    return files.createUploadHandle(`${user.userSub}/${name}`, { contentType });
  },

  async listFiles() {
    const user = await auth.requireAuth(context);
    const results = [];
    for await (const file of files.scan({ prefix: `${user.userSub}/` })) {
      results.push({ key: file.path, size: file.size, lastModified: file.lastModified.toISOString() });
    }
    return results;
  },

  async download(key: string) {
    const user = await auth.requireAuth(context);
    if (!key.startsWith(`${user.userSub}/`)) {
      throw new ApiError('Forbidden', 403, { name: 'ForbiddenError' });
    }
    return files.getFileHandle(key);
  },
}));
```

The frontend uploads and downloads with the handles:

```typescript
import { api } from 'cdk-blocks';

// Upload: the file goes from the browser to storage, not through your API
const upload = await api.startUpload(file.name, file.type);
await upload.upload(file);

// Download
const [first] = await api.listFiles();
const download = await api.download(first.key);
const blob = await download.download();
```

A deployed bucket has no cross-origin resource sharing (CORS) rules by default, and it does not inherit the stack’s allowed origins. Without `corsRules` that list your frontend origin, browser uploads work locally but fail after you deploy. A rule that combines a wildcard origin (`*`) with `PUT`, `POST`, or `DELETE` fails synthesis.

 **CDK Blocks used:** `Auth`, `FileBucket`, `ApiNamespace`

## SQL-backed application
<a name="example-sql-app"></a>

An application using relational data with joins and transactions. The `cdk-blocks/migrations/db/` folder, named after the CDK Block ID, holds numbered `.sql` files that create the tables. They run once each, before the first query locally and during the deploy in AWS. For a complete project, see the `sql` template.

```typescript
import { ApiNamespace, Scope, Database, Auth, sql } from 'aws-cdk-blocks';

const scope = new Scope('store-app');
const auth = new Auth(scope, 'auth');
export const authApi = auth.createApi();

// Runs the numbered .sql files in cdk-blocks/migrations/db/ once each, in order.
// The directory is named after the Block ID and is relative to the project root.
const db = new Database(scope, 'db');

interface Order {
  id: number;
  user_id: string;
  status: string;
  created_at: string;
}

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createOrder(items: Array<{ productId: string; qty: number }>) {
    const user = await auth.requireAuth(context);

    return db.transaction(async (trx) => {
      const [order] = await trx.query<Order>(sql`
        INSERT INTO orders (user_id, status)
        VALUES (${user.userSub}, 'pending')
        RETURNING *
      `);

      for (const item of items) {
        await trx.execute(sql`
          INSERT INTO order_items (order_id, product_id, quantity)
          VALUES (${order.id}, ${item.productId}, ${item.qty})
        `);
      }

      return order;
    });
  },

  async getOrders() {
    const user = await auth.requireAuth(context);
    return db.query<Order>(sql`
      SELECT * FROM orders
      WHERE user_id = ${user.userSub}
      ORDER BY created_at DESC
    `);
  },
}));
```

The migration creates both tables:

```sql
-- cdk-blocks/migrations/db/001_create_orders.sql
CREATE TABLE orders (
  id         BIGINT GENERATED BY DEFAULT AS IDENTITY (CACHE 65536) PRIMARY KEY,
  user_id    TEXT NOT NULL,
  status     TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
  order_id   BIGINT NOT NULL REFERENCES orders (id),
  product_id TEXT NOT NULL,
  quantity   INTEGER NOT NULL
);

CREATE INDEX ASYNC orders_user_id ON orders (user_id);
```

 **CDK Blocks used:** `Auth`, `Database`, `ApiNamespace`

## Common patterns
<a name="example-patterns-summary"></a>

| Pattern | Approach |
| --- | --- |
| User-scoped data | Use `user.userSub` as the partition key (or key prefix) to isolate data per user |
| Optimistic UI | Return the created/updated object from API methods so the frontend can update immediately |
| Background work | Use `AsyncJob` for queued work and `CronJob` for scheduled work |
| Multi-tenant | Use Scope IDs or key prefixes to partition data by tenant |
| Feature flags | Store flags in an `AppSetting` and read them in API methods before executing logic |

## Related resources
<a name="examples-further-reading"></a>

For runnable projects:
+  [CDK Blocks project templates on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/create-blocks-app/templates) used by `npm create @aws-cdk-blocks/blocks-app@latest`
+  [Test fixtures in the CDK Blocks repository](https://github.com/aws/cdk-blocks/tree/main/test-apps). These are small apps the repository uses for its own tests, and most have no README.
