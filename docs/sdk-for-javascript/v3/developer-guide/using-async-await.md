---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/using-async-await.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Use async/await
<a name="using-async-await"></a>

Rather than using promises, you should consider using async/await. Async functions are simpler and take less boilerplate than using promises. Await can only be used in an async function to asynchronously wait for a value.

The following example uses async/await to list all of your Amazon DynamoDB tables in ` us-west-2`.

**Note**
For this example to run:
Install the AWS SDK for JavaScript DynamoDB client by entering `npm install @aws-sdk/client-dynamodb` in the command line of your project.
Ensure you have configured your AWS credentials correctly. For more information, see [Set credentials](setting-credentials.md).

```
import {
  DynamoDBClient,
  ListTablesCommand
} from "@aws-sdk/client-dynamodb";
(async function () {
  const dbClient = new DynamoDBClient({ region: "us-west-2" });
  const command = new ListTablesCommand({});

  try {
    const results = await dbClient.send(command);
    console.log(results.TableNames.join('\n'));
  } catch (err) {
    console.error(err)
  }
})();
```

**Note**
 Not all browsers support async/await. See [Async functions](https://caniuse.com/#feat=async-functions) for a list of browsers with async/await support.
