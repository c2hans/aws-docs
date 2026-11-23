---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-data-storage.html
---

# Data storage

This section covers AWS CDK Blocks for persisting and retrieving data.

## Choosing a data Block
<a name="_choosing_a_data_block"></a>

| Block | Best for | Avoid when |
| --- | --- | --- |
|  `KVStore`  | Caches and session stores, and app records that you read by key, list in order inside a group, or read by another field through an index | You need JOINs, transactions, or complex SQL |
|  `Database`  | Relational data, complex queries, JOINs, transactions, migrations, with no virtual private cloud (VPC) to manage. Put it on an `aurora` cluster for triggers, extensions, Row Level Security, or large transactions | Your workload is mostly key-value lookups, which `KVStore` serves with no cluster to manage |
|  `FileBucket`  | File uploads, user-generated content, large binary objects | You need structured queries over file metadata (pair with `KVStore` for metadata) |

Feature flags and runtime config for the whole app go in `AppSetting`, not in a data CDK Block. `KVStore` is for data your app writes. For more information, see [Configuration](bb-configuration.md).

## KVStore
<a name="bb-kvstore"></a>

Key-value and document storage backed by DynamoDB. Pick one of three forms by how you read the data:
+ No options: a string key and a string value (or a type argument), for caches, sessions, and other data where you always know the key.
+ A `schema` and `indexes`: typed values on a string key, for data that you also read by another field.
+ A `schema` and a `key` (`{ partitionKey, sortKey? }`): typed records on an object key, for data that you list or query as a collection, such as the todos of one user. The key is an object with those fields, each a string or a number.

A store fixes its key when you create it, so declare a `key` for any records that you list. The following example declares a key and lists the todos of one user:

```typescript
const todos = new KVStore(scope, 'todos', {
  schema: z.object({ userId: z.string(), todoId: z.string(), title: z.string(), done: z.boolean() }),
  key: { partitionKey: 'userId', sortKey: 'todoId' },
});

await todos.put({ userId: 'alice', todoId: '001' }, { title: 'Write the docs', done: false });
for await (const { value } of todos.query({ where: { userId: { equals: 'alice' } }, limit: 20 })) {
  console.log(value.title);
}
```

Every call takes the key first, as in `put(key, value, options)`. `query()` reads one partition in sort order, by the key or by an index. `query()` and `scan()` return `{ key, value, expiresAt }` entries and a `cursor` for the next page. KVStore also has batch calls and conditional writes, and no transaction API.

 `get()` is strongly consistent by default. Pass `{ consistentRead: false }` to use half the read capacity where a stale value is acceptable. On AWS, `query()`, `scan()`, `getBatch()`, and index reads are eventually consistent.

Locally, KVStore persists data in the `.bb-data/` directory. The local implementation is always consistent and does not throttle requests, so test those behaviors in a sandbox. The local implementation applies DynamoDB’s limits as AWS does: the 400 KB item size, measured as DynamoDB measures it, the size limits on key fields, at most 32 levels of nested lists and maps, and no repeated key within one batch request. On AWS, KVStore checks the key, nesting, and batch limits before it calls DynamoDB. Each of these limits throws a `KVStoreErrors` error in both places, so match those names rather than DynamoDB’s `ValidationException`. A value that DynamoDB can’t store, such as a `Date` or `NaN`, fails locally as it does on AWS. On AWS, it provisions a DynamoDB table with a global secondary index for each entry in `indexes`. To wrap an existing table, pass `table: KVStore.fromExisting(tableName)` and a `key` that matches the table.

KVStore has these durability options:
+ Expiry: write an item with `put(key, value, { ttlSeconds })` or `{ expiresAt }`. Every read hides an expired item, and DynamoDB deletes it later. `ttl` names a number field of the value to hold the expiry.
+  `pointInTimeRecovery`: continuous backups. On by default with the production preset and off with the sandbox preset.
+  `encryption`: the AWS managed key (the default), a dedicated customer managed key, or a key you already own.
+  `protection`: `'disposable'`, `'retained'`, or `'locked'`. By default, the production preset keeps and protects tables, and the sandbox preset deletes them with the stack.

