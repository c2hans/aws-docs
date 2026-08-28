---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/spank_install.html
---

# Install SPANK plugins on AWS PCS
<a name="spank_install"></a>

Follow the plugin's documentation to install SPANK plugins on your AMI.

Compile SPANK plugins for the specific Slurm version on your cluster. The Slurm installer provided by AWS PCS stores Slurm in `/opt/aws/pcs/scheduler/slurm-{{version}}`. When you compile the plugin, specify the Slurm version.

The following example shows how to specify the Slurm version for some plugins:

```
export CFLAGS="-I/opt/aws/pcs/scheduler/slurm-{{version}}/include"
```

If you have multiple Slurm versions in the AMI, compile the plugin for each version. Store the compiled plugins in versioned folders.

The following example shows how to specify the destination folder for some plugins:

```
export DESTDIR="{{your-preferred-versioned-path}}"
```

**Important**
Plugins might require different variables. See the official documentation for the plugin that you're installing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
