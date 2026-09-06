---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/toolkit-library-gs.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Getting started with the CDK Toolkit Library
<a name="toolkit-library-gs"></a>

Get started with using the AWS CDK Toolkit Library to programmatically perform CDK actions, such as synthesis and deployment, in your code.

## Prerequisites
<a name="toolkit-library-gs-prerequisites"></a>

1. Supported version of Node.js installed.

1.  AWS credentials configured.

1. Basic familiarity with the AWS CDK.

For more information, see [AWS CDK prerequisites](prerequisites.md).

## Step 1: Installing the CDK Toolkit Library
<a name="toolkit-library-gs-install"></a>

Install the CDK Toolkit Library package in your project’s development environment by running the following:

```
npm install --save @aws-cdk/toolkit-lib
```

## Step 2: Initializing the CDK Toolkit Library
<a name="toolkit-library-gs-initialize"></a>

Create a CDK Toolkit instance to perform programmatic actions on your CDK app.

```
import { Toolkit } from '@aws-cdk/toolkit-lib';

const toolkit = new Toolkit({
    // Optional configuration options go here
});
```

You can customize the CDK Toolkit instance during creation. For instructions, see [Configure your CDK Toolkit instance](toolkit-library-configure.md).

## Step 3: Creating a cloud assembly source for your CDK app
<a name="toolkit-library-gs-ca"></a>

A cloud assembly source provides instructions for generating CloudFormation templates from your CDK app. You can create one in multiple ways. The following are a few examples:

1.  **An inline assembly builder function**:

   ```
   import * as cdk from 'aws-cdk-lib';

   const cloudAssemblySource = await toolkit.fromAssemblyBuilder(async () => {
     const app = new cdk.App();
     new MyStack(app, 'MyStack');
     return app.synth();
   });
   ```

1.  **An existing CDK app file**:

   ```
   const cloudAssemblySource = await toolkit.fromCdkApp("ts-node app.ts");
   ```

For more information, see [Configure cloud assembly sources](toolkit-library-configure-ca.md).

## Step 4: Defining programmatic actions for your CDK app
<a name="toolkit-library-gs-define"></a>

Now that you’ve created a CDK Toolkit instance and cloud assembly source, you can start to define programmatic actions. The following is a basic example that creates a deployment of the `MyStack` stack:

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

await toolkit.deploy(cloudAssemblySource, {
  stacks: {
    strategy: StackSelectionStrategy.PATTERN_MUST_MATCH, // Deploy only stacks that exactly match the provided patterns
    patterns: ["MyStack"],
  },
});
```

## Step 5: Customizing the CDK Toolkit further
<a name="toolkit-library-gs-customize"></a>

You can configure and customize the CDK Toolkit further for your needs:
+  **Messages and interactions** - Configure how the CDK Toolkit communicates with users and applications. See [Configure messages & interactions](toolkit-library-configure-messages.md).
+  **Error handling** - Implement structured error handling for CDK operations. See [Configure error handling](toolkit-library-configure.md#toolkit-library-configure-errors).

## Additional resources
<a name="toolkit-library-gs-resources"></a>

For more information on the CDK Toolkit Library `npm` package, see the [ReadMe](https://www.npmjs.com/package/@aws-cdk/toolkit-lib) in the *@aws-cdk/toolkit-lib* `npm` package.

For API reference information, see the [CDK Toolkit Library API reference](https://docs.aws.amazon.com/cdk/api/toolkit-lib/).
