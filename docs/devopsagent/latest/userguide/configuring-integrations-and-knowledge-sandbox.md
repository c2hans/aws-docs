---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-sandbox.html
---

# Set up a Sandbox

AWS DevOps Agent Sandbox (Sandbox) is a preview feature that gives AWS DevOps Agent a secure, isolated Linux environment where it can write and run code during investigations, chat conversations, and custom agent invocations. Some problems are faster and more reliable to solve with code than through reasoning alone. With Sandbox, the agent complements its reasoning with computation—for example, to analyze a large log file, calculate statistics across a set of metrics, or parse and correlate data from multiple sources.

Each sandbox is ephemeral and scoped to a single investigation, chat conversation, or custom agent invocation, so the code the agent runs stays isolated from your other resources. You control the environment's outbound network access and the registries the agent installs packages from. By default, the sandbox restricts outbound network access: until you add an entry to the networking allowlist, it can reach only AWS service endpoints.

**Note**
** Sandbox is available in preview and is subject to change.

Sandbox is available in all commercial AWS Regions (in the `aws` partition). For more information, see [Feature availability by Region](about-aws-devops-agent-supported-regions.md#feature-availability-by-region).

## How Sandbox works
<a name="how-sandbox-works"></a>

When you configure Sandbox for an Agent Space, AWS DevOps Agent automatically provisions a fresh Linux environment while it works on an investigation, a chat conversation, or a custom agent invocation. In this environment, the agent can run shell commands and read and write files, then read the results back into its analysis. The environment lasts only for as long as the agent using it is running, and no two investigations, chat conversations, or invocations share one.

The environment comes with pre-configured AWS profiles for the AWS accounts connected to your Agent Space. The agent can use these profiles to make AWS CLI and boto3 (AWS SDK for Python) calls to those accounts, scoped to the same permissions the agent already has. This lets the agent query and correlate AWS resources programmatically with code.

The agent can also make HTTP requests from the sandbox—using command line tools or Python and Node.js libraries—to any host and path permitted by your networking policy.

Two settings control what the environment can do:
+ **Networking policy** – An explicit allowlist of the hosts, HTTP methods, and paths the environment may reach. An empty allowlist denies all outbound requests except requests to AWS service endpoints and to package registries you configure.
+ **Package registries** – The registry that Python (`pip` and `uv`) and Node.js (`npm`) install packages from. The agent installs the packages it needs at runtime.

### Sandbox environment isolation
<a name="sandbox-environment-isolation"></a>

AWS DevOps Agent runs each sandbox in an isolated Lambda MicroVM. Each MicroVM is scoped to a single investigation, chat conversation, or custom agent invocation. AWS DevOps Agent discards it when that work ends. When the agent makes AWS CLI or SDK calls from the sandbox, it routes those calls through a proxy. That proxy limits the calls to read-only operations, so sandbox code cannot modify or delete your AWS resources.

### Skills in the sandbox
<a name="skills-in-the-sandbox"></a>

With Sandbox enabled, the agent reads your [Skills](about-aws-devops-agent-devops-agent-skills-index.md) from the sandbox's filesystem rather than from a virtual filesystem. This changes how the agent works with skills in two ways:
+ **Search and read with command line tools** – The agent can use standard command line tools to search across your skills and read their files, instead of loading them through a virtual filesystem. This helps it find and apply the right skill for the task.
+ **Run bundled code** – The agent can run and adapt code bundled with a skill. Without Sandbox, a skill can include only non-executable files such as Markdown instructions, references, and data files. With Sandbox, a skill can include executable code that the agent can run in the environment.

## Before you begin
<a name="before-you-begin"></a>

Sandbox is not configured by default, so until you opt in, the agent cannot run code. Until then, the **Sandbox** section displays the message "Sandbox is not configured. To opt in, configure sandbox." and a **Configure** button. The following image shows the **Sandbox** section before you configure it.

![Sandbox section with the message "Sandbox is not configured. To opt in, configure sandbox." and a Configure button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/ce021e90bdc9.png)

Before you configure Sandbox, determine the following:
+ Where the agent installs Python and Node.js packages from: the AWS managed registry (in [supported Regions](about-aws-devops-agent-supported-regions.md#feature-availability-by-region)), a registry you provide a URL for, or none.
+ The hosts, HTTP methods, and paths the agent's code needs to reach, if any.

## Configure Sandbox for an Agent Space
<a name="configure-sandbox-for-an-agent-space"></a>

1. Sign in to the AWS Management Console and open the AWS DevOps Agent console.

1. Select your Agent Space and choose the **Capabilities** tab.

1. In the **Sandbox** section, choose **Configure**.

1. Configure package registries and a networking policy as described in the following sections. Then choose **Next**.

1. On the **Review and confirm** page, check your configuration. Choose **Save**.

After you configure Sandbox, the **Sandbox** section shows the registry for each package manager and your allowlist entries. To change the configuration, choose **Edit**. To remove it, see [Remove Sandbox](#remove-sandbox).

### Configure package registries
<a name="configure-package-registries"></a>

In the **Package registries** section, choose a registry for Python packages (`pip` and `uv`) and one for Node.js packages (`npm`). The options for each are:
+ **AWS managed** – A mirror of the public PyPI or npm registry that AWS DevOps Agent maintains. Available only in [some Regions](about-aws-devops-agent-supported-regions.md#feature-availability-by-region).
+ **Custom** – An HTTPS URL for a registry that you trust, such as a private registry that you manage or the public PyPI or npm registry. Don't include a secret in the URL.
+ **None** – The agent can't install packages for that language.

The following example sets the AWS managed registry for `pip`, a custom registry for `npm`, and an empty networking allowlist. Replace the following values with your own:
+ `<AGENT_SPACE_ID>` — The ID of the Agent Space to configure.
+ `<REGION>` — The AWS Region code for your Agent Space, such as `us-east-1`.

The `update-association` command accepts the same configuration.

```
aws devops-agent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id sandbox \
  --configuration '{
    "sandbox": {
      "name": "default",
      "config": {
        "managed": {
          "packageRegistries": {
            "pypi": { "awsManaged": {} },
            "npm": { "custom": { "uri": "https://registry.example.com/npm/" } }
          },
          "networking": { "restricted": { "allowlist": [] } }
        }
      }
    }
  }' \
  --region <REGION>
```

### Configure the networking policy
<a name="configure-the-networking-policy"></a>

The sandbox restricts outbound requests to an explicit allowlist. An empty allowlist denies all outbound requests except requests to AWS service endpoints and to package registries you configure. To let the environment reach any other host, add an allowlist entry for it.

Choose **Add entry**, then configure the following for the allowlist entry:
+ **Host pattern** – The host the entry applies to. Partial label matching isn't supported. Use one of the following forms:
  + `**` – All hosts.
  + `*.example.com` – One subdomain level.
  + `**.example.com` – Any subdomain depth.
  + `example.com` – An exact host.
+ **HTTP methods** – The HTTP methods permitted for this host. Choose one or more methods, such as `GET` and `OPTIONS`, from the dropdown list.
+ **Path patterns** – The paths permitted for this host. Choose **Add path** to add one or more patterns:
  + `*` matches one segment, such as `/repos/*/pulls`.
  + Partial matching is allowed, such as `/users/aws-*/`.
  + `/**` permits all sub-paths.
  + Query parameters are ignored.

For example, an entry might allow `GET` and `OPTIONS` requests to `*.github.com` for the paths `/aws/**` and `/awslabs/**`.

Choose **Add entry** for each additional host the agent's code needs to reach. To remove an entry, choose **Remove**.

## Remove Sandbox
<a name="remove-sandbox"></a>

To opt out, select your Agent Space, go to the **Capabilities** tab, and in the **Sandbox** section, choose **Remove**. In the **Remove sandbox configuration?** dialog, choose **Remove**. Without a Sandbox configuration, the agent doesn't provision sandbox environments for investigations, chat conversations, or custom agent invocations.

## Sandbox configuration limits
<a name="sandbox-configuration-limits"></a>

The following limits apply to each Sandbox configuration during preview.

| Limit | Value |
| --- | --- |
| Networking allowlist entries | 100 |
| Path patterns per allowlist entry | 1–50 |
| HTTP methods per allowlist entry | 1–7, each listed once |
| Host pattern length | 253 characters |
| Path pattern length | 256 characters |
| Registry URL length | 2,048 characters |

## Security considerations
<a name="security-considerations"></a>

AWS DevOps Agent isolates each investigation, chat conversation, and custom agent invocation in its own sandbox environment, so code and data from one are never shared with another. AWS DevOps Agent inspects and filters all traffic leaving the sandbox so that only safe, permitted requests reach their destinations. It permits requests to AWS service endpoints and to package registries you configure, and requests that match your networking allowlist. It denies all other requests.

### Security best practices
<a name="security-best-practices"></a>

The agent writes and runs code in the sandbox, so keep the following in mind when you configure Sandbox:
+ **Keep the allowlist minimal.** Add allowlist entries only for the specific hosts, methods, and paths the agent needs.
+ **Scope allowlist entries narrowly.** Use exact host patterns and specific path patterns rather than broad wildcards such as `**` and `/**`, and grant only the HTTP methods that are required.
+ **Use package registries you trust.** Choose the **AWS managed** registry or a **Custom** registry that you manage. A registry that you manage also lets you control which packages and versions the agent can install. Choose **None** for a language the agent doesn't need.

For more information about the AWS DevOps Agent security model, see [AWS DevOps Agent Security](aws-devops-agent-security.md).
