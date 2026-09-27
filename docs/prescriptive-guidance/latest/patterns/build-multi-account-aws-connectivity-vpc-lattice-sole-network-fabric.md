---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric.html
---

# Build multi-account AWS connectivity with VPC Lattice as the sole network fabric
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric"></a>

*Rahul Sahotay, Amazon Web Services*

## Summary
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-summary"></a>

As a [multi-account AWS](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) footprint grows from a handful of accounts into the hundreds, one question keeps resurfacing: how much networking should each workload account really own? The instinctive answer is "everything it needs to be self-sufficient." So every account gets its own [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html), its own [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), its own route tables and DNS. It works. It also means the same networking stack is built, paid for, patched, and audited hundreds of times over, and the cost and operational load climb in lockstep with the account count.

There is another way to draw the line. Instead of every account owning its connectivity, you build it once in a central Network account and let workload accounts consume it. This pattern uses [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) as that shared fabric for three connectivity needs that nearly every workload has: private access to AWS services, controlled internet egress, and ingress for consumers that live outside the fabric. A workload account joins by creating a single VPC association, and from that moment it inherits private AWS-service access and filtered egress with no per-account endpoints, gateways, or route tables to stand up.

It is worth being precise about where this fits. VPC Lattice routes by DNS name and service network, not by IP address, so this is a cost-effective alternative for the service-access, egress, and ingress patterns, not a wholesale replacement for IP routing. [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) remains the right tool for east-west routing between VPCs, hybrid connectivity over Direct Connect or VPN, and centralized traffic inspection. The two are not mutually exclusive: a single VPC can hold a Transit Gateway attachment and a VPC Lattice association at the same time, each carrying the traffic it handles best.

