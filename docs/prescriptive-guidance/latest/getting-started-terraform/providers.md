---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/providers.html
---

# Providers
<a name="providers"></a>

In Terraform, a *provider* is a plugin that interacts with cloud providers, third-party tools, and other APIs. To use Terraform with AWS, you use the [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs), which interacts with AWS resources.

If you've never used the [AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) to incorporate third-party extensions into your deployment stacks, then Terraform [providers](https://developer.hashicorp.com/terraform/language/providers) might take some getting used to. Because CloudFormation is native to AWS, the provider of AWS resources is already there by default. Terraform, on the other hand, has no single default provider, so nothing can be assumed about the origins of a given resource. This means that the first thing that needs to be declared in a Terraform configuration file is exactly where the resources are going and how they're going to get there.

This distinction adds an extra layer of complexity to Terraform that doesn't exist with CloudFormation. However, that complexity provides increased flexibility. You can declare multiple providers within a single Terraform module, and then the underlying resources that are created can interact with each other as part of the same deployment layer.

This can be useful in numerous ways. Providers don't necessarily have to be for separate cloud providers. Providers can represent any source for cloud resources. For example, take Amazon Elastic Kubernetes Service (Amazon EKS). When you provision an Amazon EKS cluster, you might want to use Helm charts to manage third-party extensions and use Kubernetes itself to manage pod resources. Because AWS, [Helm](https://registry.terraform.io/providers/hashicorp/helm/latest/docs), and [Kubernetes](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) all have their own Terraform providers, you can provision and integrate these resources all at the same time and then pass values among them.

In the following code example for Terraform, the AWS Provider creates an Amazon EKS cluster, and then the resulting Kubernetes configuration information is passed along to both the Helm and Kubernetes providers.

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.33.0"
    }

    helm = {
      source  = "hashicorp/helm"
      version = "2.12.1"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.26.0"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "example_0" {
  name     = "example_0"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids
  }
}

locals {
  host        = aws_eks_cluster.example_0.endpoint
  certificate = base64decode(aws_eks_cluster.example_0.certificate_authority.data)
}

provider "helm" {
  kubernetes {
    host                   = local.host
    cluster_ca_certificate = local.certificate
    # exec allows for an authentication command to be run to obtain user
    # credentials rather than having them stored directly in the file
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_0.name]
      command     = "aws"
    }
  }
}

provider "kubernetes" {
  host                   = local.host
  cluster_ca_certificate = local.certificate
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_0.name]
    command     = "aws"
  }
}
```

There's a trade-off regarding providers when it comes to the two IaC tools. Terraform relies wholly on externally located provider packages, which are the engine that drives its deployments. CloudFormation internally supports all major AWS processes. With CloudFormation, you need to worry about third-party providers only if you want to incorporate a third-party extension. There are pros and cons to each approach. Which one is right for you is beyond the scope of this guide, but it's important to remember the difference when evaluating both tools.

## Using Terraform aliases
<a name="using-terraform-aliases"></a>

In Terraform, you can pass custom configurations into each provider. So what if you want to use multiple provider configurations within the same module? In that case you'd have to use an [alias](https://developer.hashicorp.com/terraform/language/providers/configuration#alias-multiple-provider-configurations).  Aliases help you select which provider to use at a per-resource or per-module level. When you have more than one instance of the same provider, you use an alias to define the non-default instances. For example, your default provider instance might be a specific AWS Region, but you use aliases to define alternate regions.

The following Terraform example shows how to use an alias to provision buckets in different AWS Regions. The default Region for the provider is `us-west-2`, but you can use the east alias to provision resources in `us-east-2`.

```
provider "aws" {
  region = "us-west-2"
}

provider "aws" {
  alias  = "east"
  region = "us-east-2"
}

resource "aws_s3_bucket" "myWestS3Bucket" {
  bucket = "my-west-s3-bucket"
}

resource "aws_s3_bucket" "myEastS3Bucket" {
  provider = aws.east
  bucket   = "my-east-s3-bucket"
}
```

When you use an `alias` along with the `provider` meta-argument, as shown in the previous example, you can specify a different provider configuration for specific resources. Provisioning resources in multiple AWS Regions in a single stack is just the beginning. Aliasing providers is incredibly convenient in many ways.

For example, it's very common to provision multiple Kubernetes clusters at a time. Aliases can help you configure additional Helm and Kubernetes providers so that you can use these third-party tools differently for different Amazon EKS resources. The following Terraform code example illustrates how to use aliases to perform this task.

```
resource "aws_eks_cluster" "example_0" {
  name     = "example_0"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids[0]
  }
}

resource "aws_eks_cluster" "example_1" {
  name     = "example_1"
  role_arn = aws_iam_role.cluster_role.arn
  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids              = var.subnet_ids[1]
  }
}

locals {
  host         = aws_eks_cluster.example_0.endpoint
  certificate  = base64decode(aws_eks_cluster.example_0.certificate_authority.data)
  host1        = aws_eks_cluster.example_1.endpoint
  certificate1 = base64decode(aws_eks_cluster.example_1.certificate_authority.data)
}

provider "helm" {
  kubernetes {
    host                   = local.host
    cluster_ca_certificate = local.certificate
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_0.name]
      command     = "aws"
    }
  }
}

provider "helm" {
  alias = "helm1"
  kubernetes {
    host                   = local.host1
    cluster_ca_certificate = local.certificate1
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_1.name]
      command     = "aws"
    }
  }
}

provider "kubernetes" {
  host                   = local.host
  cluster_ca_certificate = local.certificate
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_0.name]
    command     = "aws"
  }
}

provider "kubernetes" {
  alias                  = "kubernetes1"
  host                   = local.host1
  cluster_ca_certificate = local.certificate1
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.example_1.name]
    command     = "aws"
  }
}
```
