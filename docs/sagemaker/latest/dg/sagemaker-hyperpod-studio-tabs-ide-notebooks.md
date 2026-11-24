---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-tabs-ide-notebooks.html
---

# IDE and Notebooks

Amazon SageMaker HyperPod provides a view of the development spaces running on your cluster. Spaces are self-contained environments for running JupyterLab or Code Editor IDEs directly on your HyperPod EKS cluster. You can create, configure, start, stop, and open spaces directly from Studio.

In Amazon SageMaker Studio, choose **HyperPod** in the navigation pane, select a cluster, and open the **IDE and Notebooks** tab.

Key capabilities available through Studio include:
+ Create spaces with configurable compute, storage, and image settings through a guided form.
+ View all spaces in a searchable table showing name, application type, status, access type, storage, GPU, and vCPU allocations.
+ Start and stop spaces with a single click to manage compute costs.
+ Open spaces directly in the browser (JupyterLab or Code Editor) or connect through a Remote IDE. For more information, see [Remote access using SSH over SSM](vscode-access.md).
+ Delete spaces that are no longer needed.
+ Select namespaces to organize spaces by team with resource quotas and governance settings.
+ Apply templates for consistent space configurations across teams.

For information on creating a domain, see [Guide to getting set up with Amazon SageMaker AI](gs.md).

## Prerequisites
<a name="sagemaker-hyperpod-studio-tabs-ide-notebooks-prerequisites"></a>
+ Install the HyperPod add-on on your cluster. For more information, see [Install SageMaker AI Spaces Add-on](operator-install.md).
+ Set up your cluster to be used in Studio. For more information, see [Setting up an Amazon EKS cluster in Studio](sagemaker-hyperpod-studio-setup-eks.md).
+ To enable private spaces among users with the same execution role, you must ensure the `ExecutionRoleSessionNameMode` flag is set to `USER_IDENTITY`. With the HyperPod Spaces feature, the username used inside the space is automatically derived from the Studio authentication context, allowing users to have a consistent identity across Studio and HyperPod Spaces without requiring additional sign-in.

  For Studio domains configured in IAM authentication mode, the Spaces username is derived from the IAM role session name. This corresponds to the IAM session used to launch Studio, either through the AWS Management Console or through a presigned Studio URL. For Studio domains configured in IAM Identity Center authentication mode, the Spaces username is the sanitized authenticated IAM Identity Center username.

  This is set by default for new domains and can be overridden for older domains. This setting can also be overridden for each user profile. For more information, see [Execution role session name mode](execution-roles-and-spaces.md#sagemaker-execution-role-session-name).

## How it works
<a name="sagemaker-hyperpod-studio-tabs-ide-notebooks-how-it-works"></a>

Once the add-on is installed and access is configured, navigate to your HyperPod cluster in Studio and select the **IDE and Notebooks** tab to see the spaces management interface.

### Creating a space
<a name="sagemaker-hyperpod-studio-tabs-ide-notebooks-create"></a>

To create a new space, choose **Create space**. The creation form allows you to configure the following:
+ **Namespace**: Select your team namespace with resource quotas and governance settings. This determines your available compute allocation.
+ **Space settings:**
  + **Template**: Select a pre-configured template (for example, JupyterLab or Code Editor) to apply default settings.
  + **Compute**: Choose between GPU and CPU configurations with fine-grained control over GPUs, vCPUs, and memory.
  + **GPU partition**: If fractional GPU is enabled, you can choose a partition to use for your workspace.
  + **Image**: Select from available container images or custom images configured by your administrator.
  + **EBS space storage**: Configure persistent storage for your notebooks and data.
+ **Task governance**: When enabled for the namespace, spaces integrate with HyperPod task governance for resource management and priority scheduling. For more information, see [Task governance for Interactive Spaces on HyperPod](task-governance.md).

### Managing spaces
<a name="sagemaker-hyperpod-studio-tabs-ide-notebooks-manage"></a>

The spaces table provides a consolidated view of all your environments, including status and resource allocations.

From the **Actions** column, you can:
+ Stop a running space to release compute resources while preserving your data on EBS storage.
+ Open the space in your browser to launch the JupyterLab or Code Editor web interface.
+ Connect using a Remote IDE. For more information, see [Remote access using SSH over SSM](vscode-access.md).

### Connecting to your space
<a name="sagemaker-hyperpod-studio-tabs-ide-notebooks-connect"></a>

Spaces support two connection methods:

**Web UI access**

Choose **Open** from the spaces table to launch the IDE directly in your browser. This opens a fully functional JupyterLab or Code Editor interface hosted on your HyperPod cluster. No local software installation is required beyond a web browser. This is ideal for quick iterations, notebook-based exploration, and collaborative work. To enable Web UI access on your cluster, see [Web browser access](browser-access.md).

**Remote IDE connection**

Choose **Open in Remote IDE** from the spaces table to connect your local IDE to the space running on HyperPod. This provides a secure connection without requiring you to manage SSH keys or expose port 22. You get the full power of your local development environment while running code on HyperPod cluster compute. For more information, see [Remote access using SSH over SSM](vscode-access.md).