**What this pattern gives you**
+ Connectivity cost that tracks the number of environments (three), not the number of accounts (hundreds)
+ Zero-touch onboarding: one VPC association delivers full AWS-service access and filtered egress
+ Centralized, FQDN-filtered internet egress governed by a single allowlist
+ Environment isolation enforced by [IAM auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) and OU-scoped [resource sharing](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
+ Overlapping workload CIDRs supported by design, because routing never depends on IP addresses
+ One fabric that serves internal workloads and external, on-premises, and cross-Region consumers alike, through Service Network Endpoints

The shared fabric is deployed once in the Network account and exposed through three environment-scoped [service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html) (dev, test, prod). The companion repository provides reference implementations in both [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) (TypeScript, 14 stacks) and [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) (11 templates), with architecture diagrams and a security review summary.

## Prerequisites and limitations
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-prereqs"></a>

*Prerequisites*
+ An active AWS account
+ An AWS account set aside as the [central Network account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/networking-account.html), where the shared fabric will live.
+ [AWS Organizations](https://aws.amazon.com/organizations/) enabled in all-features mode, with workload accounts sorted into organizational units (OUs) for dev, test, and prod. All-features mode is required for OU-scoped resource sharing and the `aws:PrincipalOrgPaths` policy conditions, the OU structure is what later scopes who can reach which environment.
+ [AWS Resource Access Manager (RAM) ](https://aws.amazon.com/ram/)sharing with AWS Organizations turned on in the management account (`aws ram enable-sharing-with-aws-organization`). Without it, the OU-scoped service network shares cannot target OUs.
+ A Region where Amazon VPC Lattice, including Resource Gateways and Resource Configurations, is available.
+ Comfort with core AWS networking (VPCs, subnets, DNS, security groups) and multi-account building blocks (AWS Organizations, OUs, RAM).
+ For the reference implementation: AWS CDK (TypeScript) or AWS CloudFormation tooling configured.
+ A landing zone such as [AWS Control Tower](https://aws.amazon.com/controltower/) or [Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/landing-zone-accelerator-on-aws/) is not required. If you have one, the reference implementation integrates with it by re-pointing its SSM parameter paths to your framework's existing network ID parameters.

*Limitations*
+ VPC Lattice routes by DNS name and service network, not by IP. It is not suited for general-purpose, IP-routed east-west traffic between workload VPCs, hybrid routing (AWS Direct Connect or VPN), or centralized traffic inspection with firewall appliances. Retain Transit Gateway for those.
+ A VPC Lattice custom domain name is fixed once the resource is created. Changing it means deleting and recreating the resource, which drops its associations and Resource Configurations, so choose names deliberately.
+ Service networks are Regional. A multi-Region footprint repeats the pattern once per Region.
+ A single DNS record cannot serve both the Service Network Endpoint path and the VPC-association path at once. When both coexist, you need split-horizon DNS (covered in Best practices).
+ Resource Gateway subnets should be /24 or larger. The gateway scales its network interfaces with connection volume, and undersized subnets risk IP exhaustion that shows up as intermittent, hard-to-diagnose connectivity failures.
+ The shared egress proxy is a concentration point. Deploy it across multiple Availability Zones and monitor it (again, see Best practices).
+ The fabric carries a fixed base cost, so the economics work best once you are past roughly 15 to 30 accounts. Below that, per-account networking may still be cheaper.
+ Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

*Product versions*
+ Amazon VPC Lattice with Resource Gateways, Resource Configurations, and Service Network Endpoints (generally available as of re:Invent 2024).
+ AWS CDK v2 (the reference implementation targets `aws-cdk-lib` 2.150.0 or later on Node.js 20).
+ AWS CLI v2 for the CloudFormation path.
+ Squid proxy on Amazon ECS on AWS Fargate.

## Architecture
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-architecture"></a>

*Target technology stack*
+ Three VPC Lattice service networks (dev, test, prod) in a central Network account
+ Resource Gateways and Resource Configurations exposing 10 shared interface VPC endpoints (the CloudFormation path adds an 11th, `execute-api`)
+ A Squid forward proxy on Amazon ECS on AWS Fargate (2 tasks) behind an internal Network Load Balancer, exposed as a Resource Configuration for filtered egress
+ Service Network Endpoints for external, on-premises, and cross-Region ingress
+ AWS RAM shares scoped to OUs; IAM auth policies scoped by OU path

*Target architecture*

Everything in this pattern is built once in the central Network account and offered outward, so a workload account gains its connectivity the moment it creates a single VPC association. Three pillars sit on that one shared fabric:

|
|
| Pillar | What it provides | How it works |
| --- |--- |--- |
| Shared AWS service endpoints | Centralized access to SSM, STS, ECR, ECS, CloudWatch Logs, and more | 10 endpoints in an Endpoint VPC, exposed as VPC Lattice Resource Configurations |
| Centralized egress | Filtered outbound internet access with an FQDN allowlist | Squid forward proxy on ECS Fargate (2 tasks) behind an internal NLB, exposed via Resource Configuration |
| Ingress via Service Network Endpoints | External, on-premises, and cross-Region consumers reaching shared services | Service Network Endpoints (SN-E) allow consumers outside the VPC Lattice association to connect |

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f1e001b4-b79d-4071-8e5d-e02fa2aecbf6/images/18577d80-fdca-4b17-a051-e473c671b2fc.png)

*Figure 1: High-level topology showing the three pillars on a single VPC Lattice fabric.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f1e001b4-b79d-4071-8e5d-e02fa2aecbf6/images/f1845c42-7832-4c0e-bb4f-0ad523334ae9.png)

*Figure 2: Shared endpoint data flow. A workload VPC resolves an AWS service domain through the VPC Lattice-managed Private Hosted Zone, and traffic reaches the shared interface endpoint in the Network account through the Resource Gateway.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f1e001b4-b79d-4071-8e5d-e02fa2aecbf6/images/e868351c-8046-4fc3-a735-3b5096b481ad.png)

*Figure 3: Centralized egress data flow. A workload sends outbound traffic to the shared Squid proxy through the service network, where an FQDN allowlist filters the request before it leaves through the Network account.*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f1e001b4-b79d-4071-8e5d-e02fa2aecbf6/images/68f7eda8-a6de-4258-bcbd-fbc076ebfa66.png)

*Figure 4: Ingress data flow. External, on-premises, and cross-Region consumers reach shared services through a Service Network Endpoint in the ingress VPC.*

*Automation and scale*

Onboarding a workload account is deliberately dull: one VPC association with `PrivateDnsEnabled`, plus a security group that permits egress to the VPC Lattice managed prefix list, rolled out at scale through a service-managed AWS CloudFormation StackSet or AWS CDK. VPC Lattice creates Private Hosted Zones automatically so standard AWS service domains (for example, `ssm.us-east-2.amazonaws.com`) resolve to [Lattice addresses](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html#service-network-types) in the `129.224.0.0/17` range with no per-workload DNS configuration.

## Tools
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-tools"></a>

*AWS services*
+ [VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) provides the service networks, Resource Gateways, Resource Configurations, and Service Network Endpoints that form the connectivity fabric.
+ [Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) (RAM) shares the service networks with workload OUs.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) provides the OU structure that scopes RAM shares and IAM auth policies.
+ [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) roll the workload VPC association out to every current and future account in a target OU.
+ [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) carries the contract between stacks: VPC, subnet, and security group IDs are published once and resolved at deploy time, with no hardcoded IDs.
+ [ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) runs the Squid egress proxy.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) (Network Load Balancer) fronts the egress proxy.
+ [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) and [Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) (Amazon ECR) build and store the custom Squid image with its FQDN allowlist.
+ [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) provides the Private Hosted Zones used for DNS resolution, plus the [Resolver inbound endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) that lets on-premises consumers resolve ingress domains.
+ [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), and [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) power the Lambda-free ingress DNS automation, which keeps custom-domain records current as Resource Configurations change.
+ [Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html), [Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html), [ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html), [ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html), and [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) are among the shared endpoint services exposed through the fabric.

