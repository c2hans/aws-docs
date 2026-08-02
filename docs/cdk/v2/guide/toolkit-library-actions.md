---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/toolkit-library-actions.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Configuring CDK Toolkit programmatic actions
<a name="toolkit-library-actions"></a>

The AWS CDK Toolkit Library provides programmatic interfaces for application lifecycle actions such as synthesis, deployment, and stack management. This guide explains how to use each action in your code.

## Generating cloud assemblies with synth
<a name="toolkit-library-actions-synth"></a>

The `synth` action generates a cloud assembly from your cloud assembly source. For more information about synthesis, see [Configure and perform CDK stack synthesis](configure-synth.md). A cloud assembly contains the following deployment artifacts from your CDK app:
+  AWS CloudFormation templates that define your infrastructure.
+ Assets such as Lambda function code or Docker images.
+ Deployment metadata and configuration.

Here’s how to use the `synth` action to create a cloud assembly:

```
// Create a toolkit instance
const toolkit = new Toolkit();

// Create a cloud assembly source from a TypeScript app
const cloudAssemblySource = await toolkit.fromCdkApp("ts-node app.ts");

// Generate a cloud assembly
const cloudAssembly = await toolkit.synth(cloudAssemblySource);

// Use the cloud assembly for operations
await toolkit.list(cloudAssembly);
await toolkit.deploy(cloudAssembly);
await toolkit.diff(cloudAssembly);

// Query information from the cloud assembly
const template = cloudAssembly.getStack("my-stack").template;
```

