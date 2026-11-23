---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/prerequisites.html
---

# Prerequisites

Before deploying this solution, ensure the following prerequisites are met.

## Build toolchain
<a name="build-toolchain"></a>

This solution is built with the AWS Cloud Development Kit (AWS CDK) in TypeScript. You can deploy it from macOS, Linux, or Windows. Install the following tools before you deploy:
+  [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/).
+  [Node.js](https://nodejs.org/en/) 20.x LTS or later (18.x minimum).
+  [npm](https://www.npmjs.com/), which is bundled with Node.js. npm installs the CDK dependencies and runs the build and tests. The AWS CDK CLI (version 2.236.0 or later) is installed as a project dependency by `npm ci`, and `deploy.sh` runs it with `npx`, so a global CDK install is not required.
+  [Docker](https://docs.docker.com/engine/) or [Finch](https://github.com/runfinch/finch). Make sure the container runtime is running before you deploy. The Prebid Server container image, including its Java (Amazon Corretto 21) and Maven build, is built inside the container runtime, so a local JDK or Maven install is not required. `deploy.sh` uses Finch when it is installed and running, and falls back to Docker otherwise. To use Finch with CDK commands that you run outside `deploy.sh`, set `export CDK_DOCKER=finch`.
+ AWS credentials configured in your environment with permissions equivalent to `AdministratorAccess`.

Python 3 with the `venv` module is required only for the functional and load tests and for the RTB Fabric Link helper that `deploy.sh` and `destroy.sh` run on the RTB Fabric path. The helper wrapper (`deployment/simulator-fabric-link.sh`) creates its own virtual environment and installs its dependencies automatically. Python is not required for the CDK build.

If you are using the AWS CDK for the first time in the target account and Region, bootstrap it from the `source/infrastructure` directory after you run `npm ci`:

```bash
npx cdk bootstrap --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess
```

## Container image source (optional)
<a name="prebuilt-container-image"></a>

The `prebid-server-deployment-on-aws.zip` asset on the [prebid-server-deployment-on-aws releases page](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/releases) on the GitHub website contains the solution source code only. It doesn’t include a pre-built container image. By default, `deploy.sh` builds the Prebid Server container image from `deployment/ecr/prebid-server` during deployment, which requires a running Docker or Finch container runtime. To skip the image build, pass `--container-image` with an Amazon ECR image URI or the path to a `tar.gz` file of an image that you built earlier. For details, see [Container image configuration](configure-the-solution.md#container-image-parameter).

## RTB Fabric region availability
<a name="rtb-fabric-region-availability"></a>

AWS RTB Fabric is not available in all AWS Regions. If you plan to deploy with RTB Fabric connectivity for the bidder simulator, verify that your target Region supports RTB Fabric before deployment.

**Important**
If RTB Fabric is not available in your target Region, use VPC peering as the fallback connectivity mode. The `deploy.sh` script supports both modes via the `--simulator-connectivity` flag:
 `rtb-fabric` — Uses RTB Fabric Requester and Responder Gateways with a Fabric Link (recommended where available)
 `vpc-peering` — Uses VPC peering between the Prebid Server VPC and the Bidder Simulator VPC (fallback for non-RTB regions)

For the latest list of supported Regions, see the [AWS RTB Fabric product page](https://aws.amazon.com/rtb-fabric/).