*Code*

The reference implementation is in the GitHub repository aws-samples/sample-vpc-lattice-multi-account-connectivity, provided in both AWS CDK (TypeScript, 14 stacks) and AWS CloudFormation (11 templates), with 4 architecture diagrams and 15 documentation files.

## Best practices
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-best-practices"></a>

 These recommendations apply to the shared-fabric model described in this pattern. They cost nothing to adopt on day one and become expensive to retrofit later. Apply them before onboarding your first wave of workload accounts.

*Naming: make names a contract, not decoration*

VPC Lattice resource names are functional. The workload association automation looks up the target [Service Network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html) by name at deploy time, so a name is a contract the onboarding process depends on.

**Prescriptive recommendation:** Pick one short, lowercase, org-wide prefix and build every name from the same ordered parts: prefix, scope or service, environment, role. Note that only Service Networks and Service Network Endpoints are per-environment; [Resource Gateways](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html) and [Resource Configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) are shared, one per VPC or per service, and serve all three environments:

```
Per environment:
  sn-dev-shared              (dev Service Network)
  sn-test-shared             (test Service Network)
  sn-prod-shared             (prod Service Network)
  sne-dev-ingress            (Service Network Endpoint for dev ingress)

Shared across environments:
  net-endpoint-resource-gw   (Resource Gateway, one per Endpoint VPC)
  net-egress-resource-gw     (Resource Gateway, one per Egress VPC)
  ssm-endpoint-rc            (Resource Configuration, one per exposed service)
  squid-proxy-rc             (Resource Configuration for the egress proxy)
```

Encode the environment, never the account: environment is the unit of isolation in this pattern, so it belongs in the name; account identity belongs in tags.

**Why this matters:** Consistent naming enables automated lookup, simplifies IAM policy conditions, and makes [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) log analysis practical at scale.

*Tagging: make every resource attributable from day one*

Tags drive [cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html), automation filtering, and governance queries. Activate cost allocation tags in the management account billing console before deploying; activation is forward-looking only, so untagged early resources never show up in cost data.

**Mandatory tag set:**

|
|
| Tag key | Purpose | Example value |
| --- |--- |--- |
| `Environment` | Maps to Service Network (dev/test/prod) | `prod` |
| `ManagedBy` | Identifies IaC ownership | `cdk` or `cloudformation` |
| `CostCenter` | Drives chargeback | `platform-networking` |
| `ServiceNetwork` | Cross-references the parent Service Network | `sn-prod-shared` |

*Assign explicit security groups to every resource that creates an ENI*

If your landing zone ([AWS Landing Zone Accelerator](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) or similar) strips default security group rules, resources that create elastic network interfaces (Resource Gateways, Service Network Endpoints, Fargate tasks, and interface VPC endpoints) fail with silent connection timeouts rather than an explicit error. Always attach a named, explicitly configured security group to these resources. This is the most time-consuming failure mode to diagnose, because nothing logs an error; plan for it up front.

*Finalize naming and custom domains before you create resources*

VPC Lattice custom domain names cannot be changed after a resource is created. Changing a domain requires deleting and recreating the resource, which drops all of its associations and Resource Configurations. Lock the naming convention above before the first deploy.

*Use split-horizon DNS when ingress (SN-E) and VPC-association paths coexist*

A single DNS record cannot serve both paths. The Service Network Endpoint path resolves to the endpoint's per-AZ secondary IPs, while the VPC-association path resolves to VPC Lattice-managed IPs in the 129.224.0.0/17 range. If an Ingress VPC with Service Network Endpoints coexists with workload VPCs that associate directly, use separate [Private Hosted Zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) associated with the appropriate VPCs.

*Enable RAM organization sharing before standing up the fabric*

OU-scoped [Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) shares only work after sharing with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) has been enabled in the management account (`aws ram enable-sharing-with-aws-organization`). Do this first, or the shares fail.

*Monitoring: the trade-off for centralization*

The shared-fabric model concentrates connectivity into fewer components. This is both its strength (one place to govern, secure, and observe) and its primary operational trade-off (a failure in the shared fabric affects all consumers). Centralized monitoring is not optional; it is the trade you make for reducing per-account overhead.

