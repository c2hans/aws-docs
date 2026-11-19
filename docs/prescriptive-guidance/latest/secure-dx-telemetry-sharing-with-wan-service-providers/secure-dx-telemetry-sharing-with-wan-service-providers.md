---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/secure-dx-telemetry-sharing-with-wan-service-providers.html
---

# Enabling secure telemetry sharing with WAN service providers for AWS Direct Connect

*Rachel Bart, Christian Arllen, Cristian Critelli, and Len Gomes, Amazon Web Services*

## Introduction
<a name="introduction"></a>

This guide solves a common operational gap: AWS does not natively enable customers to share Direct Connect (DX) telemetry with their WAN Service Provider (WSP) or Enterprise Service Provider (ESP).** **This guide provides instructions for enabling secure, customer-controlled telemetry sharing with WSPs.

In a typical DX deployment, three parties are involved — the customer (account owner), the WSP/ESP (transport layer manager), and AWS (the DX service). Each party has visibility into only their own segment of the connection. None has a complete end-to-end view. When an issue occurs — degraded optical light levels, a BGP session flap, or a full circuit outage — troubleshooting for many customers currently requires manual coordination across all three parties before diagnosis can even begin.

This manual coordination introduces measurable delays. Consider a scenario where a connection experiences degraded optical light levels at 2:00 AM:

1. The customer's on-call engineer must wake up, log in, and review CloudWatch metrics

1. They must identify the affected connection and determine which WSP manages it

1. They locate the correct WSP contact, then relay connection details via email or phone

1. Only then** **can the WSP begin transport-side diagnosis

This process typically consumes 30 to 60 minutes before the WSP can take any action. This guidance provides mechanisms to automate manual inter-organizational communication and coordination.

### How Does It Work?
<a name="how-does-it-work-.5914871c-2067-5b3f-846f-43e3625aab98"></a>

The framework uses a well-established AWS security primitive — cross-account IAM role delegation — to give the WSP/ESP read-only, programmatic access to DX telemetry. The customer creates an IAM role with a trust policy that allows the WSP/ESP's AWS account to assume it. The role grants only read permissions: Describe, List, and Get operations. No write access is granted. All API calls are logged in CloudTrail.

With this framework deployed, the WSP's monitoring system independently:
+ **Detects** connection degradation via CloudWatch metrics
+ **Queries** connection configuration via Direct Connect Describe APIs
+ **Retrieves** customer NOC contact information from resource tags
+ **Begins diagnosis** within minutes — without waiting for the customer to initiate contact

