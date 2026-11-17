---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution and additional details for [testing](testing.md).

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws) to download the source files for this solution and to share your customizations with others.

The Guidance for Deploying a Prebid Server on AWS templates are generated using the [AWS CDK](https://aws.amazon.com/cdk/) in TypeScript. See the [README.md](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/blob/main/README.md) file for additional information.

### Project layout, build, and tests
<a name="project-layout-and-build"></a>

The CDK app and its constructs are in the `source/infrastructure` directory:
+  `app.ts` — The CDK app entry point.
+  `lib/prebid_server/` — The constructs for the Prebid Server stack (`prebid-server-deployment-on-aws`).
+  `lib/bidder_simulator/` — The construct for the optional bidder simulator stack (`BiddingServerSimulator`).
+  `lib/shared/` — Shared helpers, including `stack-constants.ts`.
+  `test/lib/` — Jest unit tests that mirror the `lib/` directory.

Run the following commands from the `source/infrastructure` directory:

```
# Install dependencies and compile the TypeScript CDK (tsc)
npm ci && npm run build

# Run the unit tests (jest)
npm test

# Synthesize all stacks as a local smoke test
npx cdk synth --all
```

 `npm test` exits with code `0` only when every test passes. On failure, it names each failing test with the assertion diff. Synthesis builds container image assets with Docker or Finch, so set `export CDK_DOCKER=finch` if you use Finch.

To build the Prebid Server container image on its own, run `deployment/ecr/build-image.sh` with `--base al2023` (the default for this script) or `--base alpine`.