**Day-one observability:**

1. [VPC Lattice access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) to CloudWatch Logs or S3, enabled on each Service Network for both the SERVICE and RESOURCE log types (they are off by default)

1. **Resource Gateway health** via [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metrics (target health, connection count)

1. **NLB target group health** for the egress proxy (unhealthy targets = egress outage)

1. **ECS task health** for the Squid proxy (running count, restart rate)

1. **CloudWatch alarms** on: Resource Configuration unhealthy targets, NLB 5xx rate, proxy task restart count, and spikes in Squid denied requests (either a misconfigured workload or a genuine exfiltration attempt; both are worth knowing about)

*Quota planning*

Track usage against the quotas that matter for this pattern. Defaults are Region-specific and adjustable through [AWS Support](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

|
|
| Quota | Default | Notes |
| --- |--- |--- |
| Service networks per Region | 50 | 3 used (dev, test, prod). Ample headroom. |
| VPC associations per service network | 500 | The real scaling ceiling. Alarm at 80% (400) and request an increase proactively. |
| Resource configurations per service network | 500 | About 11 used (10 endpoints plus egress). Comfortable. |
| Resource gateways per VPC | 500 | 1 to 2 used per VPC. Comfortable. |
| Service network VPC endpoints per service network | 200 | Relevant to the ingress (SN-E) pattern. |

The practical takeaway: at a hundreds-of-accounts estate, the binding limit is VPC associations per service network (500). Environment-scoped service networks keep you well inside it; if a single environment approaches 400 associations, request an increase early.

*Auth policy design: scope to OU paths, not account IDs*

Service Network [IAM auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) should use `aws:PrincipalOrgPaths` conditions rather than listing individual account IDs. New accounts added to an OU automatically inherit access without policy updates. The reference implementation pairs the OU-path match with an organization ID check as a second boundary:

```
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "vpc-lattice-svcs:Invoke",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:PrincipalOrgID": "o-EXAMPLE12345"
    },
    "ForAnyValue:StringLike": {
      "aws:PrincipalOrgPaths": [
        "o-EXAMPLE12345/r-EXAMPLE/ou-EXAMPLE-dev0000/*"
      ]
    }
  }
}
```

**Why this matters:** Account-ID-based policies require updates every time you onboard a new account, which defeats the zero-touch onboarding promise. OU-path conditions make the policy scale with the organization structure.

*AWS Well-Architected Framework alignment*

This pattern maps to all six pillars of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/):

|
|
| Pillar | How this pattern aligns | Trade-off to acknowledge |
| --- |--- |--- |
| **Operational Excellence** | Everything is Infrastructure as Code; onboarding is a single VPC association; shared connectivity is configured once, reducing per-account drift | Platform team becomes single point of operational responsibility |
| **Security** | Defense in depth: Service Network IAM auth policies (OU-path scoped) \+ OU-scoped RAM shares \+ centralized FQDN allowlist egress filtering \+ least-privilege IAM\* | Centralized control requires strong platform-team access governance |
| **Reliability** | Multi-AZ Resource Gateways; Squid proxy at desired count 2 with ECS auto-recovery and NLB health checks; no single-AZ dependency | Shared egress proxy is a concentration risk (mitigated by multi-AZ \+ monitoring) |
| **Performance Efficiency** | VPC Lattice routes traffic within the AWS network without additional hops; shared endpoints eliminate per-account endpoint provisioning delays | Egress proxy adds latency vs direct NAT Gateway path (acceptable for filtered egress) |
| **Cost Optimization** | Connectivity scales with environments (3), not accounts (hundreds); shared infrastructure reduces idle per-account resources | Fabric has a fixed base cost even at small scale (break-even typically between 20 and 30 accounts depending on endpoint count and AZ configuration) |
| **Sustainability** | Fewer always-on resources; shared infrastructure maximizes utilization per deployed component | Minimal incremental sustainability impact |

\*Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see Grant least privilege and Security best practices in the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

*Key trade-off: concentration risk*

This pattern deliberately concentrates connectivity into a single managed fabric. This is both its strength (one place to govern, secure, and observe) and its primary risk (a failure in the shared fabric affects all consumers). Mitigations:
+ Multi-AZ Resource Gateways (minimum 2 subnets in different AZs, each /24 or larger so the gateway has room to scale its ENIs)
+ Fargate tasks at desired count >= 2 with cross-AZ placement
+ NLB with cross-zone load balancing enabled
+ CloudWatch alarms on all shared components with automated escalation
+ Runbook for fabric degradation (documented in the repository)
+ Consider a break-glass NAT Gateway path for production workloads that need egress during a fabric outage

## Epics
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-epics"></a>

### Deploy the network foundation
<a name="deploy-the-network-foundation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the three service networks | 1. Create three service networks (`sn-dev-shared`, `sn-test-shared`, `sn-prod-shared`) with `AuthType: AWS_IAM` in the central Network account.<br />2. Attach an IAM auth policy to each network that scopes invocation by OU path using `aws:PrincipalOrgPaths`, paired with an `aws:PrincipalOrgID` check as a second boundary<br />3. Configure a RAM share for each service network, scoped to its environment's OU ARNs with external principals disabled. | Network administrator |
| Create the Network account VPCs and endpoints | 1. Deploy the Endpoint VPC and Egress VPC with /24 or larger subnets across at least two Availability Zones.<br />2. Add a NAT Gateway path to the internet in the Egress VPC (the single shared egress path for the proxy).<br />3. Provision the shared interface VPC endpoints (SSM, STS, ECR, ECS, CloudWatch Logs, and others) in the Endpoint VPC with private DNS disabled, so the endpoints keep their regional DNS names for VPC Lattice to route to.<br />4. Assign explicit, named security groups to all resources that create elastic network interfaces. | Network administrator |

### Expose shared AWS service endpoints
<a name="expose-shared-aws-service-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Resource Gateway and Resource Configurations | 1. Create the Resource Gateway in the Endpoint VPC across two subnets (one per Availability Zone).<br />2. Create a Resource Configuration for each shared endpoint, setting the custom domain name to the public service domain (for example, `ssm.us-east-2.amazonaws.com`). : this domain cannot be changed after creation.<br />3. Associate each Resource Configuration with all three service networks with private DNS enabled.<br />4. Confirm that VPC Lattice creates the managed Private Hosted Zones automatically in every associated workload VPC. | Network administrator |

### Deploy centralized egress
<a name="deploy-centralized-egress"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Squid proxy and expose it via VPC Lattice | 1. Build the Squid container image with the FQDN allowlist and store it in ECR using CodeBuild.<br />2. Create an ECS cluster and run Squid on Fargate with two tasks spread across Availability Zones.<br />3. Deploy an internal Network Load Balancer with a TCP listener on port 3128, targeting the Fargate tasks.<br />4. Create the egress Resource Gateway in the Egress VPC and expose the NLB as a Resource Configuration (`squid-proxy-rc`) on all three service networks.<br />5. Configure workloads to set `HTTP_PROXY` to the proxy's Lattice DNS name on port 3128 for filtered egress. | DevOps engineer |

### Onboard workload accounts
<a name="onboard-workload-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Associate the workload VPC and validate at scale | 1. Create a VPC association with `PrivateDnsEnabled: true` for each workload VPC, targeting the service network for its environment.<br />2. Add a security group permitting egress to the VPC Lattice managed prefix list on ports 443 and 3128.<br />3. Deploy the association at scale using a service-managed CloudFormation StackSet or AWS CDK pipeline so new accounts onboard automatically when added to the target OU.<br />4. Validate DNS resolution to confirm that AWS service domains (for example, `ssm.us-east-2.amazonaws.com`) resolve to addresses in the `129.224.0.0/17` range from inside the workload VPC.<br />5. Confirm SSM Session Manager connects, ECR image pulls succeed, and allowlisted egress works while disallowed domains are blocked by the proxy.<br />6. Verify environment isolation to confirm that a workload in the dev OU cannot reach the prod service network. | Network administrator |

### Enable ingress via Service Network Endpoints
<a name="enable-ingress-via-service-network-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy Service Network Endpoints and configure split-horizon DNS | 1. Create a Service Network Endpoint (SN-E) in the ingress VPC for each environment service network that external, on-premises, or cross-Region consumers need to reach<br />2. Assign a security group to the SN-E that restricts inbound access to approved consumer CIDRs on the required ports.<br />3. Create a private hosted zone (for example, `ingress.internal`) and add CNAME records mapping custom domain names to the SN-E generated DNS names.<br />4. Configure split-horizon DNS using separate Private Hosted Zones for the SN-E path and the VPC-association path, since they resolve to different address ranges.<br />5. Optionally automate Route 53 record creation and deletion using Amazon EventBridge and AWS Step Functions so records stay current as Resource Configurations change. | Network administrator |

## Troubleshooting
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| VPC association fails with "Service network not found" | The workload account has not received the RAM share. Confirm the account can see the network with `aws vpc-lattice list-service-networks`, check that the share status is ASSOCIATED in the workload account (`aws ram get-resource-share-associations`), and verify from the Network account that the share's principals are the correct OU ARNs. If the account sits outside the shared OUs, no association is possible by design. |
| DNS does not resolve to a Lattice IP after association | Confirm `PrivateDnsEnabled` is true on the VPC association, then test from a host inside the associated VPC (not from your workstation). Expect an address in `129.224.0.0/17`, not a public service IP and not an address in the workload VPC CIDR. |
| DNS resolves to the wrong target | A pre-existing Private Hosted Zone (often a legacy per-account endpoint PHZ) is shadowing the Lattice-managed zone. List all hosted zones associated with the workload VPC, identify the conflicting `amazonaws.com` zone, and disassociate or delete it. Route 53 answers from the most specific matching zone, so leftovers win silently. |
| Resource Gateway stuck, unhealthy, or fails to deploy | Check the gateway state (expect ACTIVE), free IP addresses in each gateway subnet (exhaustion blocks ENI scaling; subnets should be /24 or larger), and the gateway security group (443 for endpoints, 3128 for egress). Landing zones that strip default security group rules cause silent timeouts here. |
| 403 responses from VPC Lattice | IAM auth policy denial. Retrieve the auth policy from the Service Network, walk the calling account's parent OUs to build its full org path, and compare it against the policy's `aws:PrincipalOrgPaths` values (each should end with `/*`). The usual cause is an account in an OU the policy does not cover. |

## Related resources
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-resources"></a>

**GitHub repository:** [aws-samples/sample-vpc-lattice-multi-account-connectivity](https://github.com/aws-samples/sample-vpc-lattice-multi-account-connectivity)
+ CloudFormation templates (network foundation, VPC Lattice resource gateways, Squid egress proxy, workload VPC association, workload foundation)
+ CDK TypeScript stacks
+ Architecture diagrams (.drawio \+ PNG \+ SVG)
+ Documentation files covering architecture, deployment phases, best practices, and troubleshooting

**AWS documentation**
+ [Amazon VPC Lattice User Guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)
+ [VPC Lattice Resource Configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)
+ [VPC Lattice Service Network Endpoints](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-endpoints.html)
+ [AWS Resource Access Manager (RAM)](https://docs.aws.amazon.com/ram/latest/userguide/)
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/)
+ [Interface VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

**Frameworks and tools**
+ [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
+ [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/)
+ [AWS Pricing Calculator](https://calculator.aws/)
+ [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

**Related AWS Prescriptive Guidance**
+ [Guidance for VPC Lattice Automated DNS Configuration on AWS](https://docs.aws.amazon.com/solutions/amazon-vpc-lattice-automated-dns-configuration-on-aws/)
+ [Guidance for Network Security on AWS](https://aws.amazon.com/solutions/guidance/network-security-on-aws/)
+ [Guidance for Building Your Enterprise WAN on AWS](https://aws.amazon.com/solutions/guidance/building-your-enterprise-wan-on-aws/)

**Pricing references**
+ [Amazon VPC Lattice pricing](https://aws.amazon.com/vpc/lattice/pricing/)
+ [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/)
+ [NAT Gateway pricing](https://aws.amazon.com/vpc/pricing/)
+ [Interface VPC Endpoints pricing](https://aws.amazon.com/privatelink/pricing/)

## Additional information
<a name="build-multi-account-aws-connectivity-vpc-lattice-sole-network-fabric-additional"></a>

This section quantifies what the shared-fabric model changes compared to a per-account connectivity model. The numbers are expressed in resource counts and cost drivers (per-hour, per-GB, per-endpoint-hour), not in dollars. Actual savings depend on Region, traffic volume, and the specific pricing in effect when you deploy. Validate with the [AWS Pricing Calculator](https://calculator.aws/) against your own traffic profile.

**Note**
 Organizations using [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) for centralized egress and shared services already achieve consolidation compared to a fully distributed model. The comparisons below use the per-account model as the baseline. If your organization already centralizes through TGW, your savings from adopting VPC Lattice will be more modest (primarily the TGW attachment and data-processing charges for these specific patterns).

**What you will achieve:**
+ Connectivity cost decoupled from account count
+ Onboarding time reduced from hours/days to minutes
+ Reduced per-account operational overhead
+ Platform team self-service model for workload teams

*Outcome 1: Cost-predictable connectivity*

The shared-fabric model changes the cost structure from per-account (scales with estate size) to per-environment (fixed at 3 regardless of estate size).

**Shared endpoints consolidation:**

In the per-account model, each workload VPC provisions its own [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). The shared-fabric model exposes a single set in the Network account. Per-account figures are illustrative (10 endpoints x 3 AZs); the reference implementation deploys 10 shared endpoints.

|
|
| Estate size | Per-account model: endpoint ENIs (illustrative) | Shared-fabric model | Consolidation ratio |
| --- |--- |--- |--- |
| 50 accounts | \~1,500 endpoint ENIs | 10 (one shared set) | \~150:1 |
| 150 accounts | \~4,500 endpoint ENIs | 10 | \~450:1 |
| 500 accounts | \~15,000 endpoint ENIs | 10 | \~1,500:1 |

**Business impact.** Connectivity-to-AWS-services cost stops scaling with account count. The 151st or 501st account onboards with zero incremental endpoint spend.

**Centralized egress consolidation:**

In the per-account model, highly available outbound access means one [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) per AZ, per VPC, per account. The shared-fabric model consolidates this into a single egress path:

|
|
| Estate size | Per-account model: NAT Gateways (2 per account) | Shared-fabric model: centralized egress | Consolidation ratio |
| --- |--- |--- |--- |
| 50 accounts | 100 NAT Gateways | 1 shared egress path | 100:1 |
| 150 accounts | 300 NAT Gateways | 1 shared egress path | 300:1 |
| 500 accounts | 1,000 NAT Gateways | 1 shared egress path | 1,000:1 |

**Business impact.** Egress cost consolidates into one managed path that the platform team owns and right-sizes centrally.

**Transit Gateway attachment reduction (for these patterns only):**

For the specific patterns covered here (AWS-service access and filtered egress), VPC Lattice routes traffic without a TGW hop:

|
|
| Estate size | Per-account model: TGW attachments for these patterns | Shared-fabric model | Change |
| --- |--- |--- |--- |
| 50 accounts | 50 attachments | 0 (Lattice routes directly) | Attachments not needed for these patterns |
| 150 accounts | 150 attachments | 0 | Same |
| 500 accounts | 500 attachments | 0 | Same |

**Important**
If your accounts also carry east-west or hybrid traffic through TGW, those attachments remain. The change applies only to attachments that existed solely for centralized service-access and egress patterns. If TGW serves multiple purposes in your environment, your per-account attachment may still be needed.

*Outcome 2: Reduce per-account operational overhead*

The per-account model duplicates not just resources but operational work. Every endpoint, gateway, and route table must be created, secured, monitored, and kept consistent.

Onboarding contrast, per account:
+ Per-account model: 10 or more endpoints, 2 or more NAT gateways, route tables, Private Hosted Zones, and security groups, each created, secured, and kept in sync. Shared-fabric model: one VPC association.
+ DNS is manual per account in the per-account model; VPC Lattice creates the Private Hosted Zones automatically on association.
+ Onboarding drops from hours or days of IaC work to minutes through a single StackSet or CDK deploy, with far less configuration drift to manage.

**Business impact.** Platform teams shift from "deploying connectivity per account" to "maintaining one shared fabric." Workload teams get self-service: associate your VPC, start building.

*Outcome 3: Centralized security governance*

Consolidating connectivity into the shared fabric also consolidates its governance. Environment isolation comes from OU-scoped [IAM auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) on each Service Network, discovery is limited by OU-scoped [RAM shares](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) with external principals disabled, and outbound traffic is constrained by the centralized FQDN allowlist. The result is a single audit surface instead of hundreds of independent per-account configurations, so controls drift less and audits move faster. The Best practices section covers the auth-policy and RAM design in detail.

*Outcome 4: Extend the same fabric to external and cross-Region consumers*

The first three outcomes serve workloads that associate their VPC directly with a Service Network. The same fabric also reaches consumers that sit outside that association: external clients, on-premises systems (over Direct Connect or VPN), and workloads in other Regions.

A [Service Network Endpoint](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-endpoints.html) (SN-E) is the entry point for those consumers. Rather than associating an entire VPC, a consumer connects to the shared services through an SN-E placed in an ingress VPC. The SN-E resolves to per-Availability-Zone secondary IP addresses in the ingress VPC, so on-premises and cross-Region callers reach the fabric through a stable, private address they can route to, without joining the Service Network directly.

**Business impact.** One connectivity investment serves both internal workloads and external/cross-Region consumers, so you do not build and operate a parallel ingress architecture alongside the shared fabric.

*How to validate the numbers for your environment*

Resource-count changes are deterministic; dollar impacts depend on your traffic patterns, AZ count, Region, and account volume. Use the [AWS Pricing Calculator](https://calculator.aws/) with your own numbers to convert the consolidation ratios above into a defensible business case. Factor in your existing centralization (if you already use TGW for shared services, your baseline is already partially consolidated).

**Is this compatible with an existing Transit Gateway deployment?**

Yes. This pattern handles three specific patterns: AWS-service access, controlled internet egress, and ingress via [Service Network Endpoints](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-endpoints.html). [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is retained for east-west IP-routed traffic and hybrid routing. A single VPC can have both a TGW attachment and a VPC Lattice association simultaneously, because Lattice routes by DNS name and service network rather than by IP address.

**Does this replace Transit Gateway?**

No. This pattern is not positioned as a Transit Gateway replacement. It targets specific connectivity patterns (AWS-service access, controlled egress, and ingress) where VPC Lattice offers a simpler, more cost-predictable delivery mechanism. Transit Gateway remains the right tool for general-purpose IP routing, hybrid connectivity, and centralized traffic inspection. Many organizations will use both: TGW for east-west and hybrid traffic, VPC Lattice for service access and egress.

**Our organization already uses TGW with centralized egress. What does this add?**

If you already centralize egress through a TGW \+ [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) or firewall architecture, you have already achieved consolidation for that pattern. Adopting VPC Lattice for egress offers three incremental benefits:

1. **No TGW attachment required in workload accounts** for this traffic, which removes the per-attachment hourly charge and data-processing fee for these flows

1. **No CIDR coordination required** in workload VPCs (Lattice routes by DNS name and service network, supporting overlapping CIDRs)

1. **Simpler onboarding**: VPC association is one resource vs. TGW attachment \+ route table entries \+ subnet route updates

Evaluate whether these incremental benefits justify the migration effort for your specific environment.

**What is the migration path from a per-account architecture?**

Incremental and side-by-side. You never have to migrate the entire estate at once:

1. Stand up the fabric ([Service Networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html), shared endpoints, egress proxy) in the Network account. This does not affect existing workload accounts.

1. Pilot with one OU first (ideally a dev OU). Validate end-to-end: DNS resolves to Lattice IPs, `aws sts get-caller-identity` succeeds, egress proxy permits allowlisted domains.

1. Onboard in waves, OU by OU, using [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) or CDK Pipelines.

1. Decommission redundant per-account resources only after validation in each wave.

The association is additive and reversible. If anything looks wrong, disassociate the VPC and the account reverts to its previous connectivity.

**How does this work across multiple Regions?**

A VPC Lattice [Service Network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html) is a regional construct. A multi-Region deployment replicates the pattern per Region:
+ Deploy three Service Networks (dev/test/prod) in each Region
+ Deploy shared endpoints and egress proxy in each Region's Network account VPCs
+ Associate workload VPCs to the Service Network in their own Region
+ RAM shares and auth policies are regional (create in each Region)

The IaC is parameterized by Region and instantiated once per Region.

**Can I add more AWS service endpoints to the shared set?**

Yes. The reference exposes 10 endpoints (SSM, STS, ECR, ECS, CloudWatch Logs, and more). To add another:

1. Deploy the [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the Endpoint VPC

1. Add the service to the endpoints array in the CDK or CloudFormation stack

1. Redeploy. Workloads resolve the new domain automatically through the Lattice-managed [Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html), with no per-account changes required.

**What about overlapping CIDRs across workload accounts?**

VPC Lattice supports overlapping CIDRs natively. Workload VPCs can use the same CIDR blocks because Lattice routes by DNS name and service network (DNS/HTTP), not by IP address. This is particularly valuable for large organizations where CIDR coordination across hundreds of accounts is impractical or where acquired business units bring their own address space.

**What happens if the shared egress proxy goes down?**

All workload accounts using the centralized egress path lose outbound internet access for traffic routed through the proxy. Mitigations:
+ [Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) tasks run at desired count >= 2 across multiple AZs
+ [NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) health checks detect and route around unhealthy tasks
+ ECS auto-recovery replaces failed tasks automatically
+ [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms alert the platform team immediately

For production workloads that require egress even during a fabric outage, maintain a break-glass NAT Gateway path that can be activated by changing a route table entry. This is the standard resilience pattern for any centralized egress design (TGW-based or Lattice-based).

**What IP ranges does VPC Lattice resolve to?**

For VPC Resources (what this pattern uses for endpoints and the egress proxy), DNS resolves to addresses in the `129.224.0.0/17` IPv4 range. This is the AWS-managed range for VPC Lattice resource traffic.

**How do I update the egress allowlist without a full redeploy?**

By default, the allowlist is the `ALLOWED_DOMAINS` environment variable on the ECS task definition, so updating it requires a stack redeploy (ECS rolls out a new task revision). For frequent changes, source the list from [SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) and have the container read it at startup; this lets you change the allowlist without a stack deploy.

## Attachments
<a name="attachments-f1e001b4-b79d-4071-8e5d-e02fa2aecbf6"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/f1e001b4-b79d-4071-8e5d-e02fa2aecbf6/attachments/attachment.zip)
