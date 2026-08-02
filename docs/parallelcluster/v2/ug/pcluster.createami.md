---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.createami.html
---

# `pcluster createami`
<a name="pcluster.createami"></a>

(Linux/macOS) Creates a custom AMI to use with AWS ParallelCluster.

```
pcluster createami [ -h ] -ai {{BASE_AMI_ID}} -os {{BASE_AMI_OS}}
                   [ -i {{INSTANCE_TYPE}} ] [ -ap {{CUSTOM_AMI_NAME_PREFIX}} ]
                   [ -cc {{CUSTOM_AMI_COOKBOOK}} ] [--no-public-ip]
                   [ -post-install {{POST_INSTALL_SCRIPT}} ]
                   [ -c {{CONFIG_FILE}} ] [-t {{CLUSTER_TEMPLATE}}]
                   [--vpc-id {{VPC_ID}}] [--subnet-id {{SUBNET_ID}}]
                   [ -r {{REGION}} ]
```

## Required dependencies
<a name="pcluster.createami.required-dependencies"></a>

In addition to the AWS ParallelCluster CLI, the following dependency is required to run `pcluster createami`:
+ **Packer**: Download the latest version from [https://developer.hashicorp.com/packer/downloads](https://developer.hashicorp.com/packer/downloads).

**Note**
Before AWS ParallelCluster version 2.8.0, [Berkshelf](https://github.com/berkshelf/berkshelf) (installed using `gem install berkshelf`) was required to use `pcluster createami`.

## Named arguments
<a name="pcluster.createami.namedarg"></a>

**-h, --help**
Shows the help text for `pcluster createami`.

**-ai {{BASE\_AMI\_ID}}, --ami-id {{BASE\_AMI\_ID}}**
Specifies the base AMI to use for building the AWS ParallelCluster AMI.

**-os {{BASE\_AMI\_OS}}, --os {{BASE\_AMI\_OS}}**
Specifies the OS of the base AMI. Valid options are: `alinux2`, `ubuntu1804`, `ubuntu2004`, and `centos7`.
OS support changes in different AWS ParallelCluster versions:
+ Support for `centos8` was removed in AWS ParallelCluster version 2.10.4.
+ Support for `centos8` was added, and support for `centos6` was removed in AWS ParallelCluster version 2.10.0.
+ Support for alinux2 was added in AWS ParallelCluster version 2.6.0.
+ Support for ubuntu1804 was added in AWS ParallelCluster version 2.5.0.

**-i {{INSTANCE\_TYPE}}, --instance-type {{INSTANCE\_TYPE}}**
Specifies the instance type to use to create the AMI.
Defaults to `t2.xlarge`.
Support for the `--instance-type` argument was added in AWS ParallelCluster version 2.4.1.

**-ap {{CUSTOM\_AMI\_NAME\_PREFIX}}, --ami-name-prefix {{CUSTOM\_AMI\_NAME\_PREFIX}}**
Specifies the prefix name of the resulting AWS ParallelCluster AMI.
Defaults to `custom-ami-`.

**-cc {{CUSTOM\_AMI\_COOKBOOK}}, --custom-cookbook {{CUSTOM\_AMI\_COOKBOOK}}**
Specifies the cookbook to use to build the AWS ParallelCluster AMI.

**--post-install {{POST\_INSTALL\_SCRIPT}}**
Specifies the path to the post-install script. Paths must use a `s3://`, `https://`, or `file://` URL scheme. Examples include the following:
+ `https://{{bucket-name}}.s3.{{region}}.amazonaws.com/{{path}}/post_install.sh`
+ `s3://{{bucket-name}}/post_install.sh`
+ `file:///{{opt/project}}/post_install.sh`
Support for the `--post-install` argument was added in AWS ParallelCluster version 2.10.0.

**--no-public-ip**
Do not associate a public IP address to the instance used to create the AMI. By default, a public IP address is associated with the instance.
Support for the `--no-public-ip` argument was added in AWS ParallelCluster version 2.5.0.

**-c {{CONFIG\_FILE}}, --config {{CONFIG\_FILE}}**
Specifies the alternative configuration file to use.
Defaults to `~/.parallelcluster/config`.

**-t {{CLUSTER\_TEMPLATE}}, --cluster-template {{CLUSTER\_TEMPLATE}}**
Specifies the [[`cluster`] section](cluster-definition.md) of the {{CONFIG\_FILE}} to use to retrieve the VPC and subnet settings.
Support for the `--cluster-template` argument was added in AWS ParallelCluster version 2.4.0.

**--vpc-id {{VPC\_ID}}**
Specifies the ID of the VPC to use to build the AWS ParallelCluster AMI.
Support for the `--vpc-id` argument was added in AWS ParallelCluster version 2.5.0.

**--subnet-id {{SUBNET\_ID}}**
Specifies the ID of the subnet to use to build the AWS ParallelCluster AMI.
Support for the `--vpc-id` argument was added in AWS ParallelCluster version 2.5.0.

**-r {{REGION}}, --region** {{REGION}}
Specifies the AWS Region to use. Defaults to the AWS Region specified by using the [`pcluster configure`](pcluster.configure.md) command.