**Upgrading from DistributedTable or an earlier KVStore**
 `DistributedTable` is now part of `KVStore`. To keep a `DistributedTable’s deployed table and items, declare it as `new KVStore(scope, id, { schema, key, indexes, ttl })` with the same ID. Then pass the key first to `put()`, read `{ key, value }` entries from `query()`, and use `KVStoreErrors`.
A `KVStore` deployed with `@aws-cdk-blocks/bb-kv-store` 0.4.0 or earlier stores items in another format, so the deploy fails if a new `KVStore` takes over its table. To upgrade, change the class of that store to `LegacyKVStore` and keep its ID and options. Add a `KVStore` with a new ID, copy the data to it, and then remove the `LegacyKVStore`. In a sandbox, you can destroy and redeploy the stack instead. In the options of the new store, don’t use `ttl: true`, and use `protection` instead of `removalPolicy` and `deletionProtection`. Replace `ifValueEquals` on an object value with `ifFieldEquals`. For more information about the upgrade, see the [KVStore upgrade steps on GitHub](https://github.com/aws/cdk-blocks/blob/main/packages/bb-kv-store/README.md#upgrade-from-release-040-or-earlier).

For more information, see [bb-kv-store on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-kv-store).

## Database
<a name="bb-database"></a>

SQL on PostgreSQL, with migrations, transactions, foreign keys, and joins. Each `Database` is a PostgreSQL schema on a cluster. With no options, the CDK Block owns an Amazon Aurora DSQL cluster, which scales to zero and needs no VPC. Write parameterized queries with the `sql` tagged template, which turns every `${value}` into a bound parameter. The query code is the same on every cluster.

```typescript
// Owns an Aurora DSQL cluster. Its migrations are in cdk-blocks/migrations/shop/.
const shop = new Database(scope, 'shop');

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async addToOrder(orderId: number, amount: number) {
    const { userId } = await auth.requireAuth(context);
    await shop.transaction(async (tx) => {
      const order = await tx.queryOne<{ total: number }>(
        sql`SELECT total FROM orders WHERE id = ${orderId} AND customer_id = ${userId} FOR UPDATE`,
      );
      if (!order) throw new ApiError('Order not found', 404);
      await tx.execute(sql`UPDATE orders SET total = ${order.total + amount} WHERE id = ${orderId}`);
    }, { retryOnConflict: true, signal: context.request.signal });
  },
}));
```

**Upgrading from the earlier Database and DistributedDatabase**
 `Database` replaces the earlier `Database` and `DistributedDatabase` Blocks.
A `DistributedDatabase` keeps its Aurora DSQL cluster and its rows. Declare it as a `Database` with the same ID, in the same scope and stack, and CloudFormation treats it as the same cluster. `Database` reads the `_migrations` table that `DistributedDatabase` wrote, so keep the migration files and their names. No applied file runs a second time.
Before you deploy, run `cdk diff`. Check that the cluster (`AWS::DSQL::Cluster`) shows as changed (`[~]`), not as removed and added (`[-]` then `[+]`). A removed cluster means the ID, the scope, or the stack name is not the one the `DistributedDatabase` had. Under the sandbox preset’s `destroy` removal policy, the deploy then deletes that cluster with its rows.
An app that deployed the `Database` of `@aws-blocks/bb-data` keeps its Aurora cluster, its secret, and its VPC. Give a `LegacyDatabaseCluster` the ID and options of the old Block, then pass it as the `cluster` of a `Database` with a new ID. That class is deprecated and frozen, and `asUser()` is an error on it. The old package name keeps its original scope here because the package no longer exists.
 `asUser()` and `asRole()` replace `withRLS()`, and `crud()` has no replacement. An app that used `fromExisting()` keeps its migration files and `_migrations` table. Pass `DatabaseCluster.fromExisting({ name: 'db-url' })` as `cluster`, point `migrationsPath` at the same directory, and no file runs again.
For more information, see [Upgrading an older app on GitHub](https://github.com/aws/cdk-blocks/blob/main/docs/guides/upgrading-older-apps.md).

### Clusters
<a name="bb-database-clusters"></a>

To put several `Database` Blocks on one cluster, or to use full PostgreSQL, pass a `DatabaseCluster` as the `cluster` option. Each CDK Block on the cluster gets its own schema, named after its ID:

```typescript
const main = new DatabaseCluster(scope, 'main', { type: 'aurora' });
const notes = new Database(scope, 'notes', { cluster: main });
```

The cluster `type` is one of these:
+  `'dsql'`: Aurora DSQL, the engine that a `Database` without `cluster` owns. A transaction can change at most 3,000 rows and 10 MiB of data. Triggers, extensions, and Row Level Security are not available.
+  `'aurora'`: Amazon Aurora PostgreSQL Serverless v2 with the express configuration. It has all of PostgreSQL, runs outside any VPC with IAM authentication, and scales to zero by default (`minCapacity: 0`). The first request after five idle minutes then waits about 20 seconds. Set `minCapacity: 0.5` to keep it warm, and `maxCapacity` (default 2) to raise the ceiling.

Schemas separate CDK Blocks by name, not by permission: every CDK Block on a cluster connects as one database role that can read and write every schema on it. Put a CDK Block whose data must stay separate on its own cluster.

The data stays on the cluster that a CDK Block first deploys to. If you rename a `Database` or `DatabaseCluster` ID, or change the `cluster` option, the CDK Block points at a new, empty cluster or schema, and nothing copies the rows. With the production preset, a cluster that leaves the stack is retained. With the sandbox preset, it is deleted in the same deploy.

### Migrations
<a name="bb-database-migrations"></a>

Create tables in migration files. Your app’s own statements can only read and write rows. Each CDK Block runs the `.sql` files in `cdk-blocks/migrations/<id>/`, relative to the project root, in name order and once each. `migrationsPath` sets another directory. Locally, a CDK Block applies pending files before its first query. On AWS, they run during the deploy, before any function in the stack is updated.

```sql
-- cdk-blocks/migrations/shop/001_init.sql
CREATE TABLE orders (
  id          BIGINT GENERATED BY DEFAULT AS IDENTITY (CACHE 65536) PRIMARY KEY,
  customer_id TEXT NOT NULL,
  total       INTEGER NOT NULL
);

