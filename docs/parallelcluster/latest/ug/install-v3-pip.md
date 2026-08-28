---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-pip.html
---

# Installing AWS ParallelCluster in a non-virtual environment using pip
<a name="install-v3-pip"></a>

You can also install AWS ParallelCluster in a non-virtual environment using pip, a package manager for Python packages.

**Prerequisites**
+ AWS ParallelCluster requires Python 3.9 or later. If you don't already have it installed, [download a compatible version](https://www.python.org/downloads/) for your platform at [python.org](https://www.python.org/).

**Install AWS ParallelCluster**

1. Use `pip` to install AWS ParallelCluster.

   ```
   $ python3 -m pip install "aws-parallelcluster" --upgrade --user
   ```

   When you use the `--user` switch, `pip` installs AWS ParallelCluster to `~/.local/bin`.

1. Install Node Version Manager and the latest Long-Term Support (LTS) Node.js version. AWS Cloud Development Kit (AWS CDK) requires Node.js for CloudFormation for template generation.
**Note**
If your Node.js installation isn't working on your platform, you can install an LTS version prior to the latest LTS version. For more information, see the [Node.js release schedule](https://github.com/nodejs/release#release-schedule) and the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/work-with.html#work-with-prerequisites) prerequisites.

   ```
   $  nvm install --lts=Hydrogen
   ```

   ```
   $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
   $ chmod ug+x ~/.nvm/nvm.sh
   $ source ~/.nvm/nvm.sh
   $ nvm install --lts
   $ node --version
   ```

1. Verify that AWS ParallelCluster installed correctly.

   ```
   $ pcluster version
   {
     "version": "3.15.1"
   }
   ```

1. To upgrade to the latest version, run the installation command again.

   ```
   $ python3 -m pip install "aws-parallelcluster" --upgrade --user
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
