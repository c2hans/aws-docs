---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/installation-options.html
---

# Installation options
<a name="installation-options"></a>

There are two main ways to install Red Hat OpenShift on AWS:
+ Installer-provisioned infrastructure (IPI) ‒ The user provides the basic information (such as the number of control plane machines) and can choose default values for most of the questions. The Red Hat OpenShift Service on AWS command line utility (`rosa `CLI) can be placed in an IPI structure, as discussed in the next section.
+ User-provisioned infrastructure (UPI) ‒ All infrastructure components, such as Domain Name Server (DNS), Amazon virtual private clouds (VPCs), bootstrap machines, and control planes are created manually, and Red Hat OpenShift is installed on top of that infrastructure.

Both setups use the same installation program (`install-config.yaml`), which installs components based on targets and dependencies. Each target has its own dependencies, so the program can support multiple targets in parallel and ensure that the target can successfully run the cluster. The following diagram shows some of the targets and dependencies.

![Targets and dependencies for Red Hat OpenShift on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/images/guide-img/bcbfa5c1-b077-4a7c-9aab-f667a34c404d/images/2ebe28c5-273d-4c1d-a69f-f86502ed7cec.png)

## Advantages and disadvantages of each approach
<a name="adv-disadv"></a>

|
|
| Installer-provisioned infrastructure (IPI) | User-provisioned infrastructure (UPI) |
| --- |--- |
| Easy to install. | Complex; takes some time to set up. |
| Doesn't provide many customization options. | You can customize the topology and entire infrastructure. |
| Supports AWS and other public cloud options. | Supports VMware and bare metal systems as well as AWS and other cloud options. |
| Creates all infrastructure components, including load balancers and virtual networks. | Can be used when the underlying platform doesn't meet all requirements. (For example, bare metal systems don't provide load balancers.) |
| Highly automated. | Requires you to create the entire automation layer for provisioning the underlying infrastructure. You can use [AWS CloudFormation templates](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.6/html-single/installing/index#installing-aws-user-infra) for this purpose. |
| Prerequisites checks are easy to perform. | Prerequisites must be validated carefully. |

## IPI example ‒ using the ROSA CLI
<a name="ipi-example1"></a>

Red Hat OpenShift Service on AWS implements an IPI type of installation, but it provides additional benefits. You use the `rosa` CLI to manage (update, delete, or provision) a Red Hat OpenShift on AWS cluster and resources. For more information, see the [Red Hat OpenShift documentation](https://docs.openshift.com/rosa/rosa_cli/rosa-get-started-cli.html).

To provision a Red Hat OpenShift cluster on AWS, you first install the `rosa` CLI and make sure that the AWS Command Line Interface (AWS CLI) points to your AWS account. You can then use the `rosa` CLI to perform validations and provision the cluster by using commands similar to the following.

```
rosa verify permissions [arguments]
rosa download oc

rosa verify quota [arguments]
rosa init --token=<token>
rosa create cluster --cluster-name=<cluster_name>
```

When the cluster has been provisioned, you can verify it by using OpenShift commands.

```
oc get nodes (list all nodes if connected to cluster)
oc get ns (list all namespaces)
```

For more information, see the [OpenShift documentation](https://docs.openshift.com/rosa/rosa_cli/rosa-get-started-cli.html#rosa-setting-up-cli_rosa-getting-started-cli).

The benefits of using this method include the following:
+ Easy to set up and quickly provision the cluster on AWS.
+ Provides logging information; easy to troubleshoot if anything goes wrong.
+ Can validate prerequisites through the command line.
+ Can be used for deletions and other operations as well.

Some possible concerns:
+ Customization options might be limited.
+ Requires the `rosa `CLI, AWS CLI, and other basic setup.
+ All challenges with IPI apply to using the `rosa `CLI as well.

## IPI example ‒ using openshift-install
<a name="ipi-example2"></a>

`openshift-install` is a command line utility that you can use to create a cluster quickly. This command provides some flexibility through modifications to the `install-config.yaml` file. This section provides high-level steps for using the utility. For detailed installation steps, see the [OpenShift documentation](https://docs.openshift.com/container-platform/4.6/installing/installing_aws/installing-aws-default.html).

1. Get the installer from the [Red Hat website](https://console.redhat.com/openshift/install) (requires a Red Hat account).

1. Untar the package.

   ```
   tar xvf openshift-install-linux.tar.gz
   ```

1. Identify the installation directory, and run the `create cluster` command.

   ```
   ./openshift-install create cluster --dir <installation_directory> --log-level=info
   ```

1. To customize the installation, generate the `install-config.yaml` file.

   ```
    ./openshift-install create install-config --dir <installation_directory>
   ```

The following provides an excerpt from a sample `install-config.yaml` file. For configuration options, see the [OpenShift documentation](https://docs.openshift.com/container-platform/4.7/installing/installing_aws/installing-aws-customizations.html).

```
      apiVersion: v1
baseDomain: sample.com
credentialsMode: Mint
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    aws:
      zones:
      - us-east-2a
      - us-east-2b
      rootVolume:
        iops: 4000
        size: 500
        type: io1
      type: m5.xlarge
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    aws:
      rootVolume:
        iops: 2000
        size: 500
        type: io1
      type: c5.4xlarge
      zones:
      - us-east-2c
  replicas: 3
metadata:
  name: sample-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OpenShiftSDN
  serviceNetwork:
  - 172.30.0.0/16
platform:
  aws:
    region: us-west-2
    userTags:
      adminContact: jdoe
      costCenter: 7536
    amiID: ami-96c6f8f7
    serviceEndpoints:
      - name: ec2
        url: https://vpce-id.ec2.us-west-2.vpce.amazonaws.com
fips: false
sshKey: ssh-ed25519 AAAA...
pullSecret: '{"auths": ...}'
```

## UPI example ‒ installing on user-provisioned AWS infrastructure
<a name="upi-example"></a>

You can provision a Red Hat OpenShift cluster on an existing AWS infrastructure that you provision separately. To provision the infrastructure, you can use AWS CloudFormation templates to create the VPC, hosted zone, DNS records, and other components. For detailed steps and AWS CloudFormation templates, see the [OpenShift documentation](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.1/html/installing/installing-on-user-provisioned-aws).

When the cluster has been provisioned, you must approve all certificate signing requests (CSRs) to move worker nodes to a `Ready `status.

```
oc get nodes

NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.13.4+b626c2fe1
master-1  Ready     master  63m  v1.13.4+b626c2fe1
master-2  Ready     master  64m  v1.13.4+b626c2fe1
worker-0  NotReady  worker  76s  v1.13.4+b626c2fe1
worker-1  NotReady  worker  70s  v1.13.4+b626c2fe1
```

You can approve all certificates in one step by using the following command.

```
    oc get csr -ojson | jq -r '.items[] | select(.status == {} ) | .metadata.name' | xargs oc adm certificate approve
```

You can verify that all the operators are in the `Ready `stage by using the `oc` command line or from the Red Hat console.

After verification, you can delete the bootstrap resources. You can determine `stack-name` from the AWS Management Console, and from the name you provided when you created the stack.

```
 aws cloudformation delete-stack --stack-name <name>
```

Finish provisioning the cluster by using the following command.

```
./openshift-install --dir=<installation_directory> wait-for install-complete

INFO Waiting up to 30m0s for the cluster to initialize...
```

Make sure to check logs and confirm that there are no errors before you deliver the cluster to your stakeholders.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