CREATE INDEX ASYNC orders_customer_id ON orders (customer_id);
```

On a `dsql` cluster, write the DSQL forms that the Aurora DSQL documentation shows, such as `CREATE INDEX ASYNC`. CDK Blocks checks every file with `dsql-lint` at `npm run dev` and at `cdk synth`, and the error names the file and the form to use instead. A deploy that stops in a file resumes it where it stopped, so don’t edit a file that has partly run. Put the change in a new file. On an `aurora` cluster, write plain PostgreSQL. Each file runs in one transaction and, on AWS, must finish within ten minutes.

### Queries and transactions
<a name="bb-database-queries"></a>

 `query()` returns every row, `queryOne()` the first row or `null`, and `execute()` returns `{ rowCount }`. Pass a row type, as in `query<T>()`, or pass a Standard Schema such as a Zod object as `{ schema }` to validate every row. A `bigint` value, such as an identity column, comes back as a JavaScript number.

 `transaction(fn)` commits when `fn` resolves and rolls back when it throws. An `ApiError` thrown in `fn` reaches the client unchanged. Aurora DSQL never waits on a lock: when two transactions change the same row, one fails at commit with `SerializationFailure`. With `retryOnConflict: true`, the CDK Block runs `fn` again after a random wait, up to `maxRetries` times (default 8), so keep side effects such as sending email out of `fn`. Pass `context.request.signal` as `signal` so that no retry commits after the request times out.

For the Kysely query builder, install `kysely` and pass `new DatabaseDialect(db)` from `@aws-cdk-blocks/bb-database/kysely` as its dialect. `0` writes a `Tables` interface from the CDK Block’s migration files.

### Row level access
<a name="bb-database-row-access"></a>

On an `aurora` cluster, Row Level Security policies that you write in a migration can limit each user to their own rows. `db.asUser(user)` returns the CDK Block with each transaction run for that user: it first sets `request.jwt.claims` to `{ sub: user.userId }`, plus any claims you pass as the second argument. Pass the result of `requireAuth()` as `user`.

```sql
-- cdk-blocks/migrations/notes/001_notes.sql
CREATE TABLE notes (id SERIAL PRIMARY KEY, owner_id TEXT NOT NULL, body TEXT NOT NULL);
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;
CREATE POLICY notes_owner ON notes
  USING (owner_id = current_setting('request.jwt.claims', true)::jsonb ->> 'sub');
