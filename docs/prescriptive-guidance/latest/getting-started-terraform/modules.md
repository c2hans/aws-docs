---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/modules.html
---

# Modules
<a name="modules"></a>

In the realm of infrastructure as code (IaC), a *module* is a self-contained block of code that is isolated and packaged together for reuse. The concept of modules is an inescapable aspect of Terraform development. For more information, see [Modules](https://developer.hashicorp.com/terraform/language/modules) in the Terraform documentation. AWS CloudFormation also supports modules. For more information, see [Introducing AWS CloudFormation modules](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-modules/) in the AWS Cloud Operations and Migrations Blog.

The major difference between modules in Terraform and CloudFormation is that CloudFormation modules are imported by using a special resource type (`AWS::CloudFormation::ModuleVersion`). In Terraform, every configuration has at least one module, known as the [root module](https://developer.hashicorp.com/terraform/language/modules#the-root-module). Terraform resources that are in the **main.tf** file or files in a Terraform configuration file are considered to be in the root module. The root module can then call other modules for inclusion within the stack. The following example shows a root module provisioning an Amazon Elastic Kubernetes Service (Amazon EKS) cluster by using the open source [eks ](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest)module.

```
terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "2.12.1"
    }
  }
  required_version = ">= 1.2.0"
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.2.1"
  vpc_id  = var.vpc_id
}

provider "helm" {
  kubernetes {
    host                   = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  }
}
```

You might have noticed that the above configuration file does not include the AWS Provider. That's because modules are self-contained and can include their own providers. Because Terraform providers are global, providers from a child module can be used in the root module. This is not true about all module values though. Other internal values within a module are scoped by default to that module only and need to be declared as outputs to be accessible in the root module. You can leverage open source modules to simplify resource creation within your stack. For example, the eks module does more than provision an EKS cluster—it provisions a fully functioning Kubernetes environment. Using it can save you from writing dozens of extra lines of code, provided that the eks module configuration suits your needs.

## Calling modules
<a name="calling-modules"></a>

Two of the primary Terraform CLI commands that you run during Terraform deployment are [terraform init](https://developer.hashicorp.com/terraform/cli/commands/init) and [terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply). One of the default steps that the `terraform init` command performs is to locate all child modules and import them as dependencies into the `.terraform/modules` directory. During development, whenever you add a new externally sourced module, you must re-initialize before using the `apply` command. When you hear a reference to a Terraform *module*, it's referring to the packages in this directory. Strictly speaking, the module that you declare in your code is the *calling module*, so in practice, the module keyword calls the actual module, which is stored as a dependency.

In this way, the calling module serves as a more succinct representative of the full module to be replaced when deployment takes place. You can leverage this idea by creating your own modules within your stacks to enforce logical separations of resources by using whatever criteria you'd like. Just remember that the end goal of doing this should be to reduce your stack complexity. Because sharing data between modules requires you to output that data from within the module, sometimes relying too heavily on modules can overly complicate things.

## The root module
<a name="the-root-module"></a>

Because every Terraform configuration has at least one module, it can help to examine the module properties of the module you'll be dealing with the most: the root module. Whenever you're working on a Terraform project, the root module consists of all the `.tf` (or `.tf.json`) files in your top-level directory. When you run `terraform apply` in that top-level directory, Terraform attempts to run every `.tf` file it finds there. Any files in subdirectories are ignored unless they are called in one of these top-level configuration files.

This provides some flexibility in how you structure your code. It is also the reason why it's more accurate to refer to your Terraform deployment as a module than as a file because several files could be involved in a single process. There is a [standard module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure) that Terraform recommends for best practices. However, if you were to put any `.tf` file in your top-level directory, it would run along with the rest of the files. In fact, all top-level `.tf` files in a module are deployed when you run `terraform apply`. So which file does Terraform run first? The answer to that question is very important.

There's a series of steps that Terraform performs after initialization and before stack deployment. First, the existing configurations are analyzed, and then a [dependency graph ](https://developer.hashicorp.com/terraform/internals/graph)is created. The dependency graph determines what resources are called for and in what order they should be addressed. Resources that contain properties that are referenced in other resources, for example, would be handled before their dependent resources. Similarly, resources that explicitly declare dependence by using the `depends_on` parameter would be handled after the resources that they specify. When possible, Terraform can implement parallelism and handle non-dependent resources simultaneously. You can see the dependency graph before deploying by using the [terraform graph](https://developer.hashicorp.com/terraform/cli/commands/graph) command.

After the dependency graph is created, Terraform determines what needs to be done during the deployment. It compares the dependency graph with the most recent state file. The result of this process is called a *plan*, and it is very much like a CloudFormation [change set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-create.html). You can see the current plan by using the [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan) command.

As a best practice, it's recommended to stay as close as possible to the standard module structure. In cases where your configuration files are becoming too long to efficiently manage and logical separations could simplify management, you can spread your code across several files. Keep in mind how the dependency graph and plan process works to make your stacks run as efficiently as possible.
