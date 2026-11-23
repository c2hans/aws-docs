---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/troubleshooting.html
---

# Troubleshooting

## Local development issues
<a name="ts-local-dev"></a>

### Port 3000 or 3001 already in use
<a name="ts-port-in-use"></a>

 **Symptom:** Another program uses port 3000 or 3001, or a process on that port stops after you run `npm run dev`.

 `npm run dev` frees its ports when it starts. It stops whatever process listens on its API port (3000, or 3001 for templates without a frontend) and on its frontend port (3100). It sends `SIGTERM`, then `SIGKILL` if the port is still held, and prints `Reclaimed port <n>`. This happens whatever the process is, so a different app on one of those ports is stopped too. Only a running AWS CDK Blocks dev server for the same project is left alone: a second `npm run dev` exits and tells you to run `npm run dev:stop` first.

 **Solution:** To keep another program on those ports, run the dev server on different ports. `--port` sets the API port, and `--frontend-port` sets the frontend port:

```bash
npm run dev -- --port 3002 --frontend-port 3102
```

To stop a dev server on a port other than the default, pass the port to `npm run dev:stop`:

```bash
npm run dev:stop -- --port 3002
```

### Local data is stale or corrupted
<a name="ts-mock-data-stale"></a>

 **Symptom:** Local development behaves unexpectedly, returns old data, or throws deserialization errors.

 **Solution:** Delete the `.bb-data/` directory to reset all local state:

```bash
rm -rf .bb-data
npm run dev
```

### TypeScript errors after changing the backend
<a name="ts-type-errors-frontend"></a>

 **Symptom:** Frontend shows type errors after modifying API methods in `cdk-blocks/index.ts`.

 **Solution:** This is expected. This means type safety is working. Update your frontend code to match the new API signature. If your IDE doesn’t pick up the changes, restart the TypeScript language server.

## Deployment issues
<a name="ts-deployment"></a>

### CDK bootstrap required
<a name="ts-cdk-not-bootstrapped"></a>

 **Symptom:** `npm run deploy` or `npm run sandbox` stops before it synthesizes, with a message such as "CDK is not bootstrapped in Region REGION of account ACCOUNT\_ID, so `npm run deploy` cannot deploy there."

 **Solution:** Run the bootstrap command that the message prints, from your project directory:

```bash
npx cdk bootstrap aws://ACCOUNT_ID/REGION --app=
```

You need to do this only one time per account/Region combination. If your app has a support stack in `us-east-1`, bootstrap `us-east-1` too. The check that runs before a deploy does not cover it, so a deploy that reaches that stack can still fail with an error such as "SSM parameter /cdk-bootstrap/hnb659fds/version not found." For more information, see [Bootstrap the AWS CDK](deploy-to-aws.md#deploy-aws-cdk-bootstrap).

### AWS credentials expired or missing
<a name="ts-credentials-expired"></a>

 **Symptom:** Deployment fails with `ExpiredTokenException` or "Unable to locate credentials."

 **Solution:** Refresh your AWS credentials:

```bash
# If using IAM Identity Center
aws sso login

# Verify credentials work
aws sts get-caller-identity
```

### Sandbox deployment hangs or times out
<a name="ts-sandbox-stuck"></a>

 **Symptom:** `npm run sandbox` takes more than a few minutes or appears stuck.

 **Solution:** The first sandbox deploy is a full CloudFormation deployment and can take several minutes. If it fails, the sandbox usually leaves the stack in a failed state, because automatic rollback is off, and the next `npm run sandbox` cannot update it. Destroy and recreate:

```bash
npm run sandbox:destroy
npm run sandbox
```

 `sandbox:destroy` handles a stack in `ROLLBACK_COMPLETE`. If it reports `UPDATE_ROLLBACK_FAILED`, first run `aws cloudformation continue-update-rollback --stack-name <your-sandbox-stack>`. To see the stack and its events, run `npm run sandbox:console`. It opens the CloudFormation stack list filtered to the first stack in `.cdk-blocks-sandbox/outputs.json`, which your most recent `npm run sandbox` or `npm run deploy` wrote. It takes the Region from `AWS_REGION`, `AWS_DEFAULT_REGION`, or your AWS CLI configuration, not from `cdk.json`, so check that it opened the Region your stack is in.

### Permission denied during deployment
<a name="ts-permission-denied"></a>

 **Symptom:** Deployment fails with `AccessDenied` or "User is not authorized to perform" errors.

 **Solution:** Your IAM user or role needs permissions to create Lambda functions, DynamoDB tables, API Gateway APIs, IAM roles, and CloudFormation stacks. Use an account with `AdministratorAccess` for initial setup, then scope down for CI/CD.

## Runtime issues
<a name="ts-runtime"></a>

### Behavior differs between local and deployed
<a name="ts-mock-vs-production"></a>

 **Symptom:** Code works locally but fails in production, or vice versa.

 **Common causes:**

| Cause | Solution |
| --- | --- |
| A `KVStore` indexed field set to `null`  | DynamoDB rejects the write on AWS, and the local implementation accepts it. To keep an item out of an index, leave the field out |
| DynamoDB query pagination | Handle paginated responses. Local implementations return all results in a single response |
| Aurora connection limits | Reduce concurrent connections or configure connection pooling |
| Lambda cold starts | First request after idle period is slower. Not a bug |
| Configuration or environment variables missing | Use the `AppSetting` Block for runtime configuration and the `Secret` Block for secrets. For more information, see [Configuration](bb-configuration.md). To pass a value from your CDK code, such as a resource ARN, call `registerConfig(stack, 'KEY', value)` from `aws-cdk-blocks/cdk`. Every function then reads it as `process.env.KEY`. |

### API returns 500 Internal Server Error
<a name="ts-api-returns-500"></a>

 **Symptom:** Frontend receives a generic 500 error without a useful message.

 **Solution:** Unhandled exceptions from your own code return as 500s with the message "Internal error" and no name (to avoid leaking internals). Named errors that CDK Blocks throw, such as `ValidationFailedException`, keep their name and message. AWS SDK errors that pass through a CDK Block also return as "Internal error". To send an error the client can see, throw `new ApiError(message, status, { name })`. To see the full error and stack trace, check CloudWatch Logs for the Lambda function.

The handler’s log group has a name that CloudFormation generates, not `/aws/lambda/…​`. Find it in your stack’s resources, then tail it. Your stack name is `<stackId>-prod` for `npm run deploy`, or `<stackId>-<sandboxId>` for a sandbox. It is also a top-level key in `.cdk-blocks-sandbox/outputs.json` after your most recent deploy.

```bash
aws cloudformation list-stack-resources --stack-name <stack-name> \
  --query "StackResourceSummaries[?contains(LogicalResourceId, 'HandlerLogGroup')].PhysicalResourceId" \
  --output text
aws logs tail <log-group-name> --follow
```

You can also run `npm run sandbox:console`, check that it opened the Region your stack is in, choose your stack in the filtered list, and choose the log group on the **Resources** tab.

## Getting further help
<a name="ts-further-help"></a>

If your issue isn’t covered here:
+ Check [CDK Blocks GitHub Issues](https://github.com/aws/cdk-blocks/issues) for known bugs and workarounds
+ File a new issue with your error message, Node.js version, and steps to reproduce
