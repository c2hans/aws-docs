---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3.html
---

# Deploy Kubernetes resources and packages using Amazon EKS and a Helm chart repository in Amazon S3
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3"></a>

*Sagar Panigrahi, Amazon Web Services*

## Summary
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-summary"></a>

This pattern helps you to manage Kubernetes applications efficiently, regardless of their complexity. The pattern integrates Helm into your existing continuous integration and continuous delivery (CI/CD)  pipelines to deploy applications into a Kubernetes cluster. Helm is a Kubernetes package manager that helps you manage Kubernetes applications. Helm charts help to define, install, and upgrade complex Kubernetes applications. Charts can be versioned and stored in Helm repositories, which improves mean time to restore (MTTR) during outages.

This pattern uses Amazon Elastic Kubernetes Service (Amazon EKS) for the Kubernetes cluster. It uses Amazon Simple Storage Service (Amazon S3) as a Helm chart repository, so that the charts can be centrally managed and accessed by developers across the organization.

## Prerequisites and limitations
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-prereqs"></a>

**Prerequisites**
+ An active Amazon Web Services (AWS) account with a virtual private cloud (VPC)
+ An Amazon EKS cluster
+ Worker nodes set up within the Amazon EKS cluster and ready to take workloads
+ Kubectl for configuring the Amazon EKS kubeconfig file for the target cluster in the client machine
+ AWS Identity and Access Management (IAM) access to create the S3 bucket
+ IAM (programmatic or role) access to Amazon S3 from the client machine
+ Source code management and a CI/CD pipeline

**Limitations**
+ There is no support at this time for upgrading, deleting, or managing custom resource definitions (CRDs).
+ If you are using a resource that refers to a CRD, the CRD must be installed separately (outside of the chart).

**Product versions**
+ Helm v3.6.3

## Architecture
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-architecture"></a>

**Target technology stack**
+ Amazon EKS
+ Amazon VPC
+ Amazon S3
+ Source code management
+ Helm
+ Kubectl

**Target architecture **

![Client Helm and Kubectl deploy a Helm chart repo in Amazon S3 for Amazon EKS clusters.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d3f993e6-4d96-4cb9-a075-c4debe431fd7/images/2f09f7bb-440a-4c4b-b29f-08d136d1ada4.png)

