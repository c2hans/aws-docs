---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

## Setting up MDAA Dev Environment
<a name="setting-up-mdaa-dev-environment"></a>

1. Clone this repo.

1. Install NPM/Node

1. NPM Install CDK, Lerna

1. Authenticate to the MDAA NPM Repo

1. From the root of the repo, run npm install:

   ```
   npm install
   ```

1. After making code changes, run a build/test using lerna:

   ```
   lerna run build && lerna run test
   ```

   Alternatively, you can run `npm run build && npm run test` in each individual package you have modified.

### Version Requirements
<a name="version-requirements"></a>

MDAA has specific version requirements for development:
+  **Node.js**: Version 22.x or higher
+  **NPM**: Version 10.x or higher
+  **Docker**: Required for building Lambda layers and certain modules (e.g., GAIA)

## Testing
<a name="testing"></a>

### Testing Overview
<a name="testing-overview"></a>

The testing approach for MDAA changes varies depending on the type of package being tested (App, Stack, or Construct). Before testing, ensure that the entire MDAA repo is cloned, bootstrapped, and built.

### Testing Constructs and Stacks
<a name="testing-constructs-and-stacks"></a>

Constructs and Stacks should be tested via unit testing using the CDK Assertions framework. This framework can be used to ensure that the CFN resources produced by a MDAA construct or stack are defined as expected in the resulting CFN template. Specific attention should be paid in these unit tests to any resource property which has compliance implications.

#### Example Construct/Stack Unit Tests
<a name="example-constructstack-unit-tests"></a>

```
import { MdaaTestApp } from "@aws-mdaa/testing";
import { Stack } from "aws-cdk-lib";
import { MdaaKmsKey } from '@aws-mdaa/kms-constructs';
import { Match, Template } from "aws-cdk-lib/assertions";
import { NagSuppressions } from "cdk-nag";
import { MdaaBucket, MdaaBucketProps } from "../lib";

describe( 'MDAA Construct Compliance Tests', () => {
    const constructTestApp = new MdaaTestApp()
    const constructTestStack = new Stack( constructTestApp, "test-stack" )

    const testKey = MdaaKmsKey.fromMdaaKeyArn( constructTestStack, "test-key", "arn:test-partition:kms:test-region:test-account:key/test-key" )

    const testContstructProps: MdaaBucketProps = {
        naming: constructTestApp.naming,
        bucketName: "test-bucket",
        encryptionKey: testKey
    }

    const testConstruct = new MdaaBucket( constructTestStack, "test-construct", testContstructProps )
    NagSuppressions.addResourceSuppressions(
        testConstruct,
        [
            { id: 'NIST.800.53.R5-S3BucketReplicationEnabled', reason: 'MDAA Data Lake does not use bucket replication.' },
            { id: 'HIPAA.Security-S3BucketReplicationEnabled', reason: 'MDAA Data Lake does not use bucket replication.' }
        ],
        true
    );
    constructTestApp.checkCdkNagCompliance( constructTestStack )
    const template = Template.fromStack( constructTestStack );

    test( 'BucketName', () => {
        template.hasResourceProperties( "AWS::S3::Bucket", {
            "BucketName": constructTestApp.naming.resourceName( "test-bucket" )
        } )
    } )

    test( 'DefaultEncryption', () => {
        template.hasResourceProperties( "AWS::S3::Bucket", {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "aws:kms",
                            "KMSMasterKeyID": testKey.keyArn
                        }
                    }
                ]
            }
        } )
    } )

} )
```

### Testing Apps
<a name="testing-apps"></a>

MDAA Apps can be developed and tested like any other CDK app. This typically involves a `cdk list/synth/diff/deploy` from within the App source directory, while also providing the necessary context values which would otherwise be provided by the MDAA framework. Executing the cdk command will result in the application source code being built. However, any changes made in underlying dependencies (such as stacks and constructs) would require either a `lerna run build` at the root of the MDAA repo, or `npm run build` in the package folder for each of the modified dependencies.

#### Example CDK Command Invoking a MDAA App
<a name="example-cdk-command-invoking-a-mdaa-app"></a>

```
cdk synth --require-approval never -c org="" -c env="" -c domain="" -c module_configs="" -c tag_configs=""  -c module_name="" --all
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