The result (illustrative: time-to-diagnosis drops from \~50 minutes to \~3 minutes — a 94% improvement.

### Key Design Principles
<a name="key-design-principles.5a439bab-b07f-5a4c-9c5a-0b4189c6809f"></a>

|
|
| Principle | How It's Applied |
| --- |--- |
| **Customer control** | Two-tier opt-in: org approves the pattern, then individual account owners tag specific resources for sharing |
| **Least privilege** | Read-only actions; no write/update/delete; IAM self-audit scoped to the operator role and policy ARNs |
| **ExternalId protection** | Mitigates confused deputy attacks; unique per customer relationship |
| **Auditability** | Every role assumption and API call logged in CloudTrail |
| **Revocability** | Four graduated revocation levels — from tag removal to role deletion |
| **Partition independence** | Single CloudFormation template works across all AWS partitions including restricted access partitions |

### Who Should Use This Framework?
<a name="who-should-use-this-framework-.66f91d2c-4998-52f4-a2ba-e54f75348b29"></a>
+ Cloud architects designing hybrid connectivity governance
+ Network engineers managing Direct Connect circuits
+ Security/compliance teams evaluating cross-account access patterns
+ Technical Account Managers (TAMs) / Enterprise Account Engineers (EAE) recommending operational improvements
+ WAN Service Providers building monitoring integrations with customer DX environments
+ Support Engineering (SE) for troubleshooting and guidance
+ Professional services (ProServe) for implementation and deployment

### What You'll Need (Prerequisites)
<a name="what-you-ll-need--prerequisites-.c84d88d8-3350-59e8-89a0-2a9347ffa429"></a>
+ AWS Direct Connect deployed with at least one active connection
+ IAM permissions to create roles and policies in the customer account
+ CloudTrail enabled for audit logging
+ Your WSP/ESP must have an AWS account in the same AWS partition as yours
+ The WSP/ESP monitoring systems must allow for usage of AWS credentials provided through the STS `AssumeRole` API

### Assumptions
<a name="assumptions.f03c8c65-a85a-53a1-b478-f950e44adf0f"></a>

The WSP/ESP has an AWS account in the same partition as the customer. Cross-partition federation is not supported. The customer maintains ownership of all Direct Connect resources and controls tagging decisions. The WSP/ESP monitoring system supports STS role assumption. The customer understands their Direct Connect resiliency topology.

### Non-Goals and Out of Scope
<a name="non-goals-and-out-of-scope.f96b8a7e-b46a-5a7c-b1d2-348c2154998c"></a>

No API for write access is granted. No physical layer remediation automation is provided. No AWS-hosted shared dashboards are included; the WSP/ESP may build their own dashboards. No cross-partition federation is supported. EventBridge-based notifications are best-effort via CloudTrail; CloudWatch metrics remain the authoritative source for circuit health telemetry.

### Conclusion
<a name="conclusion.e1004d68-02db-5ac1-8d09-8a5ab6ca7919"></a>

This framework provides a native mechanism for sharing Direct Connect telemetry with network service providers using patterns aligned with the Security and Reliability pillars of the AWS Well-Architected Framework.

The framework is deployable via a single CloudFormation template, works across all partitions without modification, costs less than $10 per month, and delivers measurable Mean Time to Recovery (MTTR)reduction by transforming troubleshooting from a reactive coordination process into a proactive self-service model.

Organizations operating mission-critical workloads using Direct Connect should evaluate this framework as part of their hybrid connectivity governance strategy.

#### Tutorial: Setting Up Direct Connect Information Sharing
<a name="tutorial--setting-up-direct-connect-information-sharing.e08e283f-aa3e-531f-bd9a-e355246ef9b6"></a>

This tutorial walks you through deploying the framework from start to finish. By the end, your WSP/ESP will have secure, read-only access to your DX telemetry.

### Step 1: Plan Your Deployment
<a name="step-1--plan-your-deployment.db84fd5a-0d98-5dd3-8dc6-cf9bc08a3247"></a>

Before deploying anything, answer these questions:

|
|
| Decision | Options | Guidance |
| --- |--- |--- |
| **ExternalId enforcement?** | Model A: Enforced (recommended) / Model B: Removed for console access | Model A is more secure (prevents confused deputy). Model B allows use of the AWS Console "Switch Role" feature without guardrails provided by ExternalId enforcement. |
| **Which connections to share?** | All DX connections / Subset | You control this access via resource tags — only connections tagged `DXInfoSharing=enabled` provide visibility to operational metadata |
| **Optional permissions?** | VPC access / Transit Gateway access | Enable only if WSP needs routing context for troubleshooting; both disabled by default |
| **Which partition?** | Supported in all AWS partitions | Both accounts (yours and WSP's) must be in the same partition |

**Action items before proceeding:**
+ Confirm your WSP/ESP's AWS Account ID
+ Decide on ExternalId enforcement model (A or B) — seek security team review
+ Identify which DX connections to share

### Step 2: Coordinate with Your WSP/ESP
<a name="step-2--coordinate-with-your-wsp-esp.25e7404e-0f75-58eb-bed8-50637c36e24c"></a>

Contact your WSP/ESP to exchange the following information:

**You provide to WSP/ESP:**
+ Nothing yet — deployment happens first

**WSP/ESP provides to you:**
+ Their AWS Account ID (12-digit number)
+ An ExternalId value (UUID v4 format, generated by the WSP/ESP)

**Security note:** The ExternalId should be transmitted via an encrypted channel (e.g., encrypted email, secure file transfer). It should be unique to your specific customer relationship — not a shared value used across multiple customers.

### Step 3: Deploy the CloudFormation Stack
<a name="step-3--deploy-the-cloudformation-stack.0dcddc02-ff6b-5949-bc8c-b44921adad9c"></a>

Run the following bash script which runs AWS CLI commands from your AWS account (the customer account that owns the DX connections):

```
# Detect your partition, account, and region
AWS_PARTITION=$(aws sts get-caller-identity --query 'Arn' --output text | cut -d: -f2)
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
REGION=$(aws configure get region)

# Deploy the framework stack
aws cloudformation deploy \
  --template-file iac/cloudformation/dx-info-sharing.yaml \
  --stack-name dx-info-sharing \
  --parameter-overrides \
    ESPAccountId=<WSP_ACCOUNT_ID> \
    ExternalId=<EXTERNAL_ID_FROM_WSP> \
  --capabilities CAPABILITY_NAMED_IAM
```

**Replace:**
+ `<WSP_ACCOUNT_ID>` — the 12-digit AWS Account ID your WSP/ESP provided
+ `<EXTERNAL_ID_FROM_WSP>` — the UUID your WSP/ESP generated

**Optional parameters** (add to `--parameter-overrides` if needed):
+ `EnableVPCAccess=true` — grants WSP read access to VPC/VPN routing info
+ `EnableTGWAccess=true` — grants WSP read access to Transit Gateway config

**Retrieve the stack outputs:**

```
aws cloudformation describe-stacks \
  --stack-name dx-info-sharing \
  --query 'Stacks[0].Outputs' --output table
```

This creates two resources:
+ `DXNetworkOperatorPolicy` — the read-only IAM managed policy
+ `DXNetworkOperatorRole` — the IAM role the WSP/ESP will assume

### Step 4: Tag Your Direct Connect Resources
<a name="step-4--tag-your-direct-connect-resources.afbdfa29-45af-5815-a128-f2f564c606a7"></a>

Only resources you explicitly tag will provide visibility to operational metadata to the WSP/ESP. Tag each DX connection you want to share:

```
aws directconnect tag-resource \
  --resource-arn arn:${AWS_PARTITION}:directconnect:${REGION}:${ACCOUNT_ID}:dxcon/<YOUR_CONNECTION_ID> \
  --tags key=DXInfoSharing,value=enabled \
         key=AccountPOC,value=owner@example.com \
         key=TechnicalPOC,value=netadmin@example.com \
         key=NOCContact,value=noc@example.com \
         key=Criticality,value=MissionEssential
```

**Replace:**
+ `<YOUR_CONNECTION_ID>` — e.g., `dxcon-abc12345`

**Supported tags:**

|
|
| Tag Key | Purpose | Example |
| --- |--- |--- |
| `DXInfoSharing` | Opt-in flag (required) | `enabled` |
| `AccountPOC` | Business owner contact | `owner@example.com` |
| `TechnicalPOC` | Technical contact | `netadmin@example.com` |
| `NOCContact` | 24/7 operations center | `noc@example.com` |
| `Criticality` | Business impact level | `MissionEssential` / `MissionCritical` / `Standard` |
| `WSPCircuitId` | WSP's circuit reference | `CKT-12345-IAD` |
| `MaintenanceWindow` | Preferred maintenance time | `Sun 02:00-06:00 UTC` |
| `RedundancyGroup` | Resiliency set ID | `rg-prod-iad-01` |
| `ConnectionRole` | Primary or back-up | `Primary / Secondary` |
| `RedundancyModel` | Failover posture | `Active-Active / Active-Passive` |
| `BackupConnection` | Paired connection  | `dxcon-1234abcd` |
| `RedundancyLocation` | Failure domain / site | `IAD / us-east-1-iad-2` |

**Tip**
Tag ALL connections in your resiliency topology (primary and backup across locations) so the WSP can assess redundancy impact during a failure.

### Step 5: Share the Role ARN with Your WSP/ESP
<a name="step-5--share-the-role-arn-with-your-wsp-esp.606b7079-78ff-56f1-83dc-50a6fed1aeb4"></a>

After deployment, provide the WSP/ESP with:
+ The **Role ARN**: `arn:<partition>:iam::<your-account-id>:role/DXNetworkOperatorRole`

The WSP/ESP already has the ExternalId (they generated it). With the Role ARN \+ ExternalId, they can configure their monitoring system.

### Step 6: Validate the Deployment
<a name="step-6--validate-the-deployment.f736093b-eace-5fae-aa94-c58cd4d6c6c2"></a>

**From your account (customer):**

```
# Verify the role exists and has correct policies
aws iam get-role --role-name DXNetworkOperatorRole
aws iam list-attached-role-policies --role-name DXNetworkOperatorRole
```

**From the WSP/ESP account** (ask your WSP to run these):

```
# Assume the role (with ExternalId)
CREDS=$(aws sts assume-role \
  --role-arn arn:${AWS_PARTITION}:iam::<CUSTOMER_ACCOUNT_ID>:role/DXNetworkOperatorRole \
  --role-session-name dx-validation \
  --external-id <EXTERNAL_ID> \
  --query 'Credentials' --output json)

export AWS_ACCESS_KEY_ID=$(echo $CREDS | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $CREDS | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $CREDS | jq -r '.SessionToken')

# Test DX read access
aws directconnect describe-connections --max-results 5

# Test CloudWatch metric access
aws cloudwatch list-metrics --namespace AWS/DX --max-items 5

# Test tag retrieval
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=DXInfoSharing,Values=enabled \
  --resource-type-filters directconnect
```

**Success criteria:** All three commands return data without errors.

### Step 7: Verify Audit Logging
<a name="step-7--verify-audit-logging.ee2f7f27-ff72-534f-a593-694994c45953"></a>

Confirm that CloudTrail is capturing the WSP's activity:

```
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRole \
  --max-results 10 \
  --query 'Events[?contains(CloudTrailEvent, `DXNetworkOperatorRole`)]'
```

You should see the validation AssumeRole event from Step 6.

### Step 8: Establish Ongoing Governance
<a name="step-8--establish-ongoing-governance.cbcadfa7-9ea6-566b-b7b2-cafa985a3a76"></a>

With deployment complete, set up your operational cadence:

|
|
| Frequency (examples) | Action |
| --- |--- |
| **Ongoing** | Monitor CloudTrail for unexpected access patterns |
| **On resource change** | Update tags when contacts change or connections are added/decommissioned |
| **Monthly** | Verify tag accuracy across all shared connections |
| **Quarterly** | Formal access review — confirm business need, ExternalId currency, authorized personnel |
| **Annually** | Coordinate ExternalId rotation with WSP/ESP |

### Optional: Add Complementary Options
<a name="optional--add-complementary-options.34953c74-257c-5496-a68b-29e3e9f4dfef"></a>

Once the baseline (Option 1) is running, consider adding:

|
|
| Option | What It Adds | When to Use |
| --- |--- |--- |
| **Option 2: EventBridge** | Real-time notifications of DX state changes via CloudTrail events | When WSP needs event-driven alerts (not just polling) |
| **Option 3: Network Synthetic Monitor** | Network Health Indicator (NHI) metric for fault isolation | When you need to determine if an issue is on the AWS side or on-premises side |
| **Option 4: AWS Health Events** | Advance notice of planned maintenance \+ real-time service events | When WSP needs to proactively prepare for AWS-side maintenance |

**Note**
 Options 2–4 depend on services (EventBridge, CloudWatch Network Monitor, AWS Health) that may not be available in all partitions. Option 1 alone provides substantial value and works everywhere.

### Quick Reference: How to Revoke Access
<a name="quick-reference--how-to-revoke-access.40263420-6005-523c-8ab4-5aaf804d9df3"></a>

If you need to remove your WSP/ESP's access (contract end, security concern, etc.):

|
|
| Level | Action | Effect | Reversible? |
| --- |--- |--- |--- |
| 1. **Scope reduction** | Remove `DXInfoSharing` tags | WSP can still query APIs but gets no operational metadata | ✅ Re-tag to restore |
| 2. **Session revocation** | Attach `AWSRevokeOlderSessions` inline policy | All in-flight credentials invalidated within seconds | ✅ Remove policy to restore |
| 3. **Role disablement** | Modify trust policy to deny all principals | No new role assumptions possible | ✅ Restore trust policy |
| 4. **Role deletion** | Delete the role entirely | Permanent removal | ❌ Must redeploy stack |

**Escalate only as needed** — start at Level 1 and proceed upward based on severity.

## Attachments
<a name="attachments-a27cfbe8-ee56-4f7e-8dbe-badf176580a2"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