```

With this policy, `+notes.asUser(user).query(sql`SELECT id, body FROM notes`)\+` returns only that user’s notes, and the same statement on the CDK Block itself returns none. For policies written for a database role, such as `TO authenticated`, use `asRole(role, claims?)`. Both throw `DatabaseConfigurationError` on a `dsql` cluster.

### Existing PostgreSQL databases
<a name="bb-database-existing"></a>

To use a PostgreSQL database that you already run, with its tables and data, pass `cluster: DatabaseCluster.fromExisting({ name: 'db-url', ca })` and `migrationsPath: './migrations'`. The CDK Block provisions nothing, and a Lambda function outside any VPC must be able to reach the database over IPv4 with TLS. The CDK Block always verifies the server certificate, against `ca` (PEM text) or the Node.js trust store.

Never write the connection string in code. `0` reads it from a hidden prompt, checks the database, and stores it for local mode. Add `--stage production` to store it for a stage as the SSM SecureString `/<stackName>-db-url`. You can pass your own `Secret` as `connectionString` instead of `name`.

Locally, the CDK Block connects to that database and runs no migration files, so use a development database. `0` applies the pending files in `./migrations` to it, and a deploy applies them to the stage, one transaction per file. `1` records a file, such as a dump of the existing schema, without running it.

### Local mode
<a name="bb-database-local"></a>

Locally, each cluster is one PGlite database (PostgreSQL compiled to WebAssembly) in `.bb-data/`, with one schema per CDK Block. A `dsql` cluster applies the DSQL checks and limits, so SQL that Aurora DSQL rejects fails on your machine. Statements run with the grants of the deployed app, and Row Level Security applies as on AWS. PGlite runs one statement or transaction at a time. To test the retry path, call `simulateConflict(db)` from `@aws-cdk-blocks/bb-database/testing`.

### Database errors
<a name="bb-database-errors"></a>

Common request errors reach the client as named 4xx errors instead of a generic 500. Check for them with `isBlocksError()` on the server or the client, for example `isBlocksError(e, DatabaseErrors.UniqueConstraintViolation)`.

| Error | Cause | HTTP status |
| --- | --- | --- |
|  `DatabaseErrors.PermissionDenied`  | A Row Level Security policy rejected a statement from `asUser()` or `asRole()`  | 403 |
|  `DatabaseErrors.CheckViolation`  | A value fails a `CHECK` constraint | 400 |
|  `DatabaseErrors.NotNullViolation`  | A required column is missing | 400 |
|  `DatabaseErrors.UniqueConstraintViolation`  | A duplicate key | 409 |
|  `DatabaseErrors.ForeignKeyViolation`  | The referenced row does not exist, or other rows still reference the row being deleted | 409 |
|  `DatabaseErrors.SerializationFailure`  | A conflict with a concurrent transaction. Safe to retry. | 409 |

Other failures reach the client as status 500, with the name `QueryFailed` (any other SQL error, including DDL outside a migration), `ConnectionFailed`, `TransactionFailed`, `TransactionRowLimitExceeded`, or `ResultValidationFailed` (a row did not match `schema`).

For more information, see [bb-database on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-database).

## FileBucket
<a name="bb-file-bucket"></a>

File storage for uploads and downloads. Store files by path, generate presigned URLs for direct browser uploads and downloads, and list files by prefix. Versioning is on by default, so you can list and restore earlier versions of a file. Noncurrent versions expire after 90 days. Change this with `noncurrentVersionExpirationDays`.

Browser uploads and downloads that use presigned URLs need CORS rules after you deploy. A FileBucket has no CORS rules by default, and it does not use your stack’s allowed origins. The local dev server accepts any origin, so a missing rule fails only after deploy. List your frontend origin in `corsRules`. A sandbox frontend on `http://localhost:3000` also calls the deployed bucket, so add that origin for sandboxes only, for example with `getDeploymentType()`:

```typescript
const origins = ['https://app.example.com'];
if (getDeploymentType() === 'sandbox') origins.push('http://localhost:3000');

const uploads = new FileBucket(scope, 'uploads', {
  corsRules: [{
    allowedOrigins: origins,
    allowedMethods: ['GET', 'PUT'],
    allowedHeaders: ['Content-Type'],
  }],
});
```

A rule with the wildcard origin `'*'` cannot allow `PUT`, `POST`, or `DELETE`. CDK Blocks rejects it.

FileBucket also has these security options:
+  `encryption`: S3 managed keys (the default), a dedicated customer managed AWS KMS key (`'customer-managed'`), or a key you already own (`FileBucket.fromKmsKey(keyArn)`).
+  `objectLock`: write-once-read-many retention, for example `{ mode: 'governance', retentionDays: 365 }`. Decide when you create the bucket, because you cannot add Object Lock to a deployed bucket or turn it off. The bucket must be retained, and presigned uploads are not supported, so upload with `put()`.
+  `accessLogging`: S3 server access logs in a separate log bucket. Off by default. To turn it on for every FileBucket, set `storageAccessLogging: true` in your stack’s `defaults`. `defaults.accessLogging: true` also turns it on, unless `storageAccessLogging` is `false`.

Locally, FileBucket stores files in the `.bb-data/` directory on your filesystem, mirroring the S3 API behavior. On AWS, it provisions an S3 bucket. You can also wrap an existing S3 bucket with `FileBucket.fromExisting(bucketName)`. A wrapped bucket gets none of the FileBucket defaults, such as versioning, encryption, or blocked public access, and FileBucket ignores `corsRules` for it. Configure those on the bucket itself.

For more information, see [bb-file-bucket on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-file-bucket).
