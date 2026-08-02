---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/codecatalyst-overview.html
---

# Working with Amazon CodeCatalyst resources from the AWS Toolkit for Visual Studio with Amazon Q
<a name="codecatalyst-overview"></a>

The following sections provide an overview of the Amazon Amazon CodeCatalyst resource management features that are available for the AWS Toolkit for Visual Studio with Amazon Q.

**Topics**
+ [Clone a repository](#codecatalyst-overview-clone)

## Clone a repository
<a name="codecatalyst-overview-clone"></a>

CodeCatalyst is a cloud-based service that requires you to be connected to the cloud to work on CodeCatalyst projects. To work on a project locally, you can clone CodeCatalyst repositories to your local machine and sync with your CodeCatalyst project the next time that you connect to the cloud.

To clone a repository to your local machine, complete the following steps.

1. From the **Git** menu item in Visual Studio, choose **Clone Repository...**.

1. From the **Browse a Repository** section, select **Amazon CodeCatalyst** as the provider.
**Note**
If the **Connection** section displays a `Not Connected` message, complete the steps in the [Authentication and access: AWS Builder ID](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/builder-id.html) section of this User Guide before proceeding.

1. Choose the **Space** and **Project** that you want to clone a repository from.

1. From the **Repositories** section, choose the repository that you want to clone.

1. From the **Path** section, choose the folder you want to clone your repository to.
**Note**
This folder must initially be empty to clone successfully.

1. Select **Clone** to begin cloning the repository.

1. After the repository has been cloned, Visual Studio will load your cloned solution
**Note**
If Visual Studio does not open the solution in the cloned repository, your Visual Studio options can be adjusted from the **Automatically load the solution when opening a Git repository** setting, located in the **Git Global Settings**, of the **Source Control** menu.
