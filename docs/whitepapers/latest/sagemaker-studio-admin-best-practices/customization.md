---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/customization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Customization
<a name="customization"></a>

## Lifecycle configuration
<a name="lifecycle-configuration"></a>

 Lifecycle configurations are shell scripts initiated by SageMaker AI Studio lifecycle events, such as starting a new SageMaker AI Studio notebook. You can use these shell scripts to automate customization for your SageMaker AI Studio environments, such as installing custom packages, Jupyter extension for auto-shutdown of inactive notebook apps, and setting up Git configuration. For detailed instructions on how to build lifecycle configurations, refer to this blog: [Customize Amazon SageMaker AI Studio using Lifecycle Configurations](https://aws.amazon.com/blogs/machine-learning/customize-amazon-sagemaker-studio-using-lifecycle-configurations/).

## Custom images for SageMaker AI Studio notebooks
<a name="custom-images-for-sagemaker-studio-notebooks"></a>

 Studio notebooks come with a set of pre-built images, which consist of the [Amazon SageMaker AI Python SDK](https://sagemaker.readthedocs.io/en/stable/) and the latest version of the IPython runtime or kernel. With this feature, you can bring your own custom images to Amazon SageMaker AI notebooks. These images are then available to all users authenticated into the domain.

 Developers and data scientists may require custom images for several different use cases:
+  Access to specific or latest versions of popular ML frameworks such as TensorFlow, MXNet, PyTorch, or others.
+  Bring custom code or algorithms developed locally to SageMaker AI Studio notebooks for rapid iteration and model training.
+  Access to data lakes or on-premises data stores via APIs. Admins need to include the corresponding drivers within the image.
+  Access to a backend runtime (also called kernel), other than IPython (such as R, Julia, or [others](https://github.com/aws-samples/sagemaker-studio-custom-image-samples)). You can also use the approach outlined to install a custom kernel.

 For detailed instructions on how to build a custom image, refer to [Create a custom SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-create.html).

## JupyterLab extensions
<a name="jupyterlab-extensions"></a>

 With SageMaker AI Studio JuypterLab 3 Notebook, you can take advantage of the ever-growing community of open-source JupyterLab extensions. This section highlights a few that fit naturally into the SageMaker AI developer workflow, but we encourage you to [browse the available extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#installing-an-extension) or even [create your own](https://jupyterlab.readthedocs.io/en/stable/extension/extension_tutorial.html).

 JupyterLab 3 now makes the [process of packaging and installing extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#installing-extensions) significantly easier. You can install the aforementioned extensions through bash scripts. For example, in SageMaker AI Studio, [open the system terminal from the Studio launcher](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launcher.html) and run the following commands. In addition, you can automate the installation of these extensions using [lifecycle configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html) so they’re persisted between Studio restarts. You can configure this for all the users in the domain or at an individual user level.

 For example, to install an extension for an Amazon S3 file browser, run the following commands in the system terminal and be sure the refresh your browser:

```
conda init
conda activate studio
pip install jupyterlab_s3_browser
jupyter serverextension enable --py jupyterlab_s3_browser
conda deactivate
restart-jupyter-server
```

 For more information on extension management, including how to write lifecycle configurations that work for both versions 1 and 3 of JupyterLab notebooks for backward compatibility, refer to [Installing JupyterLab and Jupyter Server extensions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jl.html#studio-jl-install).

## Git repositories
<a name="git-repositories"></a>

SageMaker AI Studio comes pre-installed with a Jupyter Git extension for users to enter a bespoke URL of a Git repository, clone it to your EFS directory, push changes, and view commit history. Administrators can configure suggested git repos at the domain level so that they show up as drop-down selections for the end users. Refer to [Attach Suggested Git Repos to Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-git-attach.html) for up-to-date instructions.

If a repository is private, the extension will ask the user to enter their credentials into the terminal using the standard git installation. Alternatively, the user can store ssh credentials on their individual EFS directory for easier management.

## Conda environment
<a name="conda-environments"></a>

SageMaker AI Studio notebooks use Amazon EFS as a persistent storage layer. Data scientists can make use of the persistent storage to create custom conda environments and use these environments to create kernels. These kernels are backed by EFS, and are persistent between kernel, app, or Studio restarts. Studio automatically picks up all valid environments as KernelGateway kernels.

The process to create a conda environment is straightforward for a data scientist, but the kernels take about a minute to populate on the kernel selector. To create an environment, run the following in a system terminal:

```
mkdir -p ~/.conda/envs
conda create --yes -p ~/.conda/envs/custom
conda activate ~/.conda/envs/custom
conda install -y ipykernel
conda config --add envs_dirs ~/.conda/envs
```

For detailed instructions, refer to the *Persist Conda environments to the Studio EFS volume* section in [Four approaches to manage Python packages in Amazon SageMaker Studio notebooks](https://aws.amazon.com/blogs/machine-learning/four-approaches-to-manage-python-packages-in-amazon-sagemaker-studio-notebooks/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
