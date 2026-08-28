---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.html
---

# `pcluster`
<a name="pcluster"></a>

`pcluster` is the primary AWS ParallelCluster CLI command. You use `pcluster` to launch and manage HPC clusters in the AWS Cloud.

```
pcluster [ -h ] ( create | update | delete | start | stop | status | list |
                  instances | ssh | dcv | createami | configure | version ) ...
```

## Arguments
<a name="pcluster.arguments"></a>

**`pcluster {{command}}`**
Possible choices: [`configure`](pcluster.configure.md), [`create`](pluster.create.md), [`createami`](pcluster.createami.md), [`dcv`](pcluster.dcv.md), [`delete`](pcluster.delete.md), [`instances`](pcluster.instances.md), [`list`](pcluster.list.md), [`ssh`](pcluster.ssh.md), [`start`](pcluster.start.md), [`status`](pcluster.status.md), [`stop`](pcluster.stop.md), [`update`](pcluster.update.md), [`version`](pcluster.version.md)

## Sub-commands:
<a name="pcluster.subcommands"></a>

**Topics**
+ [Arguments](#pcluster.arguments)
+ [Sub-commands:](#pcluster.subcommands)
+ [`pcluster configure`](pcluster.configure.md)
+ [`pcluster create`](pluster.create.md)
+ [`pcluster createami`](pcluster.createami.md)
+ [`pcluster dcv`](pcluster.dcv.md)
+ [`pcluster delete`](pcluster.delete.md)
+ [`pcluster instances`](pcluster.instances.md)
+ [`pcluster list`](pcluster.list.md)
+ [`pcluster ssh`](pcluster.ssh.md)
+ [`pcluster start`](pcluster.start.md)
+ [`pcluster status`](pcluster.status.md)
+ [`pcluster stop`](pcluster.stop.md)
+ [`pcluster update`](pcluster.update.md)
+ [`pcluster version`](pcluster.version.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