**Automation and scale**
+ AWS CloudFormation can be used to automate the infrastructure creation. For more information, see [Creating Amazon EKS resources with AWS CloudFormation](https://docs.aws.amazon.com/eks/latest/userguide/creating-resources-with-cloudformation.html) in the Amazon EKS documentation.
+ Helm is to be incorporated into your existing CI/CD automation tool to automate the packaging and versioning of Helm charts (out of scope for this pattern).
+ GitVersion or Jenkins build numbers can be used to automate the versioning of charts.

## Tools
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-tools"></a>

**Tools**
+ [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) – Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service for running Kubernetes on AWS without needing to stand up or maintain your own Kubernetes control plane. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.
+ [Helm](https://helm.sh/docs/) – Helm is a package manager for Kubernetes that helps you install and manage applications on your Kubernetes cluster.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [Kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) – Kubectl is a command line utility for running commands against Kubernetes clusters.

**Code**

The example code is attached.

## Epics
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-epics"></a>

### Configure and initialize Helm
<a name="configure-and-initialize-helm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the Helm client. | To download and install the Helm client on your local system, use the following command. <pre>sudo curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash</pre> | DevOps engineer |
| Validate the Helm installation. | To validate that Helm is able to communicate with the Kubernetes API server within the Amazon EKS cluster, run `helm version`. | DevOps engineer |

### Create and install a Helm chart in the Amazon EKS cluster
<a name="create-and-install-a-helm-chart-in-the-amazon-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Helm chart for NGINX. | To create a helm chart named `my-nginx` on the client machine, run `helm create my-nginx`. | DevOps engineer |
| Review the structure of the chart. | To review the structure of the chart, run the tree command `tree my-nginx/`. | DevOps engineer |
| Deactivate service account creation in the chart. | In `values.yaml`, under the `serviceAccount` section, set the `create` key to `false`. This is turned off because there is no requirement to create a service account for this pattern. | DevOps engineer |
| Validate (lint) the modified chart for syntactical errors. | To validate the chart for any syntactical error before installing it in the target cluster, run `helm lint my-nginx/`. | DevOps engineer |
| Install the chart to deploy Kubernetes resources. | To run the Helm chart installation, use the following command. <pre>helm install --name my-nginx-release --debug my-nginx/ --namespace helm-space </pre><br />The optional `debug` flag outputs all debug messages during the installation. The `namespace` flag specifies the namespace in which the resources part of this chart will be created. | DevOps engineer |
| Review the resources in the Amazon EKS cluster. | To review the resources that were created as part of the Helm chart in the `helm-space` namespace, use the following command. <pre>kubectl get all -n helm-space</pre> | DevOps engineer |

### Roll back to a previous version of a Kubernetes application
<a name="roll-back-to-a-previous-version-of-a-kubernetes-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify and upgrade the release. | To modify the chart, in `values.yaml`, change the `replicaCount` value to `2`. Then upgrade the already installed release by running the following command.<pre>helm upgrade my-nginx-release my-nginx/ --namespace helm-space</pre> | DevOps engineer |
| Review the history of the Helm release. | To list all the revisions for a specific release that have been installed using Helm, run the following command. <pre>helm history my-nginx-release</pre> | DevOps engineer |
| Review the details for a specific revision. | Before switching or rolling back to a working version, and for an additional layer of validation before installing a revision, view which values were passed to each of the revisions by using the following command.<pre>helm get --revision=2 my-nginx-release</pre> | DevOps engineer |
| Roll back to a previous version. | To roll back to a previous revision, use the following command. <pre>helm rollback my-nginx-release 1 </pre><br />This example is rolling back to revision number 1. | DevOps engineer |

### Initialize an S3 bucket as a Helm repository
<a name="initialize-an-s3-bucket-as-a-helm-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket for Helm charts. | Create a unique S3 bucket. In the bucket, create a folder called `charts`. The example in this pattern uses `s3://my-helm-charts/charts` as the target chart repository. | Cloud administrator |
| Install the Helm plugin for Amazon S3. | To install the helm-s3 plugin on your client machine, use the following command. <pre>helm plugin install https://github.com/hypnoglow/helm-s3.git --version 0.10.0</pre><br />Note: Helm V3 support is available with plugin version 0.9.0 and above. | DevOps engineer |
| Initialize the Amazon S3 Helm repository.  | To initialize the target folder as a Helm repository, use the following command. <pre>helm S3 init s3://my-helm-charts/charts </pre><br />The command creates an `index.yaml` file in the target to track all the chart information that is stored at that location. | DevOps engineer |
| Add the Amazon S3 repository to Helm. | To add the repository in the client machine, use the following command.<pre>helm repo add my-helm-charts s3://my-helm-charts/charts </pre><br />This command adds an alias to the target repository in the Helm client machine. | DevOps engineer |
| Review the repository list. | To view the list of repositories in the Helm client machine, run `helm repo list`. | DevOps engineer |

### Package and store charts in the Amazon S3 Helm repository
<a name="package-and-store-charts-in-the-amazon-s3-helm-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Package the chart. | To package the `my-nginx` chart that you created, run `helm package ./my-nginx/`. The command packages all the contents of the `my-nginx` chart folder into an archive file, which is named using the version number that is mentioned in the `Chart.yaml` file. | DevOps engineer |
| Store the package in the Amazon S3 Helm repository. | To upload the package to the Helm repository in Amazon S3, run the following command, using the correct name of the `.tgz` file.<pre>helm s3 push ./my-nginx-0.1.0.tgz my-helm-charts</pre> | DevOps engineer |
| Search for the Helm chart. | To confirm that the chart appears both locally and in the Helm repository in Amazon S3, run the following command.<pre>helm search repo my-nginx</pre> | DevOps engineer |

### Modify, version, and package a chart
<a name="modify-version-and-package-a-chart"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify and package the chart. | In `values.yaml`, set the `replicaCount` value to `1`. Then package the chart by running `helm package ./my-nginx/`, this time changing the version in `Chart.yaml` to `0.1.1`. <br />The versioning is ideally updated through automation using tools such as GitVersion or Jenkins build numbers in a CI/CD pipeline. Automating the version number is out of scope for this pattern. | DevOps engineer |
| Push the new version to the Helm repository in Amazon S3. | To push the new package with version of 0.1.1 to the `my-helm-charts` Helm repository in Amazon S3, run the following command.<pre>helm s3 push ./my-nginx-0.1.1.tgz my-helm-charts</pre> | DevOps engineer |

### Search for and install a chart from the Amazon S3 Helm repository
<a name="search-for-and-install-a-chart-from-the-amazon-s3-helm-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Search for all versions of the my-nginx chart. | To view all the available versions of a chart, run the following command with the `--versions` flag.<pre>helm search repo my-nginx --versions</pre><br />Without the flag, Helm by default displays the latest uploaded version of a chart. | DevOps engineer |
| Install a chart from the Amazon S3 Helm repository. | The search results from the previous task show the multiple versions of the `my-nginx` chart. To install the new version (0.1.1) from the Amazon S3 Helm repository, use the following command.<pre>helm upgrade my-nginx-release my-helm-charts/my-nginx --version 0.1.1 --namespace helm-space</pre> | DevOps engineer |

## Related resources
<a name="deploy-kubernetes-resources-and-packages-using-amazon-eks-and-a-helm-chart-repository-in-amazon-s3-resources"></a>
+ [HELM documentation](https://helm.sh/docs/)
+ [helm-s3 plugin (MIT License)](https://github.com/hypnoglow/helm-s3.git)
+ [HELM client binary](https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3)
+ [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

## Attachments
<a name="attachments-d3f993e6-4d96-4cb9-a075-c4debe431fd7"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/d3f993e6-4d96-4cb9-a075-c4debe431fd7/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