**Tip**
Using a cloud assembly can optimize performance when you need to perform multiple operations, since synthesis only happens once. For more information about managing cloud assemblies, including caching and disposal, see [Create and manage cloud assemblies](toolkit-library-configure-ca.md#toolkit-library-configure-ca-cache).

## Viewing stack information with list
<a name="toolkit-library-actions-list"></a>

The `list` action retrieves information about the stacks in your CDK application, including their dependencies and current status. Use this action to inspect your infrastructure before deployment or to generate reports.

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

// Get information about specific stacks
const stackDetails = await toolkit.list(cloudAssemblySource, {
  stacks: {
    strategy: StackSelectionStrategy.PATTERN_MUST_MATCH,
    patterns: ["my-stack"], // Only include stacks matching this pattern
  }
});

// Process the returned stack information
for (const stack of stackDetails) {
  console.log(`Stack: ${stack.id}, Dependencies: ${stack.dependencies}`);
}
```

## Provisioning infrastructure with deploy
<a name="toolkit-library-actions-deploy"></a>

The `deploy` action provisions or updates your infrastructure in AWS using the cloud assembly produced during synthesis. For an introduction to deploying, see [Deploy AWS CDK applications](deploy.md). You can control deployment options such as stack selection, parameter values, and rollback behavior.

```
// Deploy stacks with parameter values
await toolkit.deploy(cloudAssemblySource, {
  parameters: StackParameters.exactly({
    "MyStack": {
      "BucketName": "amzn-s3-demo-bucket"
    }
  })
});
```

The deploy action supports different deployment methods to accommodate various workflows. For most scenarios, especially in production environments, we recommend using the default deployment method which uses CloudFormation change sets. For development environments where iteration speed is important, you can use alternative methods like hotswap.

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

// Deploy using default deployment method (recommended for production)
await toolkit.deploy(cloudAssemblySource, {
  parameters: StackParameters.exactly({
    "MyStack": {
      "BucketName": "amzn-s3-demo-bucket"
    }
  })
});

// For development environments only: Deploy with hotswap for faster iterations
// Note: We recommend using default deployment methods for production environments
await toolkit.deploy(cloudAssemblySource, {
  deploymentMethod: { method: "hotswap", fallback: true }, // Faster but introduces drift
  stacks: {
    strategy: StackSelectionStrategy.PATTERN_MUST_MATCH,
    patterns: ["dev-stack"]
  }
});
```

## Preserving deployed resources with refactor
<a name="toolkit-library-actions-refactor"></a>

**Important**
The refactor action is in preview release and is subject to change.

The `refactor` action preserves deployed resources when you refactor CDK code such as renaming constructs or moving them between stacks. Without this feature, these changes would cause CloudFormation to replace resources, potentially leading to service interruptions or data loss.

The refactor action automatically computes mappings by comparing your current code with the deployed state. It verifies that your CDK application contains exactly the same set of resources as the deployed state, differing only in their locations in the construct tree. If it detects any resource additions, deletions, or modifications, the refactoring operation will be rejected with an error message.

Once it computes the mappings, the refactor action uses CloudFormation’s refactoring API to update the logical IDs of resources without replacing them. If it encounters ambiguous mappings (where multiple possible mappings exist), you can provide explicit overrides to resolve these ambiguities.

```
// Perform refactoring operation to preserve resources
await toolkit.refactor(cloudAssemblySource);

// With optional overrides to resolve ambiguities
await toolkit.refactor(cloudAssemblySource, {
  overrides: {
    "environments": [
      {
        "account": "123456789012",
        "region": "us-east-2",
        "resources": {
          "StackA.OldName": "StackA.NewName"
        }
      }
    ]
  }
});
```

**Important**
Refactoring operations must be performed separately from other actions, such as adding new resources, deleting resources, or modifying resource properties. If you need to make such changes, you should first deploy those changes separately, and then use refactoring to reorganize your resources.

**Tip**
For more information about CDK refactoring, including how it works and when to use it, see [Preserve deployed resources when refactoring CDK code](refactor.md).

## Reverting failed deployments with rollback
<a name="toolkit-library-actions-rollback"></a>

The `rollback` action returns a stack to its last stable state when a deployment fails and cannot be automatically reversed. Use this action to recover from failed deployments that require manual intervention.

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

// Roll back stacks to their last stable state
await toolkit.rollback(cloudAssemblySource, {
  orphanFailedResources: false, // When true, removes failed resources from CloudFormation management
  stacks: {
    strategy: StackSelectionStrategy.PATTERN_MUST_MATCH,
    patterns: ["failed-stack"]
  }
});
```

## Monitoring changes with watch
<a name="toolkit-library-actions-watch"></a>

The `watch` action continuously monitors your CDK app for local file changes and automatically performs deployments or hotswaps. This creates a file watcher that runs until your code exits or is terminated.

**Warning**
Hotswap deployments update resources directly without going through CloudFormation when possible, making updates faster during development. This is enabled by default for the `watch` command. While this speeds up the development cycle, it introduces drift between your CloudFormation templates and deployed resources. Therefore, we recommend that you don’t use hotswaps in production environments.

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

// Start watching for changes
const watcher = await toolkit.watch(cloudAssemblySource, {
  include: ["lib/**/*.ts"], // Only watch TypeScript files in the lib directory
  exclude: ["**/*.test.ts"], // Ignore test files
  deploymentMethod: { method: "hotswap" }, // This is the default, shown here for clarity
  stacks: {
    strategy: StackSelectionStrategy.ALL // Watch all stacks
  }
});

// Later in your code, you can explicitly stop watching:
// await watcher.dispose();
```

The watch function returns an `IWatcher` object that allows you to explicitly control when to stop watching. Call the `dispose()` method on this object when you want to end the watch process.

## Removing infrastructure with destroy
<a name="toolkit-library-actions-destroy"></a>

The `destroy` action removes CDK stacks and their associated resources from AWS. Use this action to clean up resources when they’re no longer needed.

**Important**
The destroy action permanently removes resources without prompting for confirmation, unlike the CLI version of this command. Make sure you have backups of any important data before destroying stacks.

```
import { StackSelectionStrategy } from '@aws-cdk/toolkit-lib';

// Remove specific stacks and their resources
await toolkit.destroy(cloudAssemblySource, {
  stacks: {
    strategy: StackSelectionStrategy.PATTERN_MUST_MATCH,
    patterns: ["dev-stack"], // Only destroy stacks matching this pattern
  }
});
```
