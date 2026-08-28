---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin.html
---

# Before you begin
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-before-you-begin"></a>

Before you start the installation process, follow the steps in this section to make sure that your environment is set up to successfully install agents on the right Kubernetes clusters.

**Ensure that your version of Kubernetes is supported**
Network Flow Monitor agent installation requires Kubernetes Version 1.25, or a more recent version.

**Ensure that you have installed required tools**
The scripts that you use for this installation process require that you install the following tools. If you don’t have the tools installed already, see the provided links for more information.
+ The AWS Command Line Interface (CLI). For more information, see [Installing or updating to the latest version of the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the AWS Command Line Interface Reference Guide.
+ The Helm package manager. For more information, see [Installing Helm](https://helm.sh/docs/intro/install/) on the Helm website.
+ The `kubectl` command line tool. For more information, see [Install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) on the Kubernetes website.
+ The `make` Linux command dependency. For more information, see the following blog post: [ Intro to make Linux Command: Installation and Usage](https://ioflood.com/blog/install-make-command-linux/). For example, do one of the following:
  + For Debian based distributions, such as Ubuntu, use the following command: `sudo apt-get install make`
  + For RPM-based distributions, such as CentOS, use the following command: `sudo yum install make`

**Ensure that you have valid, correctly configured KubeConfig environment variables**
Network Flow Monitor agent installation uses the Helm package manager tool, which uses the kubeconfig variable, `$HELM_KUBECONTEXT`, to determine the target Kubernetes clusters to work with. Also, be aware that when Helm runs installation scripts, by default, it references the standard `~/.kube/config` file. You can change the configuration environment variables, to use a different config file (by updating `$KUBECONFIG`) or to define the target cluster you want to work with (by updating `$HELM_KUBECONTEXT`).

**Create a Network Flow Monitor Kubernetes namespace**
The Network Flow Monitor agent's Kubernetes application installs its resources into a specific namespace. The namespace must exist for the installation to succeed. To ensure that the required namespace is in place, you can do one of the following:
+ Create the default namespace, `amazon-network-flow-monitor`, before you begin.
+ Create a different namespace, and then define it in the `$NAMESPACE` environment variable when you run the installation to make targets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
