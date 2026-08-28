---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Get started with Node.js
<a name="getting-started-nodejs"></a>

This guide shows you how to initialize an NPM package, add a service client to your package, and use the JavaScript SDK to call a service action.

## The scenario
<a name="getting-started-nodejs-scenario"></a>

**Create a new NPM package with one main file that does the following:**
+ Creates an Amazon Simple Storage Service bucket
+ Puts an object in the Amazon S3 bucket
+ Reads the object in the Amazon S3 bucket
+ Confirms if the user wants to delete resources

## Prerequisites
<a name="getting-started-nodejs-prerequisites"></a>

Before you can run the example, you must do the following:
+ Configure your SDK authentication. For more information, see [SDK authentication with AWS](getting-your-credentials.md).
+ Install [Node.js](https://nodejs.org/en/download). AWS recommends using the Active LTS version of Node.js for development.

## Step 1: Set up the package structure and installing client packages
<a name="getting-started-nodejs-setup-structure"></a>

To set up the package structure and install the client packages:

1. Create a new folder `nodegetstarted` to contain the package.

1. From the command line, navigate to the new folder.

1. Run the following command to create a default `package.json` file:

   ```
   npm init -y
   ```

1. Run the following command to install the Amazon S3 client package:

   ```
   npm i @aws-sdk/client-s3
   ```

1. Add `"type": "module"` to the `package.json` file. This tells Node.js to use modern ESM syntax. The final `package.json` should look similar to the following:

   ```
   {
     "name": "example-javascriptv3-get-started-node",
     "version": "1.0.0",
     "description": "This guide shows you how to initialize an NPM package, add a service client to your package, and use the JavaScript SDK to call a service action.",
     "main": "index.js",
     "scripts": {
   "test": "vitest run **/*.unit.test.js"
     },
     "author": "Your Name",
     "license": "Apache-2.0",
     "dependencies": {
    "@aws-sdk/client-s3": "^3.420.0"
     },
     "type": "module"
   }
   ```

## Step 2: Add necessary imports and SDK code
<a name="getting-started-with-node-js-add-code"></a>

Add the following code to a file named `index.js` in the `nodegetstarted` folder.

```
// This is used for getting user input.
import { createInterface } from "node:readline/promises";

import {
  S3Client,
  PutObjectCommand,
  CreateBucketCommand,
  DeleteObjectCommand,
  DeleteBucketCommand,
  paginateListObjectsV2,
  GetObjectCommand,
} from "@aws-sdk/client-s3";

export async function main() {
  // A region and credentials can be declared explicitly. For example
  // `new S3Client({ region: 'us-east-1', credentials: {...} })` would
  //initialize the client with those settings. However, the SDK will
  // use your local configuration and credentials if those properties
  // are not defined here.
  const s3Client = new S3Client({});

  // Create an Amazon S3 bucket. The epoch timestamp is appended
  // to the name to make it unique.
  const bucketName = `test-bucket-${Date.now()}`;
  await s3Client.send(
    new CreateBucketCommand({
      Bucket: bucketName,
    }),
  );

  // Put an object into an Amazon S3 bucket.
  await s3Client.send(
    new PutObjectCommand({
      Bucket: bucketName,
      Key: "my-first-object.txt",
      Body: "Hello JavaScript SDK!",
    }),
  );

  // Read the object.
  const { Body } = await s3Client.send(
    new GetObjectCommand({
      Bucket: bucketName,
      Key: "my-first-object.txt",
    }),
  );

  console.log(await Body.transformToString());

  // Confirm resource deletion.
  const prompt = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const result = await prompt.question("Empty and delete bucket? (y/n) ");
  prompt.close();

  if (result === "y") {
    // Create an async iterator over lists of objects in a bucket.
    const paginator = paginateListObjectsV2(
      { client: s3Client },
      { Bucket: bucketName },
    );
    for await (const page of paginator) {
      const objects = page.Contents;
      if (objects) {
        // For every object in each page, delete it.
        for (const object of objects) {
          await s3Client.send(
            new DeleteObjectCommand({ Bucket: bucketName, Key: object.Key }),
          );
        }
      }
    }

    // Once all the objects are gone, the bucket can be deleted.
    await s3Client.send(new DeleteBucketCommand({ Bucket: bucketName }));
  }
}

// Call a function if this file was run directly. This allows the file
// to be runnable without running on import.
import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main();
}
```

The example code can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/nodegetstarted/index.js).

## Step 3: Run the example
<a name="getting-started-with-node-js-run"></a>

**Note**
Remember to sign in\! If you are using IAM Identity Center to authenticate, remember to sign in using the AWS CLI `aws sso login` command.

1. Run `node index.js`.

1. Choose whether to empty and delete the bucket.

1. If you don't delete the bucket, be sure to manually empty and delete it later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
