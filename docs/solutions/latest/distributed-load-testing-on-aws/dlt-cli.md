---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/dlt-cli.html
---

# DLT CLI
<a name="dlt-cli"></a>

The DLT CLI lets you interact with the Distributed Load Testing on AWS REST API directly from your terminal. It enables scripted automation of load tests, allowing you to list, inspect, and start test scenarios and query run results as part of repeatable workflows.

The CLI targets the same IAM-authorized API Gateway as the DLT web console, so any operation available in the browser-based interface can also be performed from the command line using the same underlying API and permissions model.

The CLI source code and full documentation live in the solution’s GitHub repository under the `source/cli` directory. The [DLT CLI README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/cli/README.md) on the GitHub website is the authoritative reference for installation, configuration, authentication, and the complete command reference.

## Key capabilities
<a name="dlt-cli-capabilities"></a>

| Command group | Description |
| --- | --- |
|  `configure`  | Configure the CLI with your DLT stack settings, either interactively or by importing an `aws-exports.json` file. |
|  `login`  | Authenticate with the DLT service and obtain the credentials needed to call the API. |
|  `logout`  | Remove stored credentials from the local machine. |
|  `token`  | Inspect and output authentication tokens and credential expiry status. |
|  `scenarios`  | Create, update, list, view details, start (re-run), cancel, and delete test scenarios. Creation supports simple HTTP tests, script file uploads (JMeter, k6, Locust), and recurring schedules. The `results` subcommand fetches the latest completed run’s metrics. It can also gate CI/CD pipelines using threshold flags. |
|  `runs`  | Query test run results, view run details, delete run history, manage baseline runs (set, get, and clear), compare runs against a baseline, and download run artifacts. |

The CLI supports three authentication modes: browser-based login using the Proof Key for Code Exchange (PKCE) flow through the Cognito Hosted UI; headless Secure Remote Password (SRP) authentication; and direct IAM credential authentication. For full setup details on each mode, see the [DLT CLI README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/cli/README.md) on the GitHub website.

The `scenarios start --wait` and `scenarios results` commands also support threshold flags (for example, error rate, p95/p99 latency, throughput, and baseline regression). These flags turn load-test outcomes into pass/fail CI/CD pipeline gates and use distinct exit codes to signal a breach. Data commands additionally support `table`, `json`, and `csv` output formats. For the complete flag and exit-code reference, see the [DLT CLI README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/cli/README.md) on the GitHub website.

## Installation and detailed reference
<a name="dlt-cli-reference"></a>

The CLI is distributed as a portable Node.js bundle that can be run directly, or you can build it from source using the repository. To get started, see the [DLT CLI README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/cli/README.md) on the GitHub website, which contains:
+ Installation instructions (portable bundle and build-from-source)
+ Configuration and authentication setup for all three auth modes
+ Full command reference with usage examples

## Quick start
<a name="dlt-cli-quick-start"></a>

**Note**
This quick-start assumes the DLT stack is already deployed.

### Option 1: Portable bundle (recommended)
<a name="option-1-portable-bundle-recommended"></a>

The fastest way to get started is the portable bundle. This does not require cloning the repository or any build steps:

```
# Download the portable bundle
curl -sLo /usr/local/bin/dlt \
  https://raw.githubusercontent.com/aws-solutions/distributed-load-testing-on-aws/main/deployment/cli/dlt-cli.mjs

# Make it executable
chmod +x /usr/local/bin/dlt

# Point the CLI at your deployed DLT stack
dlt configure

# Authenticate with the DLT service
dlt login

# Run a command (for example, list test scenarios)
dlt scenarios list
```

### Option 2: Build from source
<a name="option-2-build-from-source"></a>

If you prefer to build from source, clone the [repository](https://github.com/aws-solutions/distributed-load-testing-on-aws) first. The project uses npm workspaces, so run the following commands from the repository root:

```
# Install all workspace dependencies
npm install

# Build the CLI
npm run build -w source/cli

# Link the dlt command into your PATH
npm link -w source/cli

# Point the CLI at your deployed DLT stack
dlt configure

# Authenticate with the DLT service
dlt login

# Run a command (for example, list test scenarios)
dlt scenarios list
```
