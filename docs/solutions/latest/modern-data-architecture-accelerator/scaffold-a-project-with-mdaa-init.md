---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/scaffold-a-project-with-mdaa-init.html
---

# Scaffold a project with `mdaa init`
<a name="scaffold-a-project-with-mdaa-init"></a>

Starting with MDAA 1.8.0, the CLI has an `init` action that scaffolds a new configuration project from a starter kit, so you no longer need to clone the MDAA repository and copy the `starter_kits/` files by hand. `init` runs interactively: it prompts you to choose a starter kit, fills in the `<YOUR_…​>` placeholder values in the generated config, pins `mdaa_version` in `mdaa.yaml` so deploys use the same version that generated the schemas, and writes versioned JSON schemas and module documentation under `.mdaa/<version>/` along with AI steering files for Kiro, Claude Code, and GitHub Copilot.

To scaffold a new project into an empty directory, choosing the starter kit interactively:

```
npx @aws-mdaa/cli init ./my-data-platform
```

To scaffold a specific starter kit without prompts, pass `--starter-kit` and `--no-prompt`:

```
npx @aws-mdaa/cli init ./my-data-platform --starter-kit basic_datalake --no-prompt
```

To add the schemas, module documentation, and AI steering files to an existing config directory (one that already contains an `mdaa.yaml`), use `--enhance`:

```
npx @aws-mdaa/cli init ./existing-config --enhance
```

MDAA-owned files are always regenerated. A user-owned file such as `CLAUDE.md` that you have edited since it was generated prompts before being overwritten; pass `--overwrite` to replace those files without prompting, or `--no-prompt` to leave them untouched.

After scaffolding, edit the generated `mdaa.yaml` and module config files to match your environment (see the per-starter-kit sections below and the `TODO` markers described above), then deploy with `npx @aws-mdaa/cli deploy`.

**Note**
The clone-and-copy workflow shown in each starter-kit section below still works and remains useful when developing against the MDAA source. `mdaa init` is the recommended path for a new configuration project because it also generates version-pinned schemas and editor validation for you.

The following sections provide detailed information about each available starter package, including architecture components, deployment instructions, and usage guidelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
