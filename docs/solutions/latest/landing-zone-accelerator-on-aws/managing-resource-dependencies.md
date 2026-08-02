---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/managing-resource-dependencies.html
---

# Managing resource dependencies
<a name="managing-resource-dependencies"></a>

This solution uses a layered approach to deploying your landing zone infrastructure resources. Each stage after the **Build** stage produces at least one CloudFormation stack, with some stages producing multiple stacks. For more information on the stage ordering and stacks produced by each stage, refer to the details in [Core pipeline](deployment-pipelines.md#awsaccelerator-pipelinestack).

This stage-based approach provides the flexibility to manage the ordering of resource deployment. It also maximizes the number of resources that you can deploy for each stage while logically grouping similar resources. Finally, it provides the solution a consistent means to reference resources created in previous stages, including those created in different AWS accounts and Regions. When required, the solution uses lookup methods to retrieve details for resources with upstream dependencies.

Updating existing resources might require knowledge of the stack ordering and resource dependencies between them. The following section provides detail about identifying resources with dependencies in your accelerator configuration files.

## Identifying resources with dependencies
<a name="identifying-resources-with-dependencies"></a>

The following sections provide example VPC configurations to demonstrate how nested configurations and logical references create a downstream dependency tree for your resources. A helpful mental model to follow when updating resources with dependency trees is to start with the lowest nested item. In these examples, interface endpoints are the lowest nested item since they are dependent on subnets that, in turn, are dependent on the base VPC configuration item.

Modifying (including deleting) the lowest nested item first doesn’t result in dependency issues. However, if you the change properties of the subnet or VPC, you might encounter issues if those modifications cause the resource to be replaced (for example, changing the CIDR property of the resource) or deleted. Modifications that don’t result in resource replacement shouldn’t impact downstream dependencies. Refer to the [Services, Features, and Configuration References section](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/) before modifying configurations with downstream dependencies to determine the impact of updating a property value.

### Configuration item containing nested configuration items
<a name="configuration-item-containing-nested-configuration-items"></a>

The following is an example basic VPC configuration and its nested dependencies. Comments are denoted with hash (\#) marks:

```
vpcs:
  - name: accelerator-vpc
    account: Network
    region: us-east-1
    cidrs:
      - 10.0.0.0/24
    enableDnsHostnames: true
    enableDnsSupport: true
    instanceTenancy: default
    routeTables:
      # Items under this block are dependent
      # on the base VPC configuration item
      - name: accelerator-default
        routes: []
    subnets:
      # Items under this block are dependent
      # on the base VPC configuration item
      - name: accelerator-subnet-a
        availabilityZone: a
        routeTable: accelerator-default
        ipv4CidrBlock: 10.0.0.0/26
      - name: accelerator-subnet-b
        availabilityZone: b
        routeTable: accelerator-default
        ipv4CidrBlock: 10.0.0.64/26
```

### Configuration items referencing the logical names of other configuration items
<a name="configuration-items-referencing-the-logical-names-of-other-configuration-items"></a>

Building from our previous example, the following adds interface endpoints to the VPC. Comments are denoted with hash (\#) marks:

```
vpcs:
  - name: accelerator-vpc
    account: Network
    region: us-east-1
    cidrs:
      - 10.0.0.0/24
    enableDnsHostnames: true
    enableDnsSupport: true
    instanceTenancy: default
    routeTables:
      - name: accelerator-default
        routes: []
    subnets:
      - name: accelerator-subnet-a
        availabilityZone: a
        # Referencing the route table name
        routeTable: accelerator-default
        ipv4CidrBlock: 10.0.0.0/26
      - name: accelerator-subnet-b
        availabilityZone: b
        # Referencing the route table name
        routeTable: accelerator-default
        ipv4CidrBlock: 10.0.0.64/26
    interfaceEndpoints:
      # Referencing a policy name defined
      # in another config block
      defaultPolicy: Default
      endpoints:
        - service: ec2
      # Referencing subnet names defined
      # under this VPC configuration.
      subnets:
        - accelerator-subnet-a
        - accelerator-subnet-b
```

## Modifying resources with dependencies
<a name="modifying-resources-with-dependencies"></a>

If your update or deletion will impact downstream resources, you can use the following strategies to avoid dependency errors.

### Multiple Core pipeline runs
<a name="multiple-core-pipeline-runs"></a>

1. Starting with the lowest nested item in your dependency tree, remove or comment out the items that will be affected by your change. The following example comments out interface endpoints from the previous section:

   ```
   vpcs:
     - name: accelerator-vpc
       account: Network
       region: us-east-1
       cidrs:
         - 10.0.0.0/24
       enableDnsHostnames: true
       enableDnsSupport: true
       instanceTenancy: default
       routeTables:
         - name: accelerator-default
           routes: []
       subnets:
         - name: accelerator-subnet-a
           availabilityZone: a
           routeTable: accelerator-default
           ipv4CidrBlock: 10.0.0.0/26
         - name: accelerator-subnet-b
           availabilityZone: b
           routeTable: accelerator-default
           ipv4CidrBlock: 10.0.0.64/26
       # interfaceEndpoints:
       #  defaultPolicy: Default
       #  endpoints:
       #    - service: ec2
       #  subnets:
       #    - accelerator-subnet-a
       #    - accelerator-subnet-b
   ```

1. Release your changes to the Core pipeline. This removes the interface endpoints from the VPC subnets.

1. Modify the subnet CIDRs. The following example makes the subnet ranges smaller:

   ```
   vpcs:
     - name: accelerator-vpc
       account: Network
       region: us-east-1
       cidrs:
         - 10.0.0.0/24
       enableDnsHostnames: true
       enableDnsSupport: true
       instanceTenancy: default
       routeTables:
         - name: accelerator-default
           routes: []
       subnets:
         - name: accelerator-subnet-a
           availabilityZone: a
           routeTable: accelerator-default
           ipv4CidrBlock: 10.0.0.0/27
         - name: accelerator-subnet-b
           availabilityZone: b
           routeTable: accelerator-default
           ipv4CidrBlock: 10.0.0.32/27
       # interfaceEndpoints:
       #  defaultPolicy: Default
       #  endpoints:
       #    - service: ec2
       #  subnets:
       #    - accelerator-subnet-a
       #    - accelerator-subnet-b
   ```

1. Release your changes to the Core pipeline. This replaces the existing `/26` subnets with new `/27` subnets.

1. If you want to redeploy your lowest nested item, remove the comment from the item and release the change to the Core pipeline again. In the previous example, the interface endpoint would be deployed to the newly-provisioned subnets.

### Using the solution command line interface (CLI)
<a name="using-the-solution-command-line-interface-cli"></a>

Using the solution CLI can help you perform the steps in the previous section more quickly. Rather than performing a full pipeline run for each change, you can run targeted changes to the specific stage, account, and AWS Region that requires the changes.

**Note**
Using the solution CLI requires a development toolchain to be installed on your workstation. Our development dependencies and documentation for using the CLI are included in the [Developer Guide](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/developer-guide/) section of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/).
In our example, the stage for these changes is `network-vpc`. The stage you target for CLI changes might differ depending on the resources that you are targeting for updates.

1. Make the configuration changes from step 1 in the [Multiple Core pipeline runs](#multiple-core-pipeline-runs) section.

1. Run the following CLI command, replacing ` <LOCAL_CONFIG_DIR> ` and ` <ACCOUNT_ID> ` with your environment details:

   ```
   yarn run ts-node --transpile-only cdk.ts deploy --stage network-vpc --require-approval any-change --config-dir <LOCAL_CONFIG_DIR> --partition aws --region us-east-1 --account <ACCOUNT_ID>
   ```

   The CLI indicates when the stack deployment has completed, meaning your interface endpoints have been deleted.

1. Make the configuration changes from step 3 in the [Multiple Core pipeline runs](#multiple-core-pipeline-runs) section.

1. Run the following CLI command again, replacing ` <LOCAL_CONFIG_DIR> ` and ` <ACCOUNT_ID> ` with your environment details:

   ```
   yarn run ts-node --transpile-only cdk.ts deploy --stage network-vpc --require-approval any-change --config-dir <LOCAL_CONFIG_DIR> --partition aws --region us-east-1 --account <ACCOUNT_ID>
   ```

1. The CLI indicates when the stack deployment has completed, meaning your subnets have been replaced.

1. If you want to redeploy your lowest nested item, remove the comment from the item and run the CLI command again. In our example, the interface endpoint would be deployed to the newly-provisioned subnets.

## Strategizing network resource updates
<a name="strategizing-network-resource-updates"></a>

This solution has multiple stages and stacks associated with building your core network topology. Many of the building blocks associated with landing zone networks have tightly coupled dependencies. Some of these dependencies for this solution cross stack barriers. For this reason, updating network resources using Landing Zone Accelerator on AWS requires additional knowledge of which stage and stack specific resources are deployed in.

The following diagram is a visual aid for understanding the network resources that the solution can deploy, and how their dependencies map together. When planning updates or removal of network resources with downstream dependencies, reference this dependency map along with the guidance in the previous sections of [Managing resource dependencies](#managing-resource-dependencies).

**Note**
If the image is difficult to read on your screen, open it in a new tab.

 **Sample diagream of resource dependencies.**

![network dependency.drawio](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/network-dependency.drawio.png)
